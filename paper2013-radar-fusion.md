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
	-  e.g. points that represent corners in a camera image. 

- State estimation : the current state based on the given input, 
	- e.g. the position of a tracked vehicle

###### [ 분류 ]

- In [HL01] these are referenced as 
	- Data Level Fusion, 
	- Feature Level Fusion 
	- Declaration Level Fusion. 

#### A. Data Level Fusion

![](https://i.imgur.com/VISRuZz.png)

- Data Level Fusion or Low Level Sensor Fusion (Figure 1.1) describes 
- a method of combining raw data from different sensors with each other,
- e.g. having a calibrated camera and a calibrated Time-of-Flight (ToF) depth-sensor which creates a depth map of the environment, each camera pixel can be mapped to a distance measurement of the ToF sensor and vice versa.

#### B. Feature Level Fusion

![](https://i.imgur.com/NQv8AFk.png)

- In Feature Level Fusion (Figure 1.2) or Mid-Level Fusion, 
- the sensor data is presented via feature vectors which describe meaningful data extracted from the raw data. 
- These feature vectors build the base for fusion. 
- This method can be found in 3D-reconstruction for example. 
- In this approach image features from different cameras are extracted to identify corresponding points in each image of
different camera views.

#### A. Declaration Level Fusion

![](https://i.imgur.com/ezCh0VE.png)

- Declaration Level Fusion or High Level Fusion (Figure 1.3) is 
- the combination of independent state hypotheses from different sensors. 
- All sensors estimate the state individually. 
- The final state is a fusion of all state hypotheses from the different sensors. 
- The most famous implementation of this approach is probably the **Kalman Filter** [KB61]. 
	- Each state from the individual sensors with their respective error covariance is used for correcting the state estimate in the Kalman Filter. 
	- The error covariance represents the trust in the state estimation, e.g. a camera image is reliable for estimating the width of objects but distance or speed measurements are very inaccurate. 
	- In contrast a RADAR sensor provides very accurate distance and velocity measurements. 
	- Thus, in the final state estimate, velocity information and distance will be closer to the RADAR measurements, while the size would be closer to the measurements from the camera which, in theory, should result in a better final state estimate.

---

### 1.4 State of the Art

#### 1.4.1 RADAR-based Tracking Approaches
#### 1.4.2 Camera-based Approaches
#### 1.4.3 Sensor Fusion Approaches 

- 최근 연구는 3D 센서에 집중되어 있다. `Current research mostly focuses on sensors which provide 3-dimensional information of the environment. `

###### [LiDAR + Camera]

- The approach combines a **LIDAR sensor** with **camera data**. 
	- LIDAR sensor의 Distance Map에서 **RANSAC**와 **3D adjacency**를 이용하여 지면과 물체를 구분 할수 있다. `The distance map is used to classify parts of the image to ground plane or obstacles using RANSAC and 3D adjacency. `
	- image patches are classified to different classes by evaluating color histograms, texture descriptors from **Gaussian** and **Garbor filtered** images as well as local binary patterns. 

- Resulting in 107 features, each patch is classified by a Multi-Layer-Perceptron to different categories. 

- The size of the object determined by the LIDAR obstacle estimation as well as labels from the image analysis are passed into a fuzzy logic frame workwhich returns three labels – environment, middle high or obstacle. 

###### [RADAR + LiDAR]

- In [VBA08] a framework for **self-location** and **mapping** is presented. 

- This approach is based on an **occupancy grid** that is used to fuse information from **RADAR** and **LIDAR**. 

- An occupancy grid discretizes the environment space into small two dimensional grid tiles. 

- The LIDAR sensor is used to estimate a probability of a grid cell to be occupied. 

- A high probability means there is an obstacle in the respective grid cell. 

Moving objects are detected through changes in the occupancyof grid cells. 

Basically, if a cell is occupied at a time point, and in the next timestep, the adjacent cell is detected to be occupied, this is assumed as a motion. 

AsRADAR data is relatively sparse compared to LIDAR measurements, it is used toverify or reject motion estimations based on LIDAR data.A similar method of fusing short range RADAR and laser measurements isproposed in [PVB+09]. 

The system covers more performance optimizations than[VBA08]. 

Instead of estimating a probability representation, the grid cells areeither occupied or empty based on the number of measurements of the laser scannerfor the respective cell. 

Adjacent cells that are occupied are merged to an object.A Kalman filter [KB61] is used to track the detected objects. 

Unfortunately thefusion process of RADAR and laser data is not described in detail.The approach proposed in [ABC07] shows a fusion of RADAR and camerain which the camera is used to verify and optimize RADAR object tracks. 

Thecamera is oriented to the front. 

The center points of RADAR objects are projectedinto the image based on the camera calibration. 

The symmetry of imagesections around the projected point is estimated. 

Ideally, the symmetry is largearound the RADAR hypothesis as front views and rear views of vehicles are symmetric.Searching for higher symmetry values in a predefined environment aroundthe RADAR hypothesis is used to correct the position estimate. 

However, this approach does only work for scenarios in which vehicles are viewed from the rearor front.


<!--stackedit_data:
eyJoaXN0b3J5IjpbNzI2NzIwNTY5XX0=
-->