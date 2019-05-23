Self-Driving Cars: A Survey

https://arxiv.org/pdf/1901.04407v1.pdf

```
Summary
I. Introduction......................................................................2

II. Overview of the Architecture of Self-Driving Cars.....3

III. Perception ....................................................................4
A. Localization..............................................................4
    1) LIDAR-Based Localization .....................................5
    2) LIDAR plus Camera-Based Localization ................6
    3) Camera-Based Localization .....................................6
B. Offline Obstacle Mapping........................................7
    1) Discrete Space Metric Representations....................7
    2) Continuous Space Metric Representations...............8
C. Road Mapping..........................................................8
    1) Road Map Representation........................................8
    2) Road Map Creation ..................................................9
D. Moving Objects Tracking ......................................10
    1) Traditional Based MOT .........................................10
    2) Model Based MOT.................................................10
    3) Stereo Vision Based MOT .....................................11
    4) Grid Map Based MOT ...........................................11
    5) Sensor Fusion Based MOT ....................................11
    6) Deep Learning Based MOT ...................................12
E. Traffic Signalization Detection and Recognition.......12
    1) Traffic Light Detection and Recognition ...............12
    2) Traffic Sign Detection and Recognition.................13
    3) Pavement Marking Detection and Recognition......14

IV. Decision Making........................................................14
A. Route Planning.......................................................14
1) Goal-Directed Techniques .....................................15
2) Separator-Based Techniques..................................15
3) Hierarchical Techniques........................................15
4) Bounded-Hop Techniques .....................................15
5) Combinations.........................................................16
B. Motion Planning ....................................................16
1) Path Planning.........................................................16
2) Trajectory Planning ...............................................17
C. Control...................................................................19
1) Path Tracking Methods..........................................19
2) Hardware Actuation Control Methods...................20

V. Architecture of the UFES’s Car “IARA”...................20

VI. Self-Driving Cars under Development in the Industry
References .............................................................................24
```

# Self-Driving Cars: A Survey

```
The architecture of the autonomy system of self-driving cars is typically organized into 
- the perception system and 
- the decision-making system. 

The perception system is generally divided into many subsystems responsible for tasks such as 
- self-driving-car localization, 
- static obstacles mapping, 
- moving obstacles detection and tracking, 
- road mapping, 
- traffic signalization detection and recognition, 
- among others. 

The decision making system is commonly partitioned as well into many subsystems responsible for tasks such as 
- route planning,
- path planning, 
- behavior selection, 
- motion planning, and
- control. 
```

## I. INTRODUCTION

## II. OVERVIEW OF THE ARCHITECTURE OF SELF-DRIVING CARS

![](https://i.imgur.com/34n4ifa.png)

## III. PERCEPTION

- localizer (or localization)
- offline obstacle mapping
- road mapping
- moving object tracking
- and traffic signalization detection and recognition.

### 3.1 Localization



#### A. LIDAR-Based Localization

#### B. LIDAR plus Camera-Based Localization

#### C. Camera-Based Localization


### 3.2 Offline Obstacle Mapping

The offline obstacle mapping subsystem is responsible for computing a map of obstacles in the environment of the selfdriving car. 

> OUT-OF-SCOPE

### 3.3 Road Mapping

The road mapping subsystem is responsible for gathering information of roads and lanes in the surroundings of the selfdriving car, and representing them in a map with geometrical and topological properties, including interconnections and
restrictions. 

The main topics of the road mapping subsystem are 
- the map representation and 
- the map creation.

> OUT-OF-SCOPE

### 3.4 Moving Objects Tracking

### 3.4 Moving Objects Tracking

MOT는 자차 주변 물체 탐지 및 추적에 관련된 기능이다. `The Moving Objects Tracking (MOT) subsystem (also known as Detection and Tracking Multiple Objects - DATMO) is responsible for detecting and tracking the pose of moving obstacles in the environment around the self-driving car. This subsystem is essential to enable autonomous vehicles to take decisions and to avoid collision with potentially moving objects (e.g., other vehicles and pedestrians). `

주변 물체의 위치 는 센서등을 이용하여 매 순간 예측 된다. `Moving obstacles’ positions over time are usually estimated from data captured by ranging sensors, such as LIDAR and RADAR, or stereo cameras. Images from monocular cameras are useful to provide rich appearance information, which can be explored to improve moving obstacle hypotheses.`


센서의 불확실성을 보완 하기 위해 여러 필터들의 도움을 받는다. `To cope with uncertainty of sensor measurements, Bayes filters (e.g., Kalman and particle filter) are employed for state prediction. `

많은 관련연구 중에서 최근 10년의 연구 결과를 6개의 분류로 나누어 보았다. `Various methods for MOT have been proposed in the literature. Here, we present the most recent and relevant ones published in the last ten years. For earlier works, readers are referred to Petrovskaya et al. [PET12], Bernini et al. [BER14], and Girão et al. [GIR16]. Methods for MOT can be mainly categorized into six classes: traditional, model based, stereo vision based, grid map based, sensor fusion based, and deep learning based.`


#### A. Traditional Based MOT

전통적인 MOT는 3단계로 되어 있다. `Traditional MOT methods follow three main steps: `
- data segmentation, 
- data association, and 
- filtering [PET12]. 

```
[PET12] A. Petrovskaya, M. Perrollaz, L. Oliveira, L. Spinello, R. Triebel, A. Makris, J. D. Yoder, C. Laugier, U. Nunes, and P. Bessiere, “Awareness of road scene participants for autonomous driving”, in Handbook of Intelligent Vehicles, London: Springer, pp. 1383–1432, 2012.
```

In the data segmentation step, 
- sensor data are segmented using clustering or pattern recognition techniques. 

In the data association step, 
- segments of data are associated with targets (moving obstacles) using data association techniques. 

In the filtering phase, 
- for each target, a position is estimated by taking the **geometric mean** of the data assigned to the target. 

**Position estimates** are usually updated by Kalman or particle filters. 

Amaral et al. [AMA15] propose a traditional method for detection and tracking of moving vehicles using 3D LIDAR sensor. - 
- The 3D LIDAR point cloud is segmented into clusters of points using the **Euclidean distance**. 
- Obstacles (clusters) observed in the current scan sensor are associated with obstacles observed in previous scans using a **nearest neighbor** algorithm. 
- States of obstacles are estimated using a **particle filter** algorithm. 
- Obstacles with velocity above a given threshold are considered moving vehicles. 

```
[AMA15] E. Amaral, C. Badue, T. Oliveira-Santos, A. F. De Souza, “Detecção e Rastreamento de Veículos em Movimento para Automóveis Robóticos Autônomos”, Simpósio Brasileiro de Automação Inteligente, 2015, pp. 801–806.
```

[ZHA13]은 바운딩박스 정보를 이용하여서 차량인지 아닌지를 구분 하였다. `Zhang et al. [ZHA13] build a cube bounding box for each cluster and use box dimensions for distinguishing whether a cluster is a vehicle or not. `
- Data association is solved by an optimization algorithm. 
- A **Multiple Hypothesis Tracking** (MHT) algorithm is employed to mitigate association errors. 

```
[ZHA13] L. Zhang, Q. Li, M. Li, Q. Mao, and A. Nüchter, “Multiple vehicle-like target tracking based on the Velodyne LIDAR”, in IFAC Proceedings Volumes, vol. 46, no. 10, pp. 126–131, 2013.
```

[HWA16]는 이미지 정보를 이용해서 Lidar의 불필요한 부분을 제거 하였다. `Hwang et al. [HWA16] use images captured by a monocular camera to filter out 3D LIDAR points that do not belong to moving objects (pedestrians, cyclists, and vehicles). `
- Once filtered, object tracking is performed based on a segment matching technique using features extracted from images and 3D points.

```
[HWA16] S. Hwang, N. Kim, Y. Choi, S. Lee, and I. S. Kweon, “Fast multiple objects detection and tracking fusing color camera and 3d LIDAR for intelligent vehicles”, International Conference on Ubiquitous Robots and Ambient Intelligence, 2016, pp. 234–239
```

#### B. Model Based MOT 

모델 기반 방식은 센서 데이터에서 바로 센서의 물리 모델과 탐지 물체의 geometric모델을 이용하여서 바로 추론 작업을 진행 한다. 그리고 non-parametric filters를 사용한다. `Model-based methods directly infer from sensor data using physical models of sensors and geometric models of objects, and employing non-parametric filters (e.g., particle filters) [PET12]. `

군집화와 association작업은 불필요 하다.  `Data segmentation and association steps are not required,`
- because geometric object models associate data to targets. 


Petrovskaya and Thrun [PET09] present the model based method for detection and tracking of moving vehicles adopted by the self-driving car “Junior” [MON08]. 
- Moving vehicle hypotheses are detected using differences over LIDAR data between consecutive scans. 
- Instead of separating data segmentation and association steps, new sensor data are incorporated by updating the state of each vehicle target, which comprises vehicle pose and geometry. 
- This is achieved by a hybrid formulation that combines Kalman filter and RaoBlackwellized Particle Filter (RBPF). 


The work of Petrovskaya and Thrun [PET09] was revised by He et al. [HE16] that propose to combine RBPF with Scaling Series Particle Filter (SSPF) for geometry fitting and for motion estimate throughout the entire tracking process. 
- The geometry became a tracked variable, which means that its previous state is also used to predict the current state. 


Vu and Aycard [VU09] propose a model-based MOT method that aims at finding the most likely set of tracks (trajectories) of moving obstacles, given laser measurements over a sliding window of time. 
- A track is a sequence of object shapes (L-shape, I-shape and mass point) produced over time by an object satisfying the constraints of a measurement model and motion model from frame to frame. 
- Due to the high computational complexity of such a scheme, they employ a Data Driven Markov chain Monte Carlo (DD-MCMC) technique that enables traversing efficiently in the solution space to find the optimal solution. 
- DD-MCMC is designed to sample the probability distribution of a set of tracks, given the set of observations within a time interval. 
- At each iteration, DD-MCMC samples a new state (set of tracks) from the current state following a proposal distribution.
- The new candidate state is accepted with a given probability. 
- To provide initial proposals for the DD-MCMC, dynamic segments are detected from laser measurements that fall into free or unexplored regions of an occupancy grid map and moving obstacle hypotheses are generated by fitting predefined object models to dynamic segments. 


Wang et al. [WAN15] adopt a similar method to the model-based one, but they do not assume prior categories for moving objects.
- A Bayes filter is responsible for joint estimation of the pose of the sensor, geometry of static local background, and dynamics and geometry of objects. 
- Geometry information includes boundary points obtained with a 2D LIDAR. 
- Basically, the system operates by iteratively updating tracked states and associating new measurements to current targets. 

Hierarchical data association works in two levels. 
- In the first level, new observations (i.e., cluster of points) are matched against current dynamic or static targets. 
- In the second level, boundary points of obstacles are updated.

#### C. Stereo Vision Based MOT

Stereo vision based methods rely on color and depth information provided by stereo pairs of images for detecting and tracking moving obstacles in the environment. 


Ess et al. [ESS10] propose a method for obstacle detection and recognition that uses only synchronized video from a forwardlooking stereo camera. The focus of their work is obstacle tracking based on the per-frame output of pedestrian and car detectors. For obstacle detection, they employ a Support Vector Machine (SVM) classifier with Histogram of Oriented Gradients (HOG) features for categorizing each image region as obstacle or non-obstacle. For obstacle tracking, they apply a hypothesize-and-verify strategy for fitting a set of trajectories to the potentially detected obstacles, such that these trajectories together have a high posterior probability. The set of candidate trajectories is generated by Extended Kalman Filters (EKFs) initialized with obstacle detections. Finally, a model selection technique is used to retain only a minimal and conflict-free set of trajectories that explain past and present observations. 


Ziegler et al. [ZIE14a] describe the architecture of the modified Mercedes-Benz S-Class S500 “Bertha”, which drove autonomously on the historic BerthaBenz-Memorial-Route. For MOT, dense disparity images are reconstructed from stereo image pairs using Semi-Global Matching (SGM). All obstacles within the 3D environment are approximated by sets of thin and vertically oriented rectangles called super-pixels or stixels. Stixels are tracked over time using a Kalman filter. Finally, stixels are segmented into static background and moving obstacles using spatial, shape, and motion constraints. The spatio-temporal analysis is complemented by an appearance-based detection and recognition scheme, which exploits category-specific (pedestrian and vehicle) models and increases the robustness of the visual perception. The real-time recognition consists of three main phases: Region Of Interest (ROI) generation, obstacle classification, and object tracking. 


Chen et al. [CHEN17] compute a disparity map from a stereo image pair using a semi-global matching algorithm. Assisted by disparity maps, boundaries in the image segmentation produced by simple linear iterative clustering are classified into coplanar, hinge, and occlusion. Moving points are obtained during egomotion estimation by a modified Random Sample Consensus (RANSAC) algorithm. Finally, moving obstacles are extracted by merging super-pixels according to boundary types and their movements.

#### D. Grid Map Based MOT

이 방식은 **occupancy grid map**을 생성하는 것에서 부터 시작 한다. `Grid map based methods start by constructing an occupancy grid map of the dynamic environment [PET12]. `

Map 생성 작업은 다음과 같다. `The map construction step is followed by`
- data segmentation, 
- data association, 
- and filtering steps in order to provide object level representation of the scene. 


[NGU12]는 **양안 카메라**기반 방식을 제안 하였다. `Nguyen et al. [NGU12] propose a grid-based method for detection and tracking of moving objects using stereo camera. The focus of their work is pedestrian detection and tracking. 3D points are reconstructed from a stereo image pair. An inverse sensor model is used to estimate the occupancy probability of each cell of the grid map based on the associated 3D points. A hierarchical segmentation method is employed to cluster grid cells into segments based on the regional distance between cells. Finally, an Interactive Multiple Model (IMM) method is applied to track moving obstacles. `


 [AZI14] 는 **Octree**기반 방식을 제안 하였다. `Azim and Aycard [AZI14] use an octree-based 3D local occupancy grid map that divides the environment into occupied, free, and unknown voxels. After construction of the local grid map, moving obstacles can be detected based on inconsistencies between observed free and occupied spaces in the local grid map. Dynamic voxels are clustered into moving objects, which are further divided into layers. Moving objects are classified into known categories (pedestrians, bikes, cars, or buses) using geometric features extracted from each layer. `


Ge et al. [GE17] leverage a 2.5D occupancy grid map to model static background and detect moving obstacles. A grid cell stores the average height of 3D points whose 2D projection falls into the cell space domain. Motion hypotheses are detected from discrepancies between the current grid and the background model.

#### E. Sensor Fusion Based MOT

센서 퓨전 기반 방식은 여러 센서의 정보를 혼합하여 인지 성능을 향상시킨 방식이다. `Sensor fusion-based methods fuse data from various kinds of sensors (e.g., LIDAR, RADAR, and camera) in order to explore their individual characteristics and improve environment perception. `


Darms et al. [DAR09] present the sensor fusion-based method for detection and tracking of moving vehicles adopted by the self-driving car “Boss” [URM08]. The MOT subsystem is divided into two layers. The sensor layer extracts features from sensor data that may be used to describe a moving obstacle hypothesis according to either a point model or a box model. The sensor layer also attempts to associate features with currently predicted hypotheses from the fusion layer. Features that cannot be associated to an existing hypothesis are used to generate new proposals. An observation is generated for each feature associated with a given hypothesis, encapsulating all information that is necessary to update the estimation of the hypothesis state. Based on proposals and observations provided by the sensor layer, the fusion layer selects the best tracking model for each hypothesis and estimates (or updates the estimation of) the hypothesis state using a Kalman Filter. 


Cho et al. [CHO14] describe the new MOT subsystem used by the new experimental autonomous vehicle of the Carnegie Mellon University. The previous MOT subsystem, presented by Darms et al. [DAR09], was extended for exploiting camera data, in order to identify categories of moving objects (e.g., car, pedestrian, and bicyclists) and to enhance measurements from automotive-grade active sensors, such as LIDARs and RADARs. 


Mertz et al. [MER13] use scan lines that can be directly obtained from 2D LIDARs, from the projection of 3D LIDARs onto a 2D plane, or from the fusion of multiple sensors (LADAR, RADAR, and camera). Scan lines are transformed into world coordinates and segmented. Line and corner features are extracted for each segment. Segments are associated with existing obstacles and kinematics of objects are updated using a Kalman filter. 


Byun et al. [BYU15] merge tracks of moving obstacles generated from multiple sensors, such as RADARs, 2D LIDARs, and a 3D LIDAR. 2D LIDAR data is projected onto a 2D plane and moving obstacles are tracked using Joint Probabilistic Data Association Filter (JPDAF). 3D LIDAR data is projected onto an image and partitioned into moving obstacles using a region growing algorithm. Finally, poses of tracks are estimated or updated using Iterative Closest Points (ICP) matching or image-based data association. 


Xu et al. [XU15] describe the context-aware tracking of moving obstacles for distance keeping used by the new experimental driverless car of the Carnegie Mellon University. Given the behavioral context, a ROI is generated in the road network. Candidate targets inside the ROI are found and projected into road coordinates. The distance-keeping target is obtained by associating all candidate targets from different sensors (LIDAR, RADAR, and camera). 


Xue et al. [XUE17] fuse LIDAR and camera data to improve the accuracy of pedestrian detection. They use prior knowledge of a pedestrian height to reduce false detections. They estimate the height of the pedestrian according to pinhole camera equation, which combines camera and LIDAR measurements.

#### F. Deep Learning Based MOT 

딥러닝 기반 방식은 위치, 모양, 추적에 뉴럴 네트워크를 이용하는 방식이다. `Deep learning based methods use deep neural networks for detecting positions and geometries of moving obstacles, and tracking their future states based on current camera data. `


[HUV15]는 카메라 이미지와 CNN응 이용하였다. `Huval et al. [HUV15] propose a neural-based method for detection of moving vehicles using the Overfeat Convolutional Neural Network (CNN) [SER13] and monocular input images with focus on real-time performance. CNN aims at predicting location and range distance (depth) of cars in the same driving direction of the ego-vehicle using only the rear view of them. `

Mutz et al. [MUT17] address moving obstacle tracking for a closely related application known as “follow the leader”, which is relevant mainly for convoys of autonomous vehicles. The tracking method is built on top of the Generic Object Tracking Using Regression Networks (GOTURN) [HEL16]. GOTURN is a pre-trained deep neural network capable of tracking generic objects without further training or object specific fine-tuning. Initially, GOTURN receives as input an image(입력으로 이미지) and a manually delimited bounding box of the leader vehicle. It is assumed that the object of interest is in the center of the bounding box. Subsequently, for every new image, GOTURN gives as output an estimate of the position and geometry (height and width) of the bounding box. The leader vehicle position is estimated using LIDAR points that fall inside the bounding box and are considered to be vehicle.

```
[MUT17] F. Mutz, V. Cardoso, T. Teixeira, L. F. R. Jesus, M. A. Gonçalves, R. Guidolini, J. Oliveira, C. Badue, and A. F. De Souza, “Following the leader using a tracking system based on pre-trained deep neural networks”, International Joint Conference on Neural Networks, 2017, pp. 4332–4339.
```




### 3.5 Traffic Signalization Detection and Recognition


## 4. DECISION MAKING

> OUT-OF-SCOPE



## 5. ARCHITECTURE OF THE UFES’S CAR “IARA”

The Intelligent and Autonomous Robotic Automobile (IARA)

It follows the typical architecture of self driving cars. 

IARA is a research autonomous vehicle that was developed at the Laboratory of High Performance Computing of the Federal University of Espírito Santo (Universidade Federal do Espírito Santo – UFES)

### 5.1 장비 

IARA’s computers and sensors comprise a workstation (Dell Precision R5500, with 2 Xeon X5690 six-core 3.4GHz processors and one NVIDIA GeForce GTX-1030), 
 
networking gear, 

two LiDARs (a Velodyne HDL-32E and a SICK LDMRS),

three cameras (two Bumblebee XB3 and one ZED), 

an IMU (Xsens MTi) 

and a dual RTK GPS (based on the Trimble BD982 receiver).

## 6. SELF-DRIVING CARS UNDER DEVELOPMENT IN THE INDUSTRY

### 6.1 Torc 

Torc was one of the pioneers in developing cars with selfdriving capabilities. 

The company was founded in 2005. 

In 2007, it joined Virginia Tech’s team to participate in the 2007 DARPA Urban Challenge with their autonomous car “Odin” [BAC08], which reached third place in the competition. 

The technology used in the competition was improved since then and it was successfully applied in a variety of commercial ground vehicles, from large mining trucks to military vehicles [TOR18]. 

### 6.2 Google - Waymo

Google's self-driving car project began in 2009 and was formerly led by Sebastian Thrun, who also led the Stanford University’s team with their car “Stanley” [THR07], winner of
the 2005 DARPA Grand Challenge. 

In 2016, Google's self driving car project became an independent company called Waymo [WAY18]. 

The company is a subsidiary of the holding Alphabet Inc., which is also Google's parent company.

Waymo's self-driving car uses a sensor set composed of LIDARs to create a detailed map of the world around the car, RADARs to detect distant objects and their velocities, and high resolution cameras to acquire visual information, such as
whether a traffic signal is red or green [WAY18b]. 


### 6.3 Baidu 

Baidu, one of the giant technology companies in China, is developing an open source self-driving car project with code name Apollo [APO18]. 

The source code for the project is available in GitHub [APOL18]. 

It contains modules for perception (detection and tracking of moving obstacles, and detection and recognition of traffic lights), HD map and localization, planning, and control, among others. 

Several companies are partners of Baidu in the Apollo project, such as TomTom, Velodyne, Bosch, Intel, Daimler, Ford, Nvidia, and Microsoft. 

One of the Apollo project’s goals is to create a centralized place for original equipment manufacturers (OEMs), startups, suppliers, and research organizations to share and integrate their data and resources. 

Besides Baidu, Udacity, is also developing an open source self driving car, which is available for free in GitHub [UDA18].


### 6.5 Uber

Uber is a ride-hailing service and, in 2015, they partnered with the Carnegie Mellon University to develop self-driving cars [UBE15]. 

A motivation for Uber's project is to replace associated drivers by autonomous software [UBE18]. 

### 6.6 Lyft

Lyft is a company that provides ride sharing and on-demand driving services. 

Like Uber, Lyft is doing research and development in self-driving cars [LYF18]. 

The company aims at developing cars with level 5 of autonomy. 

### 6.7 Aptiv

> V2V comm.

Aptiv is one of Lyft's partners. 

Aptiv was created in a split of Delphi Automotive, a company owned by General Motors.

Aptiv’s objective is to build cars with level 4 and, posteriorly, level 5 of autonomy [APT18]. 

Besides other products, the company sells short-range communication modules for vehicle-to-vehicle information exchange. 

Aptiv recently acquired two relevant self-driving companies, Movimento and nuTonomy


### 6.8 Didi

Didi is a Chinese transportation service that bought Uber's rights in China. 

Didi's self-driving car project was announced in 2017 and, in February of 2018, they did the first successful demonstration of their technology. 

In the same month, company’s cars started being tested in USA and China. 

Within a year, Didi obtained the certificate for HD mapping in China. 

The company is now negotiating a partnership with Renault, Nissan, and Mitsubishi to build an electric and autonomous ride-sharing service [ENG18]. 


### 6.9 Tesla 

Tesla was founded in 2003 and, in 2012, it started selling its first electric car, the Model S. 

In 2015, the company enabled the autopilot software for owners of the Model S. 

The software has been improved since then and its current version, the so called enhanced autopilot, is now able to match speed with traffic conditions, keep within a lane, change lanes, transition from one freeway to another, exit the freeway when the destination is near, self-park when near a parking spot, and be summoned to and from the user’s garage [TES18]. 

Tesla's current sensor set does not include LIDARs.

### 6.10 LeEco 

A Chinese company called LeEco is producing self-driving luxury sedans to compete with the Tesla Model S. 

The company is also backing up Faraday Future for the development of a concept car. 

LeEco is also partnering Aston Martin for the development of the RapidE electric car [VERG16]. 

### 6.11 NVIDIA 

Besides developing hardware for general-purpose highperformance computing, NVDIA is also developing hardware and software for self-driving cars [NVI18]. 

Although their solutions rely mostly on artificial intelligence and deep learning, they are also capable of performing sensor fusion, localization in HD maps, and planning [NVID18]. 

### 6.12 Aurora 

Aurora is a new company founded by experienced engineers that worked in Google's self-driving project, Tesla, and Uber [AUR18]. 

The company plans to work with automakers and suppliers to develop full-stack solutions for cars with level 4 and, eventually, level 5 of autonomy. 

Aurora has independent partnerships with Volkswagen group (that owns Volkswagen Passenger Cars, Audi, Bentley, Skoda, and Porsche) and Hyunday [FORT18].


### 6.13 Zenuity 

Zenuity is a joint venture created by Volvo Cars and Autoliv [ZEN18]. 

Ericsson will aid in the development of Zenuity’s Connected Cloud that will use Ericsson's IoT Accelerator [ERI18]. 

TomTom also partnered with Zenuity and provided its HD mapping technology [TOM18].

TomTom’s HD maps will be used for localization, perception and path planning in Zenuity's software stack.

### 6.14 Daimler and Bosch

Daimler and Bosch are joining forces to advance the development of cars with level 4 and 5 of autonomy by the beginning of the next decade [BOS18]. 

The companies already have an automated valet parking in Stuttgart [DAA18] and they also have tested the so called Highway Pilot in trucks in USA and Germany [DAB18]. 

Besides partnering with Bosch, Daimler also merged its car sharing business, Car2Go, with BMW's ReachNow, from the same business segment, in an effort to stave off competition from other technology companies, such as Waymo and Uber [DAC18]. 

The new company will include business in car sharing, ride-hailing, valet parking, and electric vehicle charging.

### 6.15 Argo 

Argo AI founders led self-driving car teams at Google and Uber [ARG18]. 

The company received an investment of U$ 1 billion from Ford with the goal of developing a new software platform for Ford’s fully autonomous vehicle (level 4) coming in 2021. 

They have partnerships with professors from Carnegie Mellon University and Georgia Tech [ARB18]. 

### 6.16 Renesas 

Renesas Autonomy develops several solutions for automated driving assistant systems (ADAS) and automated driving [REN18]. 

The company has a partnership with the University of Waterloo [RENE18]. 


### 6.17 Hoda 

Honda revealed in 2017 plans for introducing cars with level 4 of autonomy by 2025. 

The company intends to have vehicles with level 3 of autonomy by 2020 and it is negotiating a partnership with Waymo [HON18]. 

### 6.18 Visteon 

Visteon is a technology company that manufactures cockpit electronic products and connectivity solutions for several vehicle manufacturers [VIS18]. 

In 2018, Visteon introduced its autonomous driving platform capable of level 3 of autonomy and, potentially, higher levels. 

The company does not aim at producing cars and sensors, but at producing integrated solutions and software. 


### 6.19 AI Motive 

AI motive is using low cost components to develop a selfdriving platform [AIM18]. 

Its solution relies strongly on computer vision, but it uses additional sensors. 

The company is already able to perform valet parking and navigate in highways. 

AImotive also developed a photorealistic simulator for data collection and preliminary system testing, and chips for artificial intelligence-based, latency-critic, and camera centric systems. 

As AImotive, AutoX is avoiding to use LIDARs in its solution. 

However, the company is going further than Almotive and trying to develop a level 5 car without using RADARs, ultrasonics, and differential GPS’s. 

AutoX's approach is to create a full-stack software solution based on artificial intelligence [AUT18].


### 6.20 Mobileye 

Mobileye is also seeking to develop a self-driving solution without using LIDARs, but relying mostly in a single-lensed camera (mono-camera). 

Mobileye is one of the leading suppliers of software for Advanced Driver Assist Systems (ADAS), with more than 25 partners among automakers.

Beyond ADAS, Mobileye is also developing technology to support other key components for autonomous driving, such as perception (detection of free space, driving paths, moving objects, traffic lights, and traffic signs, among others),mapping, and control. 

The company partnered with BMW and Intel to develop production-ready fully autonomous vehicles, with production launch planned for 2021 [MOB18].


### 6.21 Ambarella

Ambarella also does not use LIDAR, but only RADARs and stereo cameras. 

The company joined the autonomous driving race in 2015 by acquiring VisLAB. 

Different from other companies, Ambarella does not aim at becoming a tier one supplier or selling complete autonomous-driving systems.

Instead, they plan to sell chips and software to automakers, suppliers, and software developers. 

Ambarella’s current research and development guidelines include detection of vehicles, obstacles, pedestrians, and lanes; traffic sign recognition; terrain mapping; and issues related to technology commercialization, such as system calibration, illumination, noise, temperature, and power consumption [AMB18]. 


### 6.22 Pony.ai 

Pony.ai was founded in December of 2016 and, in July of 2017, it completed its first fully autonomous driving demonstration. 

The company signed a strategic agreement with one of the biggest Chinese car makers, the Guangzhou Auto Group (GAC) [PON18].

### 6.23 Navya and Transdev

Navya [NAA18] and Transdev [TRA18] are French companies that develop self-driving buses. 

Navya has several of their buses being tested in Europe, Asia, and Australia.

Their sensor set consists of two multi-layer 360º LIDARs, six 180º mono-layer LIDARs, front and rear cameras, odometer (wheels encoder + IMU), and a GNSS RTK [NAB18].

Transdev is also already demonstrating their self-driving buses for the public [TRA18].

### 6.24 JD

JD is a Chinese e-commerce company interested in building self-driving delivery vehicles [JD18]. 

JD's project, started in 2016, is being developed together with Idriverplus [IDR18], a Chinese self-driving car startup. 

### 6.25 Toyota 

In March, 2018, Toyota announced an investment of U$ 2.8 billion in the creation of a new company called the Toyota Research Institute-Advanced Development (TRI-AD) with the goal of developing an electric and autonomous car until 2020
[TOYT18]. 

Besides Toyota [TOY18], other car manufacturers, such as Ford [FOR18], Volvo [VOLV18], and Mercedes-Benz [MER18], have also recently presented their plans for self-driving cars. 

### 6.26 Ford

Ford defined 2021 as a deadline for presenting a fully autonomous vehicle ready for commercial operation.