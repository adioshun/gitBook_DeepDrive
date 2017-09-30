|논문명|Overview of Environment Perception for Intelligent Vehicles
|-|-|
|저자(소속)|Hao Zhu (Chongqing University)|
|학회/년도| IEEE TRANSACTIONS 2017, [논문](http://eprints.whiterose.ac.uk/111149/1/Overview_paper_IEEE_ITS_2017.pdf)|
|키워드| Lane/road detection, Traffic sign recognition, Vehicle tracking, Behavior analysis, Scene understanding|
|참고||
|코드||

# Overview of Environment Perception for Intelligent Vehicles

- lane and road detection
- traffic sign recognition
- vehicle tracking
- behavior analysis
- scene understanding

## I. INTRODUCTION

|![](https://i.imgur.com/B4DrZAr.png)|![](https://i.imgur.com/sqCqaRs.png)|
|-|-|

자율 주행 차의 주요 기술 [3]
- environment perception and modeling
- Localization and map building
- path planning and decision-making
- motion control

The main functions of environment perception are based on 
- lane and road detection
- traffic sign recognition
- vehicle tracking and behavior analysis
- scene understanding.

```
[3] H. Cheng, Autonomous Intelligent Vehicles Theory, Algorithms, and Implementation. Springer, 2011.
```

> 논문 목적 :  survey of the stateof-the-art approaches and the popular techniques used in
environment perception for intelligent vehicles.

## II. VEHICULAR SENSORS

- GPS
- INS (Inertial navigation system)
- Radar : However, measurements are usually noisy and need to be filtered extensively [7].
- LiDAR : Compared with Radar, LiDAR provides a much wider fieldof-view and cleaner measurements. However, LiDAR is more sensitive to precipitation [7].
- Vision : camera, 야간카메라, infrared night vision, stereo vision

```
[7] S. Sivaraman, “Learning, modeling, and understanding vehicle surround using multi-modal sensing,” Ph.D. dissertation, Uinversity of California, San Diego, 2013.
```

센서 & 데이터 퓨젼 

```
[4] C. Lundquist, “Sensor fusion for automotive applications,” Ph.D. dissertation, Linkoping University, Link ¨ oping, 2011. ¨
[5] N.-E. E. Faouzi, H. Leung, and A. Kurian, “Data fusion in intelligent transportation systems: Progress and challenges : A survey,” Information Fusion, vol. 12, no. 1, pp. 4 – 10, 2011.
```



## III. LANE AND ROAD DETECTION

Some surveys on recent developments in lane and road detection can be found in [10], [11], [12].


```
[10] V. Kastrinaki, M. Zervakis, and K. Kalaitzakis, “A survey of video processing techniques for traffic applications,” Image and Vision Computing, vol. 21, no. 4, pp. 359 – 381, 2003.
[11] J. C. McCall and M. M. Trivedi, “Video-based lane estimation and tracking for driver assistance: survey, system, and evaluation,” IEEE Transactions on Intelligent Transportation Systems, vol. 7, no. 1, pp. 20–37, 2006.
[12] A. Bar Hillel, R. Lerner, D. Levi, and G. Raz, “Recent progress in road and lane detection: A survey,” Machine Vision and Applications, vol. 25, no. 3, pp. 727–745, 2014.
```

The characteristics of these systems are given as follows: 
- (1) 차선 이탈 경고 Lane departure warning: By predicting the trajectory of the host vehicle, a lane departure warning system warns for near lane departure events.
- (2) 크루즈 장치 Adaptive cruise control: In the host lane, the adaptive cruise control follows the nearest vehicle with safe headway distance.
- (3) 차선 유지 장치 Lane keeping or centering: The lane keeping or centering system keeps the host vehicles in the lane center.
- (4) 차선 변경 도움 장치Lane change assist: The lane change assisting system requires the host vehicle to change the lane without danger of colliding with any object.


기술 개발이 어려운 점 The difficulty of a lane and road detection system is `condition diversity`,
- lane and road appearance diversity
- image clarity
- poor visibility

따라서, 기술 개발시 아래와 같은 가정을 하고 개발 한다. These assumptions are summarized as follows
[11]:
- (1) The lane/road texture is consistent.
- (2) The lane/road width is locally constant.
- (3) Road marking follows strict rules for appearance or placement.
- (4) The road is a flat plane or follows a strict model for elevation change.

차선 탐지의 주요 3요소 
- pre-processing
- feature extraction
- model fitting

### 3.1 Pre-processing

전처리 목적 : The objective of pre-processing is to `enhance feature of interest` and `reduce clutter`.

전처리 방법의 분류 `Preprocessing methods can be categorized into two classes`
- removing illumination-related effects 
- pruning irrelevant or misleading image parts [12].


#### A. removing illumination-related effects 

날씨, 시간등에 의한 illumination은 제거 되어야 한다. 

방법 들 
- Information fusion methods from heterogeneous sensors are effective to solve this problem.
- In [13], a perceptual fog density prediction model was proposed by using natural scene statistics and fog aware statistical features 
- Observations and modeling of fog were studied by cloud Radar and optical sensors in [14].

```
[13] L. K. Choi, J. You, and A. Bovik, “Referenceless prediction of perceptual fog density and perceptual image defogging,” IEEE Transactions on Image Processing, vol. 24, no. 11, pp. 3888–3901, 2015.
[14] Y. Li, P. Hoogeboom, and H. Russchenberg, “Observations and modeling of fog by cloud radar and optical sensors,” in Proceedings of the 11th European Radar Conference, Oct 2014, pp. 521–524
```

그림자에 의한 문제도 제거 되어야 한다. 
- Many color space transformations which are not affected by illumination changes, were proposed to eliminate the shadow effect [15], [16], [17].
- In [18], three different shadow-free images (1D, 2D, and 3D) were investigated according to simple constraints on lighting and cameras.

```
[15] H.-Y. Cheng, B.-S. Jeng, P.-T. Tseng, and K.-C. Fan, “Lane detection with moving vehicles in the traffic scenes,” IEEE Transactions on Intelligent Transportation Systems, vol. 7, no. 4, pp. 571–582, 2006.
[16] I. Katramados, S. Crumpler, and T. Breckon, “Real-time traversable surface detection by colour space fusion and temporal analysis,” in Computer Vision Systems, ser. Lecture Notes in Computer Science, M. Fritz, B. Schiele, and J. Piater, Eds. Springer Berlin Heidelberg, 2009, vol. 5815, pp. 265–274.
[17] J. Alvarez, A. Lopez, and R. Baldrich, “Shadow resistant road segmentation from a mobile monocular system,” in Pattern Recognition and Image Analysis, ser. Lecture Notes in Computer Science. Springer Berlin Heidelberg, 2007, vol. 4478, pp. 9–16.
[18] G. Finlayson, S. Hordley, C. Lu, and M. Drew, “On the removal of shadows from images,” IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 28, no. 1, pp. 59–68, 2006
```

#### B. pruning irrelevant or misleading image parts

도로 탐지에서 불필요한 부분(차량, 보행자, 하늘)은 pruning 처리 되었다. 이를 위한 traditional approach는 Regions of Interest (ROI)후 ROI에 대해서만 feature extraction을 수행 하는 것이다. 

- ROI extraction was performed by using color and intensity information [19]. 

- In [20], a set of Regions of Interests (ROIs) was detected by a `Motion Stereo technique`
to improve the pedestrian detector’s performance. 

- Using dense stereo for both ROIs generation and pedestrian classification, a novel pedestrian detection system for intelligent vehicles was presented in [21].

```
[19] M. C. Le, S. L. Phung, and A. Bouzerdoum, “Pedestrian lane detection for assistive navigation of blind people,” in Proceedings of the 21st International Conference on Pattern Recognition, 2012, pp. 2594–2597.
[20] M. Bertozzi, L. Bombini, P. Cerri, P. Medici, P. Antonello, and M. Miglietta, “Obstacle detection and classification fusing radar and vision,” in Proceedings of IEEE Intelligent Vehicles Symposium, June 2008, pp. 608–613.
[21] C. Keller, M. Enzweiler, M. Rohrbach, D. Fernandez Llorca, C. Schnorr, and D. Gavrila, “The benefits of dense stereo for pedestrian detection,” IEEE Transactions on Intelligent Transportation Systems, vol. 12, no. 4, pp. 1096–1106, 2011.
```

### 3.2 Feature extraction

#### A. Lane feature

일반적인 방법은 모양과 색상 정보를 이용하는 것이다. In general, a lane feature can be detected by appearance of `shape` or `color` [12]. 

- 모양 : solid line, dashed line,segmented line, and circular reflector. 
- 색상 : white, yellow, orange and cyan.

The simplest approach of lane feature extraction assumes that the lane color is known. 

##### 가. median local threshold

Using the median local threshold method and a morphological operation, lane markings can be extracted [22]. 

##### 나. adaptive threshold
An adaptive threshold method was proposed to lane markings detection in[23].



##### 다. 모양, 색상외 다른 특징 추출을 이용하는 방법 

Other lane feature extraction methods were based on one or more assumptions [11], [23].



The detection methods are based on differences in the appearance of lanes compared with the appearance of the whole road. 

With this assumption, gradient-based feature extraction methods can be applied. 

In [11], a steerable filterw as developed by computing three separable convolutions to a lane tracking system for robust lane detection.

In [24], [25], [26], the lane marks were assumed to have narrower shape and brighter intensity than their surroundings.

Compared with the steerable filter, a method with fixed vertical and horizontal kernels was proposed with the advantage of fast execution and disadvantage of low sensitivity to certain line orientations [24]. 

In [27], the scale of kernel can be adjusted.

Furthermore, some practical techniques ([28], [29], [30],[31]) were applied using mapping images to remove the perspective effect [12]. 

However, the inverse perspective mapping(IPM) assumes that the road should be free of obstacles.

##### 센서 퓨젼 (Lidar + Camera)

In order to resolve this problem, a robust method based on multimodal sensor fusion was proposed. 

Data from a laser range finder and the cameras were fused, so that the mappingwas not computed in the regions with obstacles [32].

By zooming into the vanishing point of the lanes, the lane markings will only move on the same straight lines they are on [33]. 

Based on this fact, a lane feature extraction approach was presented [33], [34]..

#### B. Road feature

Roads are more complicated than lanes as they are not bounded by man-made markings. 

> `도로 인식`은 사람이 만든 표시(차선)이 없기 때문에 차선 인식 보다 더 어렵다. 

Under different environments, different cues can be used for road boundaries. 

For example, curbs can be used for urban roads and barriers can be found in highway roads [12]. 

Differentroad features should be extracted in different environmentsbased on different assumptions.

##### 가. 도로에 고도차가 있다는 가정 

Roads are assumed to have an elevation gap with its surrounding [24], [35], [36], [37]. 

Stereo vision-based methodswere applied to extract the scene structure [35]. 

In [24], [36],[38], a road markings extraction method is proposed basedon three dimensional (3-D) data and a LiDAR system. 

In[37], a method was proposed to estimate the road region inimages captured by vehicle-mounted monocular camera. 

Usingan approach based on the alignment of two successive images,the road region was determined by calculating the differences between the previous and current warped images.

Another method for road feature extraction is based on road appearance and color, where it is assumed that the road has uniform appearance. 

In [17], a region growing method wasapplied to road segmentation. 

In [11], the road appearanceconstancy was assumed. 

Some methods based on `road color features` were considered in [39], [40]. 

A road-area detection algorithm based on color images was proposed. This algorithm is composed of two modules: 
- boundaries were estimated using the intensity image 
- road areas were detected using the full color image [40].

`Texture` is also used as road feature [41], [42]. 
- Using Gabor filters, texture orientations were computed. 

Then an `edge detection` technique was proposed for the detection of road boundaries [42]. 

###### 성능 향상을 위해 이전 정보(prior information)를 활용 

In order to improve the performance of road detection, methods incorporating prior information have been proposed, 
- temporal coherence [43] : Temporal coherence is averaging the results of consecutive frames. 
- shape restrictions [39] : Shape restrictions mean the modelingof the road shape and restricting the possible road area [44].

Using geographical information systems, an algorithm was proposed to estimate the road profile online and prior to building a road map [44].

### 3.3  Model fitting

The lane and road model can be categorized into three classes[12].
- parametric models
- semi-parametric models
- nonparametric models


### 3.4 Evaluation


## 4. TRAFFIC SIGN RECOGNITION

### 4.1  Segmentation

### 4.2 Shape features

### 4.3 Detection

### 4.4 Evaluation

## 5. VEHICLE DETECTION, TRACKING AND BEHAVIOR ANALYSIS

### 5.1 Vehicle detection

![](https://i.imgur.com/VL5Wvux.png)

Key developments on vehicle detection were summarized in [9], [101]. 

```
[9] S. Sivaraman and M. M. Trivedi, “Looking at vehicles on the road: A survey of vision-based vehicle detection, tracking, and behavior analysis,” IEEE Transactions on Intelligent Transportation Systems, vol. 14, no. 4, pp. 1773–1795, 2013.
[101] S. Zehang, B. George, and M. Ronald, “On-road vehicle detection: a review,” IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 28, no. 5, pp. 694 – 711, 2006.
```


분류 The vehicle detection methods can be categorized into 
- appearance-based 
- motion based[9].


#### A. Appearance-based methods (기존 CV기반 방법)

Many appearance features have been proposed to detect vehicles, such as
- color
- symmetry 
- edges
- HOG features
- Haar-like features

##### 가. Color

Using color information, vehicles can be segmented from the background.

In [102], multivariate decision trees for piecewise linear nonparametric function approximation was used to model the color of a target object from training samples. 

In [103], an adaptive color model was proposed to detect the color features of the objects around the vehicles. 

##### 나. Symmetry

In [104], symmetry as a cue for vehicle detection was studied. 

In [105], a scheme of symmetry axis detection and filtering based on symmetry constraints was proposed


##### 다. edges & HOG features

More recently, simpler image features (e.g., color, symmetry, and edges) have been transformed to robust feature sets.

In [106], vehicles were detected based on their `edges of HOG features` and symmetrical characteristics. 

In [107], `HOG symmetry vectors` were proposed to detect vehicles. 

##### 라. Haar features

Haar features are sensitive to vertical, horizontal, and symmetric structures [9]. 

In [108], Haar and Triangle features were proposed for vehicle detection systems. 

HOG and Haar features were used to detect vehicle in [109].

###### Verification

After generating the hypothesis of locations of possible vehicles, verification is necessary for the presence of vehicles.

`SVM` and `AdaBoost` methods are widely used for vehicle detection. 

A system of integrated HOG feature and SVM classification has been studied in [106], [110]. 

The combination of edge feature and SVM classification was given in [111].

AdaBoost was proposed to classify the symmetry feature and edge feature in [112] and [113], respectively. 

The Haar-like feature and AdaBoost classification has been applied to detect vehicles [114], [115].


#### B. Motion-based methods

In motion-based vehicle detection methods, `optical flow` and `occupancy grids` have been
widely used. 

##### 가. optical flow

In [116], optical flow was proposed to detect any type of frontal collision. 

In [117], the optical flow method was applied to a scene descriptor for classifying urban traffic.

The optical flow was also proposed to analyze road scenes [9], [118]. 

```
[116] E. Martinez, M. Diaz, J. Melenchon, J. A. Montero, I. Iriondo, and J. C. Socoro, “Driving assistance system based on the detection of head-on collisions,” in Proceedings of IEEE Intelligent Vehicles Symposium, 2008, pp. 913–918.
[117] A. Geiger and B. Kitt, “Object flow: A descriptor for classifying traffic motion,” in Proceedings of IEEE Intelligent Vehicles Symposium, 2010, pp. 287–293.
[9] S. Sivaraman and M. M. Trivedi, “Looking at vehicles on the road: A survey of vision-based vehicle detection, tracking, and behavior analysis,” IEEE Transactions on Intelligent Transportation Systems, vol. 14, no. 4, pp. 1773–1795, 2013.
[118] S. Bota and S. Nedevschi, “Tracking multiple objects in urban traffic environments using dense stereo and optical flow,” in Proceedings of the 14th International IEEE Conference on Intelligent Transportation Systems, 2011, pp. 791–796.
```

##### 나. Occupancy grids 

Occupancy grids are proposed for `scene segmentation` and `understanding`. 

In [119], occupancy grids were filtered both temporally and spatially. 

In [120], an occupancy grid tracking solution was proposed based on particles for tracking
the dynamic driving environment.

```
[119] M. Perrollaz, J. D. Yoder, A. Negre, A. Spalanzani, and C. Laugier, “A visibility-based approach for occupancy grid computation in disparity space,” IEEE Transactions on Intelligent Transportation Systems, vol. 13, no. 3, pp. 1383 – 1393, 2012.
[120] R. Danescu, F. Oniga, and S. Nedevschi, “Modeling and tracking the driving environment with a particle-based occupancy grid,” IEEE Transactions on Intelligent Transportation Systems, vol. 12, no. 4, pp. 1331–1342, 2011.
```
### 5.2 Vehicle tracking

목적 : The aim of vehicle tracking is to re-identify and measure dynamics and motion characteristics and to **predict** and estimate the **upcoming position** of vehicles [9]. 

문제점 : The major problems include: 
- A. measurement error uncertainty
- B. data association
- C. necessity to fuse efficiently data from multiple sensors.

#### A. Measurement uncertainty

the **measurement noise** is the main issue of measurement uncertainty. 


##### 가. 가우시안 분포 노이즈 
칼만필터를 사용하면 가우시안 분포 노이즈를 제거 할수 있다. The Kalman filter is the optimal algorithm in a linear system under Gaussian noises.

##### 나. Non-가우시안 분포 노이즈 

하지만 Radar기반 방식에서는 가우시안 분포가 아닌 경우가 있다. However, in **Radar-based tracking** non-Gaussian distributions are often observed [121]. 

해결 방안 분류 [122]: They can be classified as 
- recursive approaches
- batch approaches 

###### The recursive approaches

The recursive approaches are performed online [123], such as 
- the Masreliez filter, 
- multiple model (MM) approaches, 
- Sequential Monte Carlo (SMC) approaches, 
- interacting multiple model (IMM) filters. 

###### The batch approaches

The batch approaches are with offline implementations. 

- In [124], an expectation maximization (EM) algorithm and an IMM algorithm were developed. 

- In [125], a variational Bayesian (VB) algorithm was proposed to estimate the state and parameters in non-Gaussian noise systems.



#### B. Data association

Data association plays an important role in the multi-sensor multi-target systems. 

The algorithms of data association can be divided into 
- explicit data association algorithms 
- implicit data association algorithms [126].

##### 가. explicit data association

- the nearest neighbor (NN) algorithm [127]
- the multihypothesis tracking (MHT) approach [128]
- the probabilistic data association (PDA) approach [129]
- to the joint probability data association (JPDA) algorithms [130], [131]. 

##### 나. implicit data association

In contrast to explicit data association, implicit data association tracking approaches output a set of object hypotheses in an implicit way, such as 
- particle filtering [132], 
- probability hypothesis density (PHD) filtering [133]
- multi-target multi Bernoulli (MeMBer) filtering [134], [135], 
- labeled multi Bernoulli filtering [136].

#### C. Fusion 

The architectures for sensor data fusion can be divided into **centralized** and **decentralized** fusion. 

##### 가. centralized fusion architecture

Combining the overall system measurements, most of the data and information processing steps are performed at the fusion center in centralized fusion. 

In [137], a multi target detection and tracking approach for the case of multiple measurements per target and for an unknown and varying number of targets was proposed. 

In [138], [139], a joint sensor registration and fusion approach was developed for cooperative driving in intelligent transportation systems. 

In [140], [141], a multisensor and multitarget surveillance system was developed based on solving jointly the registration, data association and data fusion problems.

```
[137] T. De Laet, H. Bruyninckx, and J. De Schutter, “Shape-based online multitarget tracking and detection for targets causing multiple measurements: Variational Bayesian clustering and lossless data association,” IEEE Transactions on Pattern Analysis and Machine Intelligence,
vol. 33, no. 12, pp. 2477–2491, 2011.
[138] W. Li and H. Leung, “Simultaneous registration and fusion of multiple dissimilar sensors for cooperative driving,” IEEE Transactions on Intelligent Transportation Systems, vol. 5, no. 2, pp. 84–98, 2004.
[139] D. Huang and H. Leung, “An expectation-maximization-based interacting multiple model approach for cooperative driving systems,” IEEE Transactions on Intelligent Transportation Systems, vol. 6, no. 2, pp. 206–228, 2005.
[140] S. Chen, H. Leung, and l. Boss, “A maximum likelihood approach to joint registration, association and fusion for multi-sensor multi-target tracking,” in Proceedings of International Conference on Information Fusion, 2009, pp. 686–693.
[141] Z. Li, S. Chen, H. Leung, and E. Bosse, “Joint data association, registration, and fusion using EM-KF,” IEEE Transactions on Aerospace and Electronic Systems, vol. 46, no. 2, pp. 496–507, 2010.
```

##### 나. decentralized fusion architecture

For the decentralized fusion architecture, the fusion of tracks can be performed at the tracks level. 

In [142], based on equivalent measurements, a joint sensor registration and trackto-track
fusion approach was proposed. 

In [143], using a pseudo-measurement approach, a joint registration, association and fusion method at distributed architecture was developed.

In [144], using information matrix fusion, a track-to-track fusion approach was presented for automotive environment perception. 

Therefore, many heterogeneous sensor data can be fused for vehicle tracking [145].

```
[142] N. N. Okello and S. Challa, “Joint sensor registration and track-to-track fusion for distributed trackers,” IEEE Transactions on Aerospace and Electronic Systems, vol. 40, no. 3, pp. 808–823, 2004.
[143] H. Zhu, H. Leung, and K. V. Yuen, “A joint data association, registration, and fusion approach for distributed tracking,” Information Sciences, vol. 324, pp. 186–196, 2015.
[144] M. Aeberhard, S. Schlichtharle, N. Kaempchen, and T. Bertram, ¨“Track-to-track fusion with asynchronous sensors using information matrix fusion for surround environment perception,” IEEE Transactions on Intelligent Transportation Systems, vol. 13, no. 4, pp. 1717–1726,
2012.
[145] R. O. Chavez-Garcia and O. Aycard, “Multiple sensor fusion and classification for moving object detection and tracking,” IEEE Transactions on Intelligent Transportation Systems, pp. 1–10, 2015.
```

#### D. Joint lane, vehicle tracking, and vehicle classification:

> 각 서비스들의 정보를 서로 활용하면 성능을 향상할수 있다. 

The performance of vehicle tracking can be improved by utilizing the **lane information** and **vehicle characteristics** to enforce geometric constraints based on the road information.
- The lane tracking performance can be improved by exploiting **vehicle tracking results** and **eliminating spurious lane marking** filter responses from the search space [146]. 
- Vehicle characteristics can be used to enhance **data association** in multi-vehicle
tracking. 

일부 연구에서만 서로의 정보를 활용 하고 있다. `However, few works have explored simultaneous lane, vehicle tracking and classification.` 

- A joint lanes and vehicles tracking system was proposed by a PDA filter using
camera in [147]. 

- In [148], simultaneous lane and vehicle tracking method using camera was applied to improve vehicle detection.

- In [146], a synergistic approach to integrated land and vehicle tracking using camera was proposed for driver assistance. 
 
- In [149], using lane and vehicle information, a maneuvering target was tracked by Radar and image-sensor based measurement. 

- In [150], an integrated system for vehicle tracking and classification was presented. 

![](https://i.imgur.com/Eta2fPM.png)

Table VI highlights key representative works in vehicle detection and tracking.

We performed experiments on KITTI datasets. 

A total of 278 frames were used and results are obtained with the tracking by 
- detection method , 
- the scene flow-based method [158], 
- an L1-based tracking method [159], and 
- a compressive method [160]. 

These algorithms were applied to tracking single vehicle and comparative results from separate video frames results are given in Fig. 6. 

A measure of the distance between the true centerline and the estimated centerline is used
to evaluate these algorithms. 

The tracking results are given in Table. VII. It is observed that the L1-based tracker method
has the best performance.


### 5.3 Behavior analysis

Using the results from the **vehicle detection** and **tracking system**, an analysis of the behaviors of other vehicles can be performed. 

> 차량 탐지와 추적이 가능해지면 행동(context, maneuvers, trajectories, behavior classification) 분석이 가능하다. 

Four characteristics of vehicle behavior are presented, namely 
- context
- maneuvers
- trajectories 
- behavior classification [146].

#### 가. Context

The role of context is important for vehicle behavior analysis. 

In [117], modeling the driving context, the driving environment was classified. 

In [161], a dynamic visual model was designed to detect critical motions of nearby vehicles. 

In [154], the behavior of on-coming vehicles was inferred by motion and depth information.

#### 나. Maneuvers

An overtaking monitoring system was presented in [162]. 

In [163], combining the information provided by Radar and camera, an optical flow method was implemented to detect overtaking vehicles. 

In [154], an IMM was evaluated for inferring the turning behavior of oncoming vehicles. 

In [149], a Markov process was constructed to model the behavior of on-road vehicles.


#### 다. Trajectories

In [164], a long-term prediction method of vehicles was proposed. 

In [165], highway trajectories were clustered using hidden Markov model. 

In [166], vehicle tracking in combination with a long term motion prediction method was presented.


#### 라. Behavior classification

Efficient models such as Gaussian mixture models, Markov models, and Bayesian networks have been validated for vehicle behavior classification. 

In [164], the vehicle behavior was classified by a Gaussian mixture model. 

In [167], the vehicle behavior was modeled by Markov model before their future trajectories was estimated.

In [168], the behavior of vehicles was classified by a Bayesian network.

## 6.  SCENE UNDERSTANDING