|논문명|Volumetric and Multi-View CNNs for Object Classification on 3D Data
|-|-|
|저자(소속)| Charles R. Qi (Standford)|
|학회/년도| 2016 , [논문](https://arxiv.org/abs/1604.03265)|
|키워드|Volumetric CNN 성능향상, Multi-View CNNs 성능향상 |
|참고||
|코드||

# Volumetric and Multi-View CNNs for Object Classification on 3D Data

최근 개발된 3D 처리를 위한 방법

- CNNs based upon volumetric representations 
- CNNs based upon multi-view representations.

In this paper, we aim to improve both `volumetric CNNs` and `multi-view CNNs` according to extensive analysis of existing approaches.

## 1. Introduction

목표 : object classification task on 3D data obtained from both `CAD models` and commodity `RGB-D` sensors.


2D -> 3D 확장시 고려 사항 
- the additional computational complexity (volumetric domain) 
- data sparsity 


Seminal work by Wu et al. [33] propose volumetric CNN architectures on volumetric grids for object classification and retrieval. 

```
[33] Z. Wu, S. Song, A. Khosla, F. Yu, L. Zhang, X. Tang, and J. Xiao. 3d shapenets: A deep representation for volumetric shapes. In CVPR 2015, pages 1912–1920, 2015.
```

While these approaches achieve good results, it turns out that training a CNN on multiple 2D views achieves a significantly higher performance, as shown by Su et al. [32], who augment their 2D CNN with pre-training from ImageNet RGB data [6].

```
[32] H. Su, S. Maji, E. Kalogerakis, and E. G. Learned-Miller. Multi-view convolutional neural networks for 3d shape recognition. In ICCV 2015, 2015.
[6] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. FeiFei. Imagenet: A large-scale hierarchical image database. In CVPR 2009, pages 248–255. IEEE, 2009
```

These results indicate that existing 3D CNN architectures and approaches are unable to fully exploit the power of 3D representations. 

> 기존 3D CNN은 3D representations을 충분히 활용할수 없다. 

In this work, we analyze these observations and evaluate the design choices. 

Moreover, we show how to reduce the gap between volumetric CNNs and multi-view CNNs by efficiently augmenting training data, introducing new CNN architectures in 3D. 

> volumetric CNNs and multi-view CNNs 사이의 차이를 줄이기 위해 노력 하였다. 

Finally, we examine multiview CNNs; our experiments show that we are able to improve upon state of the art with improved training data augmentation and a new multi-resolution component.

### 1.1 Problem Statement

다시 살펴 보기 

### 1.2 Approach

다시 살펴 보기 

## 2. Related Work

### 2.1 Shape Descriptors 

A large variety of shape descriptors has been developed in the computer vision and graphics community. 

For instance, shapes can be represented as `histograms` or `bag-of-feature` models which are constructed from surface normals and curvatures [13]. 

Alternatives include models based on distances, angles, triangle areas, or tetrahedra volumes [26], local shape diameters measured at densely-sampled surface points [3], Heat kernel signatures [1, 19], or extensions of SIFT and SURF feature descriptors to 3D voxel grids [18]. 

The `spherical harmonic descriptor (SPH) [17]` and the `Light Field descriptor (LFD) [4] `are other popular descriptors. 
- LFD extracts geometric and Fourier descriptors from object silhouettes rendered from several different viewpoints, and can be directly applied to the shape classification task. 

In contrast to recently developed feature learning techniques, these features are handcrafted and do not generalize well across different domains.

> handcrafted 된것들이고 다른 도메인에 적용하기 어렵다. 

### 2.2 Convolutional Neural Networks 

It turns out that training from large RGB image datasets (e.g., ImageNet [6]) is able to learn general purpose image descriptors that outperform handcrafted features for a number of vision tasks, including object detection, scene recognition, texture recognition and
classification [7, 10, 27, 5, 12]. 

> 2D CNN에 대한 일반적 내용, 이미지를 이용하여 학습한 descriptors 는 handcrafted 보다 좋은 성능을 보였다. 

### 2.3 CNNs on Depth and 3D Data 

With the introduction of commodity range sensors, the `depth channel` became available to provide additional information that could be incorporated into common CNN architectures.

A very first approach combines convolutional and recursive neural networks for learning features and classifying RGB-D images [30]. 

Impressive performance for object detection from RGB-D images has been achieved using a geocentric embedding for depth images that encodes height above ground and angle with gravity for each pixel in addition to the horizontal disparity [11]. 

Recently, a CNN architecture has been proposed where the RGB and depth data are processed
in two separate streams; in the end, the two streams are combined with a late fusion network [8]. 


All these descriptors operate on single RGB-D images, thus processing 2.5D data.

```
[30] R. Socher, B. Huval, B. Bath, C. D. Manning, and A. Y. Ng. Convolutional-recursive deep learning for 3d object classification. In NIPS 2012, pages 665–673, 2012.
[11] S. Gupta, R. Girshick, P. Arbelaez, and J. Malik. Learning ´rich features from rgb-d images for object detection and segmentation. In ECCV 2014, pages 345–360. Springer, 2014.
[8] A. Eitel, J. T. Springenberg, L. Spinello, M. Riedmiller, and W. Burgard. Multimodal deep learning for robust rgb-d object recognition. In IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Hamburg, Germany, 2015.
```

#### 3DShapeNets


Wu et al. [33] lift 2.5D to 3D with their 3D ShapeNets approach by categorizing each voxel as free space, surface or occluded, depending on whether it is in front of, on, or behind the visible surface (i.e., the depth value) from the depth map. 

The resulting representation is a 3D binary voxel grid, which is the input to a CNN with 3D filter banks. 

Their method is particularly relevant in the context of this work, as they are the first to apply CNNs on a 3D representation. 

```
[33] Z. Wu, S. Song, A. Khosla, F. Yu, L. Zhang, X. Tang, and J. Xiao. 3d shapenets: A deep representation for volumetric shapes. In CVPR 2015, pages 1912–1920, 2015.
```

#### VoxNet 

A similar approach is VoxNet [24], which also uses binary voxel grids and a corresponding 3D CNN architecture. 


|The advantage of these approaches is that it can process different sources of 3D data, including LiDAR point clouds, RGB-D point clouds, and CAD models; we likewise follow this direction.|
|-|
|[중요] 3DShapeNets & VoxNet = LiDAR 데이터에도 적용할수 있다는 장점이 있다. |

```
[24] D. Maturana and S. Scherer. Voxnet: A 3d convolutional neural network for real-time object recognition. In IEEE/RSJ International Conference on Intelligent Robots and ystems,
September 2015.
```


#### 기존 2D CNN 활용 

An alternative direction is to exploit established 2D CNN architectures; to this end, 2D data is extracted from the 3D representation. 

In this context, `DeepPano [28]` converts 3D shapes into panoramic views; i.e., a cylinder projection around its principle axis. 

Current state-of-the-art uses multiple rendered views, and trains a CNN that can process all views jointly [32]. 

This multi-view CNN (MVCNN) is pre-trained on ImageNet [6] and uses view-point pooling to
combine all streams obtained from each view. 

A similar idea on stereo views has been proposed earlier [22].

```
[28] B. Shi, S. Bai, Z. Zhou, and X. Bai. Deeppano: Deep panoramic representation for 3-d shape recognition. Signal Processing Letters, IEEE, 22(12):2339–2343, 2015.
[32] H. Su, S. Maji, E. Kalogerakis, and E. G. Learned-Miller. Multi-view convolutional neural networks for 3d shape recognition. In ICCV 2015, 2015.
[6] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. FeiFei. Imagenet: A large-scale hierarchical image database. In CVPR 2009, pages 248–255. IEEE, 2009.
[22] Y. LeCun, F. J. Huang, and L. Bottou. Learning methods for generic object recognition with invariance to pose and lighting. In CVPR 2014, volume 2, pages II–97. IEEE, 2004

```

## 3. Analysis of state-of-the-art 3D Volumetric CNN versus Multi-View CNN

Two representations of generic 3D shapes are popularly used for object classification, 
- **volumetric** : The volumetric representation encodes a 3D shape as a 3D tensor of binary or real values.
- **multi-view** : The multi-view representation encodes a 3D shape as a collection of renderings from multiple viewpoints. 

Tensor로 저장되어 있으므로 두개다 CNN으로 학습 할 수 있다. `Stored as tensors, both representations can easily be used to train convolutional neural networks, i.e., volumetric CNNs and multi-view CNNs. `


당연히 `volumetric `이 Multiview`보다 많은 데이터를 포함 하고 있다. `Intuitively, a volumetric representation should encode as much information, if not more, than its multi-view counterpart. `


그러나 실험결과 `multiview CNNs`가 더 좋은 성능을 보인다. `However, experiments indicate that multiview CNNs produce superior performance in object classification.`


![](https://i.imgur.com/I1yMqvH.png)


The gap seems to be caused by two factors: 
- input resolution 
- network architecture differences. 

###### Input resolution 

The multi-view CNN downsamples each rendered view to 227 × 227 pixels (Multiview Standard Rendering in Fig 1); 

the volumetric CNN uses a 30×30×30 occupancy grid (Volumetric Occupancy Grid in Fig 1) to maintain a similar computational cost.

However, the difference in input resolution is not the primary reason for this performance gap, as evidenced by further experiments. 

> 추가적 실험 결과 입력값은 성능에 큰 영향을 주지 않는 것으로 밝혀 졌다. 

![](https://i.imgur.com/CMyNVE0.png)


###### Network 

We compare the two networks by providing them with data containing similar level of detail.

To this end, we feed the multi-view CNN with renderings of the 30 × 30 × 30 occupancy grid using sphere rendering, i.e., for each occupied voxel, a ball is placed at its center,
with radius equal to the edge length of a voxel (Multi-View Sphere Rendering in Fig 1).

We train the multi-view CNN from scratch using these sphere renderings. 

The accuracy of this multi-view CNN is reported in blue.

> 4장/5장에서 volumetric CNN/multi-view CNN의 성능 향상을 시도 한다. 

