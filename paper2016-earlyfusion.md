|논문명 | On-Board Object Detection: Multicue, Multimodal, and Multiview Random Forest of Local Experts|
| --- | --- |
| 저자\(소속\) | \(\) |
| 학회/년도 | IEEE Transactions on Cybernetics 2016, [논문](http://ieeexplore.ieee.org/document/7533479/) |
| 키워드 |EarlyFusopn |
| 데이터셋(센서)/모델 |KITTI |
| 참고 | |
| 코드 | |

# EarlyFusion 

여러 정보`(multicue, multimodality, and strong MV classifier)`들이 합쳐 졌을때 어떤 영향을 미치는지 살펴 보겠다 `we provide an extensive evaluation that gives insight into how each of these aspects (multicue, multimodality, and strong MV classifier) affect accuracy both individually and when integrated together`

사용 센서 :  fusion of RGB and depth maps(Lidar)

## 1. Introducion 

현실세계에서 Detector의 성능 향상을 위해서는 다음이 중요하다. `In order to obtain a detector that successfully operates under realistic conditions, it becomes critical to exploit sources of information along three orthogonal axis`
- 1) the integration of multiple feature cues (contours, texture, etc.); 
- 2) the fusion of multiple image modalities (color, depth, etc.); 
- 3) the use of multiple views (frontal, lateral, etc.) of the object 
by learning a strong classifier that accommodates for both different 3-D points of view and multiple flexible articulations.

![](https://i.imgur.com/Kqp3Cl6.png)
```
Fig. 1. General scheme: from RGB images and LIDAR data to object detection. 
- RGB images and LIDAR data synchronized for multimodal representation.
- Multimodal representation based on RGB images and dense depth maps (obtained from LIDAR sparse data). 
- Multicue feature extraction over the multimodal representation. 
- MV detection of different objects.
```

- 제안 방식은 그림1에서 보는 바와 같이 성능 평가 할것이다. `The proposed method (general scheme in Fig. 1) will be evaluated in key objects for autonomous and semi-autonomous vehicles such as pedestrians, cyclists, and cars.`

### 1.1 integrate different cues

- In order to integrate different cues we use 
	- **Histogram of oriented gradients (HOG)** [9], that provides a good description of the object contours 
	- **Local binary pattern (LBP)** [10] as texture-based feature. 

- [11]-[13]에 따르면 위 두 특징들은 **상호 보안적**인 요소로 **Fusion시** 좋은 효과가 난다. `These two types of features provide complementary information and the fusion of both types of features has been seen to boost the performance of either feature separately [11]–[13]. `

- [9]에 따르면 다른 종류의 **gradient-based features**와 그 **특징의 spatial distribution**을 쓰는것은 좋은 표현력을 가지게 된다. `From the seminal work of Dalal and Triggs [9], it has been seen that using different types of gradient-based features and their spatial distribution,such as in the HOG descriptor [9] provides a distinctive representation of both humans and other objects classes. `

- [14]의 연구에 따러면 제안한 **integral channel features**여러 종류의  low-level features들을 합치게 되면 spatial distribution에 대한 유연성 있는 representation 이 된다. `However, there exist in the literature other approaches such the integral channel features proposed by Dollár et al. [14] that allows integrating multiple kinds of low-level features (such as the gradient orientation over the intensity and LUV images, extracted from a large number of local windows of different sizes and at multiple positions), allowing for a flexible representation of the spatial distribution. `
	- low-level features  = gradient orientation over the intensity and LUV images, extracted from a large number of local windows of different sizes and at multiple positions

-  In [15] and [16], it has been seen that including color boosts the performance significantly, being this type of feature complementary to the ones we used in this paper. 

- **Context features**를 사용하는 방법도 제안 되었다. `Context features have also been seen to aid [17], [18]and could be easily integrated as well. `

- 지역특징`(local features)`에 대한 spatial pooling에 대한 대안들도 연구 되었다. `Exploring alternative types of spatial pooling of the local features is also beneficial as shown in [6] and is also complementary to the approach used in this paper.`

### 1.2 integrate multiple image modalities,

여러 이미지 모딜라티의 결합을 위해 본 논문에서는 **depth maps**과 **visible spectrum images**를 퓨젼 하였다. ` In order to integrate multiple image modalities, we considered the fusion of dense depth maps with visible spectrum images. `

The use of depth information has gained attention,thanks to the appearance of cheap sensors such as the one inKinect, which provides a dense depth map registered with anRGB image (RGB-D). 

However, the sensor of Kinect has amaximum range of approximately 4 m and is not very reliablein outdoor scenes, thus having limited applicability for objectsdetection in on-board sequences. 

On the other hand, lightdetection and ranging (LIDAR) sensors such as the VelodyneHDL-64E have a maximum range of up to 50 m and areappropriate for outdoor scenarios. 

In this paper, we explorethe fusion of dense depth maps (obtained based on the sparsecloud of points) with RGB images. 

Following [19], the informationprovided by each modality can be fused using eitheran early-fusion scheme, i.e., at the feature level, or a latefusionscheme, i.e., at the decision level. 

In this paper, usingan early fusion scheme, where descriptors from each modalityare concatenated, provided the best results.Object detection based on data coming from multiplemodalities has been a relatively active topic of study [1],and in particular the use of 2-D laser scanners and visiblespectrum images has been studied in several works, forinstance [20] and [21]. 

Only recently authors are starting tostudy the impact of high-definition 3-D LIDAR [20]–[26].Most of these works propose specific descriptors forextracting information directly from the 3-D cloud ofpoints [20], [22]–[26]. 

A common approach is to detect objectsindependently in the 3-D cloud of points and in the visiblespectrum images, and then combining the detections usingan appropriate strategy [22], [23], [26]. 

Following the stepsof [21], dense depth maps are obtained by first registering the3-D cloud of points captured by a Velodyne sensor with theRGB image captured with the camera, and then interpolatingthe resulting sparse set of pixels to obtain a dense map where each pixel has an associated depth value. 

Given this map, 2-Ddescriptors in the literature can be extracted in order to obtaina highly distinctive object representation. 

This paper differsfrom [21] in that we use multiple descriptors and adapt themto have a good performance in dense depth images. 

While [21]employs a late fusion scheme, in our experimental analysiswe evaluate both early and late fusion approaches in the givenmulticue and multimodality framework.Learning a model flexible enough for dealing with multipleviews and multiple positions of an articulated object is a hardtask for a holistic classifier. 

In order to fulfill this aspect wemake use of random forests (RFs) of local experts [27], whichhas a similar expressive power than the popular deformablepart models (DPMs) [28] and less computational complexity.In this method, each tree of the forest provides a differentconfiguration of local experts, where each local expert takesthe role of a part model. 

At learning time, each tree learnsone of the characteristic configurations of local patches, thusaccommodating for different flexible articulations occurring inthe training set. 

In [27], the RF approach consistently outperformedDPM. 

An advantage of the RF method is that only asingle descriptor needs to be extracted for the whole window,and each local expert reuses the part of the descriptor thatcorresponds to the spatial region assigned to it. 

Its computationalcost is further significantly reduced by applying a softcascade, operating in close to real time. 

Contrary to the DPM,the original RF method learns a single model, thus not consideringdifferent viewpoints separately. 

In this paper, we extendthis method to learn multiple models, one for each 3-D pose,and evaluate both the original single model approach and themultimodel approach. 

Several authors have proposed methodsfor combining local detectors [28], [29] and multiple localpatches [30]–[32]. 

The method in [33] also makes use of RFwith local classifiers at the node level, although it requiresto extract many complex region-based descriptors, making itcomputationally more demanding than [27].
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExMDMyMzA1ODFdfQ==
-->