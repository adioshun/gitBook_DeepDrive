|논문명|VoxNet: A 3D Convolutional Neural Network for Real-Time Object Recognition
|-|-|
|저자(소속)|Daniel Maturana (CMU)|
|학회/년도| IROS 2015, [논문](http://ieeexplore.ieee.org/document/7353481/)|
|키워드|Volumetric Occupancy Grid + 3D CNN |
|참고|이전연구: 3D convolutional neural networks for landing zone detection from lidar,” in ICRA, 2015.|
|코드|[Theano+Lasagne](https://github.com/dimatura/voxnet)|

![](http://i.imgur.com/yXb89IB.png)

# VoxNet

## 0. Abstract 

- Range sensors such as LiDAR and RGBD cameras가 많이 사용되고 있다. 

- 하지만 large amounts of point cloud data를 충분히 활용하고 있지 않다. 

- VoxNet을 제안 : integrating a `volumetric Occupancy Grid` representation with a supervised 3D Convolutional Neural Network (3D CNN).

## 1. Introduction 


본 논문에서는 `3D point cloud segment`를 이용하여서 `object 분류`의 문제점(eg. background clutter)을 살펴 본다. 

원인 : 작업 Pipe-line
- extraction and aggregation of hand-engineered features
- fed into an off-the-shelf classifier such as SVMs.

이러한 Pipe-line은 2D `object 분류`와도 비슷하다. 
- CNN의 발전으로 데이터를 활용하는 방향으로 바뀌었다. 
- 3D 기본은 같으므로 변경이 가능하다. 단, 계산 부하가 크다. 

## 2. 관련 연구 

### 2.1 Object Recognition with Point Cloud Data

3D point clouds를 이용한 물체 인식은 많은 연구가 있다. 

기존 연구 : hand-crafted features(or descriptors) + machine learning classifier ([10], [11],[12], [13]). 
    - The situation is similar for semantic segmentation,with structured output classifiers instead of single output classifiers ([14], [15], [16]). 

제안 방식 : extract features and classify objects from the `raw volumetric data`. 

    - Our volumetric representation is also richer than point clouds, as it distinguishes free space
from unknown space. 

    - In addition, features based on point clouds often require spatial neighborhood queries, which can quickly become intractable(고치기 어려운) with large numbers of points.
    
    
### 2.2 2.5D Convolutional Neural Networks

#### A. RGBD

이미지(RGB)에서 사용한 CNN기법을 RGBD로 확장하려는 연구가 진행 되었다. [17], [18], [19], [20]
- 간단한 접근법은 D를 또 다른 채널로 간주하고 처리 하는 것이다. 
- 단점 #1 : geometric information를 제대로 활용 못함 
- 단점 #2 : integrate information across viewpoints하기 어려움 

#### B. LiDAR

- [4] propose a feature that locally describes scans with a 2.5D representation, 

- [21] studies this approach in combination with a form of unsupervised feature learning. 

- [22] propose an encoding that makes better use of the 3D information in the depth, but is still 2D-centric. 

### 2.3 3D Convolutional Neural Networks

비디오 분석에서는 3D CNN이 성공적으로 적용 되었다. ([23], [24])
- 하지만 이때는 `시간 정보`가 3rd D로 작용하였다. 
- 알고림적으로 논문의 제안 방식과 비슷하지만, 사용되는 데이터 속성이 다르다. 

#### A. RGBD

- [25] uses an unsupervised volumetric feature learning approach as part of a pipeline to detect indoor objects. 
    - This approach is based on `sparse coding`, which is generally slower than convolutional models. 

-[26] propose a generative 3D convolutional model of shape and apply it to RGBD object recognition, among other tasks. 

#### B. LiDAR 

- [27] is an early work that studies a3D CNN for use with LiDAR data with a binary classification task. 

- [28], which introduced 3D CNNs for landing zone detection in UAVs. 
    - Compared to this work, we tackle a more general objectre cognition task with 3D data from different modalities. 

We also study different representations of occupancy and propose techniques to improve performance when the data varies significantly in scale and orientation

## 3. Approach