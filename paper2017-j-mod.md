|논문명|J-MOD^2: Joint Monocular Obstacle Detection and Depth Estimation|
|-|-|
|저자(소속)| Michele Mancini ()|
|학회/년도| Sep 2017 , [논문](https://arxiv.org/abs/1709.08480)|
|키워드| 1 camera, YOLO |
|참고|[홈페이지](http://isar.unipg.it/index.php?option=com_content&view=article&id=47&catid=2&Itemid=188), [Youtube](https://youtu.be/ZxHcZ0XQfI4)|
|코드||

# J-MOD^2

![](https://i.imgur.com/SkuMLvl.png)

> 깊이탐지는 [13]알고리즘 활용, 물체 탐지는 YOLO 아이디어 활용 

## I. INTRODUCTION

###### 장애물 탐지 여러 기법들 
Most fruitful approaches rely on range sensors to build 3D maps and compute obstacle-free trajectories
- laser-scanner [1], [2], 
- stereo cameras [3], [4] 
- RGB-D cameras [5], [6] 

```
[1] A. Bachrach, S. Prentice, R. He, and N. Roy, “Range–robust autonomous navigation in gps-denied environments,” Journal of Field Robotics, vol. 28, no. 5, pp. 644–666, 2011.
[2] S. Grzonka, G. Grisetti, and W. Burgard, “A fully autonomous indoor quadrotor,” IEEE Transactions on Robotics, vol. 28, no. 1, pp. 90–100, 2012.
[3] F. Fraundorfer, L. Heng, D. Honegger, G. H. Lee, L. Meier, P. Tanskanen, and M. Pollefeys, “Vision-based autonomous mapping and exploration using a quadrotor mav,” in Intelligent Robots and Systems
(IROS), 2012 IEEE/RSJ International Conference on. IEEE, 2012, pp. 4557–4564.
[4] C. De Wagter, S. Tijmons, B. D. Remes, and G. C. de Croon, “Autonomous flight of a 20-gram flapping wing mav with a 4-gram onboard stereo vision system,” in Robotics and Automation (ICRA), 2014 IEEE International Conference on. IEEE, 2014, pp. 4982–4987
[5] A. Bachrach, S. Prentice, R. He, P. Henry, A. S. Huang, M. Krainin, D. Maturana, D. Fox, and N. Roy, “Estimation, planning, and mapping for autonomous flight using an rgb-d camera in gps-denied environments,” The International Journal of Robotics Research, vol. 31, no. 11, pp. 1320–1343, 2012.
[6] A. S. Huang, A. Bachrach, P. Henry, M. Krainin, D. Maturana, D. Fox, and N. Roy, “Visual odometry and mapping for autonomous flight using an rgb-d camera,” in Robotics Research. Springer, 2017, pp.235–252.
```

###### 싱글 카메라 방법들 
- Monocular Visual SLAM (VSLAM) approaches address the above limitations by exploiting single camera pose estimation and 3D map reconstruction [7], [8], [9], [10], [11].

```
[7] R. A. Newcombe, S. J. Lovegrove, and A. J. Davison, “Dtam: Dense tracking and mapping in real-time,” in Computer Vision (ICCV), 2011 IEEE International Conference on. IEEE, 2011, pp. 2320–2327.
[8] M. W. Achtelik, S. Lynen, S. Weiss, M. Chli, and R. Siegwart, “Motion-and uncertainty-aware path planning for micro aerial vehicles,” Journal of Field Robotics, vol. 31, no. 4, pp. 676–698, 2014.
[9] D. Scaramuzza, M. C. Achtelik, L. Doitsidis, F. Friedrich, E. Kosmatopoulos, A. Martinelli, M. W. Achtelik, M. Chli, S. Chatzichristofis, L. Kneip, et al., “Vision-controlled micro flying robots: from system design to autonomous navigation and mapping in gps-denied environments,” IEEE Robotics & Automation Magazine, vol. 21, no. 3, pp. 26–40, 2014.
[10] J. Engel, T. Schops, and D. Cremers, “Lsd-slam: Large-scale direct monocular slam,” in European Conference on Computer Vision. Springer, 2014, pp. 834–849.
[11] C. Forster, M. Pizzoli, and D. Scaramuzza, “Svo: Fast semi-direct monocular visual odometry,” in Robotics and Automation (ICRA), 2014 IEEE International Conference on. IEEE, 2014, pp. 15–22.
```


###### 기존 싱글 카메라 방법의 문제점 
- the absolute scale is not observable (which easily results in wrong obstacle distance estimations); 
- they fail to compute reliable 3D maps on low textured environments; 
- the 3D map updates are slow with respect to real-time requirements of fast maneuvers.


###### CNN을 이용한 싱글 카메라 방법들  
- monocular depth estimation methods based on Convolutional Neural Networks (CNNs) [12], [13], [14].

```
[12] D. Eigen and R. Fergus, “Predicting depth, surface normals and semantic labels with a common multi-scale convolutional architecture,” in Proceedings of the IEEE International Conference on Computer
Vision, 2015, pp. 2650–2658.
[13] M. Mancini, G. Costante, P. Valigi, T. A. Ciarfuglia, J. Delmerico, and D. Scaramuzza, “Towards domain independence for learning-based monocular depth estimation,” IEEE Robotics and Automation Letters, 2017.
[14] S. Yang, S. Konam, C. Ma, S. Rosenthal, M. Veloso, and S. Scherer, “Obstacle avoidance through deep networks based intermediate perception,” arXiv preprint arXiv:1704.08759, 2017
```


###### 기존 CNN을 이용한 싱글 카메라 방법들의 문제점 

- However, these depth models are biased with respect to appearance domains and camera intrinsics. 

- Depth 측정에 초점을 두고 있지, 장애물 탐지 기능은 없다. `Furthermore, the CNN architectures so far proposed address the more general task of pixel-wise depth prediction and are not specifically devised for obstacle detection.`

###### 제안하는 CNN을 이용한 싱글 카메라 방법

- 장점 :  fast and robust to focal length(초점거리) and appearance changes

- 구조 : We achieve this by introducing a **multi-task CNN architecture** that jointly learns to predict **full depth maps** and **obstacle bounding boxes**. 

## 2. RELATED WORK

Range 제약 
- Microsoft Kinect RGB-D sensor :~5 meters
- stereo camera(MAV’s sizes) : ~ 3 meters [16]. baselines 늘리면 향상 가능 

제안 하는 monocular camera 방식 : ~20 meters(물체탐지), ~40 meters(Depth map)

### 2.1 geometric monocular algorithms : SLAM, SFM

일반적으로 물체 탐지는 (SLAM이나 SFM을 통해 생성된) 3D map을이용하여 가능하다. `Monocular obstacle detection can be achieved by dense 3D map reconstruction via SLAM or Structure from Motion (SFM) based procedures [7], [10], [19], [20].`

SLAM이나 SFM을 이용하는 방법들이 간단하기는 하지만, **triangulation of consecutive frames**에 기반하고 있어서 고속에서는 정확도가 떨어진다.   `In particular, geometric based 3D reconstruction algorithms rely on the triangulation of consecutive frames. their accuracy drops during high-speed motion, as dense alignment becomes more challenging. `

또한, 물체의 Absolute 크기 구하지 못하기 떄문에 거리 측정에도 한계가 있다. 그래서 이러한 방법들은 **optical information **을 같이 사용한다. `In addition, with standard geometric monocular systems it is not possible to recover the absolute scale of the objects. This prevents them to accurately estimate obstacle distances. For this reason, most approaches exploit optical information to detect proximity of obstacles from camera, or, similarly, detect traversable space [21], [22], [23], [24].`

### 2.2 deep learning-based algorithms 

These models produce a dense 3D representation of the environment from a single image, 
- exploiting the knowledge acquired through training on large labeled datasets, both real world and synthetic [25], [12], [26], [13]. 


```
[25] D. Eigen, C. Puhrsch, and R. Fergus, “Depth map prediction from a single image using a multi-scale deep network,” in Advances in neural information processing systems, 2014, pp. 2366–2374.
[12] D. Eigen and R. Fergus, “Predicting depth, surface normals and semantic labels with a common multi-scale convolutional architecture,” in Proceedings of the IEEE International Conference on Computer Vision, 2015, pp. 2650–2658.
[26] F. Liu, C. Shen, G. Lin, and I. Reid, “Learning depth from single monocular images using deep convolutional neural fields,” IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 38, no. 10, pp. 2024–2039, Oct 2016
[13] M. Mancini, G. Costante, P. Valigi, T. A. Ciarfuglia, J. Delmerico, and D. Scaramuzza, “Towards domain independence for learning-based monocular depth estimation,” IEEE Robotics and Automation Letters, 2017
```


#### A. 기존 MAV에 적용한 사례들 

In [27], the authors fine-tune on a self-collected dataset the global coarse depth estimation model proposed by [25]. 

Then, they compute MAV’s control signals during test flights on the basis of the estimated depth.

```
[27] P. Chakravarty, K. Kelchtermans, T. Roussel, S. Wellens, T. Tuytelaars, and L. Van Eycken, “Cnn-based single image obstacle avoidance on a quadrotor,” in Robotics and Automation (ICRA), 2017 IEEE International Conference on. IEEE, 2017, pp. 6369–6374.
[25] D. Eigen, C. Puhrsch, and R. Fergus, “Depth map prediction from a single image using a multi-scale deep network,” in Advances in neural information processing systems, 2014, pp. 2366–2374.
```

In [14] the authors exploit depth and normals estimationsof a deep model presented in [12] as an intermediate stepto train an visual reactive obstacle avoidance system. 

Differently from [14] and [27], we propose to learn a more robotic-focused model that jointly learns depth and obstacle representations to strengthen the obstacle detection task.

```
[14] S. Yang, S. Konam, C. Ma, S. Rosenthal, M. Veloso, and S. Scherer, “Obstacle avoidance through deep networks based intermediate perception,” arXiv preprint arXiv:1704.08759, 2017.
[12] D. Eigen and R. Fergus, “Predicting depth, surface normals and semantic labels with a common multi-scale convolutional architecture,” in Proceedings of the IEEE International Conference on Computer Vision, 2015, pp. 2650–2658
```


#### B. 본 논문에서 활요한 사례들 

##### 가. 장애물 탐지 

> inspired by [31]

we regress bounding boxes anchor points and dimensions, but with a slightly different implementation. 
- we remove the fully connected layers, maintaining a fully convolutional architecture. 
    - We favor this strategy over other object detection approaches because of its high computational efficiency, as it allows multiple bounding box predictions with a single forward pass. 
- In addition, we also let the obstacle detector regress the average depth and the corresponding estimate variance of the detected obstacles.

```
[31] J. Redmon, S. Divvala, R. Girshick, and A. Farhadi, “You only look once: Unified, real-time object detection,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, 2016, pp.779–788.
```

##### 나. 깊이 예측 

Depth estimation is devised following the architecture of [13], improved by taking into account the obstacle detection branch. 

In particular, 
- we correct the depth predictions by using the mean depth estimates computed by the obstacle detection branch to achieve robustness with respect to appearance changes. 
- We prove the benefits of this strategy by validating the model in test sequences with different focal length and scene appearance.

```
[13] M. Mancini, G. Costante, P. Valigi, T. A. Ciarfuglia, J. Delmerico, and D. Scaramuzza, “Towards domain independence for learning-based monocular depth estimation,” IEEE Robotics and Automation Letters, 2017.
```

## 3. NETWORK OVERVIEW

![](https://i.imgur.com/pCnKxIk.png)

- 입력이미지에서 Feature 추출 `Given an 256×160 RGB input, features are extracted with a fine-tuned version of the VGG19 network pruned of its fully connected layers [32]. `
    - VGG19 weights are initialized on the image classification task on the ImageNet dataset. 

- 추출된 Feature는 두개의 분리된 Task branch로 입력 `Features are then fed to two, task-dependent branches:`
    - 깊이 예측 `a depth prediction branch and `
    - 장애물 탐지 `a obstacle detector branch. `

###### [깊이 예측 branch ]

-  네트워크 구성 및 결과물: The former is composed by 4 upconvolution layers and a final convolution layer which outputs the **predicted depth** at original input resolution. 
    - This branch, plus the VGG19 feature extractor, is equivalent to the fully convolutional network proposed in [13]. 

- We optimize depth prediction on the following loss:


###### [장애물 탐지 branch]

- 네트워크 구성 : The obstacle detection branch is composed by 9 convolutional layer with `Glorot` initialization. 

- 탐지 방법은 YOLO와 비슷 : The detection methodology is similar to the one presented in [31-YOLO]: 
    - the input image is divided into a 8 × 5 grid of square-shaped cells of size 32 × 32 pixels. 

- 학습 대상 : For each cell, we train a detector to estimate:
    - 대상물 좌표(x,y,w,h) The (x, y) coordinates of the bounding box center & width `w` and height `h`
    - A confidence score C
    - 거리 : The average distance of the detected obstacle from the camera `m` and the variance of its depth distribution `v`
    
- 결과물 : The resulting output has a 40 × 7 shape. 
    - At test time, we consider only **predictions** with a **confidence score** over a certain threshold. 


We train the detector on the following loss:

### 3.1 Exploiting detection to correct global scale estimations

- 이미지 한장에서 깊이 예측의 절대 크기(absolute scale)를 알기는 어렵다. `The absolute scale of a depth estimation is not observable from a single image. `


- 하지만, 학습 기반 깊이 예측 방법은 특정 조건에서는 scale에 대한 정확도 추측 값`(accurate guess)`을 제공한다. `However, learning-based depth estimators are able to give an accurate guess of the scale under certain conditions. `


- 이러한 모델은 학습시에 암묵적으로 도메인에 특화된 물체 특징이나 외형 정보를 학습 한다. `While training, these models implicitly learn domain-specific object proportions and appearances.`
    - 이를 통해 `Depth map`과 `Depth map의 absolute scale`를 예측 하는데 도움이 된다. `This helps the estimation process in giving depth maps with correct absolute scale. `


- 물체의 특징과 global scale간의 상관 관계는 카메라의 focal length의 큰 영향을 받는다. `As the relations between object proportions and global scale in the image strongly depend on camera focal length, `
    - 테스트 시점에 이러한 학습 데이터의 도메인 특징은 `absolute scale`측정에 bais 요소가 된다. `at test time the absolute scale estimation are strongly biased towards the training set domain and its intrinsics. `
    - 이러한 이유로 **학습 데이터**와 **테스트 데이터**의 물체 특징 및 카메라 파라미터가 바뀌게 되면 크기(scale) 예측은 감소 한다. `For these reasons, when object proportions and/or camera parameters change from training to test, scale estimates quickly degrade. `


- 그래도 물체 특징이 roughly 하게 같고 카메라 고유값(intrinsics)가 테스트 시점에 바뀌어도 복구 시킬수 있다. `Nonetheless, if object proportions stay roughly the same and only camera intrinsics are altered at test time, it is possible to employ some recovery strategy.`

- 만약 주어진 물체의 크기를 알고 있다면 거리를 계산 할수 있으며 전체 depth map의 global scale을 복구 할수 있다. `If the size of a given object is known, we can analytically compute its distance from the camera and recover the global scale for the whole depth map. `

- 이러한 이유로 물체 탐지 branch에서는 intrinsics가 바뀌더라도 global scale을 복구 할수 있는 기능을 제공한다. `For this reason, we suppose that the obstacle detection branch can help recovering the global scale when intrinsics change. `

- 우리이 가설은 물체의 B.Box를 학습 할때 탐지 모델은 암묵적으로 크기와 특징을 Train 도메인에서 학습 할것이라고 가정하는 것이다. `We hypothesize that, while learning to regress obstacles bounding boxes, a detector model implicitly learns sizes and proportions of objects belonging to the training domain.` 

- 이후에 물체탐지 branch에서 장애물까지의 거리를 평가(evaluation)한다. 그리고 평가 결과를 "dense depth estimations"을 교정 하는데 사용한다. `We can then evaluate estimated obstacle distances from the detection branch and use them as a tool to correct dense depth estimations. `

Let $$m_j$$ be the average distance of the obstacle `j` computed by the detector, $$\hat D_j$$ the average depth estimation within the `j-th` obstacle bounding box, no the number of estimated obstacles,then we compute the correction factor `k` as:
$$
    k = \frac{\frac{1}{n_0}\sum^{n_0}_j m_j}{\frac{1}{n_0}\sum^{n_0}_j \hat D_j}
$$

Finally, we calculate the corrected depth at each pixel i as D˜i = kDi. 

To validate our hypothesis, in Section IV-D we test on target domains with camera focal lengths that differ from the one used for training.

## 4. EXPERIMENTS

### 4.1 Datasets

#### A. Unreal Dataset

#### B. Zurich Forest Dataset

### 4.2 Training and testing details

As baselines, we compare J-MOD2 with:
- The depth estimation method proposed in [13].
- Our implementation of the multi-scale Eigen’s model [12].
- A simple obstacle detector, consisting of our proposed model, trained without the depth estimation branch.

```
[13] M. Mancini, G. Costante, P. Valigi, T. A. Ciarfuglia, J. Delmerico, and D. Scaramuzza, “Towards domain independence for learning-based monocular depth estimation,” IEEE Robotics and Automation Letters, 2017
[12] D. Eigen and R. Fergus, “Predicting depth, surface normals and semantic labels with a common multi-scale convolutional architecture,” in Proceedings of the IEEE International Conference on Computer Vision, 2015, pp. 2650–2658.
```
### 4.3 Test on UnrealDataset

### 4.4 Testing robustness to focal length

### 4.5 Test: Zurich Forest Dataset

### 4.6 Navigation experiments

## 5. CONCLUSION AND FUTURE WORK

- **물체 탐지**와 **깊이 예측**이 가능한 end-to-end 모델인 J-MOD2를 제안 한다. `In this work, we proposed J-MOD2, a novel end-to-end deep architecture for joint obstacle detection and depth estimation. `

- 가상 데이터와 실제 데이터를 이용하여 테스트 하였다. `We demonstrated its effectiveness in detecting obstacles on synthetic and real-world datasets. `

- 초점거리(focal length)와 외형에 강건성을 가지는지 테스트 하였다. `We tested its robustness to appearance and camera focal length changes.`

- 추가적으로 드론에 적용하여 산악지대 에서 테스트 하였다. `Furthermore, we deployed J-MOD2 as an obstacle detector and 3D mapping module in a full MAV navigation system and we tested it on a highly photo-realistic simulated forests cenario. `

- 성능이 좋다. `We showed how J-MOD2 dramatically improves mapping quality in a previously unknown scenario, leading to a substantial lower navigation failure rate than other SotA depth estimators. `

- 향후 계획 In future works, we plan to further improve robustness over appearance changes, as this is the major challenge for the effective deployment of these algorithms in practical real-world scenarios.