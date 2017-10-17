|논문명|Vehicle Detection from 3D Lidar Using Fully Convolutional Network
|-|-|
|저자(소속)|Bo Li (Baidu)|
|학회/년도|29 Aug 2016, [논문](https://arxiv.org/abs/1608.07916)|
|키워드|It is able to predict full 3D bounding boxes even using a 2D CNN|
| 데이터셋(센서)/모델 | KITTI(Velodyne 64E) |
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

### 3.1 Data Preparation

센서 : Velodyne 64E lidar. 

아래 투영(projection)함수를 이용하여 2D pointmap으로 변경 ` points from a Velodyne scan can be roughly projected and discretized into a 2D point map, using the following projection function.`

![](https://i.imgur.com/XePouFV.png)

- $$ P = (x,y,z)^T$$: Denotes 3D Point
- $$ (r, c) $$ : Denotes the 2D map position of its projection
- $$ \theta, \phi $$ : denote the azimuth and elevation angle when observing the point
- $$ \Delta\theta, \Delta\phi$$ : the average horizontal and vertical angle resolution between consecutive beam emitters, respectively

The projected point map is analogous to cylindral images. 

We fill the element at $$(r, c)$$ in the 2D point map with 2-channel data $$(d, z)$$
- $$d = \sqrt{x^2+y^2} $$
- Note that $$x$$ and $$y$$ are coupled as $$d$$ for rotation invariance around $$z$$
 
 
![](https://i.imgur.com/oCCHDwo.png)

An example of the $$d$$ channel of the 2D point map is shown in Figure 1a. 

Rarely some points might be projected into a same 2D position, in which case the point
nearer to the observer is kept. 

Elements in 2D positions where no 3D points are projected into are filled with $$(d, z) = (0, 0)$$



### 3.2 Network Architecture

제안된 방식의 큰 흐름은 [11],[18]과 비슷하다. `The trunk part of the proposed CNN architecture is similar to Huang et al. [11], Long et al. [18]. `


```
[11] Lichao Huang, Yi Yang, Yafeng Deng, and Yinan Yu. DenseBox: Unifying Landmark Localization with End to End Object Detection. pages 1–13, 2015.
[18] Jonathan Long, Evan Shelhamer, and Trevor Darrell. Fully convolutional networks for semantic segmentation. arXiv preprint arXiv:1411.4038, 2014.
```

![](https://i.imgur.com/XDiMdhP.png)
```
[Fig. 2. The proposed FCN structure to predict vehicle objectness and bounding box simultaneously.]
- The output feature map of conv1/deconv5a, conv1/deconv5b and conv2/deconv4 are first concatenated and 
- then ported to their consecutive layers, respectively.
```

As illustrated in Figure2, 
1. the CNN feature map is down-sampled consecutively in the first 3 convolutional layers 
2. and up-sampled consecutively in deconvolutional layers. 
3. Then the trunk splits at the 4th layer into a objectness classification branch and a 3D bounding box regression branch. 

#### A. 입력

- The input point map, output objectness map and bounding box map are of the same width and height, to provide point-wise prediction. 

- Each element of the objectness map predicts whether its corresponding point is on a vehicle. 

- If the corresponding point is on a vehicle, its corresponding element in the bounding box map predicts the 3D bounding box of the belonging vehicle. 

- Section III-C explains how the objectness and bounding box is encoded.

#### B.

- In conv1, the point map is down-sampled by 4 horizontally and 2 vertically. 
 - This is because for a point map captured by Velodyne 64E, we have approximately
∆φ = 2∆θ, 
 - i.e. points are denser on horizotal direction.

- Similarly, the feature map is up-sampled by this factor of (4, 2) in deconv6a and deconv6b, respectively. 

- The rest conv/deconv layers all have equal horizontal and vertical resolution, respectively, and use squared strides of (2, 2) when up-sampling or down-sampling.


#### C.

- The output feature map pairs of conv3/deconv4, conv2/deconv5a, conv2/deconv5b are of the same sizes, respectively. 

- We concatenate these output feature map pairs before passing them to the subsequent layers. 

- This follows the idea of Long et al. [18]. 

- Combining features from lower layers and higher layers improves the prediction of small objects and object edges.


### 3.3 Prediction Encoding


### 3.4 Training Phase

#### A. Data Augmentation


#### B. Multi-Task Training


#### C. Training strategies




### 3.5 Testing Phase


## 4. EXPERIMENTS

### 4.1 Performane Analysis on Offline Evaluation

### 4.2 Related Work Comparison on the Online Evaluation

사실 3D보다 이미지 기반이 성능이 좋다 그 이유는 크게 아래와 같다. 
-  First, the image data have much higher resolution which significantly enhance the detection performance for far and occluded objects. 
- Second, the image space based criterion does not reflect the advantage of range scan methods in localizing objects in full 3D world space

> Related explanation can also be found from Wang and Posner [31].