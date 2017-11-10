| 논문명 | 3D Fully Convolutional Network for Vehicle Detection in Point Cloud |
| --- | --- |
| 저자\(소속\) | Bo Li \(Baidu\) |
| 학회/년도 | Nov. 2016 ~ Jan. 2017, [논문](https://arxiv.org/abs/1611.08069) |
| 키워드 | Bo2016b |
| 데이터셋\(센서\)/모델 | KITTI |
| 참고 | [이전 논문\(Aug. 2016\)](https://arxiv.org/pdf/1608.07916.pdf) |
| 코드 | [TF](https://github.com/yukitsuji/3D_CNN_tensorflow) |

```
- 차량 탐지 알고리즘 `For example Li (2017) presented a method for vehicle detection in ground-based LiDAR point clouds. `
    - The input point cloud was voxelized, and then a fourth binary channel was appended, representing the binary occupancy,i.e. the presence or the absence of a point within each voxel. 
    - A 3D-FCN was then trained and evaluated to produce two maps representing the objectness and bounding box scores, using the KITTI dataset.

```

# 3D FCN4VD

## 1. 개요

목표 : we design a 3D fully convolutional network \(FCN\) to detect and localize objects as 3D boxes from point cloud data.

제안 방법 : extends FCN to 3D and is applied to 3D vehicle detection for an autonomous driving system

## 2. 기존 연구

## 2.1 3D Object Detection in Point Cloud

Pipeline : 후보 영역 선정\(candidate proposal\) -&gt; 분류\(classification\)

### A. Candidate proposal에 활용 가능한 기술 들

* segmentation algorithms  \[2\], \[5\], \[11\], \[14\], \[21\], \[22\], \[28\], \[29\], \[31\],

* sliding window \[30\]

* random sampling \[13\]

* RegionProposal Network \(RPN\) \[26\]

### B. classification에 활용 가능한 기술 들

* shape model \[6\], \[13\]

* geometry statistic features \[22\], \[27\], \[29\], \[31\].

* Sparsing coding \[4\], \[15\]

* deep learning \[26\]

* 3D-2D Projecting `Besides directly operating in the 3D point cloud space, some other previous detection alogrithms project 3D point cloud onto 2D surface as depthmaps or range scans [3], [16],[17].`

  * 단점: 3D spatial information을 읽어 버리 된다. 
  * 장점: 기존 2D detection algorithms 재활용 가능 

### 2.2 Convolutional Neural Network and 3D Object Detection

* 3D정보를 2D로 투영후 2D CNN 사용 : \[3\], \[9\],\[16\], \[17\], \[24\], \[25\]

```
[3-3DOP] Xiaozhi Chen, Kaustav Kundu, Yukun Zhu, Andrew G Berneshawi, Huimin Ma, Sanja Fidler, and Raquel Urtasun. 3d object proposals for accurate object class detection. Advances in Neural Information Processing Systems, pages 424–432, 2015.
[9] S Gupta, R Girshick, P Arbelaez, and J Malik. Learning Rich Features from RGB-D Images for Object Detection and Segmentation. arXiv preprint arXiv:1407.5736, pages 1–16, 2014.
[16-VeloFCN] Bo Li, Tianlei Zhang, and Tian Xia. Vehicle detection from 3d lidar using fully convolutional network. Proceedings of Robotics: Science and Systems, 2016.
[17] Dahua Lin, Sanja Fidler, and Raquel Urtasun. Holistic scene understanding for 3D object detection with RGBD cameras. Proceedings of the IEEE International Conference on Computer Vision, pages 1417–1424, 2013.
[24] Max Schwarz, Hannes Schulz, and Sven Behnke. RGB-D Object Recognition and Pose Estimation based on Pre-trained Convolutional Neural Network Features. IEEE International Conference on Robotics and Automation (ICRA), (May), 2015.
[25] Richard Socher, Brody Huval, Bharath Bath, Christopher D Manning, and Andrew Y Ng. Convolutional-recursive deep learning for 3d object classification. Advances in Neural Information Processing Systems, pages 665–673, 2012.
```

* 3D object localization을 2D CNN에 바로 작용 하여도 동작함 \[16-VeloFCN\]

* \[10\] operates 3D voxel data but regards one dimension as a channel to apply 2D CNN.

```
[10] Michael Himmelsbach, Felix V Hundelshausen, and Hans-Joachim Wunsche. Fast segmentation of 3d point clouds for ground vehicles. Intelligent Vehicles Symposium (IV), 2010 IEEE, pages 560–565, 2010.
```

* \[8\], \[20-VoxNet\], \[26\], \[32-3DShapeNet\] are among the very few earlier works on3D CNN.
  * \[8\], \[20\], \[32\] focus on object recognition 
  * \[26\] proposes 3D R-CNN techniques for indoor object detection combining the Kinect image and point cloud.

> 복셀\(voxel : 볼륨+픽셀\) : 3D 공간에서 볼륨과 색상 정보를 포함하는 점\(포인트\)

```
[16] Bo Li, Tianlei Zhang, and Tian Xia. Vehicle detection from 3d lidar using fully convolutional network. Proceedings of Robotics: Science and Systems, 2016
[8] Ben Graham. Sparse 3D convolutional neural networks. Bmvc, pages 1–11, 2015
[20] Daniel Maturana and Sebastian Scherer. VoxNet : A 3D Convolutional Neural Network for Real-Time Object Recognition. pages 922–928, 2015
[32] Zhirong Wu and Shuran Song. 3D ShapeNets : A Deep Representation for Volumetric Shapes. IEEE Conference on Computer Vision and Pattern Recognition (CVPR2015), pages 1–9, 2015.
[26] Shuran Song and Jianxiong Xiao. Sliding shapes for 3d object detection in depth images. pages 634–651, 2014.
```

* 본 논문은 FCN이 3D를 처리 할수 있도록 변경 하였다. `In this paper, we transplant the fully convolutional network (FCN) to 3D to detect and localize object as 3D boxes in point cloud.`

* FCN은 최근 좋은 이미지넷, KITTI등에서 좋은 성과를 보이고 있다. `The FCN is a recently popular framework for end-to-end object detection, with top performance in tasks including ImageNet, KITTI, ICDAR, etc.`

  * FCN의 변종들은 다음과 같다. `Variations of FCN include DenseBox [12], YOLO [23] and SSD [18].`

* 본 연구는 DenseBox에 영향을 받았다. `The approach proposed in this paper is inspired by the basic idea of DenseBox.`

## 3. APPROACH

### 3.1 FCN Based Detection Revisited

FCN의 기본 Task는 두개로 나눌수 있다. `The procedure of FCN based detection frameworks can be summarized as two tasks,`

* Objectness prediction 
* Bounding box prediction. 

![](https://i.imgur.com/nPh3YhD.png)

FCN은 두개의 Task에 따라 서로 다른 Output Map을 생성한다. `As illustrated in Figure 1, a FCN is formed with two output maps corresponding to the two tasks respectively.`

* The objectness map : predicts if a region belongs to an object 
* The bounding box map : predicts the coordinates of the object bounding box. 

```
[16] Bo Li, Tianlei Zhang, and Tian Xia. Vehicle detection from 3d lidar using fully convolutional network. Proceedings of Robotics: Science and Systems, 2016.
```

We follow the denotion of \[16\].

* Denote $$o^a_p$$ as the output at region $$p$$ of theobjectness map, which can be encoded by softmax or hinge loss.

* Denote $$o^b_p$$ as the output of the bounding box map,which is encoded by the coordinate offsets of the boundingbox.

* Denote the ground truth objectness label at region $$p$$ as $$^l_p$$.

For simplicity each class corresponds to one label in this paper.

In some works, `(e.g. SSD or DenseBox)`, the network can have multiple objectness labels for one class, corresponding to multiple scales or aspect ratios.

The objectness loss at $$p$$is denoted as

![](https://i.imgur.com/EgQg258.png)

Denote the groundtruth bounding box coordinates offsets at region $$p$$ as $$b_p$$.

Similarly, in this paper we assume only one bounding box map is produced, though a more sophisticated network can have multiple bounding box offsets predicted for one class, corresponding to multiple scales or aspect ratios.

Each bounding box loss is denoted as

![](https://i.imgur.com/Ps3zzN0.png)

* $$w$$ used to balance the objectness loss and the bounding box loss. 
* $$P$$ denotes all regions in the objectness map 
* $$V \in P$$ denotes all object regions. 

In the deployment phase,

* the regions with postive objectness prediction are selected. 
* Then the bounding box predictions corresponding to these regions are collected and clustered as the detection results.

### 3.2 3D FCN Detection Network for Point Cloud

* 기존 연구로 discretization하는 방법들이 있지만, 본 논문에서는 point cloud를 **square grids**로 개별화\(discretize\)한다. `Although a variety of discretization embedding have been introduced for high-dimensional convolution [1], [8], for simplicity we discretize the point cloud on square grids.`

```
[1] Andrew Adams, Jongmin Baek, and Myers Abraham Davis. Fast high-dimensional filtering using the permutohedral lattice. Computer Graphics Forum, 29(2):753–762, 2010.
[8] Ben Graham. Sparse 3D convolutional neural networks. Bmvc, pages 1–11, 2015.
```

* 개별화된 데이터는 4D 배열\(length, width, height,channels\)로 표현 된다. `The discretized data can be represented by a 4D array with dimensions of length, width, height and channels.`
  * 단순화를 위해 channel은 포인트 유무에 따라 0또는 1 값뿐이다. . `For the simplest case, only one channel of value {0, 1} is used to present whether there is any points observed at the corresponding grid elements.`

Some more sophisticated features have also been introduced in the previous works, e.g. \[20-VoxNet\].

The mechanism of 2D CNN naturally extends to 3D on the square grids.

![](https://i.imgur.com/n5Xn10R.png)

```
[Fig. 2. A sample illustration of the 3D FCN structure used in this paper.]
- Feature maps are 
 - first down-sampled by three convolution operation with the stride of 1/2^3 and 
 - then up-samped by the deconvolution operation of the same stride. 
- The output objectness map (o^a) and bounding box map (o^b) are collected from the deconv4a and deconv4b layers respectively.
```

Figure 2 shows an example of the network structure used in this paper.

The network follows and simplifies the hourglass shape from \[19\].

```
[19] Jonathan Long, Evan Shelhamer, and Trevor Darrell. Fully convolutional networks for semantic segmentation. arXiv preprint arXiv:1411.4038, 2014.
```

* Layer conv1, conv2and conv3 downsample the input map by $$1/2^3$$sequentially.

* Layer deconv4a and deconv4b upsample the incoming mapby $$2^3$$respectively.

* The ReLU activation is deployed aftereach layer.

* The output objectness map \($$o^a$$\) and bounding box map \($$o^b$$\) are collected from the deconv4a and deconv4blayers respectively.

Similar to DenseBox, the objectness region V is denoted as the center region of the object.

For the proposed 3D case, a 3D sphere located at the object center is used.

Points inside the sphere are labeled as positive / foreground label.

The bounding box prediction at point p is encoded by the coordinate offsets, defined as:

![](https://i.imgur.com/QAiX1iR.png)

* where $$c_{p,\star}$$ define the 3D coordinates of 8 corners of the object bounding box corresponding to the region p.

The training and testing processes of the 3D CNN follows\[16\].

For the testing phase, candidate bounding boxes are extracted from regions predicted as objects and scored by counting its neighbors from all candidate bounding boxes.

Bounding boxes are selected from the highest score and candidates overlapping with selected boxes are suppressed.

![](https://i.imgur.com/mAH8tGK.png)

```
[Fig. 3. Intermediate results of the 3D FCN detection procedure.]
- (a) Bounding box predictions are collected from regions with high objectness confidence and are plotted as green boxes. 
- (b) Bounding boxes after clustering plotted with the blue original point cloud. 
- (c) Detection in 3D since (a) and (b) are visualized in the bird’s eye view.
```

Figure 3 shows an example of the detection intermediate results.

Bounding box predictions from objectness points are plotted as green boxes.

Note that for severely occluded vehicles, the bounding boxes shape are distorted and not clustered.

This is mainly due to the lack of similar samples in the training phase.

### 3.3 Comparison with 2D CNN

컴퓨팅 자원 소모 증가 `Compared to 2D CNN, the dimension increment of 3D CNN inevitably consumes more computational resource, mainly due to`

* 1\) the memory cost of 3D data embedding grids and
* 2\) the increasing computation cost of convolving 3D kernels.

On the other hand, naturally embedding objects in 3D space avoids perspective distortion and scale variation in the 2D case.

This make it possible to learn detection using a relatively simpler network structure.

## 4. EXPERIMENTS

---

Is there a Convolutional Neural Network implementation for 3D.... Available from: [https://www.researchgate.net/post/Is\_there\_a\_Convolutional\_Neural\_Network\_implementation\_for\_3D\_images](https://www.researchgate.net/post/Is_there_a_Convolutional_Neural_Network_implementation_for_3D_images) \[accessed Aug 14, 2017\].

