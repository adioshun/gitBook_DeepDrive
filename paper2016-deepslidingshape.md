|논문명|Deep Sliding Shapes for Amodal 3D Object Detection in RGB-D Images
|-|-|
|저자(소속)|Shuran Song (Princeton)|
|학회/년도| CVPR 2016, [논문](http://dss.cs.princeton.edu/paper.pdf)|
|키워드|Detection, object retrieval분야, RPN+ORN |
|데이터셋/모델|NYUv2, SUN RGB-D |
|참고|[CVPR2016](https://www.youtube.com/watch?v=D-lDbS9NQ_0), [Youtube](https://www.youtube.com/watch?v=zzcipxzZP9E), [Homepage](http://dss.cs.princeton.edu/) |
|코드|[matlab](https://github.com/shurans/DeepSlidingShape)|

# Deep Sliding Shapes

목표 : amodal 3D object detection in RGB-D images
    - amodal : 완성된 물체가 아닌, Not Modal 
    
Deep Sliding Shapes, a 3D ConvNet    
- 입력 : 3D volumetric scene from a RGB-D image
- 출력 : 3D object bounding boxes
- 구성 
    - 3D Region Proposal Network (RPN) to learn objectness from geometric shapes
    - joint Object Recognition Network (ORN) to extract geometric features in 3D and color features in 2D
    
성능 : 기존 Sliding Shapes대비 13.8 in mAP and is 200x faster 

## 1. Introduction

We focus on the task of amodal 3D object detection in RGB-D images,
- which aims to produce an object’s 3D bounding box that gives real-world dimensions at the object’s full extent, regardless of truncation or occlusion

- However naively converting 2D detection results to 3D does not work well (see Table 3 and [10]).

###### sliding shapes

깊이 정보 활용을 위해 저자는 `sliding shapes`를 제안 하였으나 `hand-crafted` feature로 인해 제약이 있다. 
To make good use of the depth information, Sliding Shapes [25] was proposed to slide a 3D detection window in 3D space.
    - While it is limited by the use of `hand-crafted` features,

```
[25] S. Song and J. Xiao. Sliding Shapes for 3D object detection in depth images. In ECCV, 2014.
```

###### Depth RCNN 

Depth RCNN [10] takes a 2D approach: detect objects in the 2D image plane by treating depth as extra channels of a color image, then fit a 3D model to the points inside the 2D detected window by using ICP alignment.

```
[10] S. Gupta, P. A. Arbelaez, R. B. Girshick, and J. Malik. Aligning 3D models to RGB-D images of cluttered scenes. In CVPR, 2015
```


###### which representation is better for 3D amodal object detection, 2D or 3D? 

현재는 2D-Centric D-RCNN이 성능이 더 좋다. 하지만 이건 `2D representation`가 좋은게 아니라 2D Network 설계가 잘되어서 그런건 아닐까? `Currently, the 2D-centric Depth RCNN outperforms the 3D-centric Sliding Shapes. But perhaps Depth RCNN’s strength comes from using a well-designed deep network pre-trained with ImageNet, rather than its 2D representation.` 

향후 3D 모델이 잘 설계 되면 성능이 더 잘 나올수 있다. `Is it possible to obtain an elegant but even more powerful 3D formulation by also leveraging deep learning in 3D?`

---

![](https://i.imgur.com/7oMAaGv.png)

따라서, 본 논문에서는 we introduce Deep Sliding Shapes, a complete 3D formulation to learn object proposals and classifiers using 3D convolutional neural networks (ConvNets)

제안 1 : 3D Region Proposal Network (RPN) 
- RPN takes a 3D volumetric scene as input and outputs 3D object proposals (Figure 1).
- It is designed to generate amodal proposals for whole objects at two different scales for objects with different sizes

제안 2 : joint Object Recognition Network (ORN) 
- ORN to use a 2D ConvNet to extract image features from color, and a 3D ConvNet to extract geometric features from depth (Figure 2). 
- This network is also the first to regress 3D bounding boxes for objects directly from 3D proposals.

제안 방식은 3D의 정보를 Fully 이용하기 때문에 아래 `5가지 장점`이 있다. 

1. First, we can predict 3D bounding boxes without the extra step of fitting a model from extra CAD data. 
    - This elegantly simplifies the pipeline, accelerates the speed, and boosts the performance because the network can directly optimize for the final goal. 
    
2. Second, amodal proposal generation and recognition is very difficult in 2D, because of occlusion, limited field of view, and large size variation due to projection. 
    - But in 3D, because objects from the same category typically have similar physical sizes and the distraction from occluders falls outside the window, our 3D sliding-window proposal generation can support amodal detection naturally. 

3. Third, by representing shapes in 3D, our ConvNet can have a chance to learn meaningful 3D shape features in a better aligned space. 

4. Fourth, in the RPN, the receptive field is naturally represented in real world dimensions, which guides our architecture design. 

5. Finally, we can exploit simple 3D context priors by using the Manhattan world assumption to define bounding box orientations.

제안 방식이 3D를 이용하므로써 발생하는 `3가지 도전` 사항 및 해결책 

1. (계산 부하)First, a 3D volumetric representation requires much more memory and computation.
    - To address this issue, we propose to separate the 3D Region Proposal Network with a low-res whole scene as input, and the Object Recognition Network with high-res input for each object. 
    
2. Second, 3D physical object bounding boxes vary more in size than 2D pixel-based bounding boxes (due to photography and dataset bias) [16].
    - To address this issue, we propose a multi-scale Region Proposal Network that predicts proposals with different sizes using different receptive fields. 

3. (Missing Value)Third, although the geometric shapes from depth are very useful, their signal is usually lower in frequency than the texture signal in color images.
    - To address this issue, we propose a simple but principled way to jointly incorporate color information from the 2D image patch derived by projecting the 3D region proposal.

### 1.1. Related works

- 2D 이미지 분류관련 연구들 : RCNN [8], Fast RCNN [7], and Faster RCNN [18] 

- 2D amodal  이미지 분류관련 연구 : [14] further extended RCNN to estimate the amodal
box for the whole object

```
[14] A. Kar, S. Tulsiani, J. Carreira, and J. Malik. Amodal completion and size constancy in natural scenes. In ICCV, 2015
```

#### A. 2D Object Detector in RGB-D Images 

깊이 정보를 3rd 입력으로 사용 
2D object detection approaches for RGB-D images treat depth as extra channel(s) appended to the color images, using handcrafted features [9], sparse coding [2, 3], or recursive neural networks [23]. 

##### 가. Depth-RCNN 

Depth-RCNN [11, 10] is the first object detector using deep ConvNets on RGB-D images. 

They extend the RCNN framework [8-RCNN] for color-based object detection by encoding the depth map as three extra channels (with Geocentric Encoding: Disparity, Height, and Angle) appended to the color images. 

[10] extended Depth-RCNN to produce 3D bounding boxes by aligning 3D CAD models to the recognition results. 

[12] further improved the result by cross model supervision transfer. 


```
[11] S. Gupta, R. Girshick, P. Arbelaez, and J. Malik. Learning rich features from RGB-D images for object detection and segmentation. In ECCV, 2014.
[10] S. Gupta, P. A. Arbelaez, R. B. Girshick, and J. Malik. Aligning 3D models to RGB-D images of cluttered scenes. In CVPR, 2015.
[12] S. Gupta, J. Hoffman, and J. Malik. Cross modal distillation for supervision transfer. arXiv, 2015.
```

#### 나. 3D CAD model classification

For 3D CAD model classification, [26-MVCNN] and [20-DeepPano] took a view-based deep learning approach by rendering 3D shapes as 2D image(s).

```
[26-MVCNN] H. Su, S. Maji, E. Kalogerakis, and E. G. Learned-Miller.Multi-view convolutional neural networks for 3D shape recognition. In ICCV, 2015
[20] B. Shi, S. Bai, Z. Zhou, and X. Bai. DeepPano: Deep panoramic representation for 3-D shape recognition. Signal Processing Letters, 2015.
```

#### B. 3D Object Detector 

##### 가. Sliding Shapes 

Sliding Shapes [25] is a 3D object detector that runs sliding windows in 3D to directly classify each 3D window. 

However, the algorithm uses hand-crafted features and the algorithm uses many exemplar classifiers so it is very slow. 

```
[25] S. Song and J. Xiao. Sliding Shapes for 3D object detection in depth images. In ECCV, 2014.
```

##### 나. Clouds of Oriented Gradients feature

Recently, [32] also proposed the Clouds of Oriented Gradients feature on RGB-D images.

In this paper we hope to improve these hand-crafted feature representations with 3D ConvNets that can learn powerful 3D and color features from the data.

```
[32] R. Zhile and E. B. Sudderth. Three-dimensional object detection and layout prediction using clouds of oriented gradients. In CVPR, 2016.
```

#### C. 3D Feature Learning 

HMP3D [15] introduced a hierarchical sparse coding technique for unsupervised learning
features from RGB-D images and 3D point cloud data. 

The feature is trained on a synthetic CAD dataset, and tested on scene labeling task in RGB-D video. 

본 논문의 제안 방식과 비교 : In contrast, we desire a supervised way to learn 3D features using the deep learning techniques that are proven to be more effective for image-based feature learning

```
[15] K. Lai, L. Bo, and D. Fox. Unsupervised feature learning for 3d scene labeling. In ICRA, 2014.
```

#### D. 3D Deep Learning 3D 

ShapeNets [29] introduced 3D deep learning for modeling 3D shapes, and demonstrated
that powerful 3D features can be learned from a large amount of 3D data. 

```
[29] Z. Wu, S. Song, A. Khosla, F. Yu, L. Zhang, X. Tang, and J. Xiao. 3D ShapeNets: A deep representation for volumetric shapes. In CVPR, 2015.
```

Several recent works [17, 5, 31, 13] also extract deep learning features for retrieval and classification of CAD models. 

While these works are inspiring, none of them focuses on 3D object detection in RGB-D images.

```
[17] D. Maturana and S. Scherer. VoxNet: A 3D convolutional neural network for real-time object recognition. In IROS, 2015
[5] Y. Fang, J. Xie, G. Dai, M. Wang, F. Zhu, T. Xu, and E. Wong. 3D deep shape descriptor. In CVPR, 2015.
[31] J. Xie, Y. Fang, F. Zhu, and E. Wong. DeepShape: Deep learned shape descriptor for 3D shape matching and retrieval. In CVPR, 2015.
[13] H. Huang, E. Kalogerakis, and B. Marlin. Analysis and synthesis of 3D shape families via deep-learned generative models of surfaces. Computer Graphics Forum, 2015.
```



#### E. Region Proposal 

For 2D object proposals, previous approaches [27-SelectiveSearch, 1, 11] are mostly based on merging segmentation results. 

```
[11] S. Gupta, R. Girshick, P. Arbelaez, and J. Malik. Learning
rich features from RGB-D images for object detection and
segmentation. In ECCV, 2014.
```

Recently, Faster RCNN introduces a more efficient and effective ConvNet-based formulation, which inspires us to learn 3D objectness using ConvNets. 

For 3D object proposals, [4] introduces an MRF formulation with `hand-crafted` features for a few object categories in street scenes.

```
[4] X. Chen, K. Kunku, Y. Zhu, A. Berneshawi, H. Ma, S. Fidler, and R. Urtasun. 3d object proposals for accurate object class detection. In NIPS, 2015.
``` 

We desire to learn 3D objectness for general scenes from the data using ConvNets.

## 2. Encoding 3D Representation

> 3D공간을 어떻게 가공하여 ConvNet에 입력 하여야 할까?

- For color images, naturally the input is a 2D array of pixel color

- For depth maps, Depth RCNN [10, 11] proposed to encode `depth` as a 2D color image with three channels. 
    - Although it has the advantage to reuse the pretrained ConvNets for color images [12], 


본 논문의 방식 


- we desire a way to encode the geometric shapes naturally in 3D, preserving
spatial locality.

- compared to methods using hand-crafted 3D features [5, 31], We desire a representation that encodes the 3D geometry as raw as possible, and let ConvNets learn the most discriminative features from the raw data.


![](https://i.imgur.com/Piqj68M.png)

- To encode a 3D space for recognition, we propose to adopt a directional Truncated Signed Distance Function (TSDF). 

Given a 3D space, we divide it into an equally spaced 3D voxel grid. 

The value in each voxel is defined to be the shortest distance between the voxel center and the surface from the input depth map. 

To encode the direction of the surface point, instead of a single distance value, we propose a directional TSDF to store a three-dimensional vector [dx, dy, dz] in each voxel to record the distance in three directions to the closest surface point. 

The value is clipped by `2J`, where `J` is the grid size in each dimension. The sign of the value indicates whether the cell is in front of or behind the surface

To further speed up the TSDF computation, as an approximation, we can also use projective TSDF instead of accurate TSDF where the nearest point is found only on the
line of sight from the camera. 

The projective TSDF is faster to compute, but empirically worse in performance compared
to the accurate TSDF for recognition (see Table 2).

We also experiment with other encodings, and we find that the proposed directional TSDF outperforms all the other alternatives (see Table 2). 

Note that we can also encode colors in this 3D volumetric representation, by appending RGB values to each voxel [28].


