

|논문명 | Multi-view Convolutional Neural Networks for 3D Shape Recognition |
| --- | --- |
| 저자\(소속\) | Hang Su \(\) |
| 학회/년도 | 2015, [논문](https://arxiv.org/abs/1505.00880) |
| 키워드 | MVCNN2015, |
| 데이터셋/모델 | modelnet40 |
| 참고 | [홈페이지](http://vis-www.cs.umass.edu/mvcnn/), [ppt](http://vis-www.cs.umass.edu/mvcnn/docs/1694_video.mp4) |
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

###### [Light Field descriptor]

많이 사용, Light Field descriptor [5] that extracts a set of geometric and Fourier descriptors from object silhouettes rendered from several different viewpoints. 

###### [shock graph]

Alternatively,the silhouette of an object can be decomposed into parts and then represented by a directed acyclic graph (shock graph)[23]. 

###### [Cyr and Kimia]

Cyr and Kimia [8] defined similarity metrics based on **curve matching** and **grouped similar views**, called aspect graphs of 3D models [18]. 

###### [Eitz et al/Schneider et al]

Eitz et al. [12] compared humans ketches with line drawings of 3D models produced from several different views based on local Gabor filters, 

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

Our view-based representations start from multipleviews of a 3D shape, generated by a rendering engine. 

A simple way to use multiple views is to generate a 2D image descriptor per each view, and then use the individual descriptors directly for recognition tasks based on some voting or alignment scheme. 

For example, a naıve approach would be to average the individual descriptors, treating all the views as equally important. 

Alternatively, if the views are rendered in a reproducible order, one could also concatenate the 2D descriptors of all the views. 

Unfortunately,aligning a 3D shape to a canonical orientation is hard and sometimes ill-defined. 

In contrast to the above simple approaches,an aggregated representation combining featuresfrom multiple views is more desirable since it yields a single,compact descriptor representing the 3D shape.Our approach is to learn to combine information frommultiple views using a unified CNN architecture that includesa view-pooling layer (Fig. 1). 

All the parameters ofour CNN architecture are learned discriminatively to producea single compact descriptor for the 3D shape. 

Comparedto exhaustive pairwise comparisons between singleviewrepresentations of 3D shapes, our resulting descriptorscan be directly used to compare 3D shapes leading to significantlyhigher computational efficiency.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTE3Njc4Mjg2OF19
-->