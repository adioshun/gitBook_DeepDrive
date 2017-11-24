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





