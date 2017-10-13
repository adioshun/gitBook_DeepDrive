
|
논문명 | Volumetric and Multi-View CNNs for Object Classification on 3D Data |
| --- | --- |
| 저자\(소속\) | Charles R. Qi \(Standford\) |
| 학회/년도 | 2016 , [논문](https://arxiv.org/abs/1604.03265) |
| 키워드 | VMCNN2016, Volumetric CNN 성능향상, Multi-View CNNs 성능향상 |
| 참고 | |
| 코드 | |

# Volumetric and Multi-View CNNs for Object Classification on 3D Data

최근 개발된 3D 처리를 위한 방법

* CNNs based upon volumetric representations
* CNNs based upon multi-view representations.

In this paper, we aim to improve both `volumetric CNNs` and `multi-view CNNs` according to extensive analysis of existing approaches.

## 1. Introduction

목표 : object classification task on 3D data obtained from both `CAD models` and commodity `RGB-D` sensors.

2D -&gt; 3D 확장시 고려 사항

* the additional computational complexity \(volumetric domain\)
* data sparsity

Seminal work by Wu et al. \[33\] propose volumetric CNN architectures on volumetric grids for object classification and retrieval.

```
[33] Z. Wu, S. Song, A. Khosla, F. Yu, L. Zhang, X. Tang, and J. Xiao. 3d shapenets: A deep representation for volumetric shapes. In CVPR 2015, pages 1912–1920, 2015.
```

While these approaches achieve good results, it turns out that training a CNN on multiple 2D views achieves a significantly higher performance, as shown by Su et al. \[32\], who augment their 2D CNN with pre-training from ImageNet RGB data \[6\].

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

We consider **volumetric representations** of 3D point clouds or meshes as input to the 3D object classification problem.

This is primarily inspired by recent advances in real-time scanning technology, which use volumetric data representations.

We further assume that the input data is already pre-segmented by 3D bounding boxes.

In practice, these bounding boxes can be extracted using the sliding windows, object proposals, or background subtraction.

The output of the method is the category label of the volumetric data instance.

### 1.2 Approach

We provide a detailed analysis over factors that influence the performance of volumetric CNNs, including network architecture and volumn resolution.

Based uponour analysis, we strive to improve the performance of volumetric CNNs.

We propose two volumetric CNN network architectures that signficantly improve state-of-the-art of volumetric CNNs on 3D shape classification.

This result has also closed the gap between volumetric CNNs and multi-view CNNs, when they are provided with 3D input discretized at 30×30×30 3D resolution.

- The first network introduces auxiliary learning tasks by classifying part of an object, which help to scrutize details of 3D objects more deeply.

- The second network uses long anisotropic kernels to probe for long-distance interactions.

Combining data augmentation with a multi-orientation pooling, we observe significant performance improvement for both networks.

We also conduct extensive experiments to study the in-fluence of volume resolution, which sheds light on future directions of improving volumetric CNNs.

Furthermore, we introduce a new multi-resolution component to multi-view CNNs, which improves their already compelling performance.

In addition to providing extensive experiments on 3DCAD model datasets, we also introduce a dataset of realworld 3D data, constructed using dense 3D reconstructiontaken with [25].

Experiments show that our networks can better adapt from synthetic data to this real-world data than previous methods.

## 2. Related Work

### 2.1 Shape Descriptors

A large variety of shape descriptors has been developed in the computer vision and graphics community.

For instance, shapes can be represented as `histograms` or `bag-of-feature` models which are constructed from surface normals and curvatures \[13\].

Alternatives include models based on distances, angles, triangle areas, or tetrahedra volumes \[26\], local shape diameters measured at densely-sampled surface points \[3\], Heat kernel signatures \[1, 19\], or extensions of SIFT and SURF feature descriptors to 3D voxel grids \[18\].

The `spherical harmonic descriptor (SPH) [17]` and the `Light Field descriptor (LFD) [4]`are other popular descriptors.

* LFD extracts geometric and Fourier descriptors from object silhouettes rendered from several different viewpoints, and can be directly applied to the shape classification task.

In contrast to recently developed feature learning techniques, these features are handcrafted and do not generalize well across different domains.

> handcrafted 된것들이고 다른 도메인에 적용하기 어렵다.

### 2.2 Convolutional Neural Networks

It turns out that training from large RGB image datasets \(e.g., ImageNet \[6\]\) is able to learn general purpose image descriptors that outperform handcrafted features for a number of vision tasks, including object detection, scene recognition, texture recognition and
classification \[7, 10, 27, 5, 12\].

> 2D CNN에 대한 일반적 내용, 이미지를 이용하여 학습한 descriptors 는 handcrafted 보다 좋은 성능을 보였다.

### 2.3 CNNs on Depth and 3D Data

With the introduction of commodity range sensors, the `depth channel` became available to provide additional information that could be incorporated into common CNN architectures.

A very first approach combines convolutional and recursive neural networks for learning features and classifying RGB-D images \[30\].

Impressive performance for object detection from RGB-D images has been achieved using a geocentric embedding for depth images that encodes height above ground and angle with gravity for each pixel in addition to the horizontal disparity \[11\].

Recently, a CNN architecture has been proposed where the RGB and depth data are processed
in two separate streams; in the end, the two streams are combined with a late fusion network \[8\].

All these descriptors operate on single RGB-D images, thus processing 2.5D data.

```
[30] R. Socher, B. Huval, B. Bath, C. D. Manning, and A. Y. Ng. Convolutional-recursive deep learning for 3d object classification. In NIPS 2012, pages 665–673, 2012.
[11] S. Gupta, R. Girshick, P. Arbelaez, and J. Malik. Learning ´rich features from rgb-d images for object detection and segmentation. In ECCV 2014, pages 345–360. Springer, 2014.
[8] A. Eitel, J. T. Springenberg, L. Spinello, M. Riedmiller, and W. Burgard. Multimodal deep learning for robust rgb-d object recognition. In IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Hamburg, Germany, 2015.
```

#### 3DShapeNets

Wu et al. \[33\] lift 2.5D to 3D with their 3D ShapeNets approach by categorizing each voxel as free space, surface or occluded, depending on whether it is in front of, on, or behind the visible surface \(i.e., the depth value\) from the depth map.

The resulting representation is a **3D binary voxel grid**, which is the input to a CNN with 3D filter banks.

Their method is particularly relevant in the context of this work, as they are the first to apply CNNs on a 3D representation.

```
[33] Z. Wu, S. Song, A. Khosla, F. Yu, L. Zhang, X. Tang, and J. Xiao. 3d shapenets: A deep representation for volumetric shapes. In CVPR 2015, pages 1912–1920, 2015.
```

#### VoxNet

A similar approach is VoxNet \[24\], which also uses **binary voxel grids** and a corresponding 3D CNN architecture.

| The advantage of these approaches is that it can process different sources of 3D data, including LiDAR point clouds, RGB-D point clouds, and CAD models; we likewise follow this direction. |
| --- |
| \[중요\] 3DShapeNets & VoxNet = LiDAR 데이터에도 적용할수 있다는 장점이 있다. |

```
[24] D. Maturana and S. Scherer. Voxnet: A 3d convolutional neural network for real-time object recognition. In IEEE/RSJ International Conference on Intelligent Robots and ystems,
September 2015.
```

#### 기존 2D CNN 활용

An alternative direction is to exploit established 2D CNN architectures; to this end, 2D data is extracted from the 3D representation.

In this context, `DeepPano [28]` converts 3D shapes into panoramic views; i.e., a cylinder projection around its principle axis.

Current state-of-the-art uses multiple rendered views, and trains a CNN that can process all views jointly \[32\].

This multi-view CNN \(MVCNN\) is pre-trained on ImageNet \[6\] and uses view-point pooling to
combine all streams obtained from each view.

A similar idea on stereo views has been proposed earlier \[22\].

```
[28] B. Shi, S. Bai, Z. Zhou, and X. Bai. Deeppano: Deep panoramic representation for 3-d shape recognition. Signal Processing Letters, IEEE, 22(12):2339–2343, 2015.
[32] H. Su, S. Maji, E. Kalogerakis, and E. G. Learned-Miller. Multi-view convolutional neural networks for 3d shape recognition. In ICCV 2015, 2015.
[6] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. FeiFei. Imagenet: A large-scale hierarchical image database. In CVPR 2009, pages 248–255. IEEE, 2009.
[22] Y. LeCun, F. J. Huang, and L. Bottou. Learning methods for generic object recognition with invariance to pose and lighting. In CVPR 2014, volume 2, pages II–97. IEEE, 2004
```

## 3. Analysis of state-of-the-art 3D Volumetric CNN versus Multi-View CNN

Two representations of generic 3D shapes are popularly used for object classification,

* **volumetric** : The volumetric representation encodes a 3D shape as a 3D tensor of binary or real values.
* **multi-view** : The multi-view representation encodes a 3D shape as a collection of renderings from multiple viewpoints.

Tensor로 저장되어 있으므로 두개다 CNN으로 학습 할 수 있다. `Stored as tensors, both representations can easily be used to train convolutional neural networks, i.e., volumetric CNNs and multi-view CNNs.`

당연히 `volumetric`이 Multiview 보다 많은 데이터를 포함 하고 있다. `Intuitively, a volumetric representation should encode as much information, if not more, than its multi-view counterpart.`

그러나 실험결과 `multiview CNNs`가 더 좋은 성능을 보인다. `However, experiments indicate that multiview CNNs produce superior performance in object classification.`

![](https://i.imgur.com/I1yMqvH.png)

The gap seems to be caused by two factors:
* input resolution
* network architecture differences.

###### Input resolution

> 추가적 실험 결과 입력값은 성능에 큰 영향을 주지 않는 것으로 밝혀 졌다.

The multi-view CNN downsamples each rendered view to 227 × 227 pixels \(Multiview Standard Rendering in Fig 1\);

the volumetric CNN uses a 30×30×30 occupancy grid \(Volumetric Occupancy Grid in Fig 1\) to maintain a similar computational cost.

However, the difference in input resolution is not the primary reason for this performance gap, as evidenced by further experiments.


![](https://i.imgur.com/CMyNVE0.png)

###### Network

We compare the two networks by providing them with data containing similar level of detail.

To this end, we feed the multi-view CNN with renderings of the 30 × 30 × 30 occupancy grid using sphere rendering, i.e., for each occupied voxel, a ball is placed at its center,
with radius equal to the edge length of a voxel \(Multi-View Sphere Rendering in Fig 1\).

We train the multi-view CNN from scratch using these sphere renderings.

The accuracy of this multi-view CNN is reported in blue.

> 4장/5장에서 volumetric CNN/multi-view CNN의 성능 향상을 시도 한다.

## 4. Volumetric Convolutional Neural Networks

### 4.1. Overview

We improve volumetric CNNs through three separate means
1. Network structures
2. Data augmentation
3. Feature pooling

#### A. Network Architecture

We propose two network variations that significantly improve state-of-the-art CNNs on 3D volumetric data.

##### 가. The first network

- 오버피팅 방지 목적 : Designed to **mitigate over fitting** by introducing auxiliary training tasks, which are themselves challenging.

- These auxiliary tasks encourage the network to **predict object class** labels from **partial subvolumes**.
- Therefore, no additional annotation efforts are needed.

##### 나. The second network

- 멀티뷰와 비슷한 역할 수행 : `Designed to _mimic multiview CNNs_, as they are strong in 3D shape classification`.

- 네트워크 내에서 end-to-end로 3D를 2D로 투영함 `Instead of using rendering routines from computer graphics, our network projects a 3D shape to 2D** by convolving its 3D volume with an anisotropic probing kernel.`
	- This kernel is capable of encoding long-range interactions between points.
	- An image CNN is then appended to classify the 2D projection.


In order to mitigate overfitting from too many parameters, we adopt the **mlpconv layer** from [23] as our basic building block in both network variations.

### 4.2 Network 1: Auxiliary Training by Subvolume Supervision

- 3D ShapeNets은 오버피팅 문제가 있다. `We observe significant overfitting when we train the volumetric CNN proposed by [33] in an end-to-end fashion(see supplementary). `

```
[33] Z. Wu, S. Song, A. Khosla, F. Yu, L. Zhang, X. Tang, and J. Xiao. 3d shapenets: A deep representation for volumetric shapes. In CVPR 2015, pages 1912–1920, 2015
```

- 제안 : Main task가 오버피팅 되어도 auxiliary tasks를 두어서 계속 학습 하도록 함 `We thus introduce auxiliary tasks that are closely correlated with the main task but are difficult to overfit, so that learning continues even if our main task is overfitted.`
- auxiliary tasks도 label예측을 목표로 하지만, 입력값의 local subvolume에서만 동작함 ` These auxiliary training tasks also predict the same object labels, but the predictions are made solely on a local subvolume of the input. `

- Without complete knowledge of the object, the auxiliary tasks are more challenging, and can thus better exploit the discriminative power of local regions.

- 이러한 제안은 기존의 multitask learning방식과는 다른 것이다. `This design is different from the classic multitask learning setting of hetergenous auxiliary tasks,`
- which inevitably requires collecting additional annotations (e.g., conducting both object classification and detection [9]).

We implement this design through an architecture shown in Fig 3.

![](https://i.imgur.com/5PSzKxu.png)

```
[Figure 3. Auxiliary Training by Subvolume Supervision (Sec 4.2).]
- The main innovation is that we add auxiliary tasks to predict class labels that focus on part of an object, intended to drive the CNN to more heavily exploit local discriminative features.
- An mlpconv layer is a composition of three conv layers interleaved by ReLU layers.
- The five numbers under mlpconv are the number of channels, kernel size and stride of the first conv layer, and the number of channels of the second and third conv layers, respectively.
- The kernel size and stride of the second and third conv layers are 1.
- For example, mlpconv(48, 6, 2; 48; 48) is a composition of conv(48, 6, 2), ReLU, conv(48, 1, 1), ReLU, conv(48, 1, 1) and ReLU layers.
- Note that we add dropout layers with rate=0.5 after fully connected layers.
```
#### A. Layer 1, 2, 3 : MLPconv (multilayer perceptron convolution) layers

- 첫 3개층 레이어는 MLPconv이다. `The first three layers are mlpconv (multilayer perceptron convolution) layers, `
	- a 3D extension of the 2D mlpconv proposed by [23].
	- 입/출력 값은 모두 4D 텐서 `The input and output of our mlpconv layers are both 4D tensors.`

-  mlpconv은 입력층-은닉층-출력층으로 구성된 뉴런 네트워크로 **Feature Extraction**에 좋은 성능을 보임 : `mlpconv has a three-layer structure and is thus a universal function approximator if enough neurons are provided in its intermediate layers. Therefore, mlpconv is a powerful filter for feature extraction of local patches, enhancing approximation of more abstract representations. In addition, mlpconv has been validated to be more discriminative with fewer parameters than ordinary convolution with pooling [23].`

#### B. Layer 4 :  둘로 나누어짐 
- At the fourth layer, the network branches into two.
	- **The lower branch**: 원래 업무 수행  takes the whole object as input for traditional classification.
	- **The upper branch** : 보조 업무 수행 is a novel branch for **auxiliary tasks**. 

- 두개의 네트어크로 나누어 지기 전에 512개로  쪼갬 : It slices the `512 × 2 × 2 × 2` 4D tensor (2 grids along x, y, z axes and 512 channels) into 2×2×2 = 8 vectors of dimension 512.

#### C. FC Layer / Softmax Layer

각 벡터 마다 분류 작업 수행 `- We set up a classification task for each vector.`

- **A fully connected layer** and a **softmax layer** are then appended independently to each vector to construct classification losses.

- Simple calculation shows that the receptive field of each task is 22×22×22, cover in groughly 2/3 of the entire volume.

### 4.3 Network 2: Anisotropic Probing

- 멀티뷰 CNN은 3D 물체를 2D로 투영하고 2 CNN을 적용하여 분류 작업을 한다. `multiview CNNs first project 3D objects to 2D and then make use of well-developed 2D image CNNs for classification.`
	- 일반적인 멀티뷰 CNN은 외부 CV의 도움이 필요 하다(투영파일 생성). 하지만 본 논문에서는  투영도 네트워크 안에서 진행하여 진정한 End-to-End화 하였다. 
	- `However, while multi-view CNNs use external rendering pipelines from computer graphics, we achieve the 3D-to-2D projection using network layers in a manner similar to X-rayscanning.`

- 두번째 네트워크의 주 기능은 **anisotropic kernel**을 이용하여서 3D의 global structure 을 잡아 내는 것이다. ` Key to this network is the use of an elongated anisotropic kernel which helps capture the global structure of the 3D volume. `

![](https://i.imgur.com/MfPn2d4.png)
```
[Figure 4. CNN with Anisotropic Probing kernels]
- We use an elongated kernel to convolve the 3D cube and aggregate information to a 2D plane. 
- Then we use a 2D NIN (NIN-CIFAR10 [23]) to classify the 2D projection of the original 3D shape.
```
As illustrated in Fig 4, the neural network has two modules: 
- An anisotropic probing module 
- A network innetwork module.

#### A. Anisotropic probing module 

- 이 모듈은 elongated kernels로 이루어진 3개의 Conv. 레이어로 이루러져 있다. `The anisotropic probing module contains  3 convolutional layers of elongated kernels, each followed by a nonlinear ReLU layer.`
	- 입/출력 값은 모두 3D 텐서 `Note that both the input and output of each layer are 3D tensors.`

-  이 모듈이 가지는 장점 `In contrast to traditional isotropic kernels, an anisotropic probing module has`
	-  the advantage of aggregating **long range interactions in the early feature learning** stage with fewer parameters.

-  기존 방식은 파라미터수가 많은 문제가 있다. `As a comparison, with traditional neural networks constructed from isotropic kernels, introducing long-range interactions at an early stage can only be achieved through large kernels, which inevitably introduce many more parameters.`

#### B.  adapted NIN network

- After anisotropic probing, we use an **adapted NIN network** [23] to address the **classification problem**.

- Our anistropic probing network is capable of capturing internal structures of objects through its X-ray like projection mechanism.

- Combined with multi-orientation pooling (introduced below), it is possible for this probing mechanism to capture any 3D structure, due to its relationship with the Radon transform.

- 2D로 처리 하기 때문에 높은 Resolution도 처리 가능 `In addition, this architecture is scalable to higher resolutions,since all its layers can be viewed as 2D.`

- While 3D convolution involves computation at locations of cubic resolution, we maintain quadratic compute.

### 4.4. Data Augmentation and Multi-Orientation Pooling

- 위에 이야기한 두개의 네트워크 들은 모두 model orientation에 민감하다. `The two networks proposed above are both sensitive to model orientation. `
	- subvolume 슈퍼 비젼 방식에서는 다른 model orientations은 다른local subvolumes을 정의 한다. ` In the subvolume supervision method, different model orientations define different local subvolumes`
	-  anisotropic probing 방식에서는 같은 높이와 방향에 있는 Voxel들만 interaction 할수 있따. ` in the anisotropic probing method, only voxels of the same height and along the probing direction can have interaction in the early feature extraction stage. `

- 따라서 다양한 orientation 에 대하여 augment 하고 orientation pooling하는 것이 필요 하다. `Thus it is helpful to augment the training data by varying object orientation and combining predictions through orientation pooling.`

![](https://i.imgur.com/Qxq2qOr.png)
```
[Figure 5.]
- Left: Volumetric CNN (single orientation input).
- Right: Multi-orientation volumetric CNN (MO-VCNN), which takes in various orientations of the 3D input, extracts features from shared CNN1 and then pass pooled feature through another network CNN2 to make a prediction.
```

- 이를 위해서 **Su-MVCNN** 제안을 활용 하였다. `Similar to Su-MVCNN [32] which aggregates information from multiple view inputs through a view-pooling layer and follow-on fully connected layers,'
	- 다른 orientations에서 3D 입력을 샘플링하고, multi-orientation volumetric CNN를 통해서 합치는 작업 수행 `we sample 3D input from different orientations and aggregate them in a multi-orientation volumetric CNN (MO-VCNN) as shown in Fig 5. `


- 학습시 rotations이 다른 3D 모델들을 생성 `At training time, we generate different rotations of the 3D model by changing both azimuth(방위각) and elevation(고도) angles, sampled randomly. `

- volumetric CNN은 처음에는 single rotations으로 학습 수행 `A volumetric CNN is firstly trained on single rotations. `

- 이후 네트워크를 CNN1과 CNN2로 분리 하여 Then we decompose the network to CNN1 (lower layers) and CNN2 (higher layers)to construct a multi-orientation version. 

The MO-VCNN’sweights are initialized by a previously trained volumetricCNN with CNN1’s weights fixed during fine-tuning. 

Whilea common practice is to extract the highest level features(features before the last classification linear layer) of multipleorientations, average/max/concatenate them, and traina linear SVM on the combined feature, this is just a specialcase of the MO-VCNN.

Compared to 3DShapeNets [33] which only augments data by rotating around vertical axis, our experiment shows that orientation pooling combined with elevation rotation can greatly increase performance.


## 5. Multi-View Convolutional Neural Networks




<!--stackedit_data:
eyJoaXN0b3J5IjpbODkzOTI4ODNdfQ==
-->