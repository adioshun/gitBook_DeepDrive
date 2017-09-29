|논문명|Computer Vision for Autonomous Vehicles: Problems, Datasets and State-of-the-Art
|-|-|
|저자(소속)||
|학회/년도| 2017 [논문](https://arxiv.org/abs/1704.05519v1)|
|키워드||
|참고|[홈페이지](http://www.cvlibs.net/projects/autonomous_vision_survey/), [CVPR 2016(1:02)](https://www.youtube.com/watch?v=n8T7A3wqH3Q&feature=share)|
|코드||


- ~~[A REVIEW OF POINT CLOUDS SEGMENTATION AND CLASSIFICATION ALGORITHMS](https://www.int-arch-photogramm-remote-sens-spatial-inf-sci.net/XLII-2-W3/339/2017/isprs-archives-XLII-2-W3-339-2017.pdf)~~: 딥러닝 외 방식들 (Edge based, Region growing, Model fitting, Hibrid method, Hirarchical clustering, k-mean clustering)


# Survey 

Recognition, reconstruction, motion estimation, tracking, scene understanding and end-to-end learning

![](https://i.imgur.com/f5mYsf1.png)

자율 주행차가 아직까지 먼 미래의 이야기인 이유

1. First, autonomous systems which operate in complex dynamic environments require artificial intelligence which generalizes to unpredictable situations and reasons in a timely manner. 
2. Second, informed decisions require accurate perception, yet most of the existing `computer vision systems` produce errors at a rate which is not acceptable for autonomous navigation.

> 본 논문은 2번째 이유인 CV에 초점을 둔다. 

기존 Survey 논문들 

- Winner et al. (2015) explains in detail systems for `active safety and driver assistance`, considering both their structure and their function. 
    - Their focus is to cover all aspects of driver assistance systems and the chapter about machine vision covers only the most basic concepts of the autonomous vision problem. 
- Klette (2015) provide an overview over `vision-based driver assistance systems`. 
    - They describe most aspects of the perception problem at a high level, 
    - but do not provide an in-depth review of the state-of-the-art in each task as we pursue in this paper. 
- Zhu et al. (2017) provide an overview of environment perception for intelligent vehicles, focusing on `lane detection`, `traffic sign/light recognition` as well as `vehicle tracking`.


```
Winner, H., Hakuli, S., Lotz, F., Singer, C., Geiger, A. et al. (2015). Handbook of Driver Assistance Systems . Springer Vieweg.
Klette, R. (2015).Vision-based Driver Assistance Systems .  Technical Report CITR, Auckland, New Zealand.
Zhu, H., Yuen, K. V., Mihaylova, L., & Leung, H. (2017).   Overview of en-vironment  perception  for  intelligent  vehicles. IEEE  Trans.  on  Intelligent Transportation Systems (TITS),PP , 1–18.
```

## 1. History of Autonomous Driving 

## 1.1 Autonomous Driving Projects

### A. PROMETHEUS project
started 1986 in Europe and involved more than 13 vehicle manufacturers, several research units from governments and universities of 19 European countries. 

### B. Navlab (CMU)
One of the first projects in the United States was Navlab Thorpe et al. (1988)  by  the  Carnegie  Mellon  University  which  achieved  a major milestone in 1995,


### C. etc.

> 약 1page에 걸쳐서 다른 프로젝트들 소개 

### 1.2 Autonomous Driving Competitions

#### A. The European Land Robot Trial (ELROB)

## 2. Datasets & Benchmarks

### 2.1 Real-World Datasets

#### A. Stereo and 3D Reconstruction


#### B. Optical Flow

#### C. Object Recognition and Segmentation

- ImageNet (Deng et al. (2009))
- PASCAL VOC (Everingham et al. (2010))
- Microsoft  COCO  (Lin  et  al.  (2014))
- Cityscapes  (Cordts  et  al. (2016))
- TorontoCity (Wang et al. (2016)) 

#### D. Tracking


#### E. Aerial  Image  Datasets

#### F. Autonomous Driving

- KITTI Vision Benchmark
- Cityscapes Datase
- TorontoCity benchmark

#### G. Long-Term Autonomy

Maddern et al. (2016). They collected images, LiDAR and GPS data while traversing 1,000 km in central Oxford in the UK during one year.  

This allowed them to capture large variations in scene appearance due to  illumination,  weather  and  seasonal  changes,  dynamic objects, and constructions.  

Such long-term datasets allow for in-depth investigation of problems that detain the realization of autonomous vehicles such as localization in di erent times of the year.
 
```
Maddern, W., Pascoe, G., Linegar, C., & Newman, P. (2016).  1 year, 1000km: The oxford robotcar dataset. International Journal of Robotics Research (IJRR) , 
```

### 2.2. Synthetic Data (가상 데이터)

> 실생활 데이터를 Pixel 수준으로 Labeling하는것은 어렵다. 하지만, 게임등으로 습득 하는것은 쉽다. 


## 3. Cameras Models & Calibration

## 4. Representations

`Variables` or `parameters` can be associated directly with 
- 2D pixels in an image 
- describe high-level primitives in 3D space. 

In pixel-based representation, each pixel is a separate entity, for example a random variable in a graphical model. 

픽셀은 가장 좋은 representations 중 하나이다. 하지만, 3D를 표현하기 어렵고, 고해상도에서는 계산 부하가 증가 하는 단점이 있다. 

### 4.1 Superpixels (grouping of pixels)

> 슈퍼픽셀(Superpixels): 사진 품질 저하를 최소화하면서 픽셀을 덩어리로 뭉치는 기술이다. 

![](http://www.ddaily.co.kr/data/photos/20131016/20131016025749__744R2.jpg)

정의 Superpixels  = compact  representations based on grouping of pixels

생성 방법 `Superpixel-based representations are obtained by a segmentation of the image into atomic regions`
- atomic regions are ideally similar in color and texture, and respect image boundaries 


가정 사항 `The implicit assumption each superpixel-based method makes is that`
- certain  properties  of  interest  remain  constant  within  a  super-pixel,  
- e.g.,  the  semantic  class  label  or  the  slant  of  a  surface. 

However, boundary adherence with respect to these properties is easily violated, especially for cluttered images when relying on standard segmentation algorithms which leverage color or intensity cues. 

깊이 정보가 더해 진다면 좀더 가치 있는 Feature가 될수 있다. `If  available,  depth  information  can  be  leveraged  as  valu-able  feature  for  accurate  superpixel  extraction  (Badino  et  al. (2009); Yamaguchi et al. (2014)). `

활용 분야 : Superpixels are used as `building blocks` for various tasks such as 
- stereo and flow estimation
- scene flow
- semantic segmentation
- scene  understanding
- 3D  reconstruction

In cases that include geometric reasoning  such  as  stereo  estimation,  superpixels  often  represent 3D planar segments. 

When the goal is to represent real-world scenes with independent object motion as in scene flow or opti-cal flow, superpixels can be generalized to rigidly moving segments or semantic segments 

### 4.2 Stixels

![](https://www.researchgate.net/profile/Rodrigo_Benenson/publication/221430122/figure/fig1/AS:305460738576385@1449838923566/Figure-1-The-stixel-world-is-composed-of-the-ground-plane-and-vertical-sticks-describing.png)

> 지표면에서 물체의 Top까지의 높이 정보???


Stixels are presented as a medium level representation  of  3D  traffic  scenes  with  the  goal  to  **bridge  the  gap  between pixels and objects** (Badino et al. (2009)).  

The so-called “Stixel World” representation originates from the observation that **free space in front of the vehicle is mostly limited by vertical surfaces**.  

> The stixel world is composed of the ground plane and vertical sticks describing the obstacles

Stixels are represented by a set of **rectangular sticks** standing vertically on the ground to approximate these surfaces.  

Assuming a constant width, each stixel is defined by its 3D position relative to the camera and its height.  

The main goal is to gain efficiency through a compact, complete, stable, and  robust  representation.   

In  addition,  Stixel  representations provide an encoding of the free space and the obstacles in the scene.

### 4.3 3D Primitives

Atomic regions which are geometrically meaningful allow the shape of urban objects to be better preserved.  

###### 관련 연구들 

- In Cornelis et al. (2008), 3D city models are composed of ruled surfaces for both the facades and the roads.  

- Duan & Lafarge (2016) use poly-gons with elevation estimate for 3D city modeling from pairs of satellite images.  

- de Oliveira et al. (2016) update a list of large scale polygons over time for an incremental scene representa-tion from 3D range measurements.  

- Lafarge et al. (2010) use library of 3D blocks for reconstructing buildings with different roof forms. 

- Lafarge & Mallet (2012); Lafarge et al. (2013) use 3D-primitives such as planes,  cylinders,  spheres or cones for describing regular structures of the scene.  

- Dub ́ e et al. (2016) segments point clouds into distinct elements for a  loop-closure detection algorithm based on the matching of 3D segments


## 5.  Object Detection

**Sensor **
-  The visible spectrum (VS) is typically used for daytime detections whereas the infrared spectrum can be used for night-time detection.  
- Thermal infrared (TIR) cameras capture rela-tive temperature which allows to distinguish warm objects like pedestrians from cold objects like vegetation or the road.
- Laser scanners(LiDAR) can provide range information which is helpful for detecting an object and localizing it in 3D
- 요즘은 여러 센서 정보를 함께 고려 하는 `Fusion Sensor`기술 연구 중임 

**Standard Pipeline**
- preprocessing
- region of interest extraction (ROI)
- object classification 
- verification/ refinement.

**Classification**
- Handcraft
- CNN

**Part-based Approaches**
- 연결된 물체 전체를 학습 시키는 것은 다양성 때문에 어렵다.-> 부분으로 나누어서 학습 제안 (사람 = 머리 + 몸통+팔+다리)
- 관련 연구 : The Deformable Part Model (DPM) by Felzenszwalb et al. (2008) attempts to break down the complex appearance of objects into easier parts for training SVMs 
- 문제점 : Can not represent contextual information which is necessary for occlusion reasoning


![](https://i.imgur.com/8AhdGaB.png)

### 5.1 2D Object Detection


> 추후 시간 가지고 다시 살펴 보기 




### 5.2 3D Object Detection from 2D Images 

Geometric 3D representations of object classes can recover far more details than just 2D or 3D bounding boxes, however most of today’s object detectors are focused on robust 2D match-ing.

3D representations는 2D에 비하여 정보량은 많지만, 현재 대부분의 연구는 2D에 맞추어져 있다. 
  
#### A. 3D CAD + PCA  
  
Zia et al. (2013) exploit the fact that high-quality 3D CAD models are available for many important classes.  
- From these models, they obtain coarse 3D wireframe models using principal components analysis and train detectors for the vertices of the wireframe. 
- At test time, they generate evidence for vertices by densely applying the detectors. 

```
Zia, M., Stark, M., Schiele, B., & Schindler, K. (2013). Detailed 3D representations for object recognition and modeling. IEEE Trans. on Pattern Analysis and Machine Intelligence (PAMI),35 , 2608–2623
```


#### B. Advanced 3D CAD + PCA 

Zia et al. (2015) extend this work by directly using detailed 3D CAD models in their formu-lation, combining them with explicit representations of likely occlusion patterns. 
- Further, a ground plane is jointly estimated to stabilize the pose estimation process. 
- This extension outperforms the pseudo-3D model of Zia et al. (2013) and shows the benefits of reasoning in true metric 3D space.

```
Zia, M., Stark, M., & Schindler, K. (2015).  Towards scene understanding with detailed 3d object representations. International Journal of Computer Vision (IJCV),112 , 188–203.
```

#### C. 3D geometric representation(CAD?) + real-world images

기존 방법 단점 : they can not yet compete with state-of-the-art detectors using 2D bounding boxes. 

Pepik et al. (2015) propose a 3D extension of the powerful deformable part model, 
- which combines the 3D geometric representation with robust matching to real-world images.
- They further add 3D CAD information of the object class of interest as geometry cue to enrich the appearance model.

```
Pepik, B., Stark, M., Gehler, P. V., & Schiele, B. (2015).  Multi-view and 3d deformable  part  models. IEEE  Trans.  on  Pattern  Analysis  and  Machine Intelligence (PAMI),37 , 2232–2245.
```


### 5.3 3D Object Detection from 3D Point Clouds

> 3D 데이터는 sparse하여 2D에 비하여 성능이 별로 좋지 않다. 

#### A. Vote 3D
Wang & Posner (2015) propose an efficient scheme to apply the common `2D sliding window detection` approach to 3D data. 
- More specifically, they exploit the sparse nature of the problem using  a `voting  scheme`  to  search  all  possible  object  locations and orientations.  

```
Wang, D. Z., & Posner, I. (2015). Voting for voting in online point cloud object
detection. In Proc. Robotics: Science and Systems (RSS).
```

#### B. VeloFCN

Li et al. (2016b) improve upon these results by exploiting a fully convolutional neural network for detecting vehicles from range data. 

They represent the data in a **2D point map**, and predict an objectness confidence and a bounding box simultaneously using a single 2D CNN. 

The encoding used to represent the data allows them to predict the full 3D bounding box of the vehicles. 

```
Li, B., Zhang, T., & Xia, T. (2016b). Vehicle detection from 3d lidar using fully
convolutional network. In Proc. Robotics: Science and Systems (RSS).
```
  
   
#### C. Vote3deep
    
Engelcke et al. (2016) leverage a feature-centric voting scheme to implement a novel convolutional layer which  exploits  the  sparsity  of  the  point  cloud.   

Additionally, they propose to use the $$L1$$ penalty for regularization. Relying on laser range data alone makes the detection task challenging due to the limited density of the laser scans. 

Thus, existing  LiDAR-based  approaches  perform  weaker  compared to their image-based counterparts on the KITTI datasets. 

```
Engelcke, M., Rao, D., Wang, D. Z., Tong, C. H., & Posner, I. (2016). Vote3deep: Fast object detection in 3d point clouds using efficient convolutional neural networks. arXiv.org, 609.06666.
```

#### MV3D


Chen et al. (2016c) combine `LiDAR laser` range data with `RGB images` for object detection.   

In their approach,  the sparse point cloud  is encoded  using  a  compact  multi-view  representation and a proposal generation network utilizes the bird’s eye view representation of the point cloud to generate 3D candidates. 

Finally, they combine region-wise features from multiple views with  a  deep  fusion  scheme   

```
Chen, X., Ma, H., Wan, J., Li, B., & Xia, T. (2016c). Multi-view 3d object
detection network for autonomous driving. arXiv.org, 1611.07759.
```

### 5.4 Person Detection

> 5.3 은 포괄적인 Detection에 초점을 맞추었다면 5.4는 특정 타겟(보행자) Detection에 대해 살펴 보겠다. 


### 5.5 Human Pose Estimation


### 5.6. Discussion

- 차량 탐지는 좋은 성과를 보이고 있다. 하지만, 보행자와 자전거 타는 사람 탐지는 성능이 낮다. 이는 학습 데이터가 적고, 자전거를 탄다는걸 빼고는 객체가 같아 혼란을 주는것 같다. 

- 추가 연구 분야는 `Hige Occluded Object`탐지에 관한 것이다. 
    - 이는 KITTI 리더보드의 easy, moderate and hard examples의 정확도가 많은 차이가 나는것을 보면 알수 있다. 

- A major source of errors are crowds of pedestrians, groups of cyclists and lines of cars that cause many occlusions and lead to missing detections for all methods. 

- Furthermore, a large amount of distant objects needs to be detected in some cases which is still a challenging task for modern methods since the amount of information provided by these objects is very low


## 6. Semantic Segmentation


### 6.1. Semantic Instance Segmentation

목표 : simultaneous detection, segmentation and classification of every individual object in an image. 

차이점 : Unlike semantic segmentation, it provides information about the position, semantics, shape and count of individual objects, and therefore has many applications in autonomous driving.

### 6.2. Label Propagation
        
### 6.3. Semantic Segmentation with Multiple Frames

### 6.4. Semantic Segmentation of 3D Data

#### A. Online Methods

#### B. 3D CNN

there exists relatively little work on `labeling 3D data` using convolutional networks.

##### 가. Point cloud labeling

Huang & You (2016) propose a framework for labeling3D point cloud data using a 3D Convolutional Neural Network(3D-CNN). 

Specifically, they compute 3D occupancy grids of size 203 centered at a set of randomly generated key points. 

The occupancy and the labels form the input to a 3D CNN, which is composed of convolutional layers, max-pooling layers, a fully connected layer and a logistic regression layer. 

Due to the dense voxel representation, 3D CNNs are only able to process voxel grids of very coarse resolution considering the memory limitations of modern GPUs. 

```
Huang, J., & You, S. (2016). Point cloud labeling using 3d convolutional neural network. In Proc. of the International Conf. on Pattern Recognition (ICPR)
```

##### 나. OctNets

To alleviate this problem, Riegler et al. (2017) propose OctNets,a 3D convolutional network, that allows for training deep architectures at significantly higher resolutions. 

They build onthe observation that 3D data (e.g., point clouds, meshes) is oftensparse in nature. 

The proposed OctNet exploits this sparsity property by hierarchically partitioning the 3D space into aset of octrees and applying pooling in a data-adaptive fashion.

This leads to a reduction in computational and memory requirements as the convolutional network operations are defined on the structure of these trees and thus can dynamically allocate resources depending on the structure of the input.

```
Riegler, G., Ulusoy, A. O., & Geiger, A. (2017). Octnet: Learning deep 3d representations at high resolutions. In Proc. IEEE Conf. on Computer Vision and Pattern Recognition (CVPR).
``


### 6.5. Semantic Segmentation of Street Side Views

### 6.6. Semantic Segmentation of Aerial Images

### 6.7. Road Segmentation


## 7. Reconstruction

### 7.1. Stereo

### 7.2. Multi-view 3D Reconstruction

Goal :  to model the underlying 3D geometry by inverting the image formation process often under certain prior or smoothness assumptions. 

In contrast to two-view stereo, 
- multi-view reconstruction algorithms in particular address the problems of varying viewpoints and the complete reconstruction of 3D scenes from more than two and potentially a very large number of images. 

If the camera parameters are known, solving for the 3D geometry of the scene is equivalent to solving the correspondence problem, based on a photo-consistency function which measures the agreement between different viewpoints.


#### A. 분류(Taxonomies)

Several categorizations of **multi-view reconstruction algorithms** have been proposed in the literature, typically considering the form of the photo-consistency function, the scene representation, visibility computation, priors, and initialization requirements as in Seitz et al. (2006). 

From an application perspective, the scene representation is a common way of classifying multi-view reconstruction approaches into 
- depth map
- point cloud
- volumetric
- mesh

###### Depth map

The depth map representation typically consists of 
- a depth map for each input view estimated 
- with a 3D modeling pipeline which starts with image matching followed by pose estimation and dense stereo. 

This representationis usually preferred in scene analysis due to its flexibility and scalability to large scenes. 

```
- Plane Sweeping Stereo algorithm(Collins (1996)) : 
    - It sweeps a family of parallel planes in a scene, projects images onto a plane via planar homographies, then evaluates photo-consistency values on each plane. 

In largescenes, one of the challenges is to handle massive amount ofdata in real-time. 

- Pollefeys (2008) propose a large scale, realtime3D reconstruction system based on depth map representation.
    - The real-time performance is achieved by incorporating a set of components which are particularly efficient on typical urban scenes such as a 2D feature tracker with automatic gain adaptation for handling large dynamic range in natural scenes, and parallel implementations of plane sweeping stereo and depth map fusion on GPU.
```

###### Point cloud

In contrast to a partial depthmap for each view, point-cloud or patch based surface representations reconstruct a single 3D point-cloud model using all the input images. 

Under spatial consistency assumptions, the pointcloudon the surface of the scene can grow or expand whichprovides easy model manipulation such as merging and splitting.

```
- Patch-based Multi-View Stereo (PMVS) by Furukawa & Ponce(2010). 

PMVS starts with a feature matching step to generate a sparse set of patches and then iterate between a greedy expansion step and a filtering step to make patches dense and remove erroneous matches.
```

###### Volumetric

Volumetric approaches represent geometry on a regularly `sampled 3D grid`, i.e. volume, 
- either as a discrete occupancy function (Kutulakos & Seitz (2000)) 
- or a function encoding distance to the closest surface (level-set)(Faugeras & Keriven (1998)). 

More recent approaches use aprobability map defined at regular voxel locations to encodethe probability of occupancy (Bhotika et al. (2002); Pollard &Mundy (2007); Ulusoy et al. (2015)). 

The amount of memory required is the main limitation for volumetric approaches.

There is a variety of methods for dealing with this problem such as 
- voxel hashing (Nießner et al. (2013)) 
- a data adaptive discretization of the space in the form of a Delaunay triangulation(Labatut et al. (2007)). 

One effective solution is an octree data structure which is essentially an adaptive voxel grid to allocate high resolution cells only near the surfaces.



###### Mesh or Surface

typically triangular mesh-based surfaces. 

Volumetric surface extraction fuses 3D information from an intermediate representation such as
- depth maps
- point clouds
- volumesor scans into a single, clean mesh model. 


Seminal workby Curless & Levoy (1996) proposes an algorithm to accumulate surface evidence into a voxel grid using signed distance functions. 

The surface is implicitly represented as the zero crossing of the aggregated signed distance functions. 

It can be extracted using the Marching Cube algorithm Lorensen & Cline (1987) or using volumetric graph cuts to label each voxel as interior or exterior. 

There are approaches which directly start from images and refine a mesh model using an energy function composed of a data term based on photo-consistency function and a regularization term for smoothness. 

In these approaches,the energy is usually optimized using gradient descent, where the movement of each vertex is determined by the gradient of the objective function.




#### B. Urban Reconstruction

![](https://i.imgur.com/w9kiBsn.png)

In this survey, we focus on multiview reconstruction from an autonomous driving perspective which mainly concerns the reconstruction of large urban areas, up to whole cities. 

The goal : to produce fully automatic, high-quality, dense reconstructions of urban areas by addressing inherent challenges such as 
- lighting conditions
- occlusions
- appearance changes
- high-resolution inputs
- large scale outputs. 

###### survey 논문 : urban reconstruction 

Musialski et al.(2013) provide a survey of urban reconstruction approaches by following an output-based ordering, namely buildings and semantics, facades and images, and finally blocks and cities.

### 7.3. Reconstruction and Recognition

In autonomous driving, it is important to understand both the structural and semantic information of the surroundings.

Traditionally, `image segmentation` methods employ priors entirely in the 2D image domain, i.e., spatial smoothness terms,and reconstruction methods usually encourage piecewise smooth surfaces. 

It has been long argued that semantics and 3D reconstruction carry valuable information to each other. 

Similarly to stereo, the motivation to incorporate semantics in reconstruction is photo-consistency failing in case of imperfect and ambiguous image information due to specularities, lack of texture,repetitive structures, or strong lighting changes. 

Semantic labels provide geometric cues about likely surface orientations at a certain location and help resolving inherent ambiguities.

3D reconstruction lifts the reasoning from 2D to 3D and acts as a strong regularizer by enforcing geometric consistency over multiple images for segmentation.



## 8. Motion & Pose Estimation

## 9. Tracking

## 10. Scene Understanding

## 11. End-to-End Learning of Sensorimotor Control

Current state-of-the-art approaches to autonomous driving are comprised of numerous models, 
- detection (of traffic signs, lights, cars, pedestrians), 
- segmentation (of lanes, facades),
- motion estimation, 
- tracking of traffic participants, 
- reconstruction

The results from these components are then combined in a `rule based` control system.

최근 동향 ......

## 12. Conclusion