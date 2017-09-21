|논문명|3D Fully Convolutional Network for Vehicle Detection in Point Cloud
|-|-|
|저자(소속)|Bo Li (Baidu)|
|학회/년도|Nov. 2016 ~ Jan. 2017, [논문](https://arxiv.org/abs/1611.08069)|
|키워드|project range scans as 2D maps similar to the depthmap of RGBD data |
|참고|[이전 논문(Aug. 2016)](https://arxiv.org/pdf/1608.07916.pdf)|
|코드|[TF](https://github.com/yukitsuji/3D_CNN_tensorflow)|

# 3D FCN4VD

## 1. 개요 

목표 : we design a 3D fully convolutional network (FCN) to detect and localize objects as 3D boxes from point cloud data. 

제안 방법 : extends FCN to 3D and is applied to 3D vehicle detection for an autonomous driving system

## 2. 기존 연구 

## 2.1 3D Object Detection in Point Cloud

Pipeline : 후보 영역 선정(candidate proposal) -> 분류(classification) 

### A. Candidate proposal에 활용 가능한 기술 들 

- segmentation algorithms  [2], [5], [11], [14], [21], [22], [28], [29], [31],

- sliding window [30]

- random sampling [13]

- RegionProposal Network (RPN) [26]


### B. classification에 활용 가능한 기술 들 

- shape model [6], [13] 

- geometry statistic features [22], [27], [29], [31].

- Sparsing coding [4], [15] 

- deep learning [26] 

- 3D-2D Projecting `Besides directly operating in the 3D point cloud space, some other previous detection alogrithms project 3D point cloud onto 2D surface as depthmaps or range scans [3], [16],[17]. `
 - 단점: 3D spatial information을 읽어 버리 된다. 
 - 장점: 기존 2D detection algorithms 재활용 가능 


### 2.2 Convolutional Neural Network and 3D Object Detection

- 3D정보를 2D로 투영후 2D CNN 사용 : [3], [9],[16], [17], [24], [25]

- 3D object localization을 2D CNN에 바로 작용 하여도 동작함 [16] 

- [10] operates 3D voxel data but regards one dimension as a channel to apply 2D CNN.

- [8-VeloFCN], [20-VoxNet], [26], [32-3DShapeNet] are among the very few earlier works on3D CNN.
 - [8], [20], [32] focus on object recognition 
 - [26] proposes 3D R-CNN techniques for indoor object detection combining the Kinect image and point cloud.

> 복셀(voxel : 볼륨+픽셀) : 3D 공간에서 볼륨과 색상 정보를 포함하는 점(포인트)

```
[16] Bo Li, Tianlei Zhang, and Tian Xia. Vehicle detection from 3d lidar using fully convolutional network. Proceedings of Robotics: Science and Systems, 2016
[8] Ben Graham. Sparse 3D convolutional neural networks. Bmvc, pages 1–11, 2015
[20] Daniel Maturana and Sebastian Scherer. VoxNet : A 3D Convolutional Neural Network for Real-Time Object Recognition. pages 922–928, 2015
[32] Zhirong Wu and Shuran Song. 3D ShapeNets : A Deep Representation for Volumetric Shapes. IEEE Conference on Computer Vision and Pattern Recognition (CVPR2015), pages 1–9, 2015.
[26] Shuran Song and Jianxiong Xiao. Sliding shapes for 3d object detection in depth images. pages 634–651, 2014.

```


---



Is there a Convolutional Neural Network implementation for 3D.... Available from: https://www.researchgate.net/post/Is_there_a_Convolutional_Neural_Network_implementation_for_3D_images [accessed Aug 14, 2017].
