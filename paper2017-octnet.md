|논문명|OctNet: Learning Deep 3D Representations at High Resolutions |
|-|-|
|저자(소속)| Gernot Riegler (Graz University)|
|학회/년도| CVPR 2017, [논문](https://arxiv.org/abs/1611.05009)|
|키워드| 고해상도 처리를 위한 계산 효율화 |
|참고|[CVPR 2017](https://www.youtube.com/watch?v=qYyephF2BBw), [Slide](https://griegler.github.io/papers/octnet_slides.pdf)|
|코드|[Torch](https://github.com/griegler/octnet)|


> To alleviate this problem, Riegler et al. (2017) propose OctNets,a 3D convolutional network, that allows for training deep architectures at significantly higher resolutions.
> They build onthe observation that 3D data (e.g., point clouds, meshes) is oftensparse in nature.
> The proposed OctNet exploits this sparsity property by hierarchically partitioning the 3D space into aset of octrees and applying pooling in a data-adaptive fashion.
>This leads to a reduction in computational and memory requirements as the convolutional network operations are defined on the structure of these trees and thus can dynamically allocate resources depending on the structure of the input.



# OctNet



```
Riegler et al. (2017) propose OctNets,a 3D convolutional network, that allows for training deep architectures at significantly higher resolutions. 

They build on the observation that 3D data (e.g., point clouds, meshes) is often sparse in nature. 

The proposed OctNet exploits this sparsity property by hierarchically partitioning the 3D space into aset of octrees and applying pooling in a data-adaptive fashion.

This leads to a reduction in computational and memory requirements as the convolutional network operations are defined on the structure of these trees and thus can dynamically allocate resources depending on the structure of the input.
```

our representation enables 3D convolutional networks which are both deep and high resolution. 

Towards this goal, we exploit the **sparsity** in the input data 
- to hierarchically partition the space using a set of unbalanced octrees where each leaf node stores a pooled feature representation


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

## 2. Related Work

we review existing work on **dense** and **sparse** models.

### 2.1 Dense Models

#### A. 3D Shapenets

Wu et al. [48] trained a deep belief network on shapes discretized to a $$30^3$$ voxel grid for object classification, shape completion and next best view prediction.

#### B. VoxNet

Maturana et al. [30] proposed VoxNet, a feed-forward convolutional network for classifying $$32^3$$ voxel volumes from RGB-D data. 

#### C. Boosted voxel nets

In follow-up work, Sedaghat et al. [1] showed that introducing an auxiliary orientation loss increases classification performance over the original VoxNet. 

```
[1] N. S. Alvar, M. Zolfaghari, and T. Brox. Orientation-boosted voxel nets for 3d object recognition. arXiv.org, 1604.03351, 2016.
```

#### D. Point cloud labeling & Deepcontext

Similar models have also been exploited for semantic point cloud labeling [21] and scene context has been integrated in [52].

```
[21] J. Huang and S. You. Point cloud labeling using 3d convolutional neural network. In Proc. of the International Conf. on Pattern Recognition (ICPR), 2016.
[52] Y. Zhang, M. Bai, P. Kohli, S. Izadi, and J. Xiao. Deepcontext: Context-encoding neural pathways for 3d holistic scene understanding. arXiv.org, 1603.04922, 2016.
```

#### E. generative models & auto-encoders

Recently, generative models [37] and auto-encoders [5,40] have demonstrated impressive performance in learning low-dimensional object representations from collections of low-resolution ($$32^3$$) 3D shapes. 

```
[37] D. J. Rezende, S. M. A. Eslami, S. Mohamed, P. Battaglia, M. Jaderberg, and N. Heess. Unsupervised learning of 3d structure from images. arXiv.org, 1607.00662, 2016.
[5] A. Brock, T. Lim, J. M. Ritchie, and N. Weston. Generative and discriminative voxel modeling with convolutional neural networks. arXiv.org, 1608.04236, 2016
[40] A. Sharma, O. Grau, and M. Fritz. Vconv-dae: Deep volumetric shape learning without object labels. arXiv.org, 1604.03755, 2016
```

#### F. 3D-R2N2

Interestingly, these low dimensional representations can be directly inferred from a
single image [15] or a sequence of images [8].

```
[15] R. Girdhar, D. F. Fouhey, M. Rodriguez, and A. Gupta. Learning a predictable and generative vector representation for objects. In Proc. of the European Conf. on Computer
Vision (ECCV), 2016
[8] C. B. Choy, D. Xu, J. Gwak, K. Chen, and S. Savarese. 3dr2n2: A unified approach for single and multi-view 3d object reconstruction. In Proc. of the European Conf. on Computer
Vision (ECCV), 2016.
```

#### G. high-resolution 3D

위에 제안된 방법들은 계산 부하의 문제로 $$30^3$$ voxels로 된 coarse resolution에서만 동작 한다. 

또한 고해상도 Output처리(eg.labeling 3D point clouds)를 위해서는 제한된 receptive field를 가진 비 효율적인 sliding window techniques를 반드시 사용 해야 한다. `Besides, when high-resolution outputs are desired, e.g., for labeling 3D point clouds, inefficient sliding window techniques with a limited receptive field must be adopted [21]. `

해상도를 높히면 네트워크 깊이를 줄여야 한다. `Increasing the resolution na¨ıvely [33-Vnet, 41-Deep sliding, 53-3D Unet] reduces the depth of the networks and hence their expressiveness.`
```
[33] F. Milletari, N. Navab, and S. Ahmadi. V-net: Fully convolutional neural networks for volumetric medical image segmentation. arXiv.org, 1606.04797, 2016
[41] S. Song and J. Xiao. Deep sliding shapes for amodal 3d object detection in RGB-D images. arXiv.org, 1511.02300, 2015
[53] Ozg ¨ un Cicek, A. Abdulkadir, S. S. Lienkamp, T. Brox, and O. Ronneberger. 3d u-net: Learning dense volumetric segmentation from sparse annotation. arXiv.org, 1606.06650,
2016
```

> 하지만, OctNet은 네트워크 깊이를 줄이지 않고도 고해상도를 처리할수 있다. `In contrast, the proposed OctNets allow for training deep architectures at significant higher resolutions.`

### 2.2 Sparse Models

데이터의 sparsity를 이용하는 논문의 수는 많지 않다. `There exist only few network architectures which explicitly exploit sparsity in the data. `

이러한 네트워크는 **exhaustive dense convolutions**를 필요로 하지 않기 때문에 **고해상도**를 다룰수 있다. `As these networks do not require exhaustive dense convolutions they have the potential of handling higher resolutions. `

#### A. 

Engelcke et al. [10] proposed to calculate convolutions at sparse input locations by pushing values to their target locations. 
- This has the potential to reduce the number of convolutions but does not reduce the amount of memory required.
- 3Layer의 낮은 네트워크 : Consequently, their work considers only very shallow networks with up to three layers.

#### B. 

A similar approach is presented in [16, 17] where sparse convolutions are reduced to matrix operations. 

단점 
- Unfortunately, the model only allows for 2 × 2 convolutions and results in indexing and copy overhead which prevents processing volumes of larger resolution (the maximum resolution considered in [16, 17] is $$80^3$$ voxels). 
- Besides, each layer decreases sparsity and thus increases the number of operations, even at a single resolution. 

OctNet와 차이점 : In contrast, the number of operations remains constant in our model.

#### C. 

Li et al. [28] proposed field probing networks which sample 3D data at sparse points before feeding them into fully connected layers. 

- 단점 : While this reduces memory and computation, it does not allow for exploiting the distributed computational power of convolutional networks as field probing layers can not be stacked, convolved or pooled.

#### D. 

Jampani et al. [23] introduced bilateral convolution layers(BCL) which map sparse inputs into permutohedral space where learnt convolutional filters are applied. 

- OctNet과 비슷 : Their work is related to ours with respect to efficiently exploiting the sparsity in the input data. 

- OctNet와 차이점 : However, in contrast to BCL our method is specifically targeted at 3D convolutional networks and can be immediately dropped in as a replacement in existing network architectures.


## 3. Octree Networks


![](https://i.imgur.com/PKBLnEC.png)

