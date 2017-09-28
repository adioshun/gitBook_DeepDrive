|논문명|Vehicle Detection from 3D Lidar Using Fully Convolutional Network
|-|-|
|저자(소속)|Bo Li (Baidu)|
|학회/년도|29 Aug 2016, [논문](https://arxiv.org/abs/1608.07916)|
|키워드|It is able to predict full 3D bounding boxes even using a 2D CNN|
|참고||
|코드||

# VeloFCN4VD


## 1. INTRODUCTION

robotic 분야에서 이루어진 3D 클라우드 포인트를 이용한 tasks들 :  Localization, mapping, object detection and scene parsing [16]

목표 : we design a fully convolutional network (FCN) to detect and localize objects as 3D boxes from range scan data. 

## 2. RELATED WORKS

### 2.1 Object Detection from Range Scans

Object detection algorithms = propose candidates + classify


#### A. propose candidates by segmenting the point cloud into clusters

- rule-based
  1. simply removing the ground plane 
  2. 단순하게 바닥부분 제거 하고 남은 부분끼리 클러스터링 하여 추측`cluster the remaining points can generate reasonable segmentation`[10, 5].
 
- forming graphs on the point cloud [32, 14, 21, 29, 30].


- [2] suggests to segment the scene hierarchically and keep segments of different scales.

- directly exhaust the range scan space to propose candidates to avoid incorrect segmentation.
 - For example, Johnson and Hebert [13] randomly samples points from the point cloud as correspondences.
 - Wang andPosner [31] scan the whole space by a sliding window to generate proposals.

#### B. Classification 


최근의 머신러닝 기반의 탐지 방법들은 일부 Feature들을 hand-crafted한후에 분류 하는데 사용 하였다. 
- Triebel et al. [29], Wang et al. [32], Teichmanet al. [28] use shape spin images, shape factors and shape distributions.
- Teichman et al. [28] also encodes the object moving track information for classification.
- Papon et al. [21] uses FPFH.
- Other features include normal orientation, distribution histogram and etc.

A comparison of features can be found in [1].

Besides the hand-crafted features, Deuge et al. [4], Laiet al. [15] explore to learn feature representation of point cloud via sparse coding.

#### [참고] RGBD images

range scan에서의 물체 탐지는 RGBD images [3, 17]를 이용한 탐지 방법과 깊은 연관이있다.  
- The depth channel can be interpreted as a range scan and naturally applies to some detection algorithms designed for range scan.

>  RGBD data : 색상정보(RGB) + 물체까지의 거리정보 (Depth)를 함께 측정할

> [3]은 RGBD가 아니라, 그냥 카메라 센서로 알고 있음 

```
[3] Xiaozhi Chen, Kaustav Kundu, Yukun Zhu, Andrew G Berneshawi, Huimin Ma, Sanja Fidler, and Raquel Urtasun. 3d object proposals for accurate object class detection. Advances in Neural Information Processing Systems, pages 424–432, 2015.
[17] Dahua Lin, Sanja Fidler, and Raquel Urtasun. Holistic scene understanding for 3D object detection with RGBD cameras. Proceedings of the IEEE International Conference on Computer Vision, pages 1417–1424, 2013.
```


### 2.1 Convolutional Neural Network on Object Detection

#### A. 기존 2D CNN기반 물체 탐지 

- R-CNN [8] proposes candidate regions and uses CNN to verify candidates as valid objects

- OverFeat [25], DenseBox [11] and YOLO [23] uses end-to-end unified FCN frameworks which predict the objectness confidence and the bounding boxes simultaneously over the whole image.

#### B. 3D로의 확장 연구 
Some research has also been focused on applying CNN on 3D data.

##### 가. RGBD
RGBD dat에서 D를 하나의 이미지 채널로 간주 하고 2D CNN를 이용하여 분류/탐지 하였다. [9, 24, 26].

```
[9] S Gupta, R Girshick, P Arbelaez, and J Malik. Learning ´Rich Features from RGB-D Images for Object Detection and Segmentation. arXiv preprint arXiv:1407.5736, pages 1–16, 2014.
[24] Max Schwarz, Hannes Schulz, and Sven Behnke. RGB-D Object Recognition and Pose Estimation based on Pretrained Convolutional Neural Network Features. IEEE International Conference on Robotics and Automation
(ICRA), (May), 2015.
[26] Richard Socher, Brody Huval, Bharath Bath, Christopher D Manning, and Andrew Y Ng. Convolutionalrecursive deep learning for 3d object classification. Advances in Neural Information Processing Systems, pages 665–673, 2012.
```

##### 나. Point CLoud 
 - For 3D range scan some works discretize point cloud along 3D grids and train3D CNN structure for classification [33, 19]. (포인트 클라우드를 3D 그리드 + Traind 3D CNN으로 분리) 
  
```
[33] Zhirong Wu and Shuran Song. 3D ShapeNets : A Deep Representation for Volumetric Shapes. (CVPR2015), pages 1–9, 2015.
[19] Daniel Maturana and Sebastian Scherer. VoxNet : A 3D Convolutional Neural Network for Real-Time Object Recognition. pages 922–928, 2015
```

These classifier scan be integrated with region proposal method like slidin gwindow [27] for detection tasks.

### 2.3 본 논문의 접근 방안 
In this paper, **our approach project range scans as 2D maps** similar to the depthmap of RGBD data. 

The frameworks of Huang et al. [11], Sermanet et al. [25] are transplanted to predict the objectness and the 3D object bounding boxes in a unified end-to-end manner.


## 3. 제안 방식 



