|논문명 |VoxelNet: End-to-End Learning for Point Cloud Based 3D Object Detection |
| --- | --- |
| 저자\(소속\) | Yin Zhou\(Apple\) |
| 학회/년도 | arXiv Nov 2017, [논문](https://arxiv.org/abs/1711.06396) |
| Citation ID / 키워드 | Yin2017VoxelNet, |
| 데이터셋(센서)/모델 | |
| 관련연구||
| 참고 | |
| 코드 | |


# VoxelNet


- 산재된 LiDAR를 가지고 예측을 수행 하기 위해서 사용된 방법들은 대부분 **bird’s eye view projection**같은 수작업 특징들을 이용하는 것들이다. `To interface a highly sparse LiDAR point cloud with a region proposal network (RPN), most existing efforts have focused on hand-crafted feature representations, for example, a bird’s eye view projection.`


- 본 연구를 통해 Feature 엔지니어링 작업을 없애는 VoxelNet을 제안 한다. `In this work, we remove the need of manual feature engineering for 3D point clouds and propose VoxelNet, `
    - 제안 방식은 특징 추출 및 BBox를 예측을 한번에 진행 할수 있다. `a generic 3D detection network that unifies feature extraction and bounding box prediction into a single stage, end-to-end trainable deep network. `


- 특히 VoxelNet은 새롭게 선보이는 VFE(voxel feature encoding) Layer을 이용하여 포인트 클라우드를 `equally spaced 3D voxels`과 `transforms a group of points`로 나누게 된다. 
    - Specifically, VoxelNet divides a point cloud into equally spaced 3D voxels and transforms a group of points within each voxel into a unified feature representation through the newly introduced voxel feature encoding (VFE) layer. 


- 이렇게 함으로써 포인트 클라우드는 설명령을 가지는 **volumetric representation**로 encode된다. `In this way,the point cloud is encoded as a descriptive volumetric representation,`
    - 이 representation을 PRN에 적용하여 후보 영역을 찾는다. `which is then connected to a RPN to generate detections. `


## 1. Introduction

- LiDAR는 많은 분야에 이용되고, 차량주행 등 신뢰성이 보장되는 분야에 적용된다. 

- 하지만, 포인트 클라우드 데이터는 산재되어 있고 아래와 같은 이유로 **highly variable point density**하다. ` LiDAR point clouds are sparse and have highly variable point density, due to factors such as` 
    - non-uniform sampling of the 3D space, 
    - effective range of the sensors,
    - occlusion, 
    - and the relative pose.

- 이렇나 문제를 해결하기 위하여 manually crafted feature representation기법들이 활용 되었다. 
    - `To handle these challenges, many approaches manually crafted feature representations for point clouds that are tuned for 3D object detection.

- 일부 방법은 포인트 클라우드를 원근법 시점`(perspective view)`으로 투영하고 이미지 기반 특징 추출 방식을 적용 하였다. `Several methods project point clouds into a perspective view and apply image-based feature extraction techniques[28, 15, 22]. `

```
[28] C. Premebida, J. Carreira, J. Batista, and U. Nunes. Pedestrian detection combining RGB and dense LIDAR data. In IROS, pages 0–1. IEEE, Sep 2014.
[15] A. Gonzalez, G. Villalonga, J. Xu, D. Vazquez, J. Amores, and A. Lopez. Multiview random forest of local experts combining rgb and lidar data for pedestrian detection. In IEEE Intelligent Vehicles Symposium (IV), 2015.
[22] B. Li, T. Zhang, and T. Xia. Vehicle detection from 3d lidar using fully convolutional network. In Robotics: Science and Systems, 2016.
```

- 다른 방법은 포인트 클라우드를 3D voxel grid로 래스터화 하고 각 voxel을 handcrafted features로 encode하였다. `Other approaches rasterize point clouds into a 3D voxel grid and encode each voxel with handcrafted features [41, 9, 37, 38, 21, 5-MV3D].`

```
[41] D. Z. Wang and I. Posner. Voting for voting in online point cloud object detection. In Proceedings of Robotics: Science and Systems, Rome, Italy, July 2015.
[9] M. Engelcke, D. Rao, D. Z. Wang, C. H. Tong, and I. Posner. Vote3deep: Fast object detection in 3d point clouds using efficient convolutional neural networks. In 2017 IEEE International Conference on Robotics and Automation (ICRA), pages 1355–1361, May 2017.
[37] S. Song and J. Xiao. Sliding shapes for 3d object detection in depth images. In European Conference on Computer Vision, Proceedings, pages 634–651, Cham, 2014. Springer International
Publishing.
[38] S. Song and J. Xiao. Deep Sliding Shapes for amodal 3D object detection in RGB-D images. In CVPR, 2016
[21] B. Li. 3d fully convolutional network for vehicle detection in point cloud. In IROS, 2017.
[5] X. Chen, H. Ma, J. Wan, B. Li, and T. Xia. Multi-view 3d object detection network for autonomous driving. In IEEE CVPR, 2017.
```

- 하지만 이러한 manual 방식들은 정보 Bottlenet을 유발하여 3D shape 정보를 제대로 활용하지 못하게 하고 물체 탐지를 위해서 invariances에 대한 처리 방법을 필요로 한다. `However, these manual design choices introduce an information bottleneck that prevents these approaches from effectively exploiting 3D shape information and the required invariances for the detection task. `

- 인지와 탐지 분야의 새로운 도약점(breakthrough )은 수작업 특징 추출에서 기계 학습 기반으로 넘어온 것이다. `A major breakthrough in recognition [20] and detection [13] tasks on images was due to moving from hand-crafted features to machine-learned features.`

###### [PointNet & PointNet ++]

- Recently, Qi et al.[29] proposed PointNet, an end-to end deep neural network that learns **point-wise features** directly from **point clouds**. 

- This approach demonstrated impressive results on 3D object recognition, 3D object part segmentation, and point-wise semantic segmentation tasks.

- In [30], an improved version of PointNet was introduced which enabled the network to learn **local structures** at different scales. 

- 좋은 성능을 위하여 위 두 네트워크는 모든 인풋 입력(1k points)들에 대하여 학습을 수행 하였다. `To achieve satisfactory results, these two approaches trained feature transformer networks on all input points (∼1k points). `

- 보통 포인트 클라우드로 입련 되는것이 100k point임을 감안 하면 위 방식은 자원 소모가 크다. `Since typical point clouds obtained using LiDARs contain ∼100k points, training the architectures as in [29, 30] results in high computational and memory requirements. `

- Scaling up 3D feature learning networks to orders of magnitude more points and to 3D detection tasks are the main challenges that we address in this paper. 


```
[29] C. R. Qi, H. Su, K. Mo, and L. J. Guibas. Pointnet: Deep learning on point sets for 3d classification and segmentation. Proc. Computer Vision and Pattern Recognition (CVPR), IEEE, 2017. 
[30] C. R. Qi, L. Yi, H. Su, and L. J. Guibas. Pointnet++: Deep hierarchical feature learning on point sets in a metric space. arXiv preprint arXiv:1706.02413, 2017.
```

- RPN은 물체 탐지에 최적화된 방법이다. `Region proposal network (RPN) [32] is a highly optimized algorithm for efficient object detection [17, 5, 31,24]. `

- 하지만 이 방식은 입력으로 Dense하고 텐서 구조`(e.g. image, video)`로 구성되어 이어야 하기 때문에 LiDAR에 적합하지 않다. `However, this approach requires data to be dense and organized in a tensor structure (e.g. image, video) which is not the case for typical LiDAR point clouds. `

- 본 논문에서는 `point set feature learning` 와 `RPN`간의 차이를 줄였다. `In this paper,we close the gap between point set feature learning and RPN for 3D detection task.`

