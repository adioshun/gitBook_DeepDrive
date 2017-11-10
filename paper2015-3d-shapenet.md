| 논문명 | 3D ShapeNets: A Deep Representation for Volumetric Shapes |
| --- | --- |
| 저자\(소속\) | Zhirong Wu \(Princeton University\) |
| 학회/년도 | CVPR 2015, [논문](https://arxiv.org/abs/1406.5670) |
| 키워드 | Zhirong2015, Classification & shape completion |
| 데이터셋/모델 | ModelNet10 |
| 참고 | [홈페이지](http://3dshapenets.cs.princeton.edu/), [ppt](http://vision.princeton.edu/talks/2015_CVPR/2015_3DshapeNets_CVPR.pptx) |
| 코드 | [Matlab](https://github.com/zhirongw/3DShapeNets) |

# 3D ShapeNet

3D shape는 good generic shape representation의 부재로 잘 사용하고 있지 못하고 있다.

Our model, 3D ShapeNets,

* learns the distribution of complex 3D shapes across different object categories 
* and arbitrary poses from raw CAD data, 
* and discovers hierarchical compositional part representations automatically

To train our 3D deep learning model, we construct ModelNet – a large-scale 3D CAD model dataset.

## 1. Introduction

3D representation에 대한 많은 theories가 있지만, 객체 인식에 3D기반 방법을 쓰는건 제약이 많다. `Even though there are many theories about 3D representation ([5, 22]), the success of 3D-based methods has largely been limited to instance recognition (e.g. model based keypoint matching to nearest neighbors [24, 31]).`

```
[5] I. Biederman. Recognition-by-components: a theory of human image understanding. Psychological review, 1987.
[22] J. L. Mundy. Object recognition in the geometric era: A retrospective. In Toward category-level object recognition. 2006.
```

좋은 representation의 부족으로 객체 분류 인식에 3D shape는 잘 사용되지 않았다. `For object category recognition, 3D shape is not used in any state-of-the-art recognition methods (e.g. [11, 19]), mostly due to the lack of a good generic representation for 3D geometric shapes.`

```
[11] P. F. Felzenszwalb, R. B. Girshick, D. McAllester, and D. Ramanan. Object detection with discriminatively trained part based models. PAMI, 2010.
[19] A. Krizhevsky, I. Sutskever, and G. Hinton. Imagenet classification with deep convolutional neural networks. In NIPS, 2012.
```

최근 `키넥트` 등의 저렴한 장비가 나오면서 led to a renewed interest in 2.5D object recognition from **depth maps** \(e.g. Sliding Shapes \[30\]\).

깊이 정보의 정확도가 신뢰수준이 되면서 3D 모델 representation의 필요성이 더욱 대두 되었다.

객체 분류 이외에도 **shape completion**도 중요한 도전 과제이다.

* given a 2.5D depth map of an object from one view, what are the possible 3D structures behind it?
* eg. 커피잔의 한 면만 보고도 그 안이 뚤려있을것이라고 인식 하는 것 

> 본 논문의 목적 : In this paper, we study generic **shape representation** for both `object category recognition` and `shape completion`.

we desire a data-driven way to learn the complex shape distributions from raw 3D data across object categories and poses, and automatically discover a hierarchical compositional part representation.

![Figure 1: Usages of 3D ShapeNets](https://i.imgur.com/F3YZIs8.png)  
Figure 1: Usages of 3D ShapeNets.

* Given a depth map of an object, we convert it into a volumetric representation
  and identify the observed surface, free space and occluded space. 
* 3D ShapeNets can recognize object category, complete full 3D shape, and predict the next best view if the initial recognition is uncertain. 
* Finally, 3D ShapeNets can integrate new views to recognize object jointly with all views.

As shown in Figure 1, this would allow us to infer the full 3D volume from a depth map without the knowledge of object category and pose a priori.

Beyond the ability to jointly hallucinate missing structures and predict categories, we also desire the ability to compute the potential information gain for recognition with regard to missing parts.

This would allow an active recognition system to choose an optimal subsequent view for observation, when the category recognition from the first view is not sufficiently confident.

![](https://i.imgur.com/D8S5YK9.png)

* To this end, we propose **3D ShapeNets** to represent a geometric 3D shape as a **probabilistic distribution of binary variables on a 3D voxel grid**.

* 데이터 기반으로 3D voxel의 복합한 결합 분포를 학습 하기 위하여 **Convolutional Deep Belief Network**를 사용하였다. `Our model uses a powerful Convolutional Deep Belief Network (Figure 2) to learn the complex joint distribution of all 3D voxels in a data driven manner.`

* 학습을 위해 `ModelNet`을 구축 하였다. : dataset of 3D computer graphics CAD models.

## 2. Related Work

There has been a large body of insightful research on analyzing 3D CAD model collections.

### 2.1 deformable part-based models

* Most of the works \[7, 12, 17\] use an **assembly-based approach** to build deformable part-based models.

* 제약 : These methods are limited to a specific class of shapes with small variations, with surface correspondence being one of the key problems in such approaches.

### 2.2 surface reconstruction

* For surface reconstruction of corrupted scanning input, most related works \[3, 26\] are largely based on **smooth interpolation** or **extrapolation**.

* These approache scan only tackle small missing holes or deficiencies.

### 2.3 Template-based methods

* 사용 가능한 templates에 따라 성능 차이 생김 :  Template-based methods \[27\] are able to deal with large space corruption but are mostly limited by the quality of available templates and often do not provide different semantic interpretations of reconstructions.

### 2.4 deep learning models

* 딥러닝은 2D Shape에 대한 모델을 생성할수 있게 해준다. The great generative power of deep learning models has allowed researchers to build deep generative models for 2D shapes:

  * most notably the DBN \[15\] to generate hand written digits and Shape BM \[10\] to generate horses, etc. 

* These models are able to effectively capture intra-class variations.

* We also desire this generative ability for shape reconstruction but we focus on more complex real world object shapes in 3D.

```
[15] G. E. Hinton, S. Osindero, and Y.-W. Teh. A fast learning algorithm for deep belief nets. Neural computation, 2006
[10] S. M. A. Eslami, N. Heess, and J. Winn. The shape boltzmann machine: a strong model of object shape. In CVPR, 2012.
```

### 2.5 2.5D deep learning

* For 2.5D deep learning, \[29\] and \[13\] build discriminative convolutional neural nets to model images and depth maps.

* 단지 깊이를 또 다른 채널로 사용 : Although their algorithms are applied to **depth maps**,they use depth as an extra 2D channel instead of modeling full 3D.

```
[29-CR3D2012] R. Socher, B. Huval, B. Bhat, C. D. Manning, and A. Y. Ng. Convolutional-recursive deep learning for 3d object classification. In NIPS. 2012.
[13-Saurabh2014] S. Gupta, R. Girshick, P. Arbelaez, and J. Malik. Learning ´rich features from rgb-d images for object detection and segmentation.
In ECCV. 2014.
```

### 2.6 본 논문의 방식

* Unlike \[29\], our model learns a shape distribution over a voxel grid.

* 최초의 논문이다. `To the best of our knowledge, we are the first work to build 3D deep learning models.`

* To deal with the dimensionality of high resolution voxels, **inspired by \[21\]**, we apply the same convolution technique in our model.

> \[21\] The model is precisely a convolutional DBM where all the connections are undirected, while ours is a convolutional DBN

```            
[21] H. Lee, R. Grosse, R. Ranganath, and A. Y. Ng. Unsupervised learning of hierarchical representations with convolutional deep belief networks. Communications of the ACM,            
2011.``

### 2.7 active object recognition

* Unlike static object recognition in a single image, the sensor in active object recognition \[6\] can move to new viewpoints to gain more information about the object.

* Therefore,the Next-Best-View problem \[25\] of doing view planningbased on current observation arises.

* Most previous works in active object recognition \[9, 16\] build their view planning strategy using 2D color information.

* However this multi-view problem is intrinsically 3D in nature.

### 2.8 Atanasovet al

* Atanasovet al, \[1, 2\] implement the idea in real world robots, but they assume that there is only one object associated with each class reducing their problem to instance-level recognition with no intra-class variance.

* Similar to \[9\], we use mutual information to decide the NBV.

* However, we consider this problem at the precise voxel level allowing us to infer howvoxels in a 3D region would contribute to the reduction ofrecognition uncertainty.

## 3. 3D ShapeNets

### 3.1 입력 데이터

* To study 3D shape representation, we propose to represent a geometric 3D shape as a **probability distribution of binary variables on a 3D voxel grid**.

* Each 3D mesh is represented as a binary tensor:

  * 1 indicates the voxel is inside the mesh surface, 
  * 0 indicates the voxel is outside the mesh \(i.e., it is empty space\). 
  * The grid size in our experiments is 30 × 30 × 30.

### 3.2 네트워크 특징

* To represent the probability distribution of these binary variables for 3D shapes, we design a** Convolutional DeepBelief Network** \(CDBN\).

> Deep Belief Networks \(DBN\)\[15\] are a powerful class of probabilistic models often used to model the joint probabilistic distribution over pixels and labels in 2D images.

* Here, we adapt the model from 2D pixel data to 3D voxel data, which imposes some unique challenges.

* A 3D voxel volume with reasonable resolution\(say 30 × 30 × 30\) would have the same dimensions as a high-resolution image \(165×165\).

* A fully connected DBN을 적용시 파라미터수가 많아 지므로 본 제안에서는 Convolution\(by weight sharing\) 사용 `on such an image would result in a huge number of parameters making the model intractable to train effectively. Therefore, we propose to use convolution to reduce model parameters by weight sharing.`

* 하지만, Convolution에서 일반적으로 쓰는 Pooling을 사용하지는 않았다. `However, different from typical convolutional deep learning models (e.g. [21]), we do not use any form of pooling in the hidden layers – while pooling may enhance the invariance properties for recognition, in our case, it would also lead to greater uncertainty for shape reconstruction.`

### 3.3 Energy Function

The energy, $$E$$, of a convolutional layer in our model can be computed as:


$$
E(v,h) = - \sum_f \sum_i (h^f_j (W^f \circledast v )_j + c^f h ^f_j) - \sum_l b_lv_l
$$


* $$v_l$$ : each visible unit
* $$h^f_j$$ : each hidden unit in a feature channel $$f$$
* $$W^f$$ : the convolutional filter
* $$\circledast$$ : convolution operation

* In this energy definition,

  * each visible unit $$v_l$$ is associated with a unique bias term $$b_l$$ to facilitate reconstruction, 
  * and all hidden units $$\{ h^f_j\}$$ in the same convolution channel share the same bias term $$c^f$$. 

* Similar to \[19\], we also allow for a convolution stride.

* A 3D shape is represented as a 24 × 24 × 24 voxel grid with 3 extra cells of padding in both directions to reduce the convolution border artifacts.

* The labels are presented as standard one of K softmax variables.

### 3.4 네트워크 구조

* Layer 1 : has 48 filters of size 6 and stride 2;

* Layer 2 :  has 160 filters of size 5 and stride 2 \(i.e., each filter has 48×5×5×5 parameters\);

* Layer 3 :  has 512 filters of size 4

  * each convolution filter is connected to all the feature channels in the previous layer;

* Layer 4 : a standard **fully connected RBM** with 1200 hidden units;

* Layer 5 &  final layer with 4000 hidden units takes as input a combination of multinomial label variables and Bernoulli feature variables.

* The top layer forms an **associative memory DBN** as indicated by the bi-directional arrows, while all the other layer connections are directed top-down.

### 3.2 학습 방법

* We first pre-train the model in a **layer-wise fashion** followed by a generative fine-tuning procedure

  * Layer 1~4 : trained using standard **Contrastive Divergence** \[14\], 
  * top layer : trained using **Fast Persistent Contrastive Divergence \(FPCD\)** \[32\]. 

* Once the lower layer is learned, the weights are fixed and the hidden activations are fed into the next layer as input.

#### A. 파인 튜닝

* Our fine-tuning procedure is similar to **wake sleep algorithm** \[15\] except that we keep the weights tied.

  * **In the wake phase**, we propagate the data bottom-up and use the activations to collect the positive learning signal.  
  * **In the sleep phase**, we maintain a persistent chain on the topmost layer and propagate the data top-down to collect the negative learning signal.

* This fine-tuning procedure mimics the recognition and generation behavior of the model and works well in practice.

* Layer 1 사전 학습시 `During pre-training of the first layer, we collect learning signal only in receptive fields which are non-empty.`

  * Because of the nature of the data, empty spaces occupy a large proportion of the whole volume, which have no information for the RBM and would distract the learning.

* Our experiment shows that ignoring those learning signals during gradient computation results in our model learning more meaningful filters.

* 추가적으로 **Layer 1**에는 `sparsity regularization`을 추가 하여 작은 값을 유지 하도록 하였다. `In addition, for the first layer, we also add sparsity regularization to restrict the mean activation of the hidden units to be a small constant \(following the method of \[20\]\).`

* topmost RBM 사전 학습시 Laber과 고수준 abstractions 들이 학습 된다. laber은 중요 하므로 10번 복제 하여 significance를 증가 시겼다. `During pre-training of the topmost RBM where the joint distribution of labels and high-level abstractions are learned, we duplicate the label units 10 times to increase their significance.`


---
```
The resulting representation is a 3D binary voxel grid, which is the input to a CNN with 3D filter banks.
```

```
[26] propose a generative 3D convolutional model of shape and apply it to RGBD object recognition, among other tasks.
```

```
3D shapes were provided as input (a 3D voxel grid where each voxel was a binary variable indicating whether it belonged to the 3D shape or it was empty space), while the DBN model was employed.

In order to diminish the huge number of parameters required from feeding a fully connected DBN with a 3D voxel volume of normal resolution, convolution with 3D filters was applied.

Most specifically, a Convolutional Deep Belief Network (CDBN) with five layers (three convolutional, one fully connected, and one output layer) was proposed.
The model was initially pretrained layerwise and afterward, fine-tuned by backpropagation.

Standard contrastive divergence was used for training the first four layers, but the more sophis-ticated Fast Persistent Contrastive Divergence (FPCD) was employed for training the top layer.

The proposed framework was tested on the tasks of 3D shape classification and retrieval, next-best view prediction, and view-based 2.5D recognition outperform-ing other state-of-the-art methods.
```


```
Seminal work by Wu et al. [33] propose volumetric CNN architectures on volumetric grids for object classification and retrieval.
```

```
Wu et al. [33] lift 2.5D to 3D with their 3D ShapeNets approach by categorizing each voxel as free space, surface or occluded, depending on whether it is in front of, on, or behind the visible surface (i.e., the depth value) from the depth map.+

The resulting representation is a 3D binary voxel grid, which is the input to a CNN with 3D filter banks.

Their method is particularly relevant in the context of this work, as they are the first to apply CNNs on a 3D representation.
```

```
The advantage of these approaches is that it can process different sources of 3D data, including LiDAR point clouds, RGB-D point clouds, and CAD models; we likewise follow this direction. [중요] 3DShapeNets & VoxNet = LiDAR 데이터에도 적용할수 있다는 장점이 있다.
```

```
With the exception of the recent work of Wu et al. [37]
- which learns shape descriptors from the voxel-based representation of an object through 3D convolutional nets, 
```



```
Rather than modelling an object as a set of views with 2D features, an explicit 3D shape can be learned from reconstruction[37-PASCAL VOC] or provided by CAD models [39-ShapeNET], and subsequently matched to from depth images [13- Saurabh2014], 3D reconstructions [1],or partial reconstructions with shape completion [12, 39-ShapeNet].
```

```
Recently CNNs have been applied to 3D shapes by representing them as 3D occupancy grids, and building generative [39-ShapeNet]or discriminative [26-VoxNet] networks.
```

```
Volumetric CNNs: [28-ShapeNet, 17-VoxNet, 18-VMCNN] are the pioneers applying 3D convolutional neural networks on voxelized shapes. However, volumetric representation is constrained by its resolution due to data sparsity and computation cost of 3D convolution.
```

```
3D ShapeNets [14] is a Convolutional Deep Belief Network (CDBN) which represents a 3D shape as a 30 × 30 × 30 binary tensor in which a one indicates that a voxel intersects the mesh surface, and a zero represents empty space.
```


```
Volumetric representation in the form of binary voxels was shown by [27], to be useful for classification and retrieval of 3D models. They train their network generatively.

```

```
ShapeNets [29] introduced 3D deep learning for modeling 3D shapes, and demonstrated that powerful 3D features can be learned from a large amount of 3D data.
```




