# Sensor Fusion

## 1. 정의

센서 퓨전은 여러 개의 센서에서 전송하는 데이터를 지능적으로 결합하여 애플리케이션이나 시스템의 성능을 개선하는 소프트웨어입니다. 즉, 복수의 센서에서 나오는 데이터를 취합하여 개별 센서의 결함을 수정하며 그 결과로 정확한 위치와 방향 정보를 계산할 수 있습니다.
## 2. 분류




### 2.1 Topology 기반 분류 : centralized vs. decentralized

The architectures for sensor data fusion can be divided into centralized and decentralized fusion.

#### 가. centralized fusion architecture

[137] T. De Laet, H. Bruyninckx, and J. De Schutter, “Shape-based online multitarget tracking and detection for targets causing multiple measurements: Variational Bayesian clustering and lossless data association,” IEEE Transactions on Pattern Analysis and Machine Intelligence,
vol. 33, no. 12, pp. 2477–2491, 2011.
[138] W. Li and H. Leung, “Simultaneous registration and fusion of multiple dissimilar sensors for cooperative driving,” IEEE Transactions on Intelligent Transportation Systems, vol. 5, no. 2, pp. 84–98, 2004.
[139] D. Huang and H. Leung, “An expectation-maximization-based interacting multiple model approach for cooperative driving systems,” IEEE Transactions on Intelligent Transportation Systems, vol. 6, no. 2, pp. 206–228, 2005.
[140] S. Chen, H. Leung, and l. Boss, “A maximum likelihood approach to joint registration, association and fusion for multi-sensor multi-target tracking,” in Proceedings of International Conference on Information Fusion, 2009, pp. 686–693.
[141] Z. Li, S. Chen, H. Leung, and E. Bosse, “Joint data association, registration, and fusion using EM-KF,” IEEE Transactions on Aerospace and Electronic Systems, vol. 46, no. 2, pp. 496–507, 2010.

#### 나. decentralized fusion architecture
```
[142] N. N. Okello and S. Challa, “Joint sensor registration and track-to-track fusion for distributed trackers,” IEEE Transactions on Aerospace and Electronic Systems, vol. 40, no. 3, pp. 808–823, 2004.
[143] H. Zhu, H. Leung, and K. V. Yuen, “A joint data association, registration, and fusion approach for distributed tracking,” Information Sciences, vol. 324, pp. 186–196, 2015.
[144] M. Aeberhard, S. Schlichtharle, N. Kaempchen, and T. Bertram, ¨“Track-to-track fusion with asynchronous sensors using information matrix fusion for surround environment perception,” IEEE Transactions on Intelligent Transportation Systems, vol. 13, no. 4, pp. 1717–1726,
2012.
[145] R. O. Chavez-Garcia and O. Aycard, “Multiple sensor fusion and classification for moving object detection and tracking,” IEEE Transactions on Intelligent Transportation Systems, pp. 1–10, 2015.
```

---
- 이미지 + optical flow + LiDAR가 함꺼번에 합쳐져서 DNN에 입력으로 이용 `RGB image,optical flow, and LiDAR range images are combined to forma six channel input to a deep neural network [20] for object detection.`

- 동일 모델을 이용하여 joint representation학습에도 활용 `The same network can also be used for different modalities to learn a joint representation [21].`

```
[20] M. Giering, V. Venugopalan, and K. Reddy, “Multi-modal sensor registration for vehicle perception via deep neural networks,” in High Performance Extreme Computing Conference (HPEC), 2015 IEEE,Sept 2015, pp. 1–6.
[21] L. Castrejon, Y. Aytar, C. Vondrick, H. Pirsiavash, and A. Torralba,“Learning aligned cross-modal representations from weakly aligned data,” in 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), June 2016, pp. 2940–2949.
```


### 2.2 알고리즘 기반 분류 : **early** Vs. **late** fusion.


![](https://i.imgur.com/5x0JuYR.png)
[`Shashibushan Yenkanchi, MULTI SENSOR DATA FUSION FOR AUTONOMOUS VEHICLES, 2016`]

- The fusion methods are divided into two categories, namely **early** and **late** fusion.

- 앞단/뒷단 퓨전의 다른점은 데이터를 합치는 방법의 차이로 발생 한다. `Early fusion and late fusion differ in the way they **integrate the results from feature extraction** on the various modalities. `

```
36. Henry P., Krainin M., Herbst E., Ren X., Fox D. RGB-D mapping: Using depth cameras for dense 3D modeling of indoor environments; Proceedings of the 12th International Symposium on Experimental Robotics (ISER. Citeseer); New Delhi and Agra, India. 18–21 December 2010.
37. Gupta S., Arbelaez P., Malik J. Perceptual organization and recognition of indoor scenes from RGB-D images; Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition; Portland, OR, USA. 23–28 June 2013; pp. 564–571.
38. Munera E., Poza-Lujan J.L., Posadas-Yagüe J.L., Simó-Ten J.E., Noguera J.F.B. Dynamic reconfiguration of a rgbd sensor based on qos and qoc requirements in distributed systems. Sensors. 2015

39. Adarve J.D., Perrollaz M., Makris A., Laugier C. Computing occupancy grids from multiple sensors using linear opinion pools; Proceedings of the 2012 IEEE International Conference on Robotics and Automation (ICRA); St. Paul, MN, USA. 14–18 May 2012; pp. 4074–4079.
40. Oh S.I., Kang H.B. Fast Occupancy Grid Filtering Using Grid Cell Clusters From LiDAR and Stereo Vision Sensor Data. IEEE Sens. J. 2016;16:7258–7266. doi: 10.1109/JSEN.2016.2598600. [Cross Ref]

41. González A., Villalonga G., Xu J., Vázquez D., Amores J., López A.M. Multiview random forest of local experts combining rgb and LiDAR data for pedestrian detection; Proceedings of the 2015 IEEE Intelligent Vehicles Symposium (IV); Seoul, Korea. 28 June–1 July 2015; pp. 356–361.

42. Nuss D., Yuan T., Krehl G., Stuebler M., Reuter S., Dietmayer K. Fusion of laser and radar sensor data with a sequential Monte Carlo Bayesian occupancy filter; Proceedings of the 2015 IEEE Intelligent Vehicles Symposium (IV); Seoul, Korea. 28 June–1 July 2015; pp. 1074–1081.
43. Cho H., Seo Y.W., Kumar B.V., Rajkumar R.R. A multi-sensor fusion system for moving object detection and tracking in urban driving environments; Proceedings of the 2014 IEEE International Conference on Robotics and Automation (ICRA); Hong Kong, China. 31 May–7 June 2014; pp. 1836–1843.
```


---


# Two data-fusion scheme

> Sang-Il Oh\(Catholic University\), Object Detection and Classification by Decision-Level Fusion for Intelligent Vehicle Systems 

The data-fusion scheme is generally categorized into two types, namely early and late fusion.

## 1. The early-fusion method
- 방법 : 
	- Raw데이터 병합, feature 연결 `fuses two or more data by combining raw data or concatenating feature descriptors. `
	- 측정값은 아래 방법들로 Fuse됨 `the measurements are fused by`
		-  mapping them together,
		- by concatenation, 
		- probabilistic fusion [41,44,45].

- 단점 
	- 장비의 고장 및 환경으로 인한 측정값의 경우 결과물이 ambiguous를 포함하고 있음 `it often cannot handle incomplete measurements.`
	- 제약 : However, the early fusion method suffers from problems of **non-overlapping regions** and **uncertainties**.

- 해결책 : To solve these problems, the **decision-level fusion method** is used as a **late fusion** method.


## 2. The late-fusion method

- 방법 
	- 각 센서별로 독립적으로 탐지 및 분류 진행` independently performs detection and classification from each sensor modality`
	- 각 결과값에 대하여 fuse를 하여 최종 결과를 획득 `Subsequently, the classified outputs are fused at the decision level for final classification.`

- 장점 `By using the decision-level fusion scheme for the object detection and classification task, `
	- 센서가 제대로 동작 하지 않는 상황에 대처 가능 `we can prevent the autonomous driving system from becoming non-functional when information conflicts are introduced to more than one sensor. `
	- 각 센서의 신뢰성 및 plausibility를 고려 할수 있음 `In addition, the reliability and plausibility of each sensor can be considered.`

---


## 2. FUSION SCHEMES

> Cees G.M. Snoek\(University of Amsterdam), Early versus Late Fusion in Semantic Video Analysis

## 1. Early Fusion

![](https://i.imgur.com/U1BUskU.png)

- unimodal 특징을 추출 하는 단계 부터 시작한다. `Indexing approaches that rely on early fusion first extract unimodal features. `

- 여러 unimodal을 분석후 추출된 특징은 하나의 Representation으로 합쳐 진다. `After analysis of the various unimodal streams, the extracted features are combined into a single representation. `

- In [6] unimodal 특징 백터를 연결 하여서 합쳐진 멀티모달 representation을 얻었다. `for example, we used concatenation of unimodal feature vectors to obtain a fused multimedia representation. `
- 그 이후 지도기반 분류기 적용 After combination of unimodal features in a multimodal representation, early fusion methods rely on supervised learning to classify semantic concepts.

> Early Fusion : 학습전에 unimodal 특징을 합침 `Fusion scheme that integrates unimodal features before learning concepts.`

- 특징이 시작 단계부터 합쳐졌기 때문에 **truly multimedia feature representation**를 사용 하게 된다. `Early fusion yields a truly multimedia feature representation, since the features are integrated from the start. `

- 장점 : 한번의 학습 Phase만 필요 `An added advantage is the requirement of one learning phase only.`

- 단점 : common representation로 합치기가 어려움(??) `Disadvantage of the approach is the difficulty to combine features into a common representation. `

## 2. Late Fusion

![](https://i.imgur.com/QFR8Xpp.png)

- unimodal 특징을 추출 하는 단계 부터 시작한다 `Indexing approaches that rely on late fusion also start with extraction of unimodal features. `

- 앞단 퓨전과 다르게 뒷단 퓨전은 unimodal 특징에서 바로 학습을 진행 한다. `In contrast to early fusion, (where features are then combined into a multimodal representation), approaches for late fusion learn semantic concepts directly from unimodal features. `

- In [9] for example,separate generative probabilistic models are learned for the visual and textual modality.

- 각 점수들은 합쳐져서 최종 탐지 점수 떄 사용 된다. `These scores are combined afterwards to yield a final detection score. `

- 일반적으로 뒷단 퓨전은 학습된 unimodal 점수를 multimodal representation로 합친다. `In general, late fusion schemes combine learned unimodal scores into a multimodal representation. `

- Then late fusion methods rely on supervised learning to classify semantic concepts.

> Late Fusion : 먼저 unimodal 을 각각의 학습된 결과로 reduece시킨후 이 결과를 합쳐서 활용함. Fusion scheme that first reduces unimodal features to separately learned concept scores, then these scores are integrated to learn concepts.

- 뒷단 합습은 **각 modalities의 강점(strength)**에 중점을 둔다. `Late fusion focuses on the individual strength of modalities.`

- Unimodal concept detection scores are fused into a multimodal semantic representation rather than a feature representation.

- 단점 #1 : 각 modality 마다 학습이 되어야 함으로 자원 소모가 크다. ` A big disadvantage of late fusion schemes is its expensiveness in terms of the learning effort, as every modality requires a separate supervised learning stage. `
- Moreover,the combined representation requires an additional learning stage.

- 단점 #2 : Another disadvantage of the late fusion approach is the **potential loss of correlation** in mixed feature space.


---

# MULTI-SENSOR DATA FUSION METHODS

> Raja Sekhar Rao Dheekonda, [Object Detection from a Vehicle using Deep Learning Network and Future Integration with Multi-Sensor Fusion Algorithm](https://scholarworks.iupui.edu/bitstream/handle/1805/14903/Dheekonda_2017_object.pdf?sequence=1), 2017

## 1. Probabilistic Methods

확률 기반 방법론의 제약 `The main limitations of probabilistic methods for information fusion are [11] `
- complexity (need large number of probabilities), 
- inconsistency (difficult to specify consistent set of beliefs in terms of probability) and 
- model precision (precise probabilities about almost unknown events).

### 1.1 Occupancy Grids

POG는 **베이지안 데이터 퓨전** 방법을 구현 하는 가장 간단한 방법이다. `Probabilistic occupancy grids (POGs) are conceptually the simplest approach to implement Bayesian data fusion methods. `

POG는 간단하지만 여러 문제를 다룰 수 있다. `Although simple, POGs can be applied to different problems within the perception task: `
- mapping [12], 
- moving object detection [13], 
- 센서퓨전 `sensor fusion [14]`.

### 1.2 Kalman Filter (KF)

KF features make it suited to deal with multi-sensor estimation and data fusion problems [11]. 

- First, its explicit description of processes and observations allows a wide variety of different sensor models to be incorporated within the basic algorithm.
- Second, the consistent use of statistical measures of uncertainty makes it possible to quantitatively evaluate the role each sensor plays in overall system performance.


### 1.3 Monte Carlo (MC) Methods

퓨전할 값이 **비선형** 조건일경우 유용함 `MC methods are well suited for problems where state transition models and observation models are highly non-linear [11].` 

비 선형 조건에 유용한 이유 
- The reason for this is that sample-based methods can represent very general probability densities. 
- In particular, multi-modal or multiple hypothesis density functions are well handled by Monte Carlo techniques [12].

## 2. Non-Probabilistic Methods

### 2.1 Interval Calculus (IC)

정의 : 불확실성을 바운드 값으로 표현 `In this method, uncertainty is represented by bound values. `

확률 기반 대비 강점 : One major advantage compared to probabilistic method is that IC provides better measures of uncertainties in absence of probability information but the errors of sensor data are bounded to a certain value. 

 However, IC are not generally used in data fusion because of the difficulty to get results that converge to a desired value; and the difficulty to encode dependencies between variables which are at the core of many data fusion problems [11].


### 2.2 Fuzzy Logic

Fuzzy logic is a popular method in control and sensor fusion to represent uncertainty where reasoning is based on degrees of truth rather than absolute value. 

But this method becomes more complex with the increase of sensor inputs. 

Also, validation of this method needs extensive testing where safety is an important factor [15].


### 2.3 Evidence Theory (ET)

The advantage of ET is its ability to represent incomplete evidence, total ignorance and the lack of a need for a priori probabilities [11]. 

In the field of intelligent vehicle perception there is a variety of imperfect information: uncertain or imprecise. 

For example, objects are missing (occlusions), sensor cannot measure all relevant attributes of the object (hardware limitations), and when an observation is ambiguous (partial object detection). 

But with higher number of hypotheses ET becomes less computational tractable.


---

## Sensor fusion methods

> [An Introduction to Sensor Fusion](https://www.researchgate.net/publication/267771481), 2015

### 1. Smoothing, Filtering, and Prediction

![](https://i.imgur.com/SrKJ9nJ.png)

- Smoothing (m < 0): The change of a process entity shall be reconstructed
after a series of measurements has been performed. For each instant
of interest, several measurements from previous, actual, and following
instants are used in order to estimate the value of the process variable.While the measurements have to be recorded in real time, the smoothing
algorithm can be performed offline.

- Filtering (m = 0): The actual state of a process entity shall be estimated
by using an actual measurement and information gained from previous
measurements. Usually, filtering is performed in real time.

- Prediction (m > 0): The actual state of a process entity shall be estimated
by using a history of previous measurements. The prediction problem
requires an adequate system model in order to produce a meaningful es-
timation. Typically, prediction is performed in real time.




### 2. Kalman Filtering

> 생략

### 3. Inference Methods


- Inference methods are used for decision fusion, 
- i. e., to take a decision based on given knowledge.


### 4. Occupancy Maps

- two-dimensional raster image uniformly distributed over the robot’s working space.

### 5. Certainty Grid

- A certainty grid is a special form of an occupancy ma


---

| 논문명 | Multi-View 3D Object Detection Network for Autonomous Driving |
| --- | --- |
| 저자\(소속\) | Xiaozhi Chen \(칭화대\), Bo Li \(Baidu\) |
| 학회/년도 | 2017, [논문](https://arxiv.org/pdf/1611.07759.pdf) |



#### B. Deep Fusion.

![](http://i.imgur.com/1XqvE4Q.png)

서로 다른 Feature의 정보를 합치는 방법

* 기존 : usually use early fusion \[1\] or late fusion \[23, 13\].
* 제안 : Inspired by \[15, 27\], we employ a deep fusion approach, which fuses multi-view features hierarchically.

##### 가. early fusion

For a network that has L layers, early fusion combines features $$\{f_v\}$$ from multiple views in the input stage:
![](http://i.imgur.com/6BRrT0N.png)

* $$\{H_l, l = 1, ..., L\} $$ : feature transformation functions
* $$\oplus$$ : a join operation \(e.g., concatenation, summation\)

##### 나. late fusion

In contrast, late fusion uses seperate subnetworks to learn feature transformation independently and combines their outputs in the prediction stage:

![](http://i.imgur.com/YL74QSz.png)

##### 다. deep fusion

To enable more interactions among features of the intermediate layers from different views, we design the following deep fusion process:

![](http://i.imgur.com/CWqcudp.png)

We use element-wise mean for the join operation for deep fusion since it is more flexible when combined with droppath training \[15\].





---

|논문명 |Object Detection and Tracking with Side Cameras and RADAR in an Automotive Context |
| --- | --- |
| 저자\(소속\) | Peter Hofmann\(Hella Aglaia Mobile Vision\) |
| 학회/년도 | 석사학위 2013, [논문](http://www.mi.fu-berlin.de/inf/groups/ag-ki/Theses/Completed-theses/Master_Diploma-theses/2013/Hofmann/Master-Hofmann.pdf?1381479774) |
| 키워드 | |
| 데이터셋(센서)/모델 |RADAR + Side Cameras, |
| 참고 | |
| 코드 | |


### 1.2 Sensor Fusion

###### [ 정의 ]

Data fusion techniques combine data from multiple sensors and related information to achieve more specific inferences than could be achieved by using a single, independent sensor. [HL01]

###### [ 용어 ]

- A sensor : a device which provides information of the environment in any form of raw data.

- Feature extraction : the process of extracting meaningful information from the raw data of a sensor
- e.g. points that represent corners in a camera image.

- State estimation : the current state based on the given input,
- e.g. the position of a tracked vehicle

###### [ 분류 ]

- In [HL01] these are referenced as
- Data Level Fusion,
- Feature Level Fusion
- Declaration Level Fusion.

#### A. Data Level Fusion

![](https://i.imgur.com/VISRuZz.png)

**Data Level** Fusion or **Low Level** Sensor Fusion (Figure 1.1) describes
- a method of combining raw data from different sensors with each other,
- e.g. having a calibrated camera and a calibrated Time-of-Flight (ToF) depth-sensor which creates a depth map of the environment, each camera pixel can be mapped to a distance measurement of the ToF sensor and vice versa.

#### B. Feature Level Fusion

![](https://i.imgur.com/NQv8AFk.png)

In **Feature Level** Fusion (Figure 1.2) or **Mid-Level** Fusion,
- the sensor data is presented via feature vectors which describe meaningful data extracted from the raw data.
- These feature vectors build the base for fusion.
- 3D reconstructio서 사용 `This method can be found in 3D-reconstruction for example. `
- 여러 카메라에서 찍은 사진을 활용 하는 방법 `In this approach image features from different cameras are extracted to identify corresponding points in each image of
different camera views.`

#### A. Declaration Level Fusion

![](https://i.imgur.com/ezCh0VE.png)

**Declaration Level** Fusion or **High Level** Fusion (Figure 1.3) is
- the combination of independent **state hypotheses** from different sensors.
- All sensors estimate the state **individually**.
- The final state is a fusion of all state hypotheses from the different sensors.
- 칼만필터가 대표적 구현예임`The most famous implementation of this approach is probably the Kalman Filter [KB61]. `


---

### 1.4 State of the Art

#### 1.4.1 RADAR-based Tracking Approaches
#### 1.4.2 Camera-based Approaches
#### 1.4.3 Sensor Fusion Approaches

- 최근 연구는 3D 센서에 집중되어 있다. `Current research mostly focuses on sensors which provide 3-dimensional information of the environment. `

###### [LiDAR + Camera]

- One of the recent approaches which utilize sensor fusion is [ZXY12].
- The approach combines a **LIDAR sensor** with **camera data**.
- LIDAR sensor의 Distance Map에서 **RANSAC**와 **3D adjacency**를 이용하여 지면과 물체를 구분 할수 있다. `The distance map is used to classify parts of the image to ground plane or obstacles using RANSAC and 3D adjacency. `
- image patches are classified to different classes by evaluating color histograms, texture descriptors from **Gaussian** and **Garbor filtered** images as well as local binary patterns.

- Resulting in 107 features, each patch is classified by a Multi-Layer-Perceptron to different categories.

- The size of the object determined by the LIDAR obstacle estimation as well as labels from the image analysis are passed into a fuzzy logic frame workwhich returns three labels – environment, middle high or obstacle.

```
[ZXY12] Gangqiang Zhao, Xuhong Xiao, and Junsong Yuan. Fusion of velodyne and camera data for scene parsing. In Information Fusion (FUSION), 2012 15th International Conference on, page 1172–1179, 2012
```

###### [RADAR + LiDAR]

- In [VBA08] a framework for **self-location** and **mapping** is presented.

- This approach is based on an **occupancy grid** that is used to fuse information from **RADAR** and **LIDAR**.
- An occupancy grid discretizes the environment space into small two dimensional grid tiles.
- The **LIDAR sensor** is used to **estimate** a **probability** of a grid cell to be occupied.
- A **high probability** means there is an **obstacle** in the respective grid cell.

- 이동하는 물체의 탐지는 해당 그리드값의 변화 감지를 통해 알수 있다. `Moving objects are detected through changes in the occupancy of grid cells. `
- Basically, if a cell is occupied at a time point, and in the next timestep, the adjacent cell is detected to be occupied, this is assumed as a motion.

```
[VBA08] Trung-Dung Vu, Julien Burlet, and Olivier Aycard. Grid-based localization and online mapping with moving objects detection and tracking: new results. In Intelligent Vehicles Symposium, 2008 IEEE, page 684–689, 2008.
```

###### [RADAR + Laser ]

- A similar method of fusing short range RADAR and laser measurements is proposed in [PVB+09].

- The system covers more performance optimizations than[VBA08].

- Instead of estimating a **probability representation**, the grid cells are either occupied or empty based on the number of measurements of the laser scanner for the respective cell.

- Adjacent cells that are occupied are merged to an object.

- A Kalman filter [KB61] is used to track the detected objects.

```
[KB61] Rudolph E. Kalman and Richard S. Bucy. New results in linear filtering
and prediction theory. Journal of Basic Engineering, 83(3):95–108, 1961
```

###### [ RADAR+camera ]

- The approach proposed in [ABC07] shows a fusion of RADAR and camera
- in which the camera is used to verify and optimize RADAR object tracks.

- The camera is oriented to the front.

- The center points of RADAR objects are projected into the image based on the camera calibration.

- The symmetry of image sections around the projected point is estimated.

- Ideally, the symmetry is large around the RADAR hypothesis as front views and rear views of vehicles are symmetric.

- Searching for higher symmetry values in a predefined environment around the RADAR hypothesis is used to correct the position estimate.

- However, this approach does only work for scenarios in which vehicles are viewed from the rear or front.

```
[ABC07] Giancarlo Alessandretti, Alberto Broggi, and Pietro Cerri. Vehicle and guard rail detection using radar and vision data fusion. IEEE Transactions on Intelligent Transportation Systems, 8(1):95–105, March 2007.
```

---

|논문명 |Multiple Sensor Fusion and Classification for Moving Object Detection and Tracking |
| --- | --- |
| 저자\(소속\) | Ricardo Omar Chavez-Garcia |
| 학회/년도 | IEEE TRANSACTIONS 2016, [논문](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7283636) |
| 키워드 | |
| 데이터셋(센서)/모델 | |
| 참고 | |
| 코드 | |

## 2. RELATED WORK
![](https://i.imgur.com/X0UK5vK.png)
Fig. 2 shows the different fusion levels inside a perceptionsystem.

- **low level** fusion is performed within **SLAM component**,
- **detection** and **track level** fusions are performed within **DATMO component**.

- At detection level,
- fusion is performed between lists of moving object detections provided by individual sensors.

- At track level,
- lists of tracks from individual sensor modules are fused to produce the final list of tracks.

### 2.1

Promising SLAM results obtained in [1]–[3] motivated our focus on the DATMO component.


###### [Vu [1] and Wang [3]]

- Whilst Vu [1] and Wang [3]use an almost deterministic approach to perform the association in tracking, we use an evidential approach based on mass distributions over the set of different class hypotheses.


### 2.2 track level

- Multi-sensor fusion at **track level** requires a list of updated tracks from each sensor to fuse them into a combined list of tracks.

###### [2, 4, 5]

- The works in [2], [4], [5] solve this problem focusing on the association problem between lists of tracks, and implementing stochastic mechanisms to combine the related objects.

- By using an effective fusion strategy at this level, false tracks can be reduced.

- This level is characterized by including classification information as complementary to the final output.

### 2.3 detection level

- Fusion at **detection level** aims at gathering and combining early data from sensor detections.

###### [6]

- Labayrade et al. propose to work at this level to reduce the number of mis-detections that can lead to false tracks [6].

###### [7, 8]

- Other works focus on data redundancy from active and passive sensors, and follow physical or learning constrains to increase the certainty of object detection[7], [8].

- These works do not include all the available kinetic and appearance information.

- Moreover, at this level, appearance information from sensor measurements is not considered as important as the kinetic data to discriminate moving and static objects.

- When classification is considered as an independent module inside the perception solution, this is often implemented as a single-class (e.g., only classifies pedestrians) or single-sensor based classification process [2], [5].

- This approach excludes discriminative data from multiple sensor views that can generate multi-class modules.

- Research perspectives point-out the improvement of the data association and tracking tasks as a direct enhancement when classification information is managed at early levels of perception [2], [5], [9].

- 가장 일반적인 접근법은 probabilistic methods 이다. `The most common approaches for multi-sensor fusion are based on probabilistic methods [1], [2]. `

- However, methods based on the Evidential framework proposed an alternative not only to multi-sensor fusion but to many modules of vehicle perception [5], [6], [9].

- These methods highlight the importance of incomplete and imprecise information which is not usually present in the probabilistic approaches.

### 제안 논문의 장점

- An advantage of our fusion approach at the **detection level** is that the description of the objects can be enhanced by adding knowledge from different sensor sources.

- For example, lidar data can give a good estimation of the distance to the object and its visible size.

- In addition, classification information, usually obtained from camera, allows to make assumptions about the detected objects.

- An early enrichment of objects’ description could allow the reduction of the number of false detections and integrate classification as a key element of the perception output rather than only an add-on.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTI2ODI0NDU3NV19
-->