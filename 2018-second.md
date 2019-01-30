|논문명 |SECOND:Sparsely Embedded Convolutional Detection |
| --- | --- |
| 저자\(소속\) | Yan Yan(=traveller59), Bo Li\(\) |
| 학회/년도 | 2018, [논문](https://www.mdpi.com/1424-8220/18/10/3337) |
| Citation ID / 키워드 | |
| 데이터셋(센서)/모델 | KITTI-3D Object Detection |
| 관련연구|Saprse ConvNet 아이디어 활용|
| 참고 | |
| 코드 |[깃허브](https://github.com/traveller59/second.pytorch)  |



|년도|1st 저자|논문명|코드|
|-|-|-|-|
|2014|Benjamin Graham|[Spatially-sparse convolutional neural networks](https://arxiv.org/abs/1409.6070)|[2013-2015](https://github.com/btgraham/SparseConvNet)|
|2017|Benjamin Graham|[Submanifold Sparse Convolutional Networks](https://arxiv.org/abs/1706.01307)|[SparseConvNet](https://github.com/facebookresearch/SparseConvNet)|
|2018|Benjamin Graham|[3D Semantic Segmentation with Submanifold Sparse Convolutional Networks](https://arxiv.org/abs/1711.10275)|~~[SparseConvNet(deprecated)](https://github.com/facebookresearch/SparseConvNet)~~,[spconv](https://github.com/traveller59/spconv)|
|2018|Bo Li|[SECOND:Sparsely Embedded Convolutional Detection](https://www.mdpi.com/1424-8220/18/10/3337)|[SECOND](https://github.com/traveller59/second.pytorch)|




# SECOND: Sparsely Embedded Convolutional Detection


Lidar는 여러 분야에 중요 하다. `LiDAR-based or RGB-D-based object detection is used in numerous applications, ranging from autonomous driving to robot vision. `

Voxel-based 3D convolutional networks는 Lidar데이터 에서 의미 있는 정보 수집시 사용 되어 왔다. `Voxel-based 3D convolutional networks have been used for some time to enhance the retention of information when processing point cloud LiDAR data.`

문제는 느린 성능과, 자세(=Orientation)추정 성능이다. `However, problems remain, including a slow inference speed and low orientation estimation performance. `

학습/테스트 속도를 올릴수 있는 sparse conv네트워크를 조사 하였다. `We therefore investigate an improved sparse convolution method for such networks, which significantly increases the speed of both training and inference. `

또한 새로운 자세 추정을 위한 angle LOSS와 데이터 증폭 기법을 제안 한다. `We also introduce a new form of angle loss regression to improve the orientation estimation performance and a new data augmentation approach that can enhance the convergence speed and performance. `

제안 기법은 빠른 성능을 보이면서 좋은 결과를 나타냈다. `The proposed network produces state-of-the-art results on the KITTI 3D object detection benchmarks while maintaining a fast inference speed.`
