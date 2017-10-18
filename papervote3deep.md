| 논문명 | Vote3Deep: Fast Object Detection in 3D Point Clouds Using Efficient Convolutional Neural Networks |
| --- | --- |
| 저자\(소속\) | Martin Engelcke, D. Z. Wang \(옥스포드\) |
| 학회/년도 | 2016, [논문](https://arxiv.org/abs/1609.06666) |
| 키워드 | Missing Point  |
| 데이터셋(센서)/모델 | KITTI|
| 참고 | [Youtube](https://www.youtube.com/watch?v=WUOSmAfeXIw) |
| 코드 | [Keras](https://github.com/lijiannuist/Vote3Deep_lidar) |

# Vote3Deep

## 1. Introduction

저자의 이전 연구 `Vote3D`\[5\]

* Point clouds are spatially sparse, as most regions are unoccupied
* A feature-centric voting algorithm leveraging the sparsity inherent in these point clouds
* \[5\] proves the equivalence of the voting scheme to a dense convolution operation and demonstrates its effectiveness by discretising point clouds into 3D grids and performing exhaustive 3D sliding window detection with a SVM

```
[5] D. Z. Wang and I. Posner, “Voting for Voting in Online Point Cloud Object Detection,” Robotics Science and Systems, 2015.
```

제안 방식 `Vote3Deep`

* exploit feature-centric voting to build efficient CNNs
* in order to enhance the computational benefits associated with sparse inputs throughout the entire CNN stack, 
  * we demonstrate the benefits of encouraging sparsity in the inputs to intermediate layers by imposing an L1 model regulariser during training

Vote3Deep contributions

* the construction of efficient convolutional layers as basic building blocks for CNN-based point cloud processing by leveraging a `voting mechanis`m to exploit the inherent sparsity in the input data;
* the use of `rectified linear units` and an `L1 sparsity penalty` to specifically encourage data sparsity in the intermediate representations in order to exploit sparse convolutional layers throughout the entire CNN stack.

## 2. RELATED WORK

### 2.1 VeloFCN4VD

A CNN-based approach in \[7\]

* by `projecting the point cloud into a 2D depth map`, with an additional channel for the height of a point from the ground. 

Their model predicts `detection scores` and 20`regresses to bounding boxes`.

However, the projection to a specific viewpoint discards valuable information, which is particularly detrimental, for example, in crowded scenes.

It also requires the `network filters` to learn local dependencies with regards to depth, information that is readily available in a 3D representation and which can be efficiently extracted with sparse convolutions.

```
[7] B. Li, T. Zhang, and T. Xia, “Vehicle Detection from 3D Lidar Using Fully Convolutional Network,” arXiv preprint arXiv:1608.07916, 2016.
```

### 2.2 VoxNet & Landing Zone

Dense 3D occupancy grids obtained from point clouds are processed with CNNs in \[8\] and \[9\].

With a minimum cell size of 0.1m, \[8\] reports a speed of 6ms on a GPU to classify a single crop with a grid-size of 32×32×32 cells.

Similarly, a processing time of 5ms per $$m^3$$ for landing zone detection is reported in \[9\].

With 3D point clouds often being larger than 60m × 60m × 5m, this would result in a processing time of $$60×60×5×5×10^{−3} = 90s$$ per frame, which does not comply with speed requirements typically encountered in robotics applications.

```
[8] D. Maturana and S. Scherer, “VoxNet: A 3D Convolutional Neural Network for Real-Time Object Recognition,” IROS, pp. 922–928, 2015.
[9] “3D Convolutional Neural Networks for Landing Zone Detection from LiDAR,” International Conference on Robotics and Automation, no. Figure 1, pp. 3471–3478, 2015
```

### 2.3 Sparse 3D

An alternative approach that takes advantage of sparse representations can be found in \[10\] and \[11\], in which sparse convolutions are applied to comparatively small 2D  
and 3D crops respectively.

While the convolutional kernels  
 are only applied at sparse feature locations, the presented algorithm still has to consider neighbouring values which take a value of either zero or a constant bias, leading to unnecessary operations and memory consumption.

Another method for performing sparse convolutions is introduced in \[12\] who make use of “permutohedral lattices”, but only consider comparatively small inputs, as opposed to our work.

```
[10] B. Graham, “Spatially-sparse convolutional neural networks,” arXiv Preprint arXiv:1409.6070, pp. 1–13, 2014
[11] “Sparse 3D convolutional neural networks,” arXiv preprint arXiv:1505.02890, pp. 1–10, 2015.
[12] V. Jampani, M. Kiefel, and P. V. Gehler, “Learning Sparse High Dimensional Filters: Image Filtering, Dense CRFs and Bilateral Neural Networks,” in IEEE Conf. on Computer Vision and Pattern Recognition (CVPR), 2016
```

### 2.4 biomedical image analysis

CNNs have also been applied to dense 3D data in biomedical image analysis \(e.g. \[13\], \[14\], \[15\]\).

A 3D equivalent of residual networks \[4\] is utilised in \[13\] for brain image segmentation.

A cascaded model with two stages is proposed in \[14\] for detecting cerebral microbleeds.

A combination of three CNNs is suggested in \[15\].

Each CNN processes a different 2D plane and the three streams are joined in the last layer.

These systems run on relatively small inputs and in some cases take more than a minute for processing a single frame with GPU acceleration.

## 3. METHODS



