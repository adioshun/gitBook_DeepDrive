|논문명|PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation
|-|-|
|저자(소속)|Charles R. Qi, Hao Su, Kaichun Mo, Leonidas J. Guibas (Stanford University)|
|학회/년도|Dec 2016 ~ Apr 2017, CVPR 2017,  [논문](https://arxiv.org/abs/1612.00593)|
|키워드| |
|참고|[TFKR](https://www.facebook.com/thinking.factory/posts/1408857052524274), [홈페이지](http://stanford.edu/~rqi/pointnet/),[CVPR2017](https://www.youtube.com/watch?v=Cge-hot0Oc0)|
|코드|[TF](https://github.com/charlesq34/pointnet), [pyTorch](https://github.com/fxia22/pointnet.pytorch)|




* PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation

[요약]
"Research Question: Point clouds에서 바로 feature learning을 효과적으로 하는 방법이 무엇이 있을까?"

3D로 물체를 표현할 때, 
- Point Cloud : 가장 직관적이고 정보를 잘 표현할 수 있으면서도 다른 방법에서 변환하기도 쉽고 역으로 돌아가기도 쉬우며 얻기도 편하므로 이를 많이 사용한다.
- Mesh
- Volumetric
- Projected View 등등의 방법

  
대부분의 point cloud features는 각각의 특정한 task들에 대해 handcrafted 된 경우가 많은데 이런 방식이 아니라 point clouds에서 바로 feature learning을 효과적으로 하는 방법이 무엇이 있을까?
-> PointNet : End-to-end learning for scattered, unordered point data, Unified framework for various tasks

그런데 point clouds의 특성상 data의 order에 invariant해야한다는
점 (Unordered point set as input) 그리고 이 point clouds에 geometric transformation을 가한다고 물체가 다른 것으로 분류되어서도 안된다는 점 (Invariance under geometric transformations) 이렇게 두가지 특성들을 어떻게 네트워크에 녹여낼 것인가에 대한 고민이 필요하다.

이 연구에서는 permutation invariance는 symmetric function을 도입하여 해결하고 두번째 문제는 transformer network를 하나 모듈로 붙여서 해결하였다. PointNet은 max pooling을 기준으로 앞부분의 local feature단과 뒷부분의 global feature단을 보는 것으로 나눌 수 있는데, 논문에서는 critical point로 불리는 global feature에 영향을 주는 point set은 매우 적고 주요 경계마다만 있고 대다수의 point들은 영향을 주지 않기 떄문에 전에 point clouds에서 50%까지 data loss가 있더라도 전혀 성능에 문제가 발생하지 않는다. (robustness to missing data)


