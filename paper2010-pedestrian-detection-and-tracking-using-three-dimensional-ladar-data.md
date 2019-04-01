|논문명 |Pedestrian Detection and Tracking Using Three-dimensional LADAR Data |
| --- | --- |
| 저자\(소속\) | Luis E. Navarro-Serment\(Carnegie Mellon University\) |
| 학회/년도 | 2010, [논문](https://www.ri.cmu.edu/pub_files/2009/7/navarro_et_al_fsr_09.pdf) |
| Citation ID / 키워드 |SICK |
| 데이터셋(센서)/모델 |Demo III XUV |
| 관련연구||
| 참고 | |
| 코드 |  |



|년도|1st 저자|논문명|코드|
|-|-|-|-|
|||||




# Pedestrian Detection and Tracking Using Three-Dimensional LADAR Data

The algorithm uses geometric and motion features to recognize human signatures

## 1 INTRODUCTION

과거 연구 

### 1.1 평면
In our group, we have developed detection and tracking systems using SICKTM laser line scanners; 
- 평면에서 잘 동작 `these implementations work well in situations where the ground is relatively flat [5]. `
- However, a 3D LADAR captures a more complete representation of the environment and the objects
within it. 

비 평면에서도 잘 동작 : In [6], we presented an algorithm that detects pedestrians from 3D data.
- Its main improvement over the version with 2D data was that it constructs a ground elevation map, and uses it to eliminate ground returns. 
- This allows pedestrian detection even when the surrounding ground is uneven. 

### 1.2 분류 문제 

움직임 크기 등으로 분류 `To classify the humans the algorithm uses motion, size, and noise features. `

동적인 물체는 잘 판단, 정적 물체 에러 많음 `Persons are classified well as long as they are moving. However, there are still too many false positives when classifying stationary humans.`


본 연구를 통해 정적 물체도 잘 탐지 할수 있음 

## 2 RELATED WORK

### 2.1

> 2D 거리 기반 단순한 특징 이용

The approach reported in [1] applies AdaBoost to train a strong classifier from simple features of groups of neighboring points. 

This work focuses on 2D range measurements. 

### 2.2

> 3D 정보 surface density function이용 

Examples using three-dimensional data include [4], where 3D scans are automatically clustered into objects
and modeled using a surface density function. 

A Bhattacharya similarity measure is optimized to register subsequent views of each object enabling
good discrimination and tracking, and hence detection of moving objects.

### 2.3

> 스트레오 비젼을 이용하여 3D pointcloud 생성 

In [3], the authors describe a pedestrian detection system which uses stereo vision to produce a 3D point cloud, and then classifies the cloud according to the point shape distribution considering the first two central moments of the 2D projections using a naive Bayes classifier. 

Motion is also used as a cue for human detection.

### 2.4 

> 3D lidar + inrared video 퓨젼 

In [8] the authors report an algorithm capable of detecting both stationary and moving humans. 

Their approach uses multi-sensor modalities including 3D LADAR and long wave infrared video (LWIR). 

### 2.5


Similarly, in [9] the same research group presents a technique for detecting humans that combines the use of 3D LADAR and visible spectrum imagery. 

In both efforts the authors employ a 2D template to extract features from the shape of an object. 

Among other differences, as opposed to our work, they extract a shape template from the projection in only one plane, and compute a measure of how uniformly distributed the returns are across the template. 

## 3 ALGORITHM DESCRIPTION

1. we do object detection and tracking in a 2D data subset first, 
2. and then use the object’s position and size information to partition the set of 3D measurements into smaller groups, for further analysis.

### 3.1 Projection into 2D Plane














