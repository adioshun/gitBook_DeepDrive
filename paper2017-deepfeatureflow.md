|논문명 | Deep Feature Flow for Video Recognition|
| --- | --- |
| 저자\(소속\) | Xizhou Zhu\(MS\) |
| 학회/년도 | arXiv Nov 2016 ~ [Jun 2017](https://arxiv.org/abs/1611.07715), CVPR 2017 |
| 키워드 |Xizhou2016DeepFeatureFlow  |
| 데이터셋(센서)/모델 | |
| 관련연구||
| 참고 |[Youtube](https://www.youtube.com/watch?v=J0rMHE6ehGw) |
| 코드 |[MXnet](https://github.com/msracver/Deep-Feature-Flow) |

# DeepFeatureFlow

- 아직은 이미지 인식 네트워크를 비디오에 적용할수 없다. 너무 느리고 컴퓨팅 부하가 크다. `Yet, it is nontrivial to transfer the state-of-the-art image recognition networks to videos as per-frame evaluation is too slow and unaffordable.`

- 비디오 인식을 위한 **deep feature flow**제안 `We present deep feature flow, a fast and accurate framework for video recognition. `

- 자원 소보가 큰 Conv.는 sparse key frames에서만 사용하고 `It runs the expensive convolutional sub-network only on sparse key frames `
    - 이후 flow field를 통해서 특징지도를 다음 frame에 전달 한다. `and propagates their deep feature maps to other frames via a flow field. `

- 속도 향상을 가져 왔다. `It achieves significant speedup as flow computationis relatively fast. `

- 인식 성능도 좋다. `The end-to-end training of the whole architecture significantly boosts the recognition accuracy. `

- Deep feature flow is flexible and general. 

## 1. Introduction

- CNN은 많은 2D 이미지 인식 분야에 적용 되고 좋은 성능을 보였다. `Recent years have witnessed significant success of deepconvolutional neutral networks (CNNs) for image recognition,e.g.,`
    - image classification [23, 40, 42, 16]
    - semantic segmentation [28, 4, 52]
    - object detection [13, 14, 12,35, 8, 27]

- 이후 동영상 쪽으로 확장 되었다. `With their success, the recognition tasks havebeen extended from image domain to video domain, `
    - semantic segmentation on Cityscapes dataset [6],
    - objectdetection on ImageNet VID dataset [37]. 

- 하지만, 이미지 인식용 알고리즘을 동영상에 적용하기에는 부하가 크다. `Nevertheless,applying existing image recognition networks on individual video frames introduces unaffordable computational cost for most applications.`

- 일반적으로 이미지 컨텐츠가 동영상이 되면 ....??It is widely recognized that image content varies slowly over video frames, especially the high level semantics [46,53, 21]. 
    - This observation has been used as means of regularization in feature learning, considering videos as unsupervised data sources [46, 21]. 

- 이러한 data redundancy와 연속성`(continuity)`특징을 이용하면 불필요한 연산 부하를 줄일수 있다. `Yet, such data redundancy and continuity can also be exploited to reduce the computation cost. `

- 하지만 CNN기반 비디오 인식 분야에 잘 고려 되지 않았다. `This aspect, however, has received little attention for video recognition using CNNs in the literature.`

- 모던 CNN들은 비슷한 구조를 가지고 있다. `Modern CNN architectures [40, 42, 16] share a common structure. `
    - 대부분 레이어는 Conv. 이다. `Most layers are convolutional and account for the most computation. `
    - The **intermediate convolutional feature maps** have the **same spatial extent** of the input image`(usually at a smaller resolution, e.g., 16× smaller)`.
    - They preserve the **spatial correspondences** between the low level image content and middle-to-high level semantic concepts[48]. 

- 이러한 **correspondences**를 이용하여 ,**Optical flow처럼**,큰 연산 부담 없이 특징 정보들을 다음 frame에 전달 할수 있다. `Such correspondence provides opportunities to cheaply propagate the features between nearby frames by spatial warping, similar to optical flow [17].`

### 1.1 본 논문에서는 

- In this work, we present** deep feature flow**, a fast and accurate approach for video recognition. 

- It applies an image recognition network on **sparse key frames**. 
    - It **propagates** the **deep feature maps** from key frames to other frames via a **flow field**. 

![](https://i.imgur.com/uPvmeJF.png)

```
[Figure 1. Motivation of proposed deep feature flow approach.]
- Here we visualize the two filters’ feature maps on the last convolutional layer of our ResNet-101 model (see Sec. 4 for details). 
- The convolutional feature maps are similar on two nearby frames. 
- They can be cheaply propagated from the key frame to current frame via a flow field.
```

- As exemplifed in Figure 1, two intermediate feature maps are responsive to “car” and “person” concepts.

- They are similar on two nearby frames. 

- After propagation,the propagated features are similar to the original features.

- 합성곱 연산 보다는 **flow estimation** 와 **feature propagation**이 훨씬 빠르다. `Typically, the **flow estimation** and **feature propagation** are much faster than the computation of convolutional features.`
    - 따라서 연산 보틀넥을 피하게 되어 속도 향상을 가져 온다. `Thus, the computational bottleneck is avoided and significant speedup is achieved. `

- flow field도 사용 할수 있다면 진정한 end-to-end로 학습된다.  `When the** flow field **is also estimated by a network, the entire architecture is trained **end-to-end**, `
    - with both image recognition and flow networks optimized for the recognition task. 

- Compared to per-frame evaluation, our approach achieves unprecedented speed (up to 10× faster, real time framerate) with moderate accuracy loss (a few percent). 

## 2. Related Work

- 처음 시도 되는것이라 관련 연구가 없다. 대신 관련 기술들을 살펴 보겠다. `To our best knowledge, our work is unique and there is no previous similar work to directly compare with. Nevertheless,
it is related to previous works in several aspects, as discussed below.`

### 2.1 Image Recognition

- Deep learning has been successfulon image recognition tasks. 

- The network architectures have evolved and become powerful on image classification[23, 40, 42, 15, 20, 16]. 
    
    - For object detection : the **region-based methods** [13, 14, 12, 35, 8] have become the dominant paradigm. 
    
    - For semantic segmentation : **fully convolutionalnetworks (FCNs)** [28, 4, 52] have dominated the field. 

- However, it is computationally unaffordable to directly apply such image recognition networks on all the frames for video recognition. 

### 2.2 Network Acceleration

- Various approaches have been proposed to** reduce the computation** of networks. 

- To name a few, in [50, 12] **matrix factorization** is applied to decompose large network layers into multiple small layers.

- In [7, 34, 18], network weights are **quantized**. 

- These techniques work on single images. 

- They are generic and complementary to our approach.

### 2.3 Optical Flow

- 비디오 분석의 근복적인 task이다. `It is a fundamental task in video analysis.`

- 수년간 다양한 접근 방법들이 연구 되었다. `The topic has been studied for decades and dominated by variational approaches [17-1981, 2-2004],`
    - 대부분  small displacements이다. `which mainly address small displacements [44-2006]. `

- 최근 추세는 **large displacements [3]** 와 **combinatorial matching**를 다양한 접근법과 통합 하는것이다 `The recent focus is on large displacements [3] and combinatorial matching (e.g., DeepFlow[45], EpicFlow [36]) has been integrated into the variational approach. `
    - 이런한 접근법은 모두 **hand-crafted**이다. `These approaches are all hand-crafted.`

```
[45] P. Weinzaepfel, J. Revaud, Z. Harchaoui, and C. Schmid. DeepFlow: Large displacement optical flow with deep matching. In CVPR, 2013. 2
[36] J. Revaud, P. Weinzaepfel, Z. Harchaoui, and C. Schmid. EpicFlow: Edge-Preserving Interpolation of Correspondences for Optical Flow. In CVPR, 2015
```

- 최근에는 딥러닝과 시멘틱 정보들이 optical flow에 이용 되었다. `Deep learning and semantic information have been exploited for optical flow recently. `

- FlowNet이 최초로 optical flow에 CNN적용해 모션 예측을 하였따. `FlowNet [9] firstly applies deep CNNs to directly estimate the motion and achieves good result. `
    - The **network** architecture is simplified in the recent **Pyramid Network** [33]. 

```
[9] A. Dosovitskiy, P. Fischer, E. Ilg, P. Hausser, C. Hazirbas, and V. Golkov. Flownet: Learning optical flow with convolutional networks. In ICCV, 2015.
```

- 다른연구는 **semantic segmentation**정보를 optical flow 예측에 활용 하는 것이다. `Other works attempt to exploit semantic segmentation information to help optical flow estimation[38, 1, 19],`
    -  e.g., providing specific constraints on the flow according to the category of the regions.

```
[38] L. Sevilla-Lara, D. Sun, V. Jampani, and M. J. Black. Optical flow with semantic segmentation and localized layers. In CVPR, 2016.
[1] M. Bai, W. Luo, K. Kundu, and R. Urtasun. Exploiting semantic information and deep matching for optical flow. In ECCV, 2016.
[19] J. Hur and S. Roth. Joint optical flow and temporally consistent semantic segmentation. In ECCV CVRSUAD Workshop, 2016.
```

- Optical flow를 활용한 분야 `Optical flow information has been exploited to help vision tasks, such as `
    - pose estimation [32], 
    - frame prediction[31], 
    - attribute transfer [49]. 

```
[32] T. Pfister, J. Charles, and A. Zisserman. Flowing convnets for human pose estimation in videos. In ICCV, 2015.
[31] V. Patraucean, A. Handa, and R. Cipolla. Spatio-temporal video autoencoder with differentiable memory. arXiv preprint arXiv:1511.06309, 2015.
[49] W. Zhang, P. Srinivasan, and J. Shi. Discriminative image warping with attribute flow. In CVPR, 2011.
```


- This work exploits optical flow to speed up general video recognition tasks.

### 2.4 Exploiting Temporal Information in Video Recognition

- T-CNN [22] incorporates temporal and contextual information from tubelets in videos. 

- The dense 3D CRF [24]proposes long-range spatial-temporal regularization in semantic video segmentation. 

- STFCN [10] considers a spatial-temporal FCN for semantic video segmentation.

- These works operate on volume data, show improved recognition accuracy but greatly increase the computational cost.

- By contrast, our approach seeks to reduce the computation by exploiting temporal coherence in the videos. 

- The network still runs on single frames and is fast.


### 2.5 Slow Feature Analysis 

- High level semantic concepts usually evolve slower than the low level image appearance in videos. 

- The deep features are thus expected to vary smoothly on consecutive video frames. 

- This observation has been used to regularize the feature learning in videos [46, 21, 53, 51, 41]. 

- We conjecture that our approach may also benefit from this fact.

### 2.6 Clockwork Convnets [39] 

- 본 논문과 가장 유사한 연구임 `It is the most related work to ours as`
    - it also disables certain layers in the network on certain video frames and reuses the previous features. 

- It is,however, much simpler and less effective than our approach.

- About speed up, Clockwork only saves the computation of some layers (e.g., 1/3 or 2/3) in some frames (e.g., everyother frame). 

- As seen later, our method saves that on most layers (task network has only 1 layer) in most frames (e.g.,9 out of 10 frames). 

- Thus, our speedup ratio is much higher.

- About accuracy, Clockwork does not exploit the correspondence between frames and simply copies features. 

- It only reschedules the computation of inference in an off the-shelf network and does not perform fine-tuning or retraining.

- Its accuracy drop is pretty noticeable at even small speed up. 

- In Table 4 and 6 of their arxiv paper, at 77% full runtime (thus 1.3 times faster), Mean IU drops from 31.1 to 26.4 on NYUD, from 70.0 to 64.0 on Youtube, from 65.9to 63.3 on Pascal, and from 65.9 to 64.4 on Cityscapes. 

- By contrast, we re-train a two-frame network with motion considered end-to-end. 

- The accuracy drop is small, e.g., from71.1 to 70.0 on Cityscape while being 3 times faster (Figure3, bottom).

- About generality, Clockwork is only applicable for semantic segmentation with FCN. 

- Our approach transfers general image recognition networks to the video domain.

## 3. Deep Feature Flow







