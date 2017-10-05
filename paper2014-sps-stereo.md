| 논문명 | Efficient Joint Segmentation, Occlusion Labeling,Stereo and Flow Estimation |
| --- | --- |
| 저자\(소속\) | Koichiro Yamaguchi (토요타)   |
| 학회/년도 | ECCV 2014,  [논문](https://arxiv.org/abs/1608.07711) |
| 키워드 |KITTI (stereo and Optical Flow Evaluation)
benchmarks |
| 참고 | [홈페이지](http://ttic.uchicago.edu/~dmcallester/SPS/index.html), [Youtube](https://www.youtube.com/watch?v=EcrHKd1w8t8)|
| 코드 | [Download](https://github.com/vbodlloyd/StereoSegmentation) |

![](http://ttic.uchicago.edu/~dmcallester/SPS/results.png)


# SPS-Stereo

목표 : slanted plane model제안 
    - 기능 : image segmentation, a dense depth estimate, boundary labels (such as occlusion boundaries)
    - 활용 데이터 : static scene given two frames of a stereo pair captured from a moving vehicle

## 1 Introduction

Current leading techniques are **slanted plane methods**, 
- which assume that the 3D scene is piece-wise planar and the motion is rigid or piece-wise rigid [30, 31,26]. 
- 단점 : 시간이 많이 걸린다. -> 자율 주행차에 맞지 않음 

본 논문 제안 : we propose a fast and accurate **slanted plane algorithm** that **operates on three images**
- a stereo pair 
- an image from the left stereo camera at a later point in time. 

가정 사항 : Our approach exploit the fact that in autonomous driving scenarios most of 
- the scene is static and 
- utilizes the stereo and video pairs to produce a joint estimate of depth, an image segmentation as well as boundary labels in the reference image. 

성능 평가 : faster than existing slanted plane methods [30, 31, 26]

```
30. Yamaguchi, K., Hazan, T., McAllester, D., Urtasun, R.: Continuous markov random fields for robust stereo estimation. In: ECCV (2012)
31. Yamaguchi, K., McAllester, D., Urtasun, R.: Robust monocular epipolar flow estimation. In: CVPR (2013)
26. Vogel, C., Roth, S., Schindler, K.: Piecewise rigid scene flow. In: ICCV (2013)
```


### 1.1 동작 과정 

1. semi global block matching (SGM)을 이용하여 semi-dense depth map생성 `Following [30, 31], our algorithm first uses SGM[13] to construct a semi-dense depth map on the reference image. `
    - A contribution here is the development of an SGM algorithm based on the joint evidence of the stereo and video pairs. 

2. 생성된 Semi-dense Depth map을 our slanted plane method의 입력으로 사용 하여 **segmentation**, **planes and boundary labels** inference 수행 `The semi-dense SGM depth map is then used as input to our slanted plane method for inferring the segmentation, planes and boundary` labels.

### 1.2 new inference algorithm (??)

Our new inference algorithm is a form of block-coordinate descent on a total energy involving the segmentation, the planes assigned to the segments, an “outlier-flag” at each pixel, and a line label assigned to each pair of neighboring segments giving the occlusion-status of the boundary between those segments.

In particular, each slanted plane can be optimized by a closed-form least-squares fit holding the segmentation, outlier-flags, and line-labels fixed. 

The line label scan be optimized holding the segments, planes and outlier flags fixed. 

The segmentation and the outlier flags are optimized jointly. 

The segmentation objective is an extension of the SLIC energy to handle both color and depth as well as a shape prior regularizing the length of the boundary. 

Importantly, our segmentation optimization subroutine uses unit-time single pixel moves restricted to the boundaries of segments, preserving the invariant that each segment is simply connected (connected and without holes).

Our **block-coordinate descent algorithm** is guaranteed to converge as the optimization over each set of variables (including the segmentation) is guaranteed to reduce the total energy. 

Importantly, this objective can be optimized over all unknowns on a single core in as little as 3s, while achieving state-of-the art
results. 

As a by product, when ignoring the depth energy term, our topology preserving segmentation subroutine can be used to create superpixels from single images

## 2. Related Work


Recovering depth (from a stereo and a video pair with a common reference image) is a special case of the more general **structure from motion problem**, where scene geometry is recovered from multiple images taken from different camera angles.

There is a very large literature on **structure from motion**, for example see [23,7, 10, 21]. 

Here, we are interested in a particular **three-image setting**. 

The three image case has been studied from the perspective of the **tri-focal tensor** — a generalization of the fundamental matrix to three images [11]. 

In our setting we are given the calibration between the two images of the stereo pair and for this reason we chose to work with the single fundamental matrix defined by thee go-motion underlying the video pair.

Although we assume a static scene, it is useful to review work on scenes with moving objects such as pedestrians and cars. 

The widely cited Tomasi-Kanade matrix factorization method for structure from motion [23] has been generalized to the case of scenes containing moving objects [6]. 

This algorithm groups points (correspondences) into rigid objects and assigns both a position in space and a six dimensional motion to each rigid object. 

However, it assumes that correspondences are given and the cameras are projective.

### 2.2 scene flow

The term “scene flow” was introduced in [24] for the problem of **assigning both positions and motions to a dense set of points** on the surface of objects in the scene. 

While an object has a six dimentional motion, a point does not rotate and thus only three degrees of freedom are necessary (a flow). 

Several papershave tackled the problem of estimating the 3D flow-field [28, 17, 14, 2]. 

To date, good performance has not yet been shown in challenging real-world scenarios. 

#### A. Vogel et. al.

Vogel et. al. [26] handles scenes with moving objects using a segmentation of a reference image with both a planar surface and a six dimensional rigid motion associated with each image segment. 

They incorporate the rigid-sceneassumption using a soft bias, while it is a hard constraint in our approach. 

Both systems do inference by minimizing an energy defined on planes associated with segments, however, our method is an order of magnitude faster and achieves greater accuracy on the KITTI benchmark for both stereo and flow.

Our approach is also related to the stereo and motion-stereo algorithms of Yamaguchi et. al. [30, 31]. 


### 2.3 동작과정 
As in [31], our approach first computes a semi-dense SGM depth map which then undergoes slanted-plane smoothing. 

The difference is that our SGM depth map is derived by joint inference from a stereo and a video pair and that our slanted-plane algorithm is roughly three orders of magnitude faster. 

동작 시간 
- 25 seconds computing SGM fields
- 10seconds on the slanted plane smoothing. 

Slanted plane models for stereo have a long history going back at least to [3]. 

They have proved quite successful on the Middle burry [20, 15, 4, 27] and KITTI [30] stereo benchmarks.

### 2.4 topology-preserving segmentation algorithm

The topology-preserving segmentation algorithm proposed here is related to SLIC superpixels [1]. 

However, our segmentation algorithm preserves the invariantthat segments remain simply connected. 

This eliminates the need for the post-processing step in the SLIC algorithm to simplify segments. 

This is important as this post-processing step can result in large increases of the total energy.

Furthermore, this speeds-up inference, as only boundary pixels are considered at each iteration. 

Our segmentation method also incorporates a length of boundaryenergy for shape regularization, as well as the evidence from the stereo and videopairs, which SLIC does not.