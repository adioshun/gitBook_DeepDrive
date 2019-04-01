|논문명 |Pedestrian Recognition Using High-definition LIDAR|
| --- | --- |
| 저자\(소속\) | Kiyosumi Kidono \(Toyota Central R&D Labs\) |
| 학회/년도 | 2011, [논문](http://www.aisl.cs.tut.ac.jp/~jun/pdffiles/kidono-iv2011.pdf) |
| Citation ID / 키워드 |slice feature, distribution of reflection intensities, Velodyne HDL-64ES2 |
| 데이터셋(센서)/모델 | |
| 관련연구||
| 참고 |  |
| 코드 |  |



|년도|1st 저자|논문명|코드|
|-|-|-|-|
|||||



# Pedestrian Recognition Using High-definition LIDAR

Two novel features are introduced to improve the classification performance. 
- One is the slice feature, which represents the profile of a human body by widths at the different height levels. 
- The other is the distribution of the reflection intensities of points measured on the target.
    - because each substance has its own unique reflection characteristics

Our approach applies a **support vector machine (SVM)** to train a classifier from these features.

## I. INTRODUCTION

Lidar & Radar 장단점 
- LIDAR has the excellent advantages of high spatial resolution and high range accuracy compared with millimeter wave (MMW) radar, 
- but also the following disadvantages: it does not work robustly in bad weather, such as rain and fog, and its detection range is shorter than MMW radar.


Lidar 큰 장점 : LIDAR which can obtain dense range data


본 논문의 내용 : A method for recognizing pedestrians from 3D range data acquired by high-definition LIDAR is presented in this paper

기존 연구 : A technique for estimating the ego-motion and tracking moving objects using LIDAR has been developed [1], and it has been confirmed that cars, bicycles and pedestrians can be distinguished based on their size and their velocity.

```
[1] T. Miyasaka, Y. Ohama and Y. Ninomiya, ”Ego-Motion Estimation and Moving Object Tracking using Multi-layer LIDAR,” in Proc. 2009 IEEE Intelligent Vehicles Symposium, pp. 151-156, 2009.
```

동작 원리 `The proposed method divides a `
- measured 3D point cloud into clusters corresponding to the objects in the surroundings. 
- Then the pedestrian candidates are extracted by the size of the clusters [3], [4]. 
- Several features are calculated from the 3D point cloud contained in each candidate, 
- and the classifier distinguishes the pedestrians on the basis of the features.
    - Our approach applies a support vector machine (SVM) to train the classifier. 
    - No tracking is considered in this work.
    
```
[3] S. Sato, M. Hashimoto, M. Takita, K. Takagi, and T. Ogawa, ”Multilayer Lidar-Based Pedestrian Tracking in Urban Environments,” in Proc. IEEE Intelligent Vehicles Symposium, pp. 849-854, 2010.
[4] G. Gate, A. Breheret and F. Nashashibi, ”Centralized Fusion for Fast People Detection in Dense Environment,” in Proc. 2009 IEEE Int. Conf. on Robotics and Automation, pp. 76-81, 2009.
```
    
원거리 물체 탐지 성능향상/차별점 `To improve the performance of pedestrian discrimination at a long distance, two novel features are proposed: the slice feature and the distribution of reflection intensities.`
- The slice feature is composed of the widths at different height levels of the human body. 
    - This feature can represent a rough profile of the human body from the head to the legs. 
- The latter feature is also effective for distinguishing pedestrians from false positives. 
    - The wavelength of the laser beam of LIDAR is in the near-infrared (NIR) region. 
    - In the field of spectroscopy [5], it is widely known that NIR lights have different reflection characteristics depending on the materials of the target. 
    - So the reflection intensity is considered to be effective for object recognition.

```
[5] D. Williams, Methods of Experimental Physics, Academic Press, vol. 13, 1976.
```


논문 구성 `This paper is structured as follows:`
- Section II briefly describes previous related work. 
- Section III shows the specification of LIDAR used in this paper. 
- In Section IV, the details of the proposed method for recognizing pedestrians are presented. 
- Section V contains the experimental results and 
- Section VI concludes the paper

## II. RELATED WORK

### 2.1 

> 사무실 환경, 2D range data, 2D lidar(??),AdaBoost 알고리즘, 14개 feature학습 

Arras et al. [14] detected people in 2D range data from LIDAR in a cluttered office environment. 

They used a LIDAR sensor with one horizontally scanning line and applied the AdaBoost algorithm to learn a robust classifier. 

The classifier, learned from 14 features, 
- such as the number of laser points and the values indicating the linearity and the circularity in
the 2D plane, identified the groups of beams that correspond to people’s legs. 

### 2.2

> [14]연구를  multilayer lidar로 확대, 도로/도보자 탐지, 다중분류기 사용, feature(linearity and the circularity)

Premebida et al. [15] extended the method to pedestrian detection in a road environment using multilayer
LIDAR. 

They applied a multiple classification method to detect people within a range up to 35 m. 

Those methods rely on the linearity and the circularity of the 2D range data for the feature extraction. 

단점 : Extending the approach to 3D laser range data increases the computational load.

### 2.3

> [14][15]연구를 3D lidar로 확대, 서로 다른 높이의 2D lidar로 나눔, 각 높이의 정보를 AdaBoost로 예측 /통합, 거리에 민감한 단점 

Spinello et al. [16] expanded these approaches based on a 2D point cloud into a 3D point cloud. 

They subdivided the 3D point cloud of the target into several 2D point clouds at different heights. 

The classifiers obtained by AdaBoost estimated whether each 2D point cloud was a part of a human body. 

The estimation results of all parts of the target were integrated and the target with the correct combination of
parts was identified as the pedestrian. 

단점 : However, the detection performance was very sensitive to the distance to the target.

### 2.4 

> 대사을 3개로 나누고 특징 적용 

Navarro-Serment et al. [17] also presented a method of tracking people in 3D range data from high-definition LI-
DAR. 

The 3D point cloud in the target was divided into three parts corresponding to the legs and the trunk of a pedestrian,
and the variances of the 3D points contained in each part were utilized as a feature to discriminate the pedestrians.

In addition, they represented a 3D pedestrian shape by 2D histograms on two principal planes. 

장점 : The approach has the advantage of a low computational load because the feature extraction is very simple. 

단점 : However, the performance at a long range was also reduced in this approach.



