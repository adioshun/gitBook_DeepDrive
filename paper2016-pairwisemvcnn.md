| 논문명 | Pairwise Decomposition of Image Sequences for Active Multi-View Recognition |
| --- | --- |
| 저자\(소속\) | Edward Johns (Imperial College London, UK) |
| 학회/년도 | May 2016, [논문](https://arxiv.org/abs/1605.08359) |
| 키워드 | pMVCNN2016 |
| 데이터셋(센서)/모델 | ModelNet |
| 관련연구 | MV-CNN|
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

- View-Based Multi-View Recognition : MVCNN, DeepPano
- Shape-Based Multi-View Recognition : ShapeNet, VoxNet

> View-Based방식이 Shape-Based보다 성능이 더 좋음 

### 2.1 View-Based Multi-View Recognition

In its simplest form, the view-based approach aims to add viewpoint tolerance to a 2D image of an object, 
- such as with view point invariant local descriptors [27, 29] or deformation-tolerant global descriptors [6]. 

Given training images across multiple viewpoints, a more stable set of features can be found 
- by tracking those which are shared across multiple views and clustering images accordingly [23], or 
- by learning their relative 2D displacements as the viewpoint changes, 
both with hard constraints for rigid bodies [17, 18] and flexible constraints for deformable bodies [11, 10]. 

```
[23] D. Lowe. Local Feature View Clustering for 3D Object Recognition. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2001.
[17] E. Johns and G.-Z. Yang. From Images to Scenes: Compressing an Image Cluster into a Single Scene Model for Place Recognition. In Proceedings of the International Conference on Computer Vision (ICCV), 2011.
[18] E. Johns and G.-Z. Yang. Generative Methods for LongTerm Place Recognition in Dynamic Scenes. International Journal of Computer Vision (IJCV), 106(3):297–314, 2014
[10] P. F. Felzenszwalb, R. B. Girshick, D. McAllester, and D. Ramanan. Object detection with discriminatively trained partbased models. IEEE Transactions on Pattern Analysis and Machine Intelligence (PAMI), 32(9):1627–1645, 2010. 
[11] R. Fergus, P. Perona, and A. Zisserman. Object Class Recognition by Unsupervised Scale-Invariant Learning. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2003
```

To add further fidelity to the true underlying object geometry, these 2D image elements can also be embedded within an implicit 3D model [36, 22, 28]. 

```
[36] A. Thomas, V. Ferrari, B. Leibe, T. Tuytelaars, B. Schiel, and L. Van Gool. Towards Multi-View Object Class Detection. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2006.
[22] J. Liebelt and C. Schmid. Multi-View Object Class Detection with a 3D Geometric Model. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2010
[28] B. Pepik, M. Stark, P. Gehler, and B. Schiele. MultiView and 3D Deformable Part Models. IEEE Transactions on Pattern Analysis and Machine Intelligence (PAMI),37(11):2232–2245, 2015.
```

If multiple views are available at testing, 
- images can be combined and treated as a single, larger image[31], 
- an approach which can also be addressed in two stages, by processing the individual images first to reduce the search space [5]. 

```
[31] R. Pless. Using many cameras as one. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2003.
[5] A. Collet and S. S. Srinivasa. Efficient multi-view object recognition and full pose estimation. In Proceedings of the IEEE International Conference on Robotics and Automation (ICRA), 2010.
```

Recently, CNN architectures have been extended to allow for recognition from image sequences using a single network, 
- by max pooling across all viewpoints [35-MVCNN], or 
- by unwrapping an object shape into a panorama and max pooling across each row [33-DeepPano]. 

단점 : However, both these methods assume that a **fixed-length image sequence** is provided during both training and testing, and hence are unsuitable for generalised multi-view recognition.

```
[35] H. Su, S. Maji, E. Kalogerakis, and E. G. Learned-Miller. Multi-view Convolutional Neural Networks for 3D Shape Recognition. In Proceedings of the International Conference
on Computer Vision (ICCV), 2015.
[33] B. Shi, S. Bai, Z. Zhou, and X. Bai. DeepPano: Deep Panoramic Representation for 3-D Shape Recognition. IEEE Signal Processing Letters, 22(12):2339–2343, 2015.
```

### 2.2 Shape-Based Multi-View Recognition 

Rather than modelling an object as a set of views with 2D features, an explicit 3D shape can be learned from reconstruction[37-PASCAL VOC] or provided by CAD models [39-ShapeNET], and subsequently matched to from depth images [13], 3D reconstructions [1],or partial reconstructions with shape completion [12, 39-ShapeNet].

```
[13] S. Gupta, R. Girshick, P. Arbelaez, and J. Malik. Learning Rich Features from RGB-D Images for Object Detection and Segmentation. In Proceedings of the European Conference on Computer Vision (ECCV), 2014
[1] S. Bai, X. Bai, Z. Zhou, Z. Zhang, and L. J. Latecki. GIFT: A Real-time and Scalable 3D Shape Search Engine. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2016.
[12] M. Firman, O. M. Aodha, S. Julier, and G. J. Brostow. Structured Prediction of Unobserved Voxels From a Single Depth Image. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2016
```

Shape descriptors include distributions of local surface properties [14, 32], spherical harmonic functions over voxel grids [24], and 3D local invariant features [25]. 

```
[14] B. K. P. Horn. Extended gaussian images. In Proceedings of the IEEE, 1984 
[32] B. C. R. Osada, T. Funkhouser and D. Dobkin. Shape distributions. In ACM Transactions on Graphics, 2002
[24] T. F. M. Kazhdan and S. Rusinkiewicz. Rotation invariant spherical harmonic representation of 3D shape descriptors. In Proceedings of the Symposium of Geometry Processing,2003
[25] T. F. M. Kazhdan and S. Rusinkiewicz. Hough transform and 3D SURF for robust three dimensional classification. In Proceedings of the European Conference on Computer Vision (ECCV), 2010
```

Recently CNNs have been applied to 3D shapes by representing them as 3D occupancy grids, and building generative [39-ShapeNet]or discriminative [26-VoxNet] networks.
```
[39] Z. Wu, S. Song, A. Khosla, F. Yu, L. Zhang, X. Tang, and J. Xiao. 3D ShapeNets: A Deep Representation for Volumetric Shapes. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2015.
[26] D. Maturana and S. Scherer. VoxNet: A 3D Convolutional Neural Network for Real-Time Object Recognition. In Proceedings of the IEEE/RSJ Conference on Intelligent Robots and Systems (IROS), 2015.
```

As of now however, CNNs with 2D view-based methods[35-MVCNN] have outperformed their counterpart 3D voxel-based methods [39-ShapeNet, 26-VoxNet], and we therefore adopt the 2D approach in our work. 

```
[35] H. Su, S. Maji, E. Kalogerakis, and E. G. Learned-Miller. Multi-view Convolutional Neural Networks for 3D Shape Recognition. In Proceedings of the International Conference on Computer Vision (ICCV), 2015.
```

However, it is not yet clear whether this greater performance arises from the superior abundance of 2D image data for pre-training deep networks, or the naturally more efficient representation of 2D than 3D in standard CNN architectures.


---

###### [참고] The next best view problem


The next best view problem (NBV) seeks a single additional sensor placement in order to improve an existing scene reconstruction derived from the current imaging configuration. Depending on the context, NBV can be seen as an incremental approach to building a camera network, designing a sensing strategy for autonomous exploration or selecting an input image dataset for multiview reconstruction.

We propose a next best view (NBV) algorithm that determines each view to reconstruct an arbitrary object. 


The problem addressed in this paper is to plan the **next sensor's position**, called the ‘next best view'(NBV). The NBV is the best view for the reconstruction process from a set of candidate views.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzYyNjA3Mjc1XX0=
-->

---
```
A different approach for exploiting the multiple views of a 3D object was followed by Johns et al. [2016] for the application scenario of multiview object recognition under unconstrained camera trajectories.

In this work, the collection of views was organized in pairs that were provided to a CNN together with their relative pose.

The VGG-M network [Chatfield et al. 2014] was employed in this case consisting of five convolutional and three FC layers.

입력 : Grayscale images + depth images

The outputs of the convolutional layers from the two images were concatenated before being provided to the first FC layer.

제안 방식은 voxel-based 3D ShapeNets [Wu et al. 2015], MVCNN보다 좋은 성능 보임
```


```
Recent work on Active Multi-View Recognition [10] predicts the Next Best View (NBV)
- which is most likely to give the highest extra information about the object, needing a smaller number of image sequences during test-time to predict the model class. 

```

