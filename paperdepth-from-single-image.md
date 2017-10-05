
|논문명|Single image depth estimation by dilated deep residual convolutional neural network and soft-weight-sum inference|
|-|-|
|저자(소속)|Bo Li (Baidu)|
|학회/년도| Apr 2017, [논문](https://arxiv.org/abs/1705.00534)|
|키워드||
|참고||
|코드||





--- 
- [cs231n-Report] [Depth Estimation from Single Image Using CNN-Residual Network](http://cs231n.stanford.edu/reports/2017/pdfs/203.pdf), 2017
- David Eigen, Depth Map Prediction from a Single Image using a Multi-Scale Deep Network, NIPS 2014, [논문](https://www.cs.nyu.edu/~deigen/depth/depth_nips14.pdf), [Homepage](https://www.cs.nyu.edu/~deigen/depth/),  NYU Depth v2 ,KITTI 
- Andrew Y. Ng, 3-D Depth Reconstruction from a Single Still Image, IJCV 2007, [논문](http://www.cs.cornell.edu/~asaxena/reconstruction3d/saxena_iccv_3drr07_learning3d.pdf), [Homepage](http://www.cs.cornell.edu/~asaxena/learningdepth/) 
- Nidhi Chahal, Depth estimation from single image using machine learning techniques, ICVGIP 16 [논문](https://dl.acm.org/citation.cfm?id=3010019)



---

|논문명|Depth Estimation from Single Image Using CNN-Residual Network|
|-|-|
|저자(소속)|Xiaobai Ma (Standford)|
|학회/년도| cs231n-Report 2017, [논문](http://cs231n.stanford.edu/reports/2017/pdfs/203.pdf)|
|키워드||
|참고||
|코드||

# Depth Estimation from Single Image Using CNN-Residual Network

## 1. Introduction

## 2. Related work
### 2.1. Classic methods

Most works rely on 
- camera motion (Structure-from-Motion method [21])
- variation in illumination (Shape-from-Shading [34])
- variation in focus (Shapre-from-Defocus [31]).

기존 연구 문제점 
Classic methods rely on 
- strong assumptions about the scene geometry, 
- relied on hand-crafted features and 
- probabilistic graphical models which exploits horizontal alignment of images or other
geometric information.


#### A. Saxena et al
- Saxena et al. [26] predicted depth from a set of image features using linear regression and a MRF, 
    - and later extend their work into the Make3D system for 3D model generation [27].
    - However, the system relies on horizontal alignment of images, and suffers in less controlled settings. 

#### B. Liu et al
- Inspired by this work, Liu et al. [15] combine the task of semantic segmenta-tion with depth estimation, where predicted labels are used as additional constraints to facilitate the optimization task.

#### C. Ladicky et al
- Ladicky et al. [10] instead jointly predict labels and depths in a classification approach. Hoiem et al. 

#### D. 

[6] do not predict depth explicitly, but instead categorize image regions into geometric structures and then compose a simple 3D model of the scene.


### 2.2. Feature-based mapping methods

A second type of related works perform feature-based matching between a given RGB image and the images of a RGB-D repository in order to find the nearest neighbors, the retrieved depth counterparts are then warped and combined to produce the final depth map.

#### A. Karsch

Karsch et al. [7] perform warping using SIFT Flow [16], followed by a global optimization scheme, whereas Konrad et al. 

#### B. 

[8] compute a median over the retrieved depth maps followed by cross bilateral filtering for smoothing. 

#### C. Liu et al

Instead of warping the candidates, Liu et al. [19], formulate the optimization problem as a Conditional Random Field (CRF) with continuous and discrete variable potentials. 

Notably, these approaches rely on the assumption that similarities between regions in the RGB images imply also similar depth cues.


### 2.3. CNN based methods

최근 CNN기반 방법들이 제안 되었다. 이 작업있기 때문에 기존 이 **semantic labeling**와 깊은 연관이 AlexNet, VGG 같은 방법을 기반으로 연구 되었다. `Since the task is closely related to semantic labeling, most works have built upon the most successful architectures of the ImageNet Large Scale Visual Recognition Challenge (ILSVRC) [25], often initializing their networks with AlexNet [9] or the deeper VGG [30]. Eigen et al. `

#### A. 최초의 CNN기반 방법 논문 
[3]are the first to use CNN for single image depth estimation.

The authors addressed the task by employing two deep network stacks. 

- The first network makes a global coarse depthprediction for the whole image, 
- The second refines this prediction locally. 

#### B. 확장 버젼 

This idea is later extended in [2], where three stacks of CNN are used to additionally predict surface normals and labels together with depth. 

#### C. CNN + regression forests

Unlike the deeplearning structures used in [3, 2], Roy et al. [24] combined CNN with regression forests [14], using very shallow architectures at each tree node, thus limiting the need for big data.

#### D. CNNs and graphical models. 

Liu et al. [17] propose to learn the unary and pairwise potentials during CNN training in the form of a conditional random field (CRF) loss and achieved state of-the-art result without using geometric priors. 

This idea makes sense because the depth values are continuous [18].

#### E. CNNs and graphical models. 



Li et al. [13] and Wang et al. [32] use hierarchical CRFs to refine their patch-wise CNN predictions from superpixel down to pixel level.


