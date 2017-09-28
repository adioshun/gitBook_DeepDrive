| 논문명 | VoxNet: A 3D Convolutional Neural Network for Real-Time Object Recognition |
| --- | --- |
| 저자\(소속\) | Daniel Maturana \(CMU\) |
| 학회/년도 | IROS 2015, [논문](http://ieeexplore.ieee.org/document/7353481/) |
| 키워드 | Volumetric Occupancy Grid + 3D CNN |
| 참고 | 이전연구: 3D convolutional neural networks for landing zone detection from lidar,” in ICRA, 2015. |
| 코드 | [Theano+Lasagne](https://github.com/dimatura/voxnet) |

![](http://i.imgur.com/yXb89IB.png)

# VoxNet

## 0. Abstract

* Range sensors such as LiDAR and RGBD cameras가 많이 사용되고 있다.

* 하지만 large amounts of point cloud data를 충분히 활용하고 있지 않다.

* VoxNet을 제안 : integrating a `volumetric Occupancy Grid` representation with a supervised 3D Convolutional Neural Network \(3D CNN\).

## 1. Introduction

본 논문에서는 `3D point cloud segment`를 이용하여서 `object 분류`의 문제점\(eg. background clutter\)을 살펴 본다.

원인 : 작업 Pipe-line

* extraction and aggregation of hand-engineered features
* fed into an off-the-shelf classifier such as SVMs.

이러한 Pipe-line은 2D `object 분류`와도 비슷하다.

* CNN의 발전으로 데이터를 활용하는 방향으로 바뀌었다. 
* 3D 기본은 같으므로 변경이 가능하다. 단, 계산 부하가 크다. 

## 2. 관련 연구

### 2.1 Object Recognition with Point Cloud Data

3D point clouds를 이용한 물체 인식은 많은 연구가 있다.

기존 연구 : hand-crafted features\(or descriptors\) + machine learning classifier \(\[10\], \[11\],\[12\], \[13\]\).

* The situation is similar for semantic segmentation,with structured output classifiers instead of single output classifiers \(\[14\], \[15\], \[16\]\). 

제안 방식 : extract features and classify objects from the `raw volumetric data`.

* Our volumetric representation is also richer than point clouds, as it distinguishes free space  
  from unknown space.

* In addition, features based on point clouds often require spatial neighborhood queries, which can quickly become intractable\(고치기 어려운\) with large numbers of points.

```
[10] A. Frome, D. Huber, and R. Kolluri, “Recognizing objects in range data using regional point descriptors,” ECCV, vol. 1, pp. 1–14, 2004.
[11] J. Behley, V. Steinhage, and A. B. Cremers, “Performance of histogram descriptors for the classification of 3D laser range data in urban environments,” in ICRA, 2012, pp. 4391–4398.
[12] A. Teichman, J. Levinson, and S. Thrun, “Towards 3D object recognition via classification of arbitrary object tracks,” in ICRA, 2011, pp. 4034–4041.
[13] A. Golovinskiy, V. G. Kim, and T. Funkhouser, “Shape-based recognition of 3D point clouds in urban environments,” ICCV, 2009.
[14] D. Munoz, N. Vandapel, and M. Hebert, “Onboard contextual classification of 3-D point clouds with learned high-order markov random fields,” in ICRA, 2009.
[15] H. Koppula, “Semantic labeling of 3D point clouds for indoor scenes,”NIPS, 2011.
[16] X. Ren, L. Bo, and D. Fox, “RGB-(D) scene labeling: Features and algorithms,” in CVPR, 2012.
```

### 2.2 2.5D Convolutional Neural Networks

#### A. RGBD

이미지\(RGB\)에서 사용한 CNN기법을 RGBD로 확장하려는 연구가 진행 되었다. \[17\], \[18\], \[19\], \[20\]

* 간단한 접근법은 D를 또 다른 채널로 간주하고 처리 하는 것이다. 
* 단점 \#1 : geometric information를 제대로 활용 못함 
* 단점 \#2 : integrate information across viewpoints하기 어려움 

```
[17] I. Lenz, H. Lee, and A. Saxena, “Deep learning for detecting robotic grasps,” in RSS, 2013.
[18] Richard Socher and Brody Huval and Bharath Bhat and Christopher D.Manning and Andrew Y. Ng, “Convolutional-Recursive Deep Learning for 3D Object Classification,” in NIPS, 2012.
[19] L. A. Alexandre, “3D object recognition using convolutional neural networks with transfer learning between input channels,” in IAS, vol. 301, 2014.
[20] N. Hoft, H. Schulz, and S. Behnke, “Fast semantic segmentation of RGBD scenes with gpu-accelerated deep neural networks,” in 37th Annual German Conference on AI, 2014, pp. 80–85.
```

#### B. LiDAR

* \[4\] propose a feature that locally describes scans with a 2.5D representation,

* \[21\] studies this approach in combination with a form of unsupervised feature learning.

* \[22\] propose an encoding that makes better use of the 3D information in the depth, but is still 2D-centric.

```
[4] A. Quadros, J. Underwood, and B. Douillard, “An occlusion-aware feature for range images,” in ICRA, May 14-18 2012.
[21] M. De Deuge, A. Quadros, C. Hung, and B. Douillard, “Unsupervised feature learning for classification of outdoor 3d scans,” in ACRA, 2013.
[22] S. Gupta, R. Girshick, P. Arbelaez, and J. Malik, “Learning rich features ´from RGB-D images for object detection and segmentation,” in ECCV, 2014.
```

### 2.3 3D Convolutional Neural Networks

비디오 분석에서는 3D CNN이 성공적으로 적용 되었다. \(\[23\], \[24\]\)

* 하지만 이때는 `시간 정보`가 3rd D로 작용하였다. 
* 알고림적으로 논문의 제안 방식과 비슷하지만, 사용되는 데이터 속성이 다르다. 

#### A. RGBD

* \[25\] uses an unsupervised volumetric feature learning approach as part of a pipeline to detect indoor objects.

  * This approach is based on `sparse coding`, which is generally slower than convolutional models. 

* \[26\] propose a generative 3D convolutional model of shape and apply it to RGBD object recognition, among other tasks.

```
[25] K. Lai, L. Bo, and D. Fox, “Unsupervised feature learning for 3D scene labeling,” in ICRA, 2014.
[26] Z. Wu, S. Song, A. Khosla, F. Yu, L. Zhang, X. Tang, and J. Xiao, “3d shapenets: A deep representation for volumetric shape modeling,” in CVPR, 2015.
```

#### B. LiDAR

* \[27\] is an early work that studies a3D CNN for use with LiDAR data with a binary classification task.

* \[28\], which introduced 3D CNNs for landing zone detection in UAVs.

  * Compared to this work, we tackle a more general objectre cognition task with 3D data from different modalities. 

We also study different representations of occupancy and propose techniques to improve performance when the data varies significantly in scale and orientation

```
[27] D. Prokhorov, “A convolutional learning system for object classification in 3-D lidar data,” IEEE TNN, vol. 21, no. 5, pp. 858–863, May 2010.
[28] D. Maturana and S. Scherer, “3D convolutional neural networks for landing zone detection from lidar,” in ICRA, 2015.
```

## 3. Approach



