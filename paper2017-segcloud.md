|논문명 | SEGCloud: Semantic Segmentation of 3D Point Clouds |
| --- | --- |
| 저자\(소속\) | Lyne P. Tchapmi\(스탠포\) |
| 학회/년도 | arXiv Oct 2017 , [논문](https://arxiv.org/abs/1710.07563) |
| 키워드 | 공간인지 |
| 데이터셋(센서)/모델 |실내(NYU V2, S3DIS), 실외(**KITTI**, Semantic3D.net) |
| 관련연구||
| 참고 |[홈페이지](http://segcloud.stanford.edu/) |
| 코드 | |


# SEGCloud: Semantic Segmentation of 3D Point Clouds


- We present SEGCloud, 
    - an end-to-end framework to obtain 3D point-level segmentation 
    - that combines the advantages of **NNs**, **trilinear interpolation(TI)** and **fully connected Conditional Random Fields (FC-CRF)**
    
    
- Coarse voxel predictions from a **3D Fully Convolutional NN** are transferred back to the raw 3D points via **trilinear interpolation**. 

- Then the **FC-CRF** enforces global consistency and provides fine-grained semantics on the points. 

- We implement the latter as a **differentiable Recurrent NN** to allow joint optimization. 

## 1. Introduction


- 시멘틱 세그멘테이션은 그래픽모델의 설명력`(representational power)`을 활용하여 많이 연구 되었다. 
    - Semantic segmentation of **3D point sets** or** point clouds** has been addressed through a variety of methods leveraging the **representational power of graphical models** [36,44, 3, 48, 30, 35]. 

- 일반적인 방법은 분류 단계와 CRF를 합쳐서 라벨링 하는 것이다. 
    - A common paradigm is to combine a **classifier stage** and a **Conditional Random Field(CRF)** [39] to predict spatially consistent labels for each data point [68, 69, 45, 66, 69]. 
    - 랜덤 포레스트 분류기가 이러한 작업에 좋은 성능을 나타낸다.하지만, 랜덤 포레스트 분류기와 CRF사이에 정보(최적화) 교류에 제한이 있따. `Random Forests classifiers [7, 15] have shown great performance on this task, however the Random Forests classifier and CRF stage are often optimized independently and put together as separate modules, which limits the information flow between them.`
    
    
- 3D-FCNN은 좋은 후보 알고리즘 이다. `3D Fully Convolutional Neural Networks (3D-FCNN) [42] are a strong candidate for the classifier stage in 3D Point Cloud Segmentation. `

- 하지만 다음 제약들이 있다. 
    - However, since they require a **regular grid as input**, their predictions are limited to a coarse output at the voxel (grid unit) level.
    - The **final segmentation is coarse** since all 3D points within a voxel are assigned the same semantic label, making the voxel size a factor limiting the overall accuracy. 
    - To obtain a fine-grained segmentation from 3D-FCNN, an** additional processing **of the coarse 3D-FCNN output is needed. 

```
[42] J. Long, E. Shelhamer, and T. Darrell. Fully convolutional networks for semantic segmentation. Computer Vision and Pattern Recognition (CVPR), 2015.
```

### 1.1 본 논문에서는 

- 논문 특징 `We tackle this issue in our framework `
    - which is able to leverage the coarse output of a 3D-FCNN 
    - and still provide a fine-grained labeling of 3D points using trilinear interpolation (TI) and CRF.


- 다음 3가지 요소를 사용하여서 문제 해결을 하였다. `We propose an end-to-end framework that leverages the advantages of `
    - 3D-FCNN
    - trilinear interpolation [47]
    - and fully connected Conditional Random Fields(FC-CRF) [39,37] 
to obtain fine-grained 3D Segmentation. 

- 3요소를 좀더 자세히 살펴 보면. `In detail, `
    - the **3D-FCNN** provides class probabilities at the voxel level,
    - which are transferred back to the raw 3D points using **trilinear interpolation**. 
    - We then use a **FC-CRF** to infer 3D point labels while ensuring spatial consistency. 

- Transferring class probabilities to points before the CRF step, `allows the CRF to use point level modalities (color, intensity, etc.) to learn a fine-grained labeling over the points`, which can improve the initial coarse 3D-FCNN predictions. 
    - We use an efficient CRF implementation to perform the final inference. 

- Given that each stage of our pipeline is differentiable, we are able to train the framework end-to-end using standard stochastic gradient descent. 


- 본 논문의 기여도 The contributions of this work are:
    - We propose to combine the inference capabilities of Fully Convolutional Neural Networks with the fine-grained representation of 3D Point Clouds using TI and CRF.
    - We train the voxel-level 3D-FCNN and point-level CRF jointly and end-to-end by connecting them via Trilinear interpolation enabling segmentation in the original 3D points space.

- 본 논문의 방식은 다양한 입력을 받을수 있따. `Our framework can handle 3D point clouds from various sources (laser scanners, RGB-D sensors, etc.)`


## 2. Related Work

### 2.1 Neural Networks for 3D Data

- 3D Neural Networks have been extensively used for 3D object and parts recognition[60, 54, 46, 25, 53, 21], understanding object shape priors, as well as generating and reconstructing objects [73,71, 19, 70, 12]. 

- Recent works have started exploring the use of Neural Networks for 3D Semantic Segmentation[53, 16, 32]. 

###### [PointNetDeep]

- Qi et al. [53] propose a Multilayer Perceptron(MLP) architecture 
	-  that extracts a global feature vector from a 3D point cloud of $$1m^3$$ physical size 
	-  and processes each point using the extracted feature vector and additional **point level** transformations. 

- Their method operates at the point level and thus inherently provides a fine-grained segmentation. 

- It works well for indoor semantic scene understanding,although there is no evidence that it scales to larger input dimensions without additional training or adaptation required. 

```
[53] C. R. Qi, H. Su, K. Mo, and L. J. Guibas. Pointnet: Deep learning on point sets for 3d classificatio  and segmentation. CoRR, abs/1612.00593, 2016
```

###### [3D-FCNN]

- Huang et al. [32] present a 3D-FCNN for 3D **semantic segmentation** which produces coarse voxel level segmentation. 

```
[32] S. Y. J. Huang. Point Cloud Labeling using 3D Convolutional Neural Network. In International Conference on Pattern Recognition, pages 1–6, 2016 (공중+차량 포인트 클라우드)
```

###### [16]

- Dai et al. [16] also propose a fully convolutional architecture, 
	- 그러나, but they make a single prediction for all voxels in the same voxel grid column. 
	- This makes the wrong assumption that a voxel grid column contains 3D points with the same object label. 

```
[16] A. Dai, A. X. Chang, M. Savva, M. Halber, T. Funkhouser,and M. Nießner. Scannet: Richly-annotated 3d reconstructions of indoor scenes. arXiv preprint arXiv:1702.04405, 2017
```

###### [본 논문에서 제안 하는 법 ]

- 앞서 말한것들의 제약 `All the aforementioned methods are limited by the fact that `
	- they do not explicitly enforce **spatial consistency** between **neighboring points predictions** and/or **provide a coarse labeling** of the 3D data.

- 하지만 제안 방식은 In contrast, our method makes **fine-grained predictions** for each point in the 3D input, explicitly enforces spatial consistency and models class interactions through a CRF. 

Also,in contrast to [53], we readily scale to larger and arbitrarilysized inputs, since our classifier stage is fully convolutional.




### 2.2 Graphical Models for 3D Segmentation

- **Our framework** builds on top of a long line of works **combining** **graphical models**( [61, 62, 39, 20, 38]) and **highly engineered classifiers**. 

- **Early works** on 3D Semantic Segmentation formulate the problem as a **graphical model** built on top of a set of features. 

- Such models have been used in several works to capture contextual relationships based on various features and cues such as appearance, shape, and geometry. 

- These models are shown to work well for this task [50, 49, 36, 58, 44, 3, 48].

- 최근 추세는 `A common paradigm in 3D semantic segmentation `
	- combines a **classifier stage** and a **Conditional Random Field** to impose smoothness and consistency [68, 69, 45, 66, 69].

- Random Forests [7, 15] are a popular choice of classifier in this paradigm and in 3D Segmentation in general[75, 17, 9, 8, 51, 67]; they use hand-crafted features to robustly provide class scores for voxels, over segmentsor 3D Points. 

- In [45], the spin image descriptor is used as a feature, while [68] uses a 14-dimensional feature vector based on geometry and appearance. 

- Hackel et al. [27] also define a custom set of features aimed at capturing geometry,appearance and location. 

- In these works, the RandomForests output is used as unary potentials (class scores) for a CRF whose parameters are learned independently. 

- The CRF then leverages the confidence provided by the classifier, as well as similarity between an additional set of features,to perform the final inference. 

###### [본 논문에서 제안 하는것] 

- In contrast to these methods, our framework uses a **3D-FCNN** which can learn **higher dimensional features** and provide strong **unaries** for each data point. 

- Moreover, our CRF is implemented as a fully differentiable Recurrent Neural Network, similar to[76]. 

- This allows the 3D-FCNN and CRF to be trained end-to-end,and enables information flow from the CRF to the CNN classification stage.


### 2.3 Joint CNN + CRF

- 3D CNN과 3D CRF를 합치는 연구는 이전에는 Medical 데이터에서 상처 부분을 세그멘테이션 할때 사용 되었다. `Combining 3D CNN and 3D CRF has been previously proposed for the task of lesion segmentation in 3D medical scans. `

###### [34]

- Kamnitsas et al. [34] propose a multi-scale 3D CNN with a CRF to classify 4 types of lesions from healthy brain tissues. 

- The method consists of two modules that are not trained end-to-end: 
	- a 2-stream architecture operating at 2 different scan resolutions 
	- and a CRF. 

- In the CRF training stage, the authors reduce the problem to a 2-class segmentation task in order to find parameters for the CRF that can improve segmentation accuracy.

###### [76]

- Joint end-to-end training of CNN and CRF was first demonstrated by [76] in the context of image semantic segmentation,where the CRF is implemented as a differentiableRecurrent Neural Network (RNN). 

The combinationof CNN and CRF trained in an end-to-end fashion demonstratedstate-of-the-art accuracy for semantic segmentationin images. 

In [76] and other related works [42, 10], theCNN has a final upsampling layer with learned weightswhich allows to obtain pixel level unaries before the CRFstage. 

Our work follows a similar thrust by defining theCRF as an RNN and using a trilinear interpolation layer totransfer the coarse output of the 3D-FCNN to individual 3Dpoints before the CRF stage. 

In contrast to [34], our frameworkis a single stream architecture which jointly optimizesthe 3D CNN and CRF, targets the domain of 3D Scene PointClouds, and is able to handle a large number of classes bothat the CNN and CRF stage. 

Unlike [76, 42, 10], we choose to use deterministic interpolation weights that take into accountthe metric distance between a 3D point and its neighboringvoxel centers (Section 3.2). 

Our approach reducesthe number of parameters to be learned, and we find it towork well in practice. 

We show that the combination ofjointly trained 3D-FCNN and CRF with TI consistently performsbetter than a stand alone 3D-FCNN.


## 3. SEGCloud Framework
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjA1MTA4OTE0M119
-->