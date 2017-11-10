| 논문명 | 3D Deep Shape Descriptor |
| --- | --- |
| 저자\(소속\) | Yi Fang \( New York University\) |
| 학회/년도 | IEEE 2015, [논문](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7298845) |
| 키워드 | Yi20155, |
| 데이터셋/모델 | SHREC’10 ShapeGoogle and McGill 3D benchmark datasets |
| 참고 |  |
| 코드 |  |

# 3D Deep Shape Descriptor

논문 산출물

* we developed geometrically informative shape descriptor 
* new methods of defining **Eigen-shape descriptor** and **Fisher-shape descriptor**
  to guide the training of a deep neural network.

제안된 SD의 특징 :  Our deep shape descriptor tends to maximize the inter-class margin  
while minimize the intra-class variance

## 1. Introduction

### 1.1 Background

SD 정의 : Shape descriptor refers to an informative description that provides a 3D object with an identification as a member of some category.

좋은 3SD의 요구 사항 `3D shape descriptor poses several technical challenges,Therefore, effective solutions must be able to address the following issues.`

1. The high data complexity of 3D models \[36, 8, 46, 9\].

   * 3D geometric data is often featured as a highly complex and abstract representation for an object and with severe loss of critical descriptive information such as color, texture and appearance \[6\] to some extent.
   * The high data complexity in 3D model representation therefore presents great challenges in the development of a concise but geometrically informative description for efficient and real-time 3D shape analysis.

2. The structural variations present in 3D models \[8, 46,17\].

   * Many 3D objects contain dynamical units with their shape flexibility and variations play an essential role in certain types of functional processes. 
   * Therefore, the geometric structures of 3D models are often compounded by highly variable complexity causing large structural variations. 
   * For instance, 3D human models are dynamical units with different poses, and 3D protein models are functional units with their 3D shape flexibility playing an essential role in a variety of biological processes.

3. Noise, incompleteness, and occlusions, etc \[17, 16\].

   * 3D data are often noisy and incomplete after acquisition and meshing \[36, 6\]. 
   * A 3D model is composed of an unorganized sets of polygons that form “polygonsoups”. 
   * As stated in \[36\], a 3D model often contains missing, wrongly oriented, intersecting, disjoint,and /or overlapping polygons. 
   * For example, the classic model Utah teapot is missing its bottom and rim, and the Stanford Bunny has several holes along its base.

### 1.2 Related Works

위에서 언급한 3가지 사항에 대한 관련 연구들. 두가지 접근 방법으로 분류 가능  
1. develop better 3D shape signature and descriptor  
2. develop methods to automatically learn the 3D features

#### A. 3D shape signatures and descriptors

* 정의 : 3D shape **signature** and **descriptor** are succinct and compact** representations** of 3D object that capture the geometric essence of a 3D object\[19\]. 

> shape signature\(SS\) : a local description for a point on a 3D surface  
> shape descriptor\(SD\) :a global description for the entire shape.

```
[19] R. Gal, A. Shamir, and D. Cohen-Or. Pose-oblivious shape signature. IEEE Transcations on Visualization and Computer Graphics, 13:261–271, 2007.
```

* **heat diffusion**에 기반한 SS와 SD가 3D를 표현하는데 효과적이다. `Shape signatures and descriptors, which are based on heat diffusion, have been proved to be very effective in capturing the geometric essence of 3D shapes.`

* **heat diffusion**에 기반하지 않는 SS/SD도 많이 제안 되었다. `On the other hand, a large amount of non-diffusion based shape features are also proposed in the literature`,

  * D2 shape distribution \[36\]
  * statistical moments \[15\]
  * Fourier descriptor\[49, 42\]
  * Light Field Descriptor \[10\]
  * Eigenvalue Descriptor\[25\], etc. 

* 최근 연구는 **diffusion **에 기반한것들이 대부분 이다. `Recent efforts on robust 3D shape feature development are mainly based on diffusion [45, 9, 41, 37].`

##### 가. global point signature \(GPS\)\[41\]

* The global point signature \(GPS\)\[41\] uses `eigen value`s and `eigen functions` of the `Laplace-Beltrami` defined on a 3D surface to characterize points. 

##### 나. Heat kernel signature \(HKS\) and wave kernel signature \(WKS\)

* Heat kernel signature \(HKS\) and wave kernel signature \(WKS\) \[2, ?\] have gained attention because of their multi-scale property and invariance toisometric deformations. 

> 단점 : GPS, HKS, WKS = point-based shape signatures -&gt; **do not provide a global description** of the entire shape.

##### 다. temperature distribution\(TD\)

* **A global shape descriptor**, named TD descriptor, is developed based on HKS information at a single scale \[17\] to represent the entire shape.

* 제약 : it only describes the entire shape at one single scale resulting in an incomplete description of 3D objects \[17\].

* As indicated in \[17\] the selection of an appropriate scale is often not straightforward.

```
[17] Y. Fang, M. Sun, and K. Ramani. Temperature distribution descriptor for robust 3d shape retrieval. pages 9–16, June 2011.
```

#### B. Feature learning

* 직접 만든 SD들은 강건성이 부족하다. `Hand-crafted shape descriptors are often not robust enough to deal with structural variations present in 3D models.`

* 데이터에서 Feature를 배우는 방식이 이러한 문제를 해결 할수 있다. `Discriminative feature learning from large datasets provides an alternative way to construct deformation-invariant features.`

##### 가. BOF

* The bag-of-features \(BOF\) method is used to extract a frequency histogram of geometric words for shape retrieval in previous works \[13, 14, 22\].

* However, when performing k-means clustering method, the coding vector on the visual word has only nonzero entry \(i.e., 1\) to indicate the cluster label.

* 문제점 : Due to the restrictive constraint, the learned ball-like clusters may not accurately characterize the intricate feature space of shapes with large variations.

* In addition, as a holistic structure representation, BOF does not contain local structural information \[51\], so that this method does not perform well in discriminating structural variations among shapes from different classes.

##### 나. supervised BOF

* Beyond the regular BOF approach,Litiman et al. \[31\] propose a supervised BOF method to learn shape descriptors for shape retrieval. 

##### 다. Auto-encoder / CNN / 볼츠만 머신

* 많은 딥러닝 기반 연구들도 제안 되었다. `Recently, deep models like deep auto-encoder [5, 48, 39], convolutional neural network [38, 29, 26], restricted Boltzmann machine[21, 33, 34] and their variants are widely used in computer vision applications.`

* 이미지/비디어오에서는 딥러닝이 성공적이지만, 3D 분야에서는 많은 연구가 이루어 지지 않았다.

  * Despite the success of deeplearning as a technique for feature learning in images and videos \[3, 32, 52, 50\], 
  * very few techniques based on deeplearning have been developed for learning 3D shape features. 

##### 라. Zhu et al. \[53\]

* Zhu et al. \[53\] attempt to learn a 3D shape representation by projecting a 3D shape into many 2D views and then perform training on the projected 2D shapes.

* 특징 : 2D 이미지용 방식을 적용 `The shape representation developed in [53] is essentially based on 2D image feature learning.`

  * This does not result in a concise shape descriptor that can represent the 3D shape well.

* 단점들 It has the following shortcomings:  
  1. a collection of 2Dprojection images is not a concise form to represent a 3Dshape as it increases the size of the data,  
  2. a collection of 2D projection images is not geometrically informative as it does not capture the underlying geometric essence of a 3D object.

  * For instance it is very sensitive to isometric geometrictrans formation, 
    1. Projected 2D shapes are basically 2D contour representation of 3D shapes. 

They do not include critical descriptive information such as color, texture and appearance.

Therefore, the rationale of learning 3D shape representation from 2D contours needs to be further justified.

```
[53] Z. Zhu, X. Wang, S. Bai, C. Yao, and X. Bai. Deep learning representation using autoencoder for 3d shape retrieval. CoRR, abs/1409.7164, 2014.
```

> Gitboot 정리 : [Paper\_2015\_DL Representation]()

### 1.3 Our solution: 3D Deep Shape Descriptor

#### A. Deep SD제안

* 딥러닝을 이용하여 descriptor\(Deep SD\)을 학습 하는 방법 제안 `we have developed techniques for learning a deep shape descriptor (DeepSD) based on the use of a deep neural network.`

* Specifically, we have developed

  * 1\) **heat shape descriptor** \(HeatSD\) based on point based **heat kernel signature** \(HKS\) 
  * 2\) new definitions of **Eigen-shape descriptor** \(ESD\) and **Fisher-shape descriptor** \(ESD\) to guide the training of deep neural network.

> Heat kernel signature has been widely used for 3D shape analysis \[45\].

* 제안 DeepSD의 목표 : Our deep shape descriptor has high discriminative power

  * maximizes the inter-class margin / minimizing the intra-class variance. 

* 제안 방식은 2D에도 적용 가능

```
[45] J. Sun, M. Ovsjanikov, and L. Guibas. A concise and provably informative multi-scale signature based on heat diffusion. In Computer graphics forum, volume 28, pages 1383–1392. Wiley Online Library, 2009.
```

#### B. Pipeline

![](https://i.imgur.com/enAhZSu.png)

Given input shapes, three steps are included along with the pipeline:

1. Heat kernel signatures are extracted for each shape in the database. 
   * Heat shape descriptor are computed based on HKS.
2. Heat shape descriptors are fed into two deep neural networks with target values using ESD and FSD, respectively. 
3. The deep shape descriptor is formed by concatenating nodes in hidden layer \(circled by yellow dash lines\).

#### C. 4가지 구성 요소 \(Input Shape, Shape Features,Deep Learning, and Target\)

![](https://i.imgur.com/Nel3wPu.png)

1. 3D shape database :large volume of shapes are stored. 
2. shape feature extraction : two features are extracted. 
   * heat kernel signature \(HKS\) 
   * heat shape descriptor \(HeatSD\)
3. deep neural network for learning deep shape descriptor. 
   * A collection of HeatSDs are used in the training of PCA and LDA`(linear discriminant analysis)` to generate the **Eigen-shape descriptor** \(FSD\) and **Fisher-shape descriptor**\(ESD\) respectively. 
4. The fourth component is the target value of Deep Neural Network \(DNN\) where pre-computed ESD and FSD are used as target values in the training the DNN. 

In the pipeline, there are two communication routes,indicated by orange and blue arrows.

* blue : for the training of the DNN model, where training data from 3D shape database are used as input.
* orange : for the testing data.

After training, the deep encoder is used to construct deep shape descriptor.

Features in the middle hidden layers are extracted as deep shape descriptor for representing the 3D shape.

## 2. Method

### 2.1 Shape Feature Extraction

#### A. Heat Kernel Signature

> Heat kernel signature has been widely used for 3D shape analysis \[45\].

#### B. Heat shape descriptor

> To describe the entire shape, we develop a multi-scale shape descriptor based on HKS.

### 2.2 Deep shape descriptor

* hand-crafted SD가 강건성을 가지기란 쉽지 않다. 다행히 빅데이터와 연산력의 향상으로 insensitive할수 있게 되었따. `It is challenging to find hand-crafted shape descriptors that are robust to large structural variations. Fortunately,the large volume of data and powerful computational resourcesmake it possible to learn a deep shape descriptorthat is insensitive to structural variations.`

As illustrated inFigure 2, four components, Input Shape, Shape Features,Deep Learning, and Target are included in the process of learning a deep shape descriptor.

We will explain two components related to training DNN: Deep learning and Target.

Since one of the contributions in this project is the development of **Eigen-shape descriptor \(ESD\)** and **Fisher-shapedescriptor \(FSD\)** to guide the training of DNN in order to maximize inter-class margin while minimizing intra-classvariance,

we will first explain the target component and then explain the deep learning component.

#### A. Target values

The target of the our proposed DNN is ESD or FSD.

![](https://i.imgur.com/Fc8ohbd.png)  
Figure 4: Pipeline of generating Eigen-shape descriptor and Fisher-shape descriptor.

* **Eigen-shape descriptors**\(on the right column\): are computed by training a **principle component analysis \(PCA\)** model on a set of pre-computed `HeatSD` obtained from each group \(in middle column\).

* **Fisher-shape descriptors** \(on the left column\): are computed by training a **linear discriminative analysis \(LDA\)** model on a set of pre-computed `HeatSDs` obtained from each group.

Separate **Eigen-shape descriptors** and **Fishershape descriptors** are trained for each group.

The DNN will force the mapping of HeatSDs from the same groupto their assigned ESD or FSD \(the mapping process will be explained below\).

![](https://i.imgur.com/kWoqxI3.png)

#### B. Deep Learning

* We use the architecture of a **many-to one encoder** neural network to develop our encoder for deepshape descriptor \[4, 20\].

* A many-to-one encoder forces the inputs from the same class to be mapped to a unique target value, which is different from the original auto-encoder that sets the target value to be identical to the input.

* By enforcing the target value to be unique for input HeatSDs from the same group but with structural variations, the deep shape descriptor represented by the neurons in the hidden layer is invariant to within-group structural variations but will discriminate against other groups.

* We developed a new training method by setting target value as pre-computed Eigen shape descriptor and Fisher-shape descriptor for each group as described earlier.

* This new training strategy will increase the discriminative power of deep shape descriptor by maximizinginter-class margin and minimizing intra-class variance.

To avoid over-fitting, we impose the $$l_2$$ norm constrainton the weights of the many-to-one encoder neuralnetwork.

We formulate the objective function of the proposed sparse many-to-one encoder by the square-loss function with sparse constraint on the weights as:

![](https://i.imgur.com/iU9M8dg.png)

* $$L$$ : the number of layers in the deep neural network,
* $$W$$ : the weight matrix of the multiple-hidden-layer neural network
* $$b$$ : the bias matrix of the neural network,
* $$x_i^j$$: the j-th training sample from the i-th group
* $$h(x_i^j, W, b)$$: a non-linear mapping from the input $$x_i^j$$ to the output
* $$ \lambda$$ : the weight of the regularizer
* $$Y_i$$ : the target value for the i-th group. 

For each group of shapes, two encoders will be trained:

* one is trained by setting the target value $$Y_i$$ as the `i-th` ESD
* the other is trained by setting the target value $$Y_i$$ as the `i-th` FSD \(see Figure 4\). 

Because we impose that the target value be unique for all input HeatSDs from the same group, the deep shape descriptor extracted from hidden layer will be  
insensitive to intra-class structural variations.

At the same time, because of discriminative power of target values \(either ESD or FSD\), the deep shape descriptor will be discriminative with a large inter-class margin.

## 3. Experiments



