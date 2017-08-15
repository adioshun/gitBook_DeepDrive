|논문명|3D Fully Convolutional Network for Vehicle Detection in Point Cloud
|-|-|
|저자(소속)|Bo Li (Baidu)|
|학회/년도|2017, [논문](https://arxiv.org/pdf/1611.08069.pdf)|
|키워드|project range scans as 2D maps similar to the depthmap of RGBD data |
|참고|[2016논문](https://arxiv.org/pdf/1608.07916.pdf)|
|코드|[TF](https://github.com/yukitsuji/3D_CNN_tensorflow)|

# 3D CNN for Vehicle Detection 

## 1. 개요 

Baidu의 연구 결과로 기존 CNN(2D)를 3D 데이터로 확장 

2D 이미지 대비 장점 : pose and shape of the detected objects

2D CNN `DenseBox.`를 기반으로 아이디어 확장 

## 2. 기존 연구 
- 기존 연구 Pipeline : 후보 영역 선정 -> 분류 

- rule-based segmentation is suggested for specific scene [10, 20, 5].


### 2.1 Convolutional Neural Network and 3D Object Detection

> [논문](https://arxiv.org/pdf/1611.08069.pdf)

- [3], [9],[16], [17], [24], [25] embed 3D information in 2D projection and use 2D CNN for recognition or detection.
- [16] also suggest it possible to predict 3D object localization by 2D CNN network on range scans.

- [10] operates 3D voxel data but regards one dimension as a channel to apply 2D CNN.

- [8], [20], [26], [32] are among the very few earlier works on3D CNN.

 - [8], [20], [32] focus on object recognition and 
 - [26] proposes 3D R-CNN techniques for indoor object detection combining the Kinect image and point cloud.

> 복셀(voxel : 볼륨+픽셀) : 3D 공간에서 볼륨과 색상 정보를 포함하는 점(포인트)

### 2.1 Object Detection from Range Scans

> Range Sensor = LiDAR, RGBD Camera (cf. Range scans??)

#### A. 후보영역 탐지
1. simply removing the ground plane 
2. cluster the remaining points can generate reasonable segmentation[10, 5].

개선된 방안 : forming graphs on the point cloud [32, 14, 21, 29, 30].

###### 후보영역 추천 알로리즘들 Candidates can be proposed by 
- segmentation algorithms [2], [5], [11], [14], [21], [22], [28], [29], [31], 
- sliding window [30], 
- random sampling [13], 
- Region Proposal Network (RPN) [26].


#### B. 분류 방법들 

For the classification stage, research have been 
 - drawn to features including shape model [6], [13] and geometry statistic features [22], [27], [29], [31].
 - Sparsing coding [4], [15] 
 - deep learning [26] are also used for feature representation.

3D를 2D로 투영하는 방법 : Besides directly operating in the 3D point cloud space,some other previous detection alogrithms project 3D point cloud onto 2D surface as depthmaps or range scans [3], [16],[17].
 - 3D위치 정보를 잃어 버리는 문제점 있음 

Behley et al. [2] suggests to segment the scene hierarchically and keep segments of different scales.

Other methods directly exhaust the range scan space to propose candidates to avoid incorrect segmentation.
 - For example, Johnson and Hebert [13] randomly samples points from the point cloud as correspondences.
 - Wang andPosner [31] scan the whole space by a sliding window to generate proposals.

기존의 연구들은 분류를 위해서 알려진 모습(Shape)을 가지고 데이터를 비교 하였다. [6, 13].

최근의 머신러닝 기반의 탐지 방법들은 일부 Feature들을 hand-crafted한후에 분류 하는데 사용 하였다. 
- Triebel et al. [29], Wang et al. [32], Teichmanet al. [28] use shape spin images, shape factors and shape distributions.
- Teichman et al. [28] also encodes the object moving track information for classification.
- Papon et al. [21] uses FPFH.
- Other features include normal orientation, distribution histogram and etc.

A comparison of features can be found in [1].

Besides the hand-crafted features, Deuge et al. [4], Laiet al. [15] explore to learn feature representation of point cloud via sparse coding.

#### C. RGBD images

range scan에서의 물체 탐지는 RGBD images [3, 17]를 이용한 탐지 방법과 깊은 연관이있다.  
- The depth channel can be interpreted as a range scan and naturally applies to some detection algorithms designed for range scan.

>  RGBD data : 색상정보(RGB) + 물체까지의 거리정보 (Depth)를 함께 측정할

### 2.1 Convolutional Neural Network on Object Detection

#### A. 기존 2D CNN기반 물체 탐지 

- R-CNN [8] proposes candidate regions and uses CNN to verify candidates as valid objects

- OverFeat [25], DenseBox [11] and YOLO [23] uses end-to-end unified FCN frameworks which predict the objectness confidence and the bounding boxes simultaneously over the whole image.

#### B. 3D로의 확장 연구 
Some research has also been focused on applying CNN on 3D data.

##### 가. RGBD
RGBD dat에서 D를 하나의 이미지 채널로 간주 하고 2D CNN를 이용하여 분류/탐지 하였다. [9, 24, 26].

> - [9] S Gupta, R Girshick, P Arbelaez, and J Malik. Learning ´Rich Features from RGB-D Images for Object Detection and Segmentation. arXiv preprint arXiv:1407.5736, pages 1–16, 2014.
> - [24] Max Schwarz, Hannes Schulz, and Sven Behnke. RGB-D Object Recognition and Pose Estimation based on Pretrained Convolutional Neural Network Features. IEEE International Conference on Robotics and Automation
(ICRA), (May), 2015.
> - [26] Richard Socher, Brody Huval, Bharath Bath, Christopher D Manning, and Andrew Y Ng. Convolutionalrecursive deep learning for 3d object classification. Advances in Neural Information Processing Systems, pages 665–673, 2012.

##### 나. Point CLoud 
 - For 3D range scan some works discretize point cloud along 3D grids and train3D CNN structure for classification [33, 19]. (포인트 클라우드를 3D 그리드 + Traind 3D CNN으로 분리) 
  
> - [33] Zhirong Wu and Shuran Song. 3D ShapeNets : A Deep Representation for Volumetric Shapes. IEEE Conference
on Computer Vision and Pattern Recognition (CVPR2015), pages 1–9, 2015.
> - [19] Daniel Maturana and Sebastian Scherer. VoxNet : A 3D Convolutional Neural Network for Real-Time Object
Recognition. pages 922–928, 2015

These classifier scan be integrated with region proposal method like slidin gwindow [27] for detection tasks.

### 2.3 본 논문의 접근 방안 
In this paper, **our approach project range scans as 2D maps** similar to the depthmap of RGBD data. 

The frameworks of Huang et al. [11], Sermanet et al. [25] are transplanted to predict the objectness and the 3D object bounding boxes in a unified end-to-end manner.


## 3. 제안 방식 



---

[1] Z. Wu, S. Song, A. Khosla, F. Yu, L. Zhang, X. Tang and J. Xiao. 3D ShapeNets: A Deep Representation for Volumetric Shapes. CVPR2015.
[2] D. Maturana and S. Scherer. VoxNet: A 3D Convolutional Neural Network for Real-Time Object Recognition. IROS2015.
[3] H. Su, S. Maji, E. Kalogerakis, E. Learned-Miller. Multi-view Convolutional Neural Networks for 3D Shape Recognition. ICCV2015.
[4] B Shi, S Bai, Z Zhou, X Bai. DeepPano: Deep Panoramic Representation for 3-D Shape Recognition. Signal Processing Letters 2015.
[5] Song Bai, Xiang Bai, Zhichao Zhou, Zhaoxiang Zhang, Longin Jan Latecki. GIFT: A Real-time and Scalable 3D Shape Search Engine. CVPR 2016.
[6] Edward Johns, Stefan Leutenegger and Andrew J. Davison. Pairwise Decomposition of Image Sequences for Active Multi-View Recognition CVPR 2016. 
[7] Vishakh Hegde, Reza Zadeh 3D Object Classification Using Multiple Data Representations. 

Is there a Convolutional Neural Network implementation for 3D.... Available from: https://www.researchgate.net/post/Is_there_a_Convolutional_Neural_Network_implementation_for_3D_images [accessed Aug 14, 2017].
