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

- Data Level Fusion or Low Level Sensor Fusion (Figure 1.1) describes a method of combining raw data from different sensors with each other, e.g. having a calibrated camera and a calibrated Time-of-Flight (ToF) depth-sensor which creates
a depth map of the environment, each camera pixel can be mapped to a distance measurement of the ToF sensor and vice versa.

#### B. Feature Level Fusion

![](https://i.imgur.com/NQv8AFk.png)

In Feature Level Fusion (Figure 1.2) or Mid-Level Fusion, the sensor data is
presented via feature vectors which describe meaningful data extracted from the
raw data. These feature vectors build the base for fusion. This method can be
found in 3D-reconstruction for example. In this approach image features from
different cameras are extracted to identify corresponding points in each image of
different camera views.

#### A. Declaration Level Fusion

![](https://i.imgur.com/ezCh0VE.png)

Declaration Level Fusion or High Level Fusion (Figure 1.3) is the combination
of independent state hypotheses from different sensors. All sensors estimate the
state individually. The final state is a fusion of all state hypotheses from the
different sensors. The most famous implementation of this approach is probably
the Kalman Filter [KB61]. Each state from the individual sensors with their
respective error covariance is used for correcting the state estimate in the Kalman
Filter. The error covariance represents the trust in the state estimation, e.g. a
camera image is reliable for estimating the width of objects but distance or speed
measurements are very inaccurate. In contrast a RADAR sensor provides very
accurate distance and velocity measurements. Thus, in the final state estimate,
velocity information and distance will be closer to the RADAR measurements,
while the size would be closer to the measurements from the camera which, in
theory, should result in a better final state estimate.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg1OTg2MTk1NV19
-->