|논문명|Instant Object Detection in Lidar Point Clouds
|-|-|
|저자(소속)|Attila Börcs|
|학회/년도| IEEE Letter 2017, [논문](http://ieeexplore.ieee.org/document/7927715/)|
|키워드|4단계 Pipeline정의 |
|참고|[Dataset](http://web.eee.sztaki.hu/i4d/SZTAKI-Velo64Road-DB.html)|
|코드||



# Instant Object Detection in Lidar Point Clouds

## 1. INTRODUCTION

3D Object Perception 
- RMB
- MLS

### 1.1 RMB


rotating multibeam (RMB) Lidar system can largely support this process, since they can record accurate and high frame-rate point cloud sequences from large environment, with compact measurement size (64K points/frame) that makes possible online data transfer and processing

### 1.2 MLS
Object detection and recognition from dense mobile laser scanning (MLS) data has already a solid methodology background in the literature, using among others shape-based [3], pairwise 3-D shape context-based [4], or multiscale voxel-based approaches [5].

```
[3] B. Yang and Z. Dong, “A shape-based segmentation method for mobile laser scanning point clouds,” ISPRS J. Photogram. Remote Sens., vol. 81, pp. 19–30, Jul. 2013.
[4] Y. Yu, J. Li, J. Yu, H. Guan, and C. Wang, “Pairwise three-dimensional shape context for partial object matching and retrieval on mobile laser scanning data,” IEEE Geosci. Remote Sens. Lett., vol. 11, no. 5, pp. 1019–1023, May 2014.
[5] B. Yang, Z. Dong, G. Zhao, and W. Dai, “Hierarchical extraction of urban objects from mobile laser scanning data,” ISPRS J. Photogram. Remote Sens., vol. 99, pp. 45–57, Jan. 2015.
```


## 1.3 RMB Vs. MLS

Compared with `MLS-based` techniques, `RMB Lidar point cloud`s is highly challenging 

- due to the low and strongly inhomogeneous measurement density, which rapidly decreases as a function of the distance from the sensor [6]. 

- In addition, in cluttered scenes, the vehicles, pedestrians, trees, and further street objects often occlude each other causing partially extracted object blobs in the recorded measurement streams.

```
[6] J. Behley, V. Steinhage, and A. B. Cremers, “Performance of histogram descriptors for the classification of 3D laser range data in urban environments,” in Proc. IEEE Int. Conf. Robot. Autom. (ICRA), St. Paul,
```

## 1.4 기존 연구 (object recognition from RMB Lidar frames)

In [7-2012], an object detection technique is introduced, where the classification is based on a simple shape analysis of the bounding boxes. 

```
[7] A. Azim and O. Aycard, “Detection, classification and tracking of moving objects in a 3D environment,” in Proc. 4th IEEE Intell. Veh.Symp., Alcalá de Henares, Spain, Jun. 2012, pp. 802–807.
```

The method of [8-2008] uses a support vector machine classifier relying on a set of object level and point level features, implementing a binary vehicle/nonvehicle classification. A well-known public database is the KITTI [1], which is used by various methods [9] for quantitative evaluation. 

```
[8] M. Himmelsbach, A. Müller, T. Lüettel, and H.-J. Wuensche, “LIDARbased 3-D Object Perception,” in Proc. Int. Workshop Cognition for Tech. Syst., Munich, Germany, Oct. 2008, pp. 1–7.
``

Here, a limitation is that the ground truth annotation only concerns the field of view (FoV) of the forward looking cameras, which is only a segment of the 360° FoV of RMB Lidar scanners. 

If long object tracks can be extracted temporal information can be efficiently exploited in object recognition [10-2011], but in crowded situations, decision should be often made from a single time frame, immediately after a sudden appearance of an object. 

```
[10] A. Teichman, J. Levinson, and S. Thrun, “Towards 3D object recognition via classification of arbitrary object tracks,” in Proc. Int. Conf. Robot. Autom., May 2011, pp. 4033–4041.
```

Reference [11-2013] proposed a feature learning technique for urban object recognition, and published a reference database of 588 objects from 14 different categories. 

```
[11] M. De Deuge, A. Quadros, C. Hung, and B. Douillard, “Unsupervised feature learning for outdoor 3-D scans,” in Proc. Australasian Conf. Robot. Autom., 2013, pp. 1–9.
```

However, it remains there an open issue, how the quality of the object extraction step effects the classification results, and for some object classes, only a few test examples are provided. 

Voxel-based approaches allow to perform a detailed interpretation of the scene [9]; however, here, the computational requirements are proportional to the number of voxels and it is less straightforward to incorporate global contextual descriptors to a voxel-based local decision process.

```
[9] D. Z. Wang and I. Posner, “Voting for voting in online point cloud object detection,” in Proc. Robot., Sci. Syst., Rome, Italy, Jul. 2015, pp. 1–9.
```


## 2. WORKFLOW OF THE PROPOSED MODEL

목적 : Detect and localize all vehicles and pedestrians in the proximity of the mobile Lidar
platform, as shown in Fig. 1. 

###### [1단계] 4개의 영역으로 분류(지면, 낮은 물체, 높은 물체, 희미한 부분)
First, the input point cloud is segmented into four regions: ground, low foreground, high foreground, and sparse areas. 
- Low foreground is the estimated region of short street objects, such as cars, pedestrians, benches,mail boxes, billboards,
- high foreground covers tall objects, among others building walls, trees, traffic signs, and lamp posts. 
- Following the segmentation, ground and sparse areas are `removed`, as they are not used by the further processing steps. 

###### [2단계] 낮은/높은 물체를 연결된 blob으로 나눔
Second, both the low and high foreground regions are divided into connected blobs representing individual object candidates. 

###### [3단계] Classification 
Third, objects extracted from the low foreground region undergo an appearance-based classification, which provides evidences for discriminating vehicles and pedestrians from other street entities. 

In parallel, large facade segments—called as anchor facades—are detected within the high foreground’s object set. 

###### [4단계] 후처리 

Fourth, the classification result of the previous purely appearance-based step is refined with
contextual information, considering the relative positions of the various sorts of short objects and anchor facades.

### 2.1  Point Cloud Segmentation

### 2.2  Object Separation With Fast Connected Component Analysis

### 2.3 Appearance-Based Object Recognition

### 2.4 Contextual Labeling Refinement