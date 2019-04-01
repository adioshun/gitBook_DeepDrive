|논문명 |Pedestrian Recognition Using High-definition LIDAR|
| --- | --- |
| 저자\(소속\) | Kiyosumi Kidono \(Toyota Central R&D Labs\) |
| 학회/년도 | 2011, [논문](http://www.aisl.cs.tut.ac.jp/~jun/pdffiles/kidono-iv2011.pdf) |
| Citation ID / 키워드 |slice feature, distribution of reflection intensities, Velodyne HDL-64ES2 |
| 데이터셋(센서)/모델 |SVM + RBF kernel |
| 관련연구||
| 참고 |  |
| 코드 |  |



|년도|1st 저자|논문명|코드|
|-|-|-|-|
|2008|T Miyasaka|[Ego-Motion Estimation and Moving Object Tracking using Multi-layer LIDAR](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=5164269)||



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

> 대을 3개로 나누고 특징 적용 

Navarro-Serment et al. [17] also presented a method of tracking people in 3D range data from high-definition LI-
DAR. 

The 3D point cloud in the target was divided into three parts corresponding to the legs and the trunk of a pedestrian,
and the variances of the 3D points contained in each part were utilized as a feature to discriminate the pedestrians.

In addition, they represented a 3D pedestrian shape by 2D histograms on two principal planes. 

장점 : The approach has the advantage of a low computational load because the feature extraction is very simple. 

단점 : However, the performance at a long range was also reduced in this approach.


## III. HIGH-DEFINITION LIDAR

Velodyne HDL-64ES2 사용 


## IV. PROPOSED METHOD


### 4.1 Overview of Processing Flow

![](https://i.imgur.com/uGOJ56I.png)

The processing flow at each scan is shown in Fig. 3. And each process is explained in detail.

#### A. 1) Data acquisition

A 3D point cloud is acquired from LIDAR.


#### B. 2) Segmentation

The acquired 3D point cloud is divided into two classes, ground plane and objects, by using an
occupancy grid map [18]. 

> [18]의 occupancy grid map기법을 이용하여 바닦제거 

All of the 3D points are projected onto the 2D occupancy grid, which is parallel to the ground plane. 

The difference between the maximum height and the minimum height in each cell is investigated. 

If the difference is larger than a threshold, the points in the cell are segmented as objects. 

The cell size of the occupancy grid is 0.1 m and the threshold of the height for segmentation is 0.3 m.

#### C. 3) Clustering

The clusters corresponding to vehicles and pedestrians are generated by a distance-based clustering algorithm. 

To reduce the computational burden, the clustering process is carried out on the occupancy grid by using the labeling technique for image processing. 
- If the distance between two points is within 0.5 m, these points are integrated into the same cluster. 
- A rectangular parallelepiped is applied to each cluster by the Rotating Calipers method [19]. 
- Then the pedestrian candidates are extracted on the basis of the size of the clusters. 
- The conditions are as follows: `0.8 ≤ height ≤ 2.0,width ≤ 1.2,length ≤ 1.2,`

#### D. 4) Classification

A feature vector is computed from the 3D point cloud of each candidate and evaluated to classify the candidate into a pedestrian or not. 

The proposed method applies SVM with a radial basis function (RBF) kernel to learn the classifier.

### 4.2 Pedestrian Classification

![](https://i.imgur.com/oK1QSRR.png)

- Features f 1 and f 2 are introduced by the Premebida method [15]. 
- The features from f 3 to f 7 are proposed by the Navarro-Serment method [17]. 
- To improve the classification performance, the proposed method adds the following two features.


```
[15] C. Premebida, O. Ludwig and U. Nunes, ”Exploiting LIDAR-based Features on Pedestrian Detection in Urban Scenarios,” in Proc. 12th Int. IEEE Conf. on Intelligent Transportation Systems, 2009
[17] L. E. Navarro-Serment, C. Mertz, and M. Hebert, ”Pedestrian Detection and Tracking Using Three-Dimensional LADAR Data,” in Proc. Int. Conf. on Field and Service Robotics, 2009.

```

#### A. 1) Slice Feature for a Cluster

사람은 다리 길이, 머리-어깨 길이의 특징을 가진다. `The pattern of the legs and the profile from the head to the shoulder are distinctive human shapes. `

하지만 먼거리 물체는 이를 구분하기 어렵다. `It is, however, difficult to extract these partial features at a long distance, where the spatial resolution decreases. `

A rough profile from the head to the legs is therefore utilized as the 3D shape of the pedestrians.

Three principal axes for the pedestrian candidates are calculated by principal component analysis (PCA). 

We assume that most pedestrians are in an upright position, so the principal eigenvector is expected to be vertically aligned with the person’s body. 

![](https://i.imgur.com/FRDTz62.png)

3D points in the cluster are divided into N blocks of the same size along the principal eigenvector,as shown in the left image of Fig. 4. 

As a result of the division, a common feature can be extracted from pedestrians of different heights, such as an adult and a child. 

Then, the 3D points in each block are projected onto a plane orthogonal to the principal eigenvector, and two widths along the other eigenvectors are computed as the feature. 

The number of blocks is 10. The feature vector is represented as follows.

`f 8 = {w 10 , w 11 , · · · , w j0 , w j1 , · · · , w N0 , w N1 }`

This feature vector is called the ”slice feature” in this paper.

#### B. 2) Distribution of Reflection Intensities in the Cluster

As known in the field of spectroscopy, a substance has its own unique reflectance characteristics. 

The reflection intensities of a pedestrian might have large individual variability because their clothing and their belongings are composed of various materials. 

It is, however, expected that materials leading to false positives, such as trees and utility poles, are comparatively homogeneous. 

Therefore, the reflection intensities of 3D points can contribute to the discrimination of pedestrians and false positives. 

Examples of the reflection intensities of a pedestrian and a utility pole are shown in Fig. 5.

![](https://i.imgur.com/383Nv01.png)

The reflection intensity `P_r` is defined by the following equation. 

It is in inverse proportion to the square of the distance `r`:

![](https://i.imgur.com/zA5Asf1.png)

- `P_0` is the intensity of the emitted laser beam 
- `k` is the coefficient defined by the LIDAR specifications, 
- `σ` is the reflectance of the target.

Strictly speaking, the reflection intensity has to be normalized by the square of the distance. 

We can directly use the sensor output since LIDAR outputs an 8 bit value normalized for the distance as the reflection intensity.

반사도 정보를 이용한 3가지 feature`The following three values are computed from the reflection intensities of the 3D points contained in each candidate:`
- Mean intensity
- Standard deviation of the intensities
- Normalized histogram: the number of bins is 25 and the range of the intensities is divided at equal intervals.

## V. RESULTS

## VI. CONCLUSION

목적 : This paper presents a method for recognizing pedestrians from 3D range data acquired by high-definition LIDAR. 

제안 특징 The slice feature and the distribution of the reflection intensities are proposed to improve the recognition performance at a long range with low spatial resolution. 
- The slice feature can represent the rough profile of a pedestrian shape efficiently and 
- the distribution of the reflection intensities is effective to discriminate the materials of the targets. 

결과 
- The quantitative evaluation using real 3D range data confirms that the proposed method achieves higher performance than the Navarro-Serment method. 
- Moreover, the proposed features can improve the classification ability at a range of more than 30 m.

