| 논문명 | PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation |
| --- | --- |
| 저자\(소속\) | Charles R. Qi, Hao Su, Kaichun Mo, Leonidas J. Guibas \(Stanford University\) |
| 학회/년도 | Dec 2016 ~ Apr 2017, CVPR 2017,  [논문](https://arxiv.org/abs/1612.00593) |
| 키워드 |  |
| 참고 | [TFKR](https://www.facebook.com/thinking.factory/posts/1408857052524274), [홈페이지](http://stanford.edu/~rqi/pointnet/),[CVPR2017](https://www.youtube.com/watch?v=Cge-hot0Oc0) |
| 코드 | [TF](https://github.com/charlesq34/pointnet), [pyTorch](https://github.com/fxia22/pointnet.pytorch) |

# PointNet

Due to Point cloud's irregular format, most researchers transform such data to

* regular 3D voxel grids or 
* collections of images

we design a novel type of neural network that directly consumes point clouds

## 1. Introduction

??

## 2. Related Work

### 2.1 Point Cloud Features

> Point Cloud 특징들은 `수작업`으로 만든것들이다. 이전 CV 방식 처럼

Most existing features for point cloud are `handcrafted` towards specific tasks.

Point features often encode certain statistical properties of points and are designed to be invariant to certain transformations, which are typically classified as intrinsic \[2, 24, 3\] or extrinsic \[20, 19, 14, 10, 5\].

They can also be categorized as `local features` and `global features`.

For a specific task, it is not trivial to find the optimal feature combination.

### 2.2 Deep Learning on 3D Data

3D data has multiple popular representations, leading to various approaches for learning.

#### A. Volumetric CNNs

Volumetric CNNs: \[28, 17, 18\] are the pioneers applying 3D convolutional neural networks on voxelized shapes.

> ShpaeNet, VoxNet, Vol/Multi-View CNNs

However, volumetric representation is constrained by its resolution due to data sparsity and computation cost of 3D convolution.

`FPNN [13]` and `Vote3D [26]` proposed special methods to deal with the sparsity problem; - however, their operations are still on sparse volumes, it’s challenging for them to process very large point clouds.

```
[28] Z. Wu, S. Song, A. Khosla, F. Yu, L. Zhang, X. Tang, and J. Xiao. 3d shapenets: A deep representation for volumetric shapes. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pages 1912–1920, 2015.
[17] D. Maturana and S. Scherer. Voxnet: A 3d convolutional neural network for real-time object recognition. In IEEE/RSJ International Conference on Intelligent Robots and Systems, September 2015
[18] C. R. Qi, H. Su, M. Nießner, A. Dai, M. Yan, and L. Guibas. Volumetric and multi-view cnns for object classification on 3d data. In Proc. Computer Vision and Pattern Recognition (CVPR), IEEE, 2016. 
[13] Y. Li, S. Pirk, H. Su, C. R. Qi, and L. J. Guibas. Fpnn: Field probing neural networks for 3d data. arXiv preprint arXiv:1605.06240, 2016.
[26] D. Z. Wang and I. Posner. Voting for voting in online point cloud object detection. Proceedings of the Robotics: Science and Systems, Rome, Italy, 1317, 2015
```

#### B. Multiview CNNs

> 3D Point Cloud를 2D 이미지로 맵핑하고 2D CNN을 접목하는 방법, 성능이 잘 나옴

Multiview CNNs: \[23, 18\] have tried to render 3D point cloud or shapes into 2D images and then apply 2D conv nets to classify them.

With well engineered image CNNs, this line of methods have achieved dominating performance on shape classification and retrieval tasks \[21\].

However, it’s nontrivial to extend them to scene understanding or other 3D tasks such as point classification and shape completion.

```
[23] H. Su, S. Maji, E. Kalogerakis, and E. G. Learned-Miller. Multi-view convolutional neural networks for 3d shape recognition. In Proc. ICCV, to appear, 2015
[18] C. R. Qi, H. Su, M. Nießner, A. Dai, M. Yan, and L. Guibas. Volumetric and multi-view cnns for object classification on 3d data. In Proc. Computer Vision and Pattern Recognition (CVPR), IEEE, 2016
[21] M. Savva, F. Yu, H. Su, M. Aono, B. Chen, D. Cohen-Or, W. Deng, H. Su, S. Bai, X. Bai, et al. Shrec16 track largescale 3d shape retrieval from shapenet core55.
```

#### D. Spectral CNNs

Spectral CNNs: Some latest works \[4, 16\] use spectral CNNs on meshes.

However, these methods are currently constrained on manifold meshes such as organic objects and it’s not obvious how to extend them to non-isometric shapes such as furniture.

```
[4] J. Bruna, W. Zaremba, A. Szlam, and Y. LeCun. Spectral networks and locally connected networks on graphs. arXiv preprint arXiv:1312.6203, 2013
[16] J. Masci, D. Boscaini, M. Bronstein, and P. Vandergheynst. Geodesic convolutional neural networks on riemannian manifolds. In Proceedings of the IEEE International Conference on Computer Vision Workshops, pages 37–45, 2015.
```

#### E. Feature-based DNNs

Feature-based DNNs: \[6, 8\]firstly convert the 3D data into a vector, by extracting traditional shape features and then use a fully connected net to classify the shape.

We think they are constrained by the representation power of the features extracted.

> 특징 추출단계에서 표현력 제약 발생 가능

```
[6] Y. Fang, J. Xie, G. Dai, M. Wang, F. Zhu, T. Xu, and E. Wong. 3d deep shape descriptor. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pages 2319–2328, 2015. 
[8] K. Guo, D. Zou, and X. Chen. 3d mesh labeling via deep convolutional neural networks. ACM Transactions on Graphics (TOG), 35(1):3, 2015.
```

### 2.3 Deep Learning on Unordered Sets

From a data structure point of view, a point cloud is an unordered set of vectors.

While most works in deep learning focus on regular input representations like sequences \(in speech and language processing\), images and volumes \(video or 3D data\), not much work has been done in deep learning on point sets.

One recent work from Oriol Vinyals et al \[25\] looks into this problem.

They use a read-process-write network with attention mechanism to consume unordered input sets and show that their network has the ability to sort numbers.

However, since their work focuses on generic sets and NLP applications, there lacks the role of geometry in the sets.

```
[25] O. Vinyals, S. Bengio, and M. Kudlur. Order matters: Sequence to sequence for sets. arXiv preprint arXiv:1511.06391, 2015.
```

---

\[요약\]  
"Research Question: Point clouds에서 바로 feature learning을 효과적으로 하는 방법이 무엇이 있을까?"

3D로 물체를 표현할 때,

* Point Cloud : 가장 직관적이고 정보를 잘 표현할 수 있으면서도 다른 방법에서 변환하기도 쉽고 역으로 돌아가기도 쉬우며 얻기도 편하므로 이를 많이 사용한다.
* Mesh
* Volumetric
* Projected View 등등의 방법

대부분의 point cloud features는 각각의 특정한 task들에 대해 handcrafted 된 경우가 많은데 이런 방식이 아니라 point clouds에서 바로 feature learning을 효과적으로 하는 방법이 무엇이 있을까?  
-&gt; PointNet : End-to-end learning for scattered, unordered point data, Unified framework for various tasks

그런데 point clouds의 특성상 data의 order에 invariant해야한다는  
점 \(Unordered point set as input\) 그리고 이 point clouds에 geometric transformation을 가한다고 물체가 다른 것으로 분류되어서도 안된다는 점 \(Invariance under geometric transformations\) 이렇게 두가지 특성들을 어떻게 네트워크에 녹여낼 것인가에 대한 고민이 필요하다.

이 연구에서는 permutation invariance는 symmetric function을 도입하여 해결하고 두번째 문제는 transformer network를 하나 모듈로 붙여서 해결하였다. PointNet은 max pooling을 기준으로 앞부분의 local feature단과 뒷부분의 global feature단을 보는 것으로 나눌 수 있는데, 논문에서는 critical point로 불리는 global feature에 영향을 주는 point set은 매우 적고 주요 경계마다만 있고 대다수의 point들은 영향을 주지 않기 떄문에 전에 point clouds에서 50%까지 data loss가 있더라도 전혀 성능에 문제가 발생하지 않는다. \(robustness to missing data\)

