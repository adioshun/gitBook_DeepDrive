| 논문명 | Pairwise Decomposition of Image Sequences for Active Multi-View Recognition |
| --- | --- |
| 저자\(소속\) | Edward Johns (Imperial College London, UK) |
| 학회/년도 | May 2016, [논문](https://arxiv.org/abs/1605.08359) |
| 키워드 |  |
| 데이터셋(센서)/모델 | ModelNet |
| 참고 |[CVPR2016](https://www.youtube.com/watch?v=7Bw0HGlidtg)  |
| 코드 |  |


# Pairwise MVCNN

We propose to bring Convolutional Neural Networks to generic multi-view recognition, by 
- decomposing an image sequence into a set of image pairs, 
- classifying each pair independently, and 
- then learning an object classifier by weighting the contribution of each pair

제안 방식의 장점 : This allows for recognition over arbitrary(임의) camera trajectories(궤도), without requiring explicit training over the potentially infinite number of camera paths and lengths. 

Building these pairwise relationships then naturally extends to the **next-best-view problem** in an active recognition framework. 
- To achieve this, we train a second Convolutional Neural Network to map directly from an observed image to next viewpoint.

Finally, we incorporate this into a trajectory optimisation task, whereby the best recognition confidence is sought for
a given trajectory length.

## 1. Introduction

![](https://i.imgur.com/hsqKgpl.png)
```
[Figure 1]
- We propose a method for multi-view object recognition, by decomposing an image sequence into a set of image pairs. 
- Training on these pairs then allows for recognition and trajectory planning, without the need to train directly over the infinite possible number of camera paths that may exist.
```

그림 1을 예로 볼때 카메라를 어느 위치에 두는게 가장 좋은 결과를 가져 올까? `Consider the scenario in Figure 1. What trajectory should the camera move around the object in order to achieve the highest recognition confidence in a given time?`
- 실생활에서는 multi-view image sequence에서 물체를 인식하는게 single-image에서 인식하는것보다 더 realistic setting이다. `For practical tasks, recognition from a multi-view image sequence is a more realistic setting than the single-image recognition tasks typically addressed in computer vision, and controlling a camera actively for efficient recognition has great significance in real-world applications, where time or power constraints become realities. `

학계에서는 3D 메쉬를 인조 회색 이미지`(synthetic greyscale images)`로 렌더링 하여 분류 하는게 좋은 성능을 보이는 것으로 알려져 있다. `It was subsequently shown that rendering these meshes as synthetic greyscale images, and classifying objects in a view-based manner with a CNN architecture acting over a fixed trajectory, achieved state of-the-art results for multi-view recognition [35].`

하지만 이 방식을 입력 이미지의 **fixed-length**가 필요 하기 때문에 일반적으로 사용하기는 어렵다. `However, extending this to generalised recognition over trajectories of arbitrary paths and lengths is not readily adopted by traditional CNN architectures, due to the need for fixed-length input data.`

>  **fixed-lengtht** ???

```
[35-MVCNN2015] H. Su, S. Maji, E. Kalogerakis, and E. G. Learned-Miller. Multi-view Convolutional Neural Networks for 3D Shape Recognition. In Proceedings of the International Conference on Computer Vision (ICCV), 2015.
```

### 1.1 CNNs for Generalised Multi-View Recognition

위 문제에 대한 간단한 해결책은 모든 뷰에서의 이미지를 합쳐서 입력으로 사용하는 것이다. 하지만 이경우 학습 시간이 길어 지고 무엇보다 모든 가능한 뷰를 고려 해야 하는것은 어렵다 `One solution to multi-view recognition with CNNs would be to simply concatenate all observed images into a single input to a network. However, this would require intractable training due to the large size of each input, but more importantly, due to the need to train over every possible path of all possible lengths, which is of potentially infinite scale. `

본 논문의 해결 방안 : **relaxing the joint model over images** + **decomposing an image sequence into a set of pairs** `We propose to address this by relaxing the joint model over images and decomposing an image sequence into a set of pairs, one for every pair of images across the sequence.`
- Given this decomposition, a CNN is then trained on a fixed length input consisting of the image pair, together with the relative pose between the associated viewpoints. 
- To achieve classification of the full sequence, an **ensemble framework is adopted**, with weighting to increase the contribution of those image pairs which cover a more informative set of poses.

이후 문제는 가장 좋은 예측 정확도를 가지기 위해 카메라가 이동해야 하는 지점 지정하는 문제를 목적으로 하는 active recognition으로 변하게 된다. `The problem then shifts to active recognition, with the aim of determining along which trajectory the camera should move, in order to achieve the best recognition accuracy in a given number of images. `
- 이러한 문제는 NBV라고 불리운다. `This is often presented as a Next-Best-View (NBV) prediction, where the mutual information is determined between the __class probability distribution__ and __each potential next view__. `
- 하지만 이를 위해서는 generative model을 학습을 필요로 한다. `However, this typically requires learning a generative model of the object and synthesising new views as an intermediate step. `

제안 방식에서는 NBV도 포함 하고 있다. `We propose to learn NBV prediction with a more powerful discriminative model, training a second CNN to map directly from an observed image to the rotation angle over which the camera should subsequently move.`

Finally, we extend our NBV prediction to a full trajectory-optimisation framework, where we consider all possible images that can acquired along a trajectory as contributions, rather than simply following a sequence of NBV images as is often employed. 

To achieve this, we train a third CNN in a similar manner to the above NBV CNN, but training for regression to a recognition confidence score for all possible next viewpoints, rather then classification for the overall best viewpoint. 

As the image sequence evolves, all un-visited viewpoints accumulate scores based on the newly-observed images, and the optimum trajectory is chosen as the one which maximises the summation of these scores.


### 1.2 Contributions

In this paper, we present three key technical contributions all based on powerful CNN learning:

1. Multi-view object recognition over arbitrary camera trajectories by training only on image pairs,
2. Discriminatively-trained Next-Best-View prediction directly from an input image to the next viewpoint, 
3. Trajectory optimisation by considering the impact of all observable images along the sequence.

All three contributions achieve state-of-the-art results in their respective benchmarks on the ModelNet dataset

## 2. Related Work

### 2.1 View-Based Multi-View Recognition

In its simplest form, the view-based approach aims to add viewpoint tolerance to a 2D image of an object, 
- such as with view point invariant local descriptors [27, 29] or deformation-tolerant global descriptors [6]. 

Given training images across multiple viewpoints, a more stable set of features can be found by tracking those which are shared across multiple views and clustering images accordingly [23], or by learning theirrelative 2D displacements as the viewpoint changes, bothwith hard constraints for rigid bodies [17, 18] and flexibleconstraints for deformable bodies [11, 10]. 

To add furtherfidelity to the true underlying object geometry, these 2D imageelements can also be embedded within an implicit 3Dmodel [36, 22, 28]. 

If multiple views are available at testing,images can be combined and treated as a single, larger image[31], an approach which can also be addressed in twostages, by processing the individual images first to reducethe search space [5].Recently, CNN architectures have been extended to allowfor recognition from image sequences using a singlenetwork, by max pooling across all viewpoints [35], or byunwrapping an object shape into a panorama and max poolingacross each row [33]. 

However, both these methods assumethat a fixed-length image sequence is provided duringboth training and testing, and hence are unsuitable for generalisedmulti-view recognition.


---

The next best view problem (NBV) seeks a single additional sensor placement in order to improve an existing scene reconstruction derived from the current imaging configuration. Depending on the context, NBV can be seen as an incremental approach to building a camera network, designing a sensing strategy for autonomous exploration or selecting an input image dataset for multiview reconstruction.

We propose a next best view (NBV) algorithm that determines each view to reconstruct an arbitrary object. 


The problem addressed in this paper is to plan the **next sensor's position**, called the ‘next best view'(NBV). The NBV is the best view for the reconstruction process from a set of candidate views.
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzk5MDg5MTIwXX0=
-->