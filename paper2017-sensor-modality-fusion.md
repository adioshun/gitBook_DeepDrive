| 논문명 | Sensor Modality Fusion with CNNs for UGV Autonomous Driving in Indoor Environments |
| --- | --- |
| 저자\(소속\) | Naman Patel\(NYU\) |
| 학회/년도 | 2017, [논문](http://cims.nyu.edu/~achoroma/NonFlash/Papers/SMF_CNN.pdf) |
| 키워드 |   |
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


- RNN기반 RGB images and depth map학습 semantic segmentation연구 `Deep learning for a recurrent neural network [18] was applied to implicitly learn the dependencies between RGB images and depth map to perform semantic segmentation.`

In [19], RGB image and its corresponding 3D point cloudare used as inputs for 3D object detection. 

RGB image,optical flow, and LiDAR range images are combined to forma six channel input to a deep neural network [20] for objectdetection. 

The same network can also be used for different modalities to learn a joint representation [21]. 

RGB imagesand depth maps (HHA images) were fused in [22] for anindoor scene recognition application using a multi-modallearning framework and the learned features were classifiedusing a support vector machine.Compared to the prior works summarized above, the proposedsystem introduces several novel aspects as summarizedin the introduction. 

Specifically, we introduce a new gatingmechanism based architecture that enables modality fusionfor robust end-to-end learning of autonomous corridor drivingand improved training techniques that enable resiliencyto sensor failure. 

The efficacy of the proposed approach isdemonstrated through experimental studies (Figure 2).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIyMjM3MzQ2MF19
-->