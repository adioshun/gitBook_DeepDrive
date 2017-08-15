|논문명|Multi-View 3D Object Detection Network for Autonomous Driving
|-|-|
|저자(소속)|Xiaozhi Chen (칭화대), Bo Li (Baidu)|
|학회/년도|2017, [논문](https://arxiv.org/pdf/1611.07759.pdf)|
|키워드| |
|참고|[홈페이지](https://xiaozhichen.github.io), [Youtube](https://youtu.be/POqBiiLaslk), [MobileNets](https://www.gitbook.com/book/adioshun/deep_drive/edit#/edit/master/papermovilenet.md?_k=rydhgy)|
|코드|[3rd Reader](https://github.com/hengck23/didi-udacity-2017)|

# Multi-View 3D CNN for Vehicle Detection 

## 0. Abstract

목표 : A sensory-fusion framework 
 - 입력 : LIDAR point cloud + RGB images
 - 출력 : predicts oriented 3D bounding boxes

구성 
- 3D object proposal generation 
- multi-view feature fusion

특징
- Generates 3D candidate boxes efficiently from the bird’s eye view representation of
3D point cloud. 
- We design a deep fusion scheme to combine region-wise features from multiple views and enable interactions between intermediate layers of different paths.


## 1. Introduction

### 1.1 기존 연구 
각 센서들의 장점 
- Laser scanners have the advantage of accurate depth information 
- cameras preserve much more detailed semantic information

최근 LIDAR기반 방식들 기술 동향 
- Place 3D windows in 3D voxel grids to score the point cloud [26, 7] 
- Apply CNN to the front view point map in a dense box prediction scheme [17].


최근 Image기반 방식들 기술 동향 
- Image-based methods [4, 3] typically first generate 3D box proposals and then perform region-based recognition using the Fast RCNN [10] pipeline.

최근 LiDAR + Image 기반 방식들 기술 동향 
- [11, 8] combine LIDAR and images for 2D detection by employing early or late fusion schemes. 

### 1.2 본 논문 제안 

The main idea for utilizing multimodal information is to perform `region-based` feature fusion.

![](http://i.imgur.com/RDijuv4.png)
구성 : a 3D Proposal Network + a Region-based Fusion Network. 


1. We first propose a multi-view encoding scheme to obtain a compact and effective representation for sparse 3D point cloud.

#### A. 3D proposal network
- 목적 : 포인트 클라우드의 bird’s eye view를 이용하여서 3D 후보 영역을 추천 한다. 
 - `The 3D proposal network utilizes a bird’s eye view representation of point cloud to generate highly accurate 3D candidate boxes.`

- 장점 : The benefit of 3D object proposals is that **it can be projected to any views in 3D space**.

#### B. Region-based Fusion Network

The multi-view fusion network extracts region-wise features by projecting 3D proposals to the feature maps from mulitple views.

We design a deep fusion approach to enable interactions of intermediate layers from different views.

### C. 성능 향상을 위한 기타 방법 

- Combined with drop-path training [15] and auxiliary loss, our approach shows superior performance over the early/late fusion scheme.

Given the multi-view feature representation,the network performs oriented 3D box regression which predict accurate 3D location, size and orientation of objects in 3D space.


## 2. 관련 연구 

### 2.1 3D Object Detection in Point Cloud

대부분의 방법들은 3D 포인트 클라우드를 Voxel 그리드로 인코딩 시키는 것이다. `Most existing methods encode 3D point cloud with voxel grid representation. `


- Sliding Shapes [22] and Vote3D [26] apply SVM classifers on 3D grids encoded with geometry features.
- Some recently proposed methods [23, 7, 16] improve feature representation with 3D convolutions.

- In addition to the 3Dvoxel representation, VeloFCN [17] projects point cloud to the front view, obtaining a 2D point map. 
 - They apply a fully convolutional network on the 2D point map and predict 3D boxes densely from the convolutional feature maps.
 
- [24, 18, 12] investigate volumetric and multi-view representation of point cloud for 3D object classification. 


In this work, we encode 3D point cloud with multi-view feature maps, enabling region-based representation for multimodal fusion


[22] S. Song and J. Xiao. Sliding shapes for 3d object detection in depth images. In ECCV. 2014.
[26] D. Z. Wang and I. Posner. Voting for voting in online point cloud object detection. In Proceedings of Robotics: Science and Systems, 2015.
[23] S. Song and J. Xiao. Deep sliding shapes for amodal 3d object detection in rgb-d images. In CVPR, 2016. 
[7] M. Engelcke, D. Rao, D. Zeng Wang, C. Hay Tong, and I. Posner. Vote3Deep: Fast Object Detection in 3D Point Clouds Using Efficient Convolutional Neural Networks. arXiv:1609.06666, 2016.
[16] B. Li. 3d fully convolutional network for vehicle detection in point cloud. IROS, 2017. 
[17] B. Li, T. Zhang, and T. Xia. Vehicle detection from 3d lidar using fully convolutional network. In Robotics: Science and Systems, 2016.
[24] H. Su, S.Maji, E.Kalogerakis, and E. Learned-Miller. Multiview convolutional neural networks for 3d shape recognition. In ICCV, 2015. 
[18] C. R. Qi, M. N. H. Su, A. Dai, M. Yan, and L.Guibas. Volumetric and multi-view cnns for object classification on 3d data. In CVPR, 2016. 
[12] V. Hegde and R. Zadeh. Fusionnet: 3d object classification using multiple data representations. CoRR, abs/1607.05695, 2016. 

### 2.2 3D Object Detection in Images. 

- 3DVP [28] introduces 3D voxel patterns and employ a set of ACF detectors to do 2D detection and 3D pose estimation. 

- 3DOP [4] reconstructs depth from stereo images and uses an energy minimization approach to generate 3D box proposals, which are fed to an R-CNN [10] pipeline for object recognition.
 
- Mono3D [3] shares the same pipeline with 3DOP, it generates 3D proposals from monocular images. 

- [31, 32] introduces a detailed geometry representation of objects using 3D wire frame models. 

- To incorporate temporal information, some work[6, 21] combine structure from motion and ground estimation to lift 2D detection boxes to 3D bounding boxes. 

- Image-based methods usually rely on accurate depth estimation or landmark detection. 

본 논문에서는 : Our work shows how to incorporate LIDAR point cloud to improve 3D localization.

### 2.3 Multimodal Fusion

자율 주행 분야에서는 멀티모달 퓨전에 대하여서는 많은 연구가 이루어 지지는 않았다. 


- [11] combines images, depth and optical flow using a mixture-of-experts framework for 2D pedestrian detection. 

- [8] fuses RGB and depth images in the early stageand trains pose-based classifiers for 2D detection. 

본 논문에서는 FractalNet [15] and Deeply-Fused Net [27]에 영감을 받았다. 
 - In FractalNet[15] , a base module is iteratively repeated to construct a networkwith exponentially increasing paths. 
 - Similarly, [27] constructs deeply-fused networks by combining shallow and deep sub networks. 

위 방식과 다른점 :  `Our network differs from them by using the same base network for each column and adding auxiliary paths and losses for regularization.`

### 2.4 3D Object Proposals 
2D와 유사한 방법으로 3D에서는 Object Proposals 을 수행 한다.  
 - generate a smallset of 3D candidate boxes in order to cover most of the objects in 3D space. 

- 3DOP [4] designs some depth features in stereo point cloud to score a large set of 3D candidate boxes. 

- Mono3D [3] exploits the ground plane priorand utilizes some segmentation features to generate 3D proposals from a single image. 

Both 3DOP and Mono3D (use hand-crated) features. 

- Deep Sliding Shapes [23] exploits more powerful deep learning features. 
 - However, it operates on 3D voxel grids and uses computationally expensive 3D convolutions. 

본 논문에서는 : We propose a more efficient approach by introducing a bird’s eye view representation of point cloud and employing 2D convolutions to generate accurate 3D proposals.

## 3. MV3D Network

###### Step 1. 입력 =  multi-view representation of 3D point cloud(Bird Eye view, Front view) + 이미지

###### Step 2. 3D 후보영역 선발 : bird’s eye view이용

###### Step 3. region-based representation을 통해 Multi-view representation 통합(Fuse)

###### Step 4. 분류 및 BBox 찾기 (category classification and oriented 3D box regression)

### 3.1. 3D Point Cloud Representation

기존 방식 
- Usually encodes 3D LIDAR point cloud into a 3D grid [26, 7] 
 - Raw 데이터를 잘 유지하고 있지만, feature extraction 계산 부하가 크다. 
- Usually encodes 3D LIDAR point cloud into a front view map [17]. 


제안 방식
- Encodes 3D LIDAR point cloud into the bird’s eye view
- Encodes 3D LIDAR point cloud into the front view

![](http://i.imgur.com/atUf0Of.png)

#### A. Bird’s Eye View Representation. 
The bird’s eye view representation is encoded by height, intensity and density.

We discretize the projected point cloud into a 2D grid with resolution of 0.1m. 

##### 가. height feature

- For each cell, the height feature is computed as the maximum height of the points in the cell. 

- To encode more detailed height information, the point cloud is devided equally into M slices. 

- A height map is computed for each slice, thus we obtain M height maps. 

##### 나. intensity feature(빛의 반사)

- The intensity feature is the reflectance value of the point which has the maximum height in each cell. 

##### 다. density feature

- The point cloud density indicates the number of points in each cell. 


##### 라. 3개의 Feature 처리 방법 

- To normalize the feature, it is computed as $$min(1.0, \frac{log(N+1)}{log(54)})$$
 -  $$N$$ = the number of points in the cell. 


- Note that the **intensity** and **density** features are computed for the whole point cloud while the **height** feature is computed for M slices, thus in total the bird’s eye view map is encoded as (M +2)-channel features.

#### B. Front View Representation. 

- Front view는 bird’s eye view에 추가적 정보(complementary information)들 제공(provide)

- LiDAR 포인트 클라우드는 sparse하기 때문에 이미지에 투영하게 되면 sparse 2D pointmap이 생성된다. 
 - `As LIDAR point cloud is very sparse, projecting it into the image plane results in a sparse 2D pointmap. `

- 따라서, 제안 방식은 `cylinder plane`에 투영하여 `dense front view map`을 생성한다. [17:Bo Li]

As LIDAR point cloud is very sparse, projecting it into the image plane results in a sparse 2D pointmap. 
  - `Instead, we project it to a cylinder plane to generate a dense front view map as in [17].`

Given a 3D point $$p = (x, y, z)$$, its coordinates $$p_{fv} = (r, c)$$ in the front view map can be computed using
