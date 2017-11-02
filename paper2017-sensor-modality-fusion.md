| 논문명 | Sensor Modality Fusion with CNNs for UGV Autonomous Driving in Indoor Environments |
| --- | --- |
| 저자\(소속\) | Naman Patel\(NYU\) |
| 학회/년도 | 2017, [논문](http://cims.nyu.edu/~achoroma/NonFlash/Papers/SMF_CNN.pdf) |
| 키워드 | 조향 각도 예측  |
| 데이터셋(센서)/모델 | own dataset(LiDAR + Camera) |
| 참고 |  |
| 코드 |  |

# SMF_CNN

- We present a novel end-to-end learning framework by fusing **raw pixels** from cameras and depth measurements from a **LiDAR**. 

- **A deep neural network** architecture is introduced to effectively perform **modality fusion** and reliably **predict steering commands** even in the presence of sensor failures. 

## 1. INTRODUCTION

- Our work focuses on the problem of **navigating** of an autonomous UGV using **vision** and **depth** measurements in an indoor environment. 

- We propose a **deep learning architecture** for the **sensor fusion** problem that consists of two convolutional neural networks (CNNs), each consisting of a different input modality, which are fused with a **gating mechanism**. 

> 각센서를 위해 다른 CNN네트워크가 존재 하며 추후 **gating mechanism**을 이용하여 Fuse 됨 

## 2. RELATED WORK

- Vision과  depth를 기반으로 한 자율 주행 로봇에 대한 연구가 많이 이루어 지고 있다. `Various aspects of robot autonomy in both indoor and outdoor environments using vision and depth based sensor processing have been extensively studied in the literature[1]–[6]. `

- 강화 학습 역시 센서 정보를 사용하여 장애물 회피에 적용되고 있다. `Reinforcement learning techniques have also been utilized to teach the mobile robot to avoid obstacles and navigate through the corridor using sensors such as a laser range finder [7]. `

- [8]에서는 An online navigation 프레임워크를 제안 하였다. `An online navigation framework relying on object recognition was presented in [8]. `

- CNN기반 자율 주행 차량 연구들 `CNNs have been successfully used for learning driving decision rules for autonomous navigation [9] and for end-to-end navigation of a car using a single front facing camera [10] (alternately,debugging tools were developed for these systems to understandthe visual cues the network used to produce a steeringcommand, e.g. [11]). `

- NN기반 indoor navigation 연구들 `Neural network based indoor navigation has also been studied in multiple works including [12]–[16].`

- 센서퓨전 기반 연구[17]들 `In the deep learning literature, fusion of different modalities has been studied for various applications in recent year ssuch as in [17] for object detection using images and depth maps. `

```
[17] S. Gupta, R. Girshick, P. Arbelaez, and J. Malik, “Learning rich ´features from rgb-d images for object detection and segmentation,” in European Conference on Computer Vision, Sept. 2014, pp. 345–360
```


- RNN기반 images & depth map의 연관관계 학습을 통한 semantic segmentation `Deep learning for a recurrent neural network [18] was applied to implicitly learn the dependencies between RGB images and depth map to perform semantic segmentation.`

```
[18] C. Hazirbas, L. Ma, C. Domokos, and D. Cremers, “Fusenet: Incorporating depth into semantic segmentation via fusion-based cnn architecture,” in Proc. ACCV, vol. 2, Nov. 2016, pp. 213–228.
```

- [19]에서는 RGB와 라이다 정보를 활용하여 3D 물체 탐지를 한다. `In [19], RGB image and its corresponding 3D point cloud are used as inputs for 3D object detection. `

```
[19] S. Song and J. Xiao, “Deep sliding shapes for amodal 3D object detection in RGB-D images,” in 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), June 2016, pp. 808–816.
```

- 이미지 +  optical flow + LiDAR가 함꺼번에 합쳐져서 DNN에 입력으로 이용 `RGB image,optical flow, and LiDAR range images are combined to forma six channel input to a deep neural network [20] for object detection. `
	- 동일 모델을 이용하여 joint representation학습에도 활용 `The same network can also be used for different modalities to learn a joint representation [21]. `

```
[20] M. Giering, V. Venugopalan, and K. Reddy, “Multi-modal sensor registration for vehicle perception via deep neural networks,” in High Performance Extreme Computing Conference (HPEC), 2015 IEEE,Sept 2015, pp. 1–6.
[21] L. Castrejon, Y. Aytar, C. Vondrick, H. Pirsiavash, and A. Torralba,“Learning aligned cross-modal representations from weakly aligned data,” in 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), June 2016, pp. 2940–2949.
```

- 이미지 + depth maps `(HHA)`를 퓨젼후 SVM을 이용하여 학습 하는 연구 `RGB images and depth maps (HHA images) were fused in [22] for an indoor scene recognition application using a multi-modal learning framework and the learned features were classified using a support vector machine.`

```
[22] H. Zhu, J.-B. Weibel, and S. Lu, “Discriminative multi-modal feature fusion for rgbd indoor scene recognition,” in 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), June 2016, pp.
2969–2976.
```

- 본 논문의 제안에서는 새로운 **gating mechanism**을 사용하여 성능 향상을 보임 ` Specifically, we introduce a new gating mechanism based architecture that enables modality fusion for robust end-to-end learning of autonomous corridor driving and improved training techniques that enable resiliency to sensor failure. `

### 3. PROBLEM FORMULATION

- 사람의 원격 조정 값을 학습시 사용한다. `The proposed deep learning based system is trained using data recorded under human teleoperation of the UGV.`

각 센서는 단점이 있다. `As illustratedin Figure 3, each sensor separately can have limitations in environment perception. There are also other complementary sensory performance characteristics of camera and LiDAR,e.g., sensitivity of a camera to lighting conditions, limitations of a LiDAR in detecting small objects.`

## 4. PROPOSED SENSOR FUSION FRAMEWORK

### 4.1 System Framework

- The LiDAR measurements are encoded as a 16-bit grayscale depth range image. 
- The depth range image and RGB image from the camera are used to generate a steering command 
	- that is used by the onboard autopilot to send appropriate signals to the motor controllers of the ground vehicle.

### 4.2 Network Architectures

The architectures of **NetEmb**, **NetConEmb**, and **NetGatedare** described in Tables I, II, and III, respectively. 

#### A. NetEmb

![](https://i.imgur.com/0LPYU7q.png)
```
TABLE I: NetEmb: 
- Deep learning based modality fusion architecture using embeddings. 
- The left side of the table is for processing of the RGB image from the camera and 
- the right side of the table is for processing of the depth range image from the LiDAR. 
- The feature vectors (of length 512) constructed from camera and LiDAR are concatenated at layer 24.
```
- In NetEmbfeature maps from RGB image and LiDAR depth range image are extracted through a series of convolutional layers.
- Next, the features extracted from the convolutional layers in both the parallel networks are embedded into a feature vector using a fully connected network. 

#### B. NetConEmb

![](https://i.imgur.com/5k3d8rE.png)
```
TABLE II: NetConEmb: 
- Fusion architecture where the convolutional feature maps are directly passed through a fully connected network instead of first converting them into feature embeddings as done in NetEmb. 
- The first 20 layers are identical to NetEmb.
```
- In NetConEmb, the convolutional feature maps are passed into a fully connected network. 

#### C. NetGatedare

![](https://i.imgur.com/u5ZtFGF.png)
```
TABLE III: NetGated: 
- Fusion architecture with gating mechanism based on computing scalar weights from the feature embeddings andthen constructing a combination of the feature embeddings based on the scalar weights. 
- The first 20 layers are identical to NetEmb.
```

- In NetGated, the gating network generates two weights, used to perform a weighted sum of the two embeddings obtained from the camera and lidar-range image.
- 
- This weighted sum is then passed through two fully connectednetworks to obtain the steering command. 

- Each of the considered network architectures is an end-to-end deeplearning system that takes an RGB image and a LiDAR depth range image as input and fuses the modalities using a deepneural network to predict the appropriate steering command of the UGV for autonomous navigation.

![](https://i.imgur.com/FnFDsYn.png)
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzc1MDA5NTI0XX0=
-->