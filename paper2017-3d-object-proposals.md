|논문명|3D Object Proposals for Accurate Object Class Detection
|-|-|
|저자(소속)|Xiaozhi Chen|
|학회/년도|TPAMI 2017,  [논문](https://arxiv.org/abs/1608.07711)|
|키워드| MV3D 저자,  |
|참고|[홈페이지](http://www.cs.toronto.edu/objprop3d/), [보충자료](http://www.cs.toronto.edu/objprop3d/3DOP_journal_suppl.pdf), [이전버젼(2015)](http://www.cs.toronto.edu/objprop3d/3dopNIPS15.pdf) |
|코드|[Download](http://www.cs.toronto.edu/objprop3d/downloads.php)|

# 3DOP

목표 : generating a set of 3D object proposals by exploiting stereo imagery

방법 : We formulate the problem as `minimizing an energy function` that encodes 
- object size priors
- placement of objects on the ground plane
- several depth informed features that reason about free space, point cloud densities and distance to the ground

Fusion하면 성능이 더 좋음 : Furthermore, we experiment also with the setting where `LIDAR information is available`, and show that using both LIDAR and stereo leads to the best result.

## 1. INTRODUCTION


물체 탐지 분야에서 CNN기반 `후보영역`방법을 이용하는 것[4-RCNN][5]은 `Sliding Window[3]`방식 보다 20%성능이 좋다. 

```
[3] P. F. Felzenszwalb, R. B. Girshick, D. McAllester, and D. Ramanan,“Object detection with discriminatively trained part based models,”PAMI, 2010.
[5] Y. Zhu, R. Urtasun, R. Salakhutdinov, and S. Fidler, “SegDeepM:Exploiting segmentation and context in deep neural networks for object detection,” in CVPR, 2015.
```

KITTI Dataset은 작고, 가려지거나(occluded), 잘린(truncated)부분이 많다. 따라서 PASCAL VOC에서 좋은 성능을 보인것도 그대로 사용하면 성능이 않좋다. 


In this paper, we propose a novel 3D object detection approach that exploits `stereo imagery` and `contextual information` specific to the domain of autonomous driving

## 1.1 연구 순서 

1. `We propose a 3D object proposal method that goes beyond 2D bounding boxes and is capable of generating highquality 3D bounding box proposals. `

2. We make use of the 3D information estimated from a stereo camera pair by placing 3D candidate boxes on the ground plane 

3. scoring them via 3D point cloud features. 

> 최종 결과를 3D point cloud값과 비교 

In particular, our `scoring function` encodes several depth informed features such as
- point densities inside a candidate box, 
- free space, 
- visibility
- object size priors
- height above the ground plane

학습절차는 Learning can be done using `structured SVM` [17] to obtain class-specific weights for these features. 

탐지 네트워크는 입력으로 3D 후보를 받아, 출력으로 3D BBox를 출력 한다. 
We also present a `3D object detection neural network` that takes 3D object proposals as input and predict accurate 3D bounding boxes. 

제안 네트워크는 최종적으로  The neural net exploits `contextual information` and uses a `multi-task loss` to jointly regress to bounding box coordinates and object orientation.

성능 : In particular, compared with the state-of-the-art RGB-D method MCG-D [18], we obtain 25% higher recall with 2K proposals

```
[17] T. Joachims, T. Finley, and C.-N. J. Yu, “Cutting-plane training of
structural svms,” JLMR, 2009.
[18] S. Gupta, R. Girshick, P. Arbelaez, and J. Malik, “Learning rich features from RGB-D images for object detection and segmentation,” in ECCV, 2014.
```
### 1.2 이전 연구 대비 추가된 부분 

A preliminary version of this work was presented in [19]. In this manuscript, we make extensions in the following aspects: 
- 1) A more detailed description of the inference process of proposal generation. 

- 2) The 3D object proposal model is extended with a class-independent variant. 

- 3) The detection neural network is extended to a two-stream network to leverage both appearance and depth features.

- 4) We further apply our model to point clouds obtained via LIDAR, and provide comparison of the stereo, LIDAR and the hybrid settings. 

- 5) We extensively evaluate the 3D bounding box recall and 3D object detection performance.

- 6) Our manuscript includes ablation studies of network design, depth features, as well as ground plane estimation.

```
[19] X. Chen, K. Kundu, Y. Zhu, A. Berneshawi, H. Ma, S. Fidler, and R. Urtasun, “3d object proposals for accurate object class detection,” in NIPS, 2015.
```

## 2. RELATED WORK


### 2.1 Object Proposal Generation.

#### A. RGB [7], [8], [10], [11], [13], [20]

In RGB, one typical paradigm is to generate candidatesegments by grouping superpixels or multiple figuregroundsegmentations with diverse seeds. 

Grouping-basedmethods [7], [8], [26] build on multiple oversegmentationsand merge superpixels based on complementary cues suchas color, texture and shape. 

Geodesic proposals [27] learnto place diverse seeds and identify promising regions bycomputing geodesic distance transforms. 

CPMC [20] solvesa sequence of binary parametric min-cut problems withdifferent seeds and unary terms. 

The resulting regions arethen ranked using Gestalt-like features and diversified usingmaximum marginal relevance measures. 

This approach is widely used in recognition tasks [5], [28], [29]. 

Somerecent approaches also follow this pipeline by learningan ensemble of local and global CRFs [12] or minimizingparametric energies that encode mid-level cues such assymmetry and closure [13]. 

Another paradigm generatesbounding box proposals by scoring exhaustively sampledwindows. 

In [9], a large pool of windows are scored with adiverse set of features such as color contrast, edges, locationand size. 

BING [10] scores windows using simple gradientfeatures which serve as an object closure measure and canbe computed extremely fast. 

BING++ [30] further improvesits localization quality using edge and superpixel based boxrefinement [31]. 

EdgeBoxes [11] design an effective scoringfunction by computing the number of contours that exist inor straddle the bounding box. 

[14] computes integral imagefeatures from inverse cascading layers of CNN for candidatebox scoring and refinement. 

A detailed comparison of existingproposal methods has been carried out in [32]. 

Whilemost of these approaches achieve more than 90% recall with2K proposals on the PASCAL VOC benchmark [6], theyhave significant lower recall on the KITTI dataset.

#### B. RGB-D [18], [21],[22], [23]

In RGB-D, [21], [22] extend CPMC [20] with depth cuesand fit 3D cubes around candidate regions to generatecuboid object proposals. 

[18] extends MCG [8] with RGB-Dcontours as well as depth features to generate 2.5D proposals.They obtain significantly better performance comparedwith purely RGB approaches. 

In [23], candidate objects areproposed from 3D meshes by oversegmentation and severalintrinsic shape measures. 

Our work is also relevant to SlidingShapes [33], which densely evaluates 3D windows withexemplar-SVM classifiers in 3D point clouds. 

However, theytrain exemplar classifiers on CAD models with hundredsof rendered views and complex shape features, resultingin very inefficient training and inference. 

In our work, weadvance over past work by exploiting the physical sizesof objects, the ground plane, as well as depth features andcontextual information in 3D.


#### C. video [24], [25]



### 2.2 3D Object Detection.


In the domain of autonomous driving, accurate 3D localization and pose estimation of objects beyond 2D boxes are desired. 

#### A. 3D DPM

In [34], the Deformable Part-based Model [3] is extended to 3D by adding viewpoint information and 3D part geometry. 

The potentials are parameterized in 3D object coordinates instead of the image plane. 

```
[34] B. Pepik, M. Stark, P. Gehler, and B. Schiele, “Multi-view and 3d deformable part models,” PAMI, 2015.
```

#### B. 

Zia et al. [35] initialize a set of candidate objects using a variant of poselets detectors and model part level occlusion and configuration with 3D deformable wireframes.

```
[35] M. Zia, M. Stark, and K. Schindler, “Towards scene understanding with detailed 3d object representations,” IJCV, 2015.
```

#### D. 

[36] trains an ensemble of subcategory models by clustering object instances with appearance and geometry features. 

```
[36] E. Ohn-Bar and M. M. Trivedi, “Learning to detect vehicles by clustering appearance patterns,” IEEE Transactions on Intelligent Transportation Systems, 2015.
```

#### E. 

In [37], a top-down bounding box re-localizationscheme is proposed to refine Selective Search proposalswith Regionlets features. 

```
[37] C. Long, X. Wang, G. Hua, M. Yang, and Y. Lin, “Accurate object detection with location relaxation and regionlets relocalization,” in ACCV, 2014. 
```


#### F. 

[38] combines cartographic map priors and DPM detectors into a holistic model to re-reasonobject locations. 

```
[38] S. Wang, S. Fidler, and R. Urtasun, “Holistic 3d scene understanding from a single geo-tagged image,” in CVPR, 2015.
```

#### G. 

[39] uses And-Or models to learn car-to car context and occlusion patterns.

```
[39] B. Li, T. Wu, and S. Zhu, “Integrating context and occlusion for car detection by hierarchical and-or model,” in ECCV, 2014.
```

#### H. 

[40] learns AdaBoost classifier with dense local features within subcategories. 

```
[40] Q. Hu, S. Paisitkriangkrai, C. Shen, A. van den Hengel, and F. Porikli, “Fast detection of multiple objects in traffic scenes with a common detection framework,” T-ITS, 2015.
```


#### I. 3DVP 

There cently proposed 3DVP [41] employs ACF detectors [42]and learns occlusion patterns with 3D voxels.

With the shift of low-level features to multi-layer visual representation, most of recent approaches exploit CNNs for object detection also in the context of autonomous driving.

```
[41] Y. Xiang, W. Choi, Y. Lin, and S. Savarese, “Data-driven 3d voxel patterns for object category recognition,” in CVPR, 2015.
[42] P. Dollar, R. Appel, S. Belongie, and P. Perona, “Fast feature pyramids for object detection,” PAMI, 2014.
```

#### J. 

In [43], R-CNN is applied on pedestrian detection with proposals generated by SquaresChnFtrs detector, achieving moderate performance. 

```
[43] J. Hosang, M. Omran, R. Benenson, and B. Schiele, “Taking a deeper look at pedestrians,” CVPR, 2015.
```

#### K. 

[44] learns part detectors with convolutionalfeatures to handle occlusion in pedestrian detection.

```
[44] Y. Tian, P. Luo, X. Wang, and X. Tang, “Deep learning strong parts for pedestrian detection,” in ICCV, 2015.
```


#### L.

[45] designs a complexity-aware cascade pedestriandetector with convolutional features. 

```
[45] Z. Cai, M. Saberian, and N. Vasconcelos, “Learning complexityaware cascades for deep pedestrian detection,” in ICCV, 2015.
```

#### M. Faster R-CNN 

Parallel to our work, Faster R-CNN improves upon their prior R-CNN pipeline by integrating proposal generation and R-CNN into an end-to-end trainable network. 

However, these methods only produce 2D detections, whereas our work aims at 3D object detection in order to infer both, accurate object pose as well as the distance from the ego-car.

