|논문명|3D Fully Convolutional Network for Vehicle Detection in Point Cloud|
|-|-|
|저자(소속)|Bo Li (Baidu)|
|학회/년도|2017, [논문](https://arxiv.org/pdf/1611.08069.pdf)|
|키워드| |
|참고|[2016논문](https://arxiv.org/pdf/1608.07916.pdf)|
|코드|[TF](https://github.com/yukitsuji/3D_CNN_tensorflow)|

# 3D CNN for Vehicle Detection 

## 1. 개요 

Baidu의 연구 결과로 기존 CNN(2D)를 3D 데이터로 확장 

2D 이미지 대비 장점 : pose and shape of the detected objects


## 2. 기존 연구 
- 기존 연구 Pipeline : 후보 영역 선정 -> 분류 

- rule-based segmentation is suggested for specific scene [10, 20, 5].

### 2.1 후보영역 탐지
1. simply removing the ground plane 
2. cluster the remaining points can generate reasonable segmentation[10, 5].

개선된 방안 : forming graphs on the point cloud [32, 14, 21, 29, 30].

### 2.2 분류 방법들 
- Behley et al. [2] suggests to segment the scene hierarchically and keep segments of different scales.

- Other methods directly exhaust the range scan space to propose candidates to avoid incorrect segmentation.
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


We would also like to mention that object detection on RGBD images [3, 17] is closely related to the topic of object detection on range scan.

The depth channel can be interpreted as a range scan and naturally applies to some detection algorithms designed for range scan.

On the otherhand, numerous researches have been done on exploiting both depth and RGB information in object detection tasks.

We omit detailed introduction about traditional literatures on RGBD data here but the proposed algorithm in this paper can also be generalized to RGBD data.


