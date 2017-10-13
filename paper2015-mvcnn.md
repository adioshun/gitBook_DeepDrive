

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

An early example of a view-based approach is the work by Murase and Nayar [24] that recognizesobjects by matching their appearance in parametriceigenspaces formed by large sets of 2D renderings of 3Dmodels under varying poses and illuminations. 

Another example,which is particularly popular in computer graphicssetups, is the LightField descriptor [5] that extracts a set ofgeometric and Fourier descriptors from object silhouettesrendered from several different viewpoints. 

Alternatively,the silhouette of an object can be decomposed into parts andthen represented by a directed acyclic graph (shock graph)[23]. 

Cyr and Kimia [8] defined similarity metrics basedon curve matching and grouped similar views, called aspectgraphs of 3D models [18]. 

Eitz et al. [12] compared humansketches with line drawings of 3D models produced fromseveral different views based on local Gabor filters, whileSchneider et al. [30] proposed using Fisher vectors [26]on SIFT features [22] for representing human sketches ofshapes. 

These descriptors are largely “hand-engineered”and some do not generalize well across different domains
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzNzI2MjY2ODVdfQ==
-->