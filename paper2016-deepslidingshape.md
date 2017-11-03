| 논문명 | Deep Sliding Shapes for Amodal 3D Object Detection in RGB-D Images |
| --- | --- |
| 저자\(소속\) | Shuran Song \(Princeton\) |
| 학회/년도 | CVPR 2016, [논문](http://dss.cs.princeton.edu/paper.pdf) |
| 키워드 | Song2016, Detection\(가려진 물체 탐지\),  RPN+ORN, TSDF Representation, Raw 3D 이용, |
| 데이터셋/모델 | NYUv2, SUN RGB-D / ~~ORN의 2D Network = VGGnet pre-trained on ImageNet~~ |
| 참고 | [CVPR2016](https://www.youtube.com/watch?v=D-lDbS9NQ_0), [Youtube](https://www.youtube.com/watch?v=zzcipxzZP9E), [Homepage](http://dss.cs.princeton.edu/) |
| 코드 | [matlab](https://github.com/shurans/DeepSlidingShape) |

# Deep Sliding Shapes

목표 : amodal 3D object detection in RGB-D images

* amodal : 완성된 물체가 아닌, Not Modal 

Deep Sliding Shapes, a 3D ConvNet

* 입력 : 3D volumetric scene from a RGB-D image
* 출력 : 3D object bounding boxes
* 구성 
  * 3D Region Proposal Network \(RPN\) to learn objectness from geometric shapes
  * joint Object Recognition Network \(ORN\) to extract geometric features in 3D and color features in 2D

성능 : 기존 Sliding Shapes대비 13.8 in mAP and is 200x faster

## 1. Introduction

We focus on the task of amodal 3D object detection in RGB-D images,

* which aims to produce an object’s 3D bounding box that gives real-world dimensions at the object’s full extent, regardless of truncation or occlusion

* However naively converting 2D detection results to 3D does not work well \(see Table 3 and \[10\]\).

###### \[sliding shapes\]

깊이 정보 활용을 위해 저자는 `sliding shapes`를 제안 하였으나 `hand-crafted` feature로 인해 제약이 있다.   
To make good use of the depth information, Sliding Shapes \[25\] was proposed to slide a 3D detection window in 3D space.

* While it is limited by the use of `hand-crafted` features,

```
[25] S. Song and J. Xiao. Sliding Shapes for 3D object detection in depth images. In ECCV, 2014.
```

###### \[Depth RCNN \]

Depth RCNN \[10\] takes a 2D approach: detect objects in the 2D image plane by treating depth as extra channels of a color image, then fit a 3D model to the points inside the 2D detected window by using ICP alignment.

```
[10] S. Gupta, P. A. Arbelaez, R. B. Girshick, and J. Malik. Aligning 3D models to RGB-D images of cluttered scenes. In CVPR, 2015
```

###### \[which representation is better for 3D amodal object detection, 2D or 3D?\]

현재는 2D-Centric D-RCNN이 성능이 더 좋다. 하지만 이건 `2D representation`가 좋은게 아니라 2D Network 설계가 잘되어서 그런건 아닐까? `Currently, the 2D-centric Depth RCNN outperforms the 3D-centric Sliding Shapes. But perhaps Depth RCNN’s strength comes from using a well-designed deep network pre-trained with ImageNet, rather than its 2D representation.`

향후 3D 모델이 잘 설계 되면 성능이 더 잘 나올수 있다. `Is it possible to obtain an elegant but even more powerful 3D formulation by also leveraging deep learning in 3D?`

---

* 따라서, 본 논문에서는 we introduce **Deep Sliding Shapes**, 
  * a complete 3D formulation to learn **object proposals** and **classifiers** using 3D convolutional neural networks \(ConvNets\)

![](https://i.imgur.com/ov9Wu0a.png)

```
[Figure 1. 3D Amodal Region Proposal Network:]
- Taking a 3D volume from depth as input, 
- our fully convolutional 3D network extracts 3D proposals at two scales with different receptive fields.
```

제안 1 : 3D Region Proposal Network \(RPN\)

* RPN takes a 3D volumetric scene as input and outputs 3D object proposals \(Figure 1\).
* It is designed to generate amodal proposals for whole objects at two different scales for objects with different sizes

![](https://i.imgur.com/iopicsj.png)

```
[Figure 2. Joint Object Recognition Network:]
- For each 3D proposal, we feed the 3D volume from depth to a 3D ConvNet, and 
- feed the 2D color patch (2D projection of the 3D proposal) to a 2D ConvNet, to jointly learn object category and 3D box regression.
```

제안 2 : joint Object Recognition Network \(ORN\)

* ORN to use a 2D ConvNet to extract image features from color, and a 3D ConvNet to extract geometric features from depth \(Figure 2\). 
* This network is also the first to regress 3D bounding boxes for objects directly from 3D proposals.

###### \[제안 방식은 3D의 정보를 Fully 이용하기 때문에 아래 5가지 장점이 있다. \]

1. First, we can predict 3D bounding boxes without the extra step of fitting a model from extra CAD data.

   * This elegantly simplifies the pipeline, accelerates the speed, and boosts the performance because the network can directly optimize for the final goal. 

2. Second, amodal proposal generation and recognition is very difficult in 2D, because of occlusion, limited field of view, and large size variation due to projection.

   * But in 3D, because objects from the same category typically have similar physical sizes and the distraction from occluders falls outside the window, our 3D sliding-window proposal generation can support amodal detection naturally. 

3. Third, by representing shapes in 3D, our ConvNet can have a chance to learn meaningful 3D shape features in a better aligned space.

4. Fourth, in the RPN, the receptive field is naturally represented in real world dimensions, which guides our architecture design.

5. Finally, we can exploit simple 3D context priors by using the Manhattan world assumption to define bounding box orientations.

###### \[제안 방식이 3D를 이용하므로써 발생하는 3가지 도전 사항 및 해결책 \]

1. \(계산 부하\)First, a 3D volumetric representation requires much more memory and computation.

   * To address this issue, we propose to separate the 3D Region Proposal Network with a low-res whole scene as input, and the Object Recognition Network with high-res input for each object. 

2. Second, 3D physical object bounding boxes vary more in size than 2D pixel-based bounding boxes \(due to photography and dataset bias\) \[16\].

   * To address this issue, we propose a multi-scale Region Proposal Network that predicts proposals with different sizes using different receptive fields. 

3. \(Missing Value\)Third, although the geometric shapes from depth are very useful, their signal is usually lower in frequency than the texture signal in color images.

   * To address this issue, we propose a simple but principled way to jointly incorporate color information from the 2D image patch derived by projecting the 3D region proposal.

### 1.1. Related works

* 2D 이미지 분류관련 연구들 : RCNN \[8\], Fast RCNN \[7\], and Faster RCNN \[18\]

* 2D amodal  이미지 분류관련 연구 : \[14\] further extended RCNN to estimate the amodal  
  box for the whole object

```
[14] A. Kar, S. Tulsiani, J. Carreira, and J. Malik. Amodal completion and size constancy in natural scenes. In ICCV, 2015
```

#### A. 2D Object Detector in RGB-D Images

깊이 정보를 3rd 입력으로 사용   
2D object detection approaches for RGB-D images treat depth as extra channel\(s\) appended to the color images, using handcrafted features \[9\], sparse coding \[2, 3\], or recursive neural networks \[23\].

##### 가. Depth-RCNN

Depth-RCNN \[11, 10\] is the first object detector using deep ConvNets on RGB-D images.

They extend the RCNN framework \[8-RCNN\] for color-based object detection by encoding the depth map as three extra channels \(with Geocentric Encoding: Disparity, Height, and Angle\) appended to the color images.

\[10\] extended Depth-RCNN to produce 3D bounding boxes by aligning 3D CAD models to the recognition results.

\[12\] further improved the result by cross model supervision transfer.

```
[11] S. Gupta, R. Girshick, P. Arbelaez, and J. Malik. Learning rich features from RGB-D images for object detection and segmentation. In ECCV, 2014.
[10] S. Gupta, P. A. Arbelaez, R. B. Girshick, and J. Malik. Aligning 3D models to RGB-D images of cluttered scenes. In CVPR, 2015.
[12] S. Gupta, J. Hoffman, and J. Malik. Cross modal distillation for supervision transfer. arXiv, 2015.
```

#### 나. 3D CAD model classification

For 3D CAD model classification, \[26-MVCNN\] and \[20-DeepPano\] took a view-based deep learning approach by rendering 3D shapes as 2D image\(s\).

```
[26-MVCNN] H. Su, S. Maji, E. Kalogerakis, and E. G. Learned-Miller.Multi-view convolutional neural networks for 3D shape recognition. In ICCV, 2015
[20] B. Shi, S. Bai, Z. Zhou, and X. Bai. DeepPano: Deep panoramic representation for 3-D shape recognition. Signal Processing Letters, 2015.
```

#### B. 3D Object Detector

##### 가. Sliding Shapes

Sliding Shapes \[25\] is a 3D object detector that runs sliding windows in 3D to directly classify each 3D window.

However, the algorithm uses hand-crafted features and the algorithm uses many exemplar classifiers so it is very slow.

```
[25] S. Song and J. Xiao. Sliding Shapes for 3D object detection in depth images. In ECCV, 2014.
```

##### 나. Clouds of Oriented Gradients feature

Recently, \[32\] also proposed the Clouds of Oriented Gradients feature on RGB-D images.

In this paper we hope to improve these hand-crafted feature representations with 3D ConvNets that can learn powerful 3D and color features from the data.

```
[32] R. Zhile and E. B. Sudderth. Three-dimensional object detection and layout prediction using clouds of oriented gradients. In CVPR, 2016.
```

#### C. 3D Feature Learning

HMP3D \[15\] introduced a hierarchical sparse coding technique for unsupervised learning  
features from RGB-D images and 3D point cloud data.

The feature is trained on a synthetic CAD dataset, and tested on scene labeling task in RGB-D video.

본 논문의 제안 방식과 비교 : In contrast, we desire a supervised way to learn 3D features using the deep learning techniques that are proven to be more effective for image-based feature learning

```
[15] K. Lai, L. Bo, and D. Fox. Unsupervised feature learning for 3d scene labeling. In ICRA, 2014.
```

#### D. 3D Deep Learning 3D

ShapeNets \[29\] introduced 3D deep learning for modeling 3D shapes, and demonstrated  
that powerful 3D features can be learned from a large amount of 3D data.

```
[29] Z. Wu, S. Song, A. Khosla, F. Yu, L. Zhang, X. Tang, and J. Xiao. 3D ShapeNets: A deep representation for volumetric shapes. In CVPR, 2015.
```

Several recent works \[17, 5, 31, 13\] also extract deep learning features for retrieval and classification of CAD models.

While these works are inspiring, none of them focuses on 3D object detection in RGB-D images.

```
[17] D. Maturana and S. Scherer. VoxNet: A 3D convolutional neural network for real-time object recognition. In IROS, 2015
[5] Y. Fang, J. Xie, G. Dai, M. Wang, F. Zhu, T. Xu, and E. Wong. 3D deep shape descriptor. In CVPR, 2015.
[31] J. Xie, Y. Fang, F. Zhu, and E. Wong. DeepShape: Deep learned shape descriptor for 3D shape matching and retrieval. In CVPR, 2015.
[13] H. Huang, E. Kalogerakis, and B. Marlin. Analysis and synthesis of 3D shape families via deep-learned generative models of surfaces. Computer Graphics Forum, 2015.
```

#### E. Region Proposal

For 2D object proposals, previous approaches \[27-SelectiveSearch, 1, 11\] are mostly based on merging segmentation results.

```
[11] S. Gupta, R. Girshick, P. Arbelaez, and J. Malik. Learning
rich features from RGB-D images for object detection and
segmentation. In ECCV, 2014.
```

Recently, Faster RCNN introduces a more efficient and effective ConvNet-based formulation, which inspires us to learn 3D objectness using ConvNets.

For 3D object proposals, \[4\] introduces an MRF formulation with `hand-crafted` features for a few object categories in street scenes.

```
[4] X. Chen, K. Kunku, Y. Zhu, A. Berneshawi, H. Ma, S. Fidler, and R. Urtasun. 3d object proposals for accurate object class detection. In NIPS, 2015.
```

We desire to learn 3D objectness for general scenes from the data using ConvNets.

## 2. Encoding 3D Representation

> 3D공간을 어떻게 가공하여 ConvNet에 입력 하여야 할까?

* 이미지는 간단하다. For color images, naturally the input is a 2D array of pixel color

* Depth Map의 경우 Depth RCNN은 이미지의 3rd 채널로 취급하는 법을 제안 하였다. . `For depth maps, Depth RCNN [10, 11] proposed to encode depth as a 2D color image with three channels.`

  * Although it has the advantage to reuse the pretrained ConvNets for color images \[12\], 

### 2.1 본 논문의 방식

* 가능한 3D 정보를 그대로`(naturally)` 사용 하기로 함, we desire a way to encode the geometric shapes naturally in 3D, preserving spatial locality.

* hand-crafted 3D features와 비교 하여 본 논문에서는 3D정보를 가능한 Raw한상태로 encode하고 Conv 특징을 학습 하도록 하였다. `We desire a representation that encodes the 3D geometry as raw as possible, and let ConvNets learn the most discriminative features from the raw data.`

![](https://i.imgur.com/Piqj68M.png)

* 3D encode을 위해 TSDF`(directional Truncated Signed Distance Function)`를 적용 `To encode a 3D space for recognition, we propose to adopt a TSDF.`

* Given a 3D space, we divide it into an equally spaced 3D voxel grid.

* The value in each voxel is defined to be the shortest distance between the voxel center and the surface from the input depth map.

* To encode the direction of the surface point, instead of a single distance value, we propose a directional TSDF to store a three-dimensional vector \[dx, dy, dz\] in each voxel to record the distance in three directions to the closest surface point.

* The value is clipped by `2J`,

  * `J` is the grid size in each dimension. 
  * The **sign** of the value indicates whether the cell is in **front of** or **behind** the surface

* TSDF 연산 성능 향상을 위해 projective TSDF사용 `To further speed up the TSDF computation, as an approximation, we can also use projective TSDF instead of accurate TSDF where the nearest point is found only on the line of sight from the camera.`

  * 빠르긴 하지만 성능은 안 좋음 `The projective TSDF is faster to compute, but empirically worse in performance compared to the accurate TSDF for recognition (see Table 2).`

* 다른 encodings방식들도 적용 했지만, TSDF 가 가장 좋았음 `We also experiment with other encodings, and we find that the proposed directional TSDF outperforms all the other alternatives (see Table 2).`

* Note that we can also encode colors in this 3D volumetric representation, by appending RGB values to each voxel \[28\].

## 3. Multi-scale 3D Region Proposal Network

## 4. Joint Amodal Object Recognition Network

* 주어진 3D 후보영역을 ORN에 입력으로 준다. `Given the 3D proposal boxes, we feed the 3D space within each box to the Object Recognition Network (ORN).`

* In this way, the final proposal feed to ORN could be the actual bounding box for the object, which allows the ORN to look at the full object to increase recognition performance, while still being computationally efficient.

* 후보 영역이 **amodal boxes**이므로 제안 방식은 가려진 물건이나 Missing 데이터에 좀더 invariant하다. `Furthermore, because our proposals are amodal boxes containing the whole objects at their full extent, the ORN can align objects in 3D meaningfully to be more invariant to occlusion or missing data for recognition.`

### 4.1 3D object recognition network

#### A. 전처리

* 주어진 후보 영역 크기의 12.5%정도를 추가로 pad하여 contextual information용 공간을 확보 한다. `For each proposal box, we pad the proposal bounding box by 12.5% of the sizes in each direction to encode some contextual information.`

* 다음, Space를 $$30 \tiems 30 \tiems 30$$ voxel grid로 나누고 TSDF를 이용하여 도형적 모양을 encode한다. `Then, we divide the space into a 30 x 30 x 30 voxel grid and use TSDF (Section 2) to encode the geometric shape of the object.`

#### B. 네트워크 구조

* All the **max pooling layers** are 23 with stride 2.

* For the **three convolution layers**, the window sizes are 53, 33, and 33, all with stride 1.

* Between the fully connected layers are **ReLU** and **dropout layers** \(dropout ratio 0.5\).

![](https://i.imgur.com/Ksz1CEG.png)

```
[Figure 5. 2D t-SNE embedding of the last layer features learned from the 3D ConvNet. Color encodes object category]
```

* Figure5 visualizes the 2D t-SNE embedding of 5,000 foreground volumes using their the last layer features learned from the3D ConvNet. 
  * Color encodes object category.

### 4.2 2D object recognition network

* 위에서 살펴본 3D network는 Color정보 없이 depth map만 사용한다. The 3D network only makes use of the depth map, but not the color.

* 물체 분류에서 색상 정보는 중요하며, 기존 네트워크 중 이미지 기반 물체 분류기를 사용하면 좋다. `For certain object categories, color is a very discriminative feature, and existing ConvNets provide very powerful features for image-based recognition that could be useful.`

* 3D proposal box들에 대하여 투영하여 2D box를 얻는다. `For each of the 3D proposal box, we project the 3D points inside the proposal box to 2D image plane, and get the 2D box that contains all these 2D point projections.`

* VGGnet을 이용하여 이미지에서 color features를 추출 하였다. We use the state-of the-art VGGnet \[22\] pre-trained on ImageNet \[19\] \(without fine-tuning\) to extract color features from the image.

* Fast RCNN의 ROI Pooling 레이어 이용하여  `We use a Region-of-Interest Pooling Layer from Fast RCNN[7]`

  * to uniformly sample 7x7 points from `conv5_3 laye`r using the 2D window with one more fully connected layer togenerate 4096-dimensional features as the feature from 2Dimages.

* Color정보를 3D voxel에 encode하는 방법을 고려 하였는데 성능이 더 안 좋았다. `We also tried the alternative to encode color on 3D voxels, but it performs much worse than the pre-trained VGGnet(Table 2 [dxdydz+rgb] vs. [dxdydz+img]).`

  * 그 이유는 아마도 : This might be because encoding color in 3D voxel grid significantly lowers the resolution compared to the original image, and hence high frequency signal in the image get lost. 
  * In addition, by using the pre-trained model of VGG, we are able toleverage the large amount of training data from ImageNet, and the well engineered network architecture.

### 4.3 2D and 3D joint recognition

* Color와 Depth정보를 모두 사용하기 위하여 Joint Network를 구성 하였다. `We construct a joint 2D and3D network to make use of both color and depth.`

* 2D VGG Net\(4,096 dimensions\) + 3D ORN\(4,096 dimensions\) -&gt; one feature vector -&gt; FC3\_fully connected layer\(1,000 dimensionto \)

  * `The feature from both 2D VGG Net and our 3D ORN (each has 4,096 dimensions) are concatenated into one feature vector, and fed into a fully connected layer , which reduces the dimensionto 1000.`

* 이후 FC 3D Box & FC CLass에서 이를 입력으로 받아 Label과 3D box를 생성 한다. `Another two fully connected layer(FC 3D Box & FC CLass) take this feature as input and predict the object label and 3D box.`

### 4.4. Multi-task loss

* Similarly to RPN, the loss function consists of a **classification loss** and a **3D box regression loss**:


$$
L(p,p^{\star}, t, t^{\star}) = L_{cls} (p, p^{\star}) + \lambda\prime \[p^{\star} \> 0\] L_{reg}(t, t^{\star})
$$


* the p is the predicted probability over 20 object categories\(negative non-objects is labeled as class 0\).

* For each **mini-batch**, we sample 384 examples from different images, with a positive to negative ratio of 1:3.

* For the **box regression**, each target offset $$t^{\star}$$ is normalized element-wise with the object category specific mean and standard deviation.

* During testing, we 0.1 as the **3D NMS threshold**.

* For box regressions, we directly use the results from the network.

#### 4.5 Object size pruning

* Bounding boxes 크기 정보도 유용한 힌트가 될수 있다. `When we use amodal bounding boxes to represent objects, the bounding box sizes provide useful information about the object categories.`

* To make use of this information, for each of the detected box, we checkthe box size in each direction, aspect ratio of each pair of box edge.

* We then compare these numbers with the distribution collected from training examples of the same category.

* If any of these values falls outside 1st to 99th percentile of the distribution, which indicates this box has a very different size, we decrease its score by 2.

## 5. Experiments

![](https://i.imgur.com/zrzpEO3.png)

* RPN takes 5.62s and ORN takes 13.93s per image

* Comparison on 3D Object Detection

  * depth only 67.8
  * depth + img : 72.3


---

- [19]에서는 RGB와 라이다 정보를 활용하여 3D 물체 탐지를 한다. `In [19], RGB image and its corresponding 3D point cloud are used as inputs for 3D object detection. `


- A pipeline for 3D object detection and recognition in RGB-D scenes was presented in Song and Xiao [2016].
  - 흥미로운 점은 depth channel을 사용하는 대신 TSDF를 이용하여 full 3D voxel grid 컨버젼 하는 방법을 채택 한것이다. Interestingly, instead of just working on the depth channel, Song and Xiao exploited the raw 3D information of the scenes by converting each depth image to a full 3D voxel grid using a directional Truncated Signed Distance Function (TSDF).
  - A fully 3D convolutional network, called 3D Region Proposal Network (RPN), was then utilized in order to generate 3D object bounding boxes from the 3D voxel grid at two different scales so that it could handle different object sizes.
  - Objectness scores were also provided for each generated object proposal.
  - Moreover, each detected 3D proposal box and its corresponding 2D color patch (i.e., 2D projection of the 3D proposal) were fed to a 3D ConvNet and a 2D ConvNet, respectively, for jointly learning the object’s category and 3D box regression.

- Deep Sliding Shapes [23] exploits more powerful deep learning features.
  - However, it operates on 3D voxel grids and uses computationally expensive 3D convolutions.
  
---

[Sliding Shape [DeepSlidingShape 기존연구] 
- Sliding Shapes for 3D object detection in depth images (Song2014)


깊이 정보 활용을 위해 저자는 sliding shapes를 제안 하였으나 hand-crafted feature로 인해 제약이 있다. To make good use of the depth information, Sliding Shapes [25] was proposed to slide a 3D detection window in 3D space.+

- While it is limited by the use of `hand-crafted` features,

Sliding Shapes [25] is a 3D object detector that runs sliding windows in 3D to directly classify each 3D window. +

However, the algorithm uses hand-crafted features and the algorithm uses many exemplar classifiers so it is very slow.

Sliding Shapes [22] and Vote3D [26] apply SVM classifers on 3D grids encoded with geometry features.

