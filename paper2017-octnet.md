|논문명|OctNet: Learning Deep 3D Representations at High Resolutions |
|-|-|
|저자(소속)| Gernot Riegler (Graz University)|
|학회/년도| CVPR 2017, [논문](https://arxiv.org/abs/1611.05009)|
|키워드| 고해상도 처리를 위한 계산 효율화 |
|참고|[CVPR 2017](https://www.youtube.com/watch?v=qYyephF2BBw)|
|코드|[Torch](https://github.com/griegler/octnet)|



# OctNet

```
To alleviate this problem, Riegler et al. (2017) propose OctNets,a 3D convolutional network, that allows for training deep architectures at significantly higher resolutions. 

They build on the observation that 3D data (e.g., point clouds, meshes) is often sparse in nature. 

The proposed OctNet exploits this sparsity property by hierarchically partitioning the 3D space into aset of octrees and applying pooling in a data-adaptive fashion.

This leads to a reduction in computational and memory requirements as the convolutional network operations are defined on the structure of these trees and thus can dynamically allocate resources depending on the structure of the input.


our representation enables 3D convolutional networks which are both deep and high resolution. 

Towards this goal, we exploit the **sparsity** in the input data 
- to hierarchically partition the space using a set of unbalanced octrees where each leaf node stores a pooled feature representation
```

## 1. Introduction

Most existing 3D network architectures [8,30-VoxNet,35,48-shapenets] replace the 2D pixel array by its 3D analogue, (i.e., a dense and regular 3D voxel grid), and process this grid using 3D convolution
and pooling operations.

```
[8] C. B. Choy, D. Xu, J. Gwak, K. Chen, and S. Savarese. 3dr2n2: A unified approach for single and multi-view 3d object reconstruction. In Proc. of the European Conf. on Computer
Vision (ECCV), 2016.
[30] D. Maturana and S. Scherer. Voxnet: A 3d convolutional neural network for real-time object recognition. In Proc. IEEE International Conf. on Intelligent Robots and Systems (IROS), 2015.
[35] C. R. Qi, H. Su, M. Nießner, A. Dai, M. Yan, and L. Guibas. Volumetric and multi-view cnns for object classification on 3d data. In Proc. IEEE Conf. on Computer Vision and Pattern Recognition (CVPR), 2016.
[48] Z. Wu, S. Song, A. Khosla, F. Yu, L. Zhang, X. Tang, and J. Xiao. 3d shapenets: A deep representation for volumetric shapes. In Proc. IEEE Conf. on Computer Vision and Pattern
Recognition (CVPR), 2015.
```

Consequently, existing 3D networks are limited to **low 3D resolutions**, typically in the
order of $$30^3$$ voxels. 

To fully exploit the rich and detailed geometry of our 3D world, however, **much higher resolution networks** are required. 

![](https://i.imgur.com/PJ7HFYz.png)

### 1.1 Motivation. 

For illustration purposes, we trained a dense convolutional network to classify 3D shapes from [48]. 
- Given a voxelized bed as input, we show the maximum response across all feature maps at intermediate layers (a-c) of the network before pooling. 
- Higher activations are indicated with darker colors. (Voxels with zero activation are not displayed.)
- The `first row` visualizes the responses in 3D while the `second row shows a 2D slice.
- Note how voxels close to the object contour respond more strongly than voxels further away. 
- We exploit the sparsity in our data by allocating memory and computations using a space partitioning data structure (`bottom row`).


We illustrate this in Fig. 1 for a 3D classification example. 
- Given the 3D meshes of [48] we voxelize the input at a resolution of `643` and train a simple 3D convolutional network to minimize a classification loss. 
- We depict the maximum of the responses across all feature maps at different layers of the network. 
- It is easy to observe that high activations occur only near the object boundaries

```
[48] Z. Wu, S. Song, A. Khosla, F. Yu, L. Zhang, X. Tang, and J. Xiao. 3d shapenets: A deep representation for volumetric shapes. In Proc. IEEE Conf. on Computer Vision and Pattern
Recognition (CVPR), 2015.
```

### 1.2 제안 방식 

Our OctNet hierarchically partitions the 3D space into a set of unbalanced octrees [32]. 

```
[32] A. Miller, V. Jain, and J. L. Mundy. Real-time rendering and dynamic updating of 3-d volumetric data. In Proc. of the Workshop on General Purpose Processing on Graphics Processing Units (GPGPU), page 8, 2011.
```

Each octree splits the 3D space according to the **density** of the data. 
- More specifically, we recursively split octree nodes that contain a data point in its domain, (i.e., 3D points, or mesh triangles), stopping at the finest resolution of the tree. 
- Therefore, leaf nodes vary in size, e.g., an empty leaf node may comprise up to $$8^
3 = 512$$ voxels for a tree of depth 3 and each leaf node in the octree stores a pooled summary of all feature activations of the voxel it comprises. 

The convolutional network operations are directly defined on the structure of these trees. 

Therefore, our network dynamically focuses computational and memory resources, depending on the 3D structure of the input.
- 이렇게 함으로써 계산 자원을 줄일수 있다. 


