|논문명 | Deep Feature Flow for Video Recognition|
| --- | --- |
| 저자\(소속\) | Xizhou Zhu\(MS\) |
| 학회/년도 | arXiv Nov 2016 ~ [Jun 2017](https://arxiv.org/abs/1611.07715), CVPR 2017 |
| 키워드 | |
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


- In this work, we present deep feature flow, a fast and accurate approach for video recognition. 

- It applies an image recognition network on sparse key frames. 

- It propagates the deep feature maps from key frames to other frames via a flow field. 

As exemplifed in Figure 1, two intermediatefeature maps are responsive to “car” and “person” concepts.They are similar on two nearby frames. 

After propagation,the propagated features are similar to the original features.Typically, the flow estimation and feature propagationare much faster than the computation of convolutional features.Thus, the computational bottleneck is avoided andsignificant speedup is achieved. 

When the flow field is alsoestimated by a network, the entire architecture is trainedend-to-end, with both image recognition and flow networksoptimized for the recognition task. 

The recognition accuracyis significantly boosted.In sum, deep feature flow is a fast, accurate, general,and end-to-end framework for video recognition. 

It canadopt most state-of-the-art image recognition networks inthe video domain. 

Up to our knowledge, it is the firstwork to jointly train flow and video recognition tasks ina deep learning framework. 

Extensive experiments verifyits effectiveness on video object detection and semanticsegmentation tasks, on recent large-scale video datasets.Compared to per-frame evaluation, our approach achievesunprecedented speed (up to 10× faster, real time framerate) with moderate accuracy loss (a few percent). 

The high performance facilitates video recognition tasks inpractice.