|논문명 | Multi-view Convolutional Neural Networks for 3D Shape Recognition |
| --- | --- |
| 저자\(소속\) | Hang Su \(\) |
| 학회/년도 | 2015, [논문](https://arxiv.org/abs/1505.00880) |
| 키워드 | Su2015, The Fisher vector + CNN feature, VGG |
| 데이터셋/모델 | modelnet40 |
| 참고 | [홈페이지](http://vis-www.cs.umass.edu/mvcnn/), [ppt](http://vis-www.cs.umass.edu/mvcnn/docs/1694_video.mp4), [Youtube](https://www.youtube.com/watch?v=QQbOy6J2PI0), [Youtube](https://youtu.be/8CenT_4HWyY?t=21m00s) |
| 코드 | [matlab](https://github.com/suhangpro/mvcnn), [Caffe](https://github.com/suhangpro/mvcnn/tree/master/caffe), [TF](https://github.com/WeiTang114/MVCNN-TensorFlow), [Torch](https://github.com/eriche2016/mvcnn.torch) |


# MVCNN

Representation of 3D shapes for recognition에 대한 학계의 오래된 질문
-  3D Shape는 native 3D formats인 Voxel grid로 표현 해야 할까? View-based로 표현 해야 할까? ` should 3D shapes be represented with descriptors operating on their native 3D formats, such as voxel grid or polygon mesh, or can they be effectively represented with view-based descriptors?`



## 1. Introduction

Native 3D formats인 Voxel grid를 사용 하는 방법이 ShapeNet을 통해 제안 되었다[37]. 

 View-based도 좋은 성능을 보인다. 실험 결과 여러 view로 학습후 하나의 이미지만 보여 줬어도 인식률이 7%나 증가 하였다. ` In particular, a convolutional neural network (CNN) trained on a fixed set of rendered views of a 3D shape and only provided with a single view at test time increases category recognition accuracy by a remarkable 8% (77% → 85%) over the best models [37-ShpaeNet] trained on 3D representations.`
- 이유 1 :  ??? (3D 의 resolution 문제)
- 이유 2 :  Adnavced image descriptor와 풍부한  Datasets 들을 사용할수 있다. 

```
[37] Z. Wu, S. Song, A. Khosla, F. Yu, L. Zhang, X. Tang, and J. Xiao. 3D ShapeNets: A deep representation for volumetric shape modeling. In Proc. CVPR, 2015.
```

## 2. Related Work

### 2.1 Shape descriptors

Shape descriptors can be classified into two broad categories
- 3D shape descriptors : directly work on the n**ative 3D representations** of objects, 
	- eg. polygon meshes, **voxel-based discretizations**, **point clouds**, or implicit surfaces
- viewbased descriptors : describe the shape of a 3D object by “**how it looks**” in a collection of 2D projections.


#### A. 3D shape descriptors

###### [3D ShapeNet]
With the exception of the recent work of Wu et al. [37] 
	- which learns shape descriptors from the voxel-based representation of an object through 3D convolutional nets,  


###### [기존 hand-designed]

> 이런게 있었다라는 참고만 

shapes can be represented with histograms or bag-of-features models constructed out of surface normals and curvatures [15], distances, angles,triangle areas or tetrahedra volumes gathered at sampledsurface points [25], 

properties of spherical functions defined in volumetric grids [16],

 local shape diameters measured at densely sampled surface points [4], 
heat kernel signatures on polygon meshes [2, 19], 

or extensions of the SIFT and SURF feature descriptors to 3D voxel grids [17]. 

###### [ Challenges ]

- 3D Shape를 이용한 분류 문제 처리의 challenges `Developing classifiers and other supervised machine learning algorithms on top of such 3D shape descriptors poses a number of challenges. `

- 데이터셋이 적다  First, the size of organized databases with annotated 3D models is rather limited compared to imagedatasets, e.g., ModelNet contains about 150K shapes (its 40category benchmark contains about 4K shapes). In contrast,the ImageNet database [9] already includes tens of millionsof annotated images. 

- 오버피팅 문제 : 3D데이터는 고차원이라 **차원의 저주**로 인해 오버피팅 발생  `Second, 3D shape descriptors tend to be very high-dimensional, making classifiers prone to over-fitting due to the so-called ‘curse of dimensionality’.`

#### B. view-based descriptors

위 Challenge에 비해 view-based 은 좋은 특징이 있따. 
- they are relatively low-dimensional, 
- efficient to evaluate, 
- robust to 3D shape representation artifacts, such as holes, imperfect polygon mesh tesselations,noisy surfaces. 
- The rendered shape views can also be directly compared with other 2D images, silhouettes or even hand-drawn sketches. 

###### [Murase and Nayar]

초반기 연구, An early example of a view-based approach is the work by Murase and Nayar [24] that recognizes objects by matching their appearance in parametric eigenspaces formed by large sets of 2D renderings of 3D models under varying poses and illuminations. 

```
[24] H. Murase and S. K. Nayar. Visual learning and recognition of 3-D objects from appearance. 14(1), 1995.
```

###### [Light Field descriptor]

많이 사용, Light Field descriptor [5] that extracts a set of geometric and Fourier descriptors from object silhouettes rendered from several different viewpoints. 

###### [shock graph]

Alternatively,the silhouette of an object can be decomposed into parts and then represented by a directed acyclic graph (shock graph)[23]. 

###### [Cyr and Kimia]

Cyr and Kimia [8] defined similarity metrics based on **curve matching** and **grouped similar views**, called aspect graphs of 3D models [18]. 

###### [Eitz et al/Schneider et al]

Eitz et al. [12] compared human sketches with line drawings of 3D models produced from several different views based on local Gabor filters, 

while Schneider et al. [30] proposed using Fisher vectors [26]on SIFT features [22] for representing human sketches of shapes. 

단점 : These descriptors are largely “**hand-engineered**”and some do **not generalize** well across different domains

#### C. Convolutional neural networks.

There has been existing work on recognizing 3D objects with CNNs [21] using two concatenated views (binocular images) as input. 
```
[21] Y. LeCun, F. Huang, and L. Bottou. Learning methods for generic object recognition with invariance to pose and lighting. In Proc. CVPR, 2004.
```

본 논문에서의 CNN과 기존과의 차별점 
- 입력으로 여러 views를 하고 출력 으로 shape descriptor 생성 
	- Our network instead learns a **shape representation** that aggregates information from any number of input views without any specific ordering, and always **outputs a compact shape descriptor** of the same size. 
- Train시 이미지와 Shpe dataset을 같이 사용 `Furthermore, we leverage both image and shape datasets to train our network.`

 In contrast our multi-view CNN architecture 
 - learns to recognize 3D shapes from views of the shapes using image-based CNNs but in the context of other views via a view-pooling layer. 
 - As a result, information from multiple views is effectively accumulated into a single, compact **shape descriptor**.

## 3. Method

view-based representations는 멀티뷰에서 부터 시작한다. `Our view-based representations start from multipleviews of a 3D shape, generated by a rendering engine. `

###### [A simple way]

간단한 멀티뷰를 이용하는 방법은 `A simple way to use multiple views is to`
- generate a 2D image descriptor per each view,
- then use the individual descriptors directly for recognition tasks based on some voting or alignment scheme. 

예 
- a **naıve approach** would be to average the individual descriptors, treating all the views as **equally important**. 
- 반대로, Alternatively, if the views are rendered in a **reproducible order**, one could also concatenate the 2D descriptors of all the views. 
	- Unfortunately,aligning a 3D shape to a canonical orientation is hard and sometimes ill-defined. 

###### [aggregated representation]

- In contrast to the above simple approaches, an aggregated representation combining features from multiple views is more desirable since it yields a single, compact descriptor representing the 3D shape.

- Our approach is to learn to combine information from multiple views using a unified CNN architecture that includes a view-pooling layer (Fig. 1). 

- All the parameters of our CNN architecture are learned discriminatively to produce a single compact descriptor for the 3D shape. 


###### [single view와의 비교 ]

Compared to exhaustive pairwise comparisons between single view representations of 3D shapes, our resulting descriptors can be directly used to compare 3D shapes leading to significantly higher computational efficiency.

### 3.1. Input: A Multi-view Representation

대부분의 인터넷 3D 모델들은  **polygon meshes**,로 저장되어 있다.  
	- polygon meshes :  collections of points connected with edges forming faces. 

#### A. 전처리 작업 

렌더링 이미지 생성을 위해 ** Phong reflection model **모델 사용 `To generate rendered views of polygon meshes, we use the Phong reflection model [27]. `

The mesh polygons are rendered under a perspective projection and the pixel color is determined by interpolating
the reflected intensity of the polygon vertices. 

Shapes are uniformly scaled to fit into the viewing volume.

#### B. 카메라 셋업 

To create a multi-view shape representation, we need to setup viewpoints (virtual cameras) for rendering each mesh.

We experimented with two camera setups. 

##### 가. For the 1st camera setup, 

물체가 upright oriented 상태라고 가정 :  12개의 이미지 생성 

```
- we assume that the input shapes are upright oriented along a consistent axis (e.g., z-axis). 
- Most models in modern online repositories, such as the 3D Warehouse, satisfy this requirement, and some previous recognition methods also follow the same assumption [37]. 
- In this case, we create 12 rendered views by placing 12 virtual cameras around the mesh every 30 degrees (see Fig. 1). 
- The cameras are elevated 30 degrees from the ground plane, pointing towards the centroid of the mesh. 
- The centroid is calculated as the weighted average of the mesh face centers, where the weights are the face areas. 
```

##### 나. For the 2nd camera setup,

물체가 upright oriented 상태라고 가정 **안함** :  20개의 이미지 생성 

```
- we do not make use of the assumption about consistent upright orientation of shapes. 
- In this case, we render from several more viewpoints since we do not know beforehand which ones yield good representative views of the object.
- The renderings are generated by placing 20 virtual cameras at the 20 vertices of an icosahedron enclosing the shape. 
- All cameras point towards the centroid of the mesh. 
- Then we generate 4 rendered views from each camera, using 0, 90, 180, 270 degrees rotation along the axis passing through the camera and the object centroid, yielding total 80 views.
```



### 3.2 Recognition with Multi-view Representations

In the first setting, we make use of existing 2D image features directly and produce a descriptor for each view. 

This is the most straightforward approach to utilize the multi-view representation. 

However, it results in multiple 2D image descriptors per 3D shape, one per view, which need to be integrated somehow for recognition tasks.

#### A. Image descriptors.

We consider two types of image descriptors for each 2D view: 
- a state-of-the-art “hand-crafted” image descriptor based on Fisher vectors [29] with multiscale SIFT, 
-  CNN activation features [10].

##### 가. The Fisher vector

The Fisher vector image descriptor is implemented using VLFeat [36]. 

For each image multi-scale SIFT descriptors are extracted densely. 

These are then projected to 80 dimensions with PCA, followed by Fisher vector pooling with a Gaussian mixture model with 64 components, square-root and `2 normalization.

##### 나. CNN features

For our CNN features we use the VGG-M network from [3] which consists of mainly 
- five convolutional layers $$conv_{1,...,5} $$ followed by 
- three fully connected layers $$fc_{6,...,8}$$ 
- softmax classification layer. 
- The penultimate(끝에서 두번째) layer fc7 (after ReLU non-linearity, 4096-dimensional) is used as image descriptor. 

- 이메지넷을 이용하여 사전 학습 됨/ 파인튜닝  `The network is pre-trained on ImageNet images from 1k categories, and then fine-tuned on all 2D views of the 3D shapes in training set. `


성능 평가 : Both **Fisher vectors** and **CNN features** yield very good performance in classification and retrieval compared with popular 3D shape descriptors (e.g., SPH [16], LFD [5]) as well as 3D ShapeNets [37].

#### B. Classification. 

We train **one-vs-rest linear SVMs**` (each view is treated as a separate training sample)` to classify shapes using their image features. 

테스트는 모든 12개 뷰에 대한 SVM결과값을 합쳐서 가장 값이 높은것 선택 `At test time, we simply sum up the SVM decision values over all 12 views and return the class with the highest sum. `


#### C. Retrieval. 

> A **distance** or **similarity measure** is required for retrieval tasks.

For shape x with $$n_x$$ image descriptors and shape $$y$$ with $$n_y$$ image descriptors, the distance between them is defined in `Eq. 1`. 

Note that the distance between two 2D images is defined as the $$l_2$$ distance between their feature vectors, ($$i.e. \parallel x_i - y_i \parallel_2 $$.

![](https://i.imgur.com/I4TmnBg.png)

To interpret this definition, we can first define the distance between a 2D image $$x_i$$ and a 3D shape $$y$$ as $$ d(x_i
, y) = min_j \parallel x_i - y_i \parallel_2$$. 

Then given all $$n_x$$ distances between x’s 2D projections and y, the distance between these two shapes is computed by simple averaging. 

In Eq. 1, this idea is applied in both directions to ensure symmetry.

We investigated alternative distance measures, such as minimun distance among all $$n_x · n_y$$ image pairs and the distance between average image descriptors, but they all led to inferior performance


### 3.3. Multi-view CNN: Learning to Aggregate Views

existing 3D descriptors보다 **multiple separate descriptors**를 이용하면 분류 문제는 잘 처리 할수 있지만, 불편하고 비 효율적이다. ` Although having multiple separate descriptors for each 3D shape can be successful for classification and retrieval compared to existing 3D descriptors, it can be inconvenient and inefficient in many cases. `
- 예를 들어 공식 1에서는 .... `For example, in Eq. 1, we need to compute all $$n_x \times n_y$$ pairwise distances between images in order to compute distance between two 3D shapes.`
- 그렇다고 간단히 평균을 내거나 합치는 작업은 성능 저하를 가져 온다. `Simply averaging or concatenating the image descriptors leads to inferior performance. `


본 장에서는 멀티뷰를 합치는 문제에 대하여 알아 보겠다.  In this section, we focus on the **problem of learning to aggregate multiple views** in order to synthesize the information from all views into a single, compact 3D shape descriptor.

![](https://i.imgur.com/PaExi1h.png)
```
[Figure 1. Multi-view CNN for 3D shape recognition (illustrated using the 1st camera setup)].
- At test time a 3D shape is rendered from 12 different views and are passed thorough CNN1 to extract view based features. 
- These are then pooled across views and passed through CNN2 to obtain a compact shape descriptor
```

We design the **multi-view CNN (MVCNN)** on top of image-based CNNs (Fig. 1). 

1. Each image in a 3D shape’s multi-view representation is passed through the first part of the network (CNN1) separately, 
2. aggregated at a view pooling layer, 
3. then sent through the remaining part of the network (CNN2). 

All branches in the first part of the network share the same parameters in CNN1. 

###### [view-pooling Layer]

- We use element-wise maximum operation across the views in the view-pooling layer. 

- 뷰-풀링 레이어는 아무 곳나 위치 해도 된다. `The view-pooling layer can be placed anywhere in the network.`
	- 하지만 실험 결과 최적 위치는 close to the last conv5 for optimal classification and retrieval performance. 

- 맥스 풀링/맥스 아웃 레이어와 연관이 깊다. `View-pooling layers are closely related to max-pooling layers and maxout layers[14], `
	-  단지 차이는 with the only difference being the dimension that their pooling operations are carried out on. 


###### [Train / Fine-tune]

The MVCNN is a directed acyclic graphs and can be trained or fine-tuned using **stochastic gradient descent** with back-propagation.

Using fc7 (after ReLU non-linearity) in an MVCNN as an aggregated shape descriptor, we achieve higher performance than using separate image descriptors from an image-based CNN directly, especially in retrieval (62.8%→ 70.1%). 

Perhaps more importantly, the aggregated descriptoris readily available for a variety of tasks, e.g., shape classification and retrieval, and offers significant speed-ups against multiple image descriptors.

An MVCNN can also be used as a general frame work to integrate perturbed image samples (also known as datajittering). 

We illustrate this capability of MVCNNs in the context of sketch recognition in Sect. 4.2.

###### [Low-rank Mahalanobis metric]

> 성능 향상 방법 

## 4. Experiments


## 5. Conclusion


---


```
Recently, CNN architectures have been extended to allow for recognition from image sequences using a single network,
by max pooling across all viewpoints [35-MVCNN],

단점 : However, both these methods assume that a fixed-length image sequence is provided during both training and testing, and hence are unsuitable for generalised multi-view recognition.

```

```
Current state-of-the-art uses multiple rendered views, and trains a CNN that can process all views jointly [32]. This multi-view CNN (MVCNN) is pre-trained on ImageNet [6] and uses view-point pooling to combine all streams obtained from each view.

```

```
Multiple views of a 3D object were also exploited in the work of Su et al. [2015] in order to build a compact shape descriptor for the tasks of 3D object classification and retrieval.

In order to obtain different views of the models, two setups were tested.
- The first setup included 12 rendered views of the 3D objects by placing an equal number of virtual cameras around them, while the second involved 80 views.

네트워크
- All the available views of an object passed through the first part of the network separately
- and then, elementwise max pooling was performed across all views in the view pooling layer.
- Finally, the aggregated result passed through the remaining network.

For retrieval, the penultimate seventh layer of the network (which is fully connected) was used as shape descriptor.

The employed network was pretrained using the ImageNet1K dataset and then, fine-tuned using the 3D dataset ModelNet40 [Wu et al. 2015] that was used in the experimental evaluation of the MVCNN architecture.

제안된 Shape descriptors(여러 2D)는 3D ShapeNets of Wu et al. [2015]보다 좋은 성능 보임

```

```
While these approaches achieve good results, it turns out that training a CNN on multiple 2D views achieves a significantly higher performance, as shown by Su et al. [32], who augment their 2D CNN with pre-training from ImageNet RGB data [Imagenet].

```

```
As of now however, CNNs with 2D view-based methods[35-MVCNN] have outperformed their counterpart 3D voxel-based methods [39-ShapeNet, 26-VoxNet], and we therefore adopt the 2D approach in our work.

```

```
Multiview CNNs: [23-MVCNN, 18-VMCNN] have tried to render 3D point cloud or shapes into 2D images and then apply 2D conv nets to classify them.+

With well engineered image CNNs, this line of methods have achieved dominating performance on shape classification and retrieval tasks.
However, it’s nontrivial to extend them to scene understanding or other 3D tasks such as point classification and shape completion.

```



```
Multi-view CNN

There was a significant jump in classification and retrieval performance by simply using 2D projections of the 3D model and using networks pre-trained on ImageNet [4] for classification as shown by [24].+

A part of this significant jump in performance is due to highly efficient and data independent features learned in the pre-training stage (on ImageNet data), which generalize well to other 2D images.

```


```
Multi-View CNN (MV-CNN), introduced in [24] aggregates 2D projections of the polygon mesh using a standard VGG-M network

[24] where for each of the 20 views, the camera is rotated 0, 90, 180 and 270 degrees along the axis passing through the camera into the centroid of the object, giving 80 views per object. 

```


```
```


```
```