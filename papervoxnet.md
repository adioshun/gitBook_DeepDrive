| 논문명 | VoxNet: A 3D Convolutional Neural Network for Real-Time Object Recognition |
| --- | --- |
| 저자\(소속\) | Daniel Maturana \(CMU\) |
| 학회/년도 | IROS 2015, [논문](http://ieeexplore.ieee.org/document/7353481/) |
| 키워드 | Daniel2015, Volumetric Occupancy Grid + 3D CNN, LiDAR와 비교 실험\(결과는?\) |
| 데이터셋/모델 | Sydney Urban Objects\(차량 고려\), NYUv2, ModelNet40 |
| 참고 | 이전연구: 3D convolutional neural networks for landing zone detection from lidar,” in ICRA, 2015. |
| 코드 | [Theano+Lasagne](https://github.com/dimatura/voxnet) |






# VoxNet

## 0. Abstract

* Range sensors such as LiDAR and RGBD cameras가 많이 사용되고 있다.

* 하지만 large amounts of point cloud data를 충분히 활용하고 있지 않다.

* VoxNet을 제안 : integrating a `volumetric Occupancy Grid` representation with a supervised 3D Convolutional Neural Network \(3D CNN\).

## 1. Introduction

본 논문에서는 `3D point cloud segment`를 이용하여서 `object 분류`의 문제점\(eg. background clutter\)을 살펴 본다.

원인 : 작업 Pipe-line

* extraction and aggregation of hand-engineered features
* fed into an off-the-shelf classifier such as SVMs.

이러한 Pipe-line은 2D `object 분류`와도 비슷하다.

* CNN의 발전으로 데이터를 활용하는 방향으로 바뀌었다. 
* 3D 기본은 같으므로 변경이 가능하다. 단, 계산 부하가 크다. 

## 2. 관련 연구

### 2.1 Object Recognition with Point Cloud Data

3D point clouds를 이용한 물체 인식은 많은 연구가 있다.

기존 연구 : hand-crafted features\(or descriptors\) + machine learning classifier \(\[10\], \[11\],\[12\], \[13\]\).

* The situation is similar for semantic segmentation,with structured output classifiers instead of single output classifiers \(\[14\], \[15\], \[16\]\). 

제안 방식 : extract features and classify objects from the `raw volumetric data`.

* Our volumetric representation is also** richer than point clouds**, as it distinguishes free space  
  from unknown space.

* In addition, features based on point clouds often require spatial neighborhood queries, which can quickly become intractable\(고치기 어려운\) with large numbers of points.

```
[10] A. Frome, D. Huber, and R. Kolluri, “Recognizing objects in range data using regional point descriptors,” ECCV, vol. 1, pp. 1–14, 2004.
[11] J. Behley, V. Steinhage, and A. B. Cremers, “Performance of histogram descriptors for the classification of 3D laser range data in urban environments,” in ICRA, 2012, pp. 4391–4398.
[12] A. Teichman, J. Levinson, and S. Thrun, “Towards 3D object recognition via classification of arbitrary object tracks,” in ICRA, 2011, pp. 4034–4041.
[13] A. Golovinskiy, V. G. Kim, and T. Funkhouser, “Shape-based recognition of 3D point clouds in urban environments,” ICCV, 2009.
[14] D. Munoz, N. Vandapel, and M. Hebert, “Onboard contextual classification of 3-D point clouds with learned high-order markov random fields,” in ICRA, 2009.
[15] H. Koppula, “Semantic labeling of 3D point clouds for indoor scenes,”NIPS, 2011.
[16] X. Ren, L. Bo, and D. Fox, “RGB-(D) scene labeling: Features and algorithms,” in CVPR, 2012.
```

### 2.2 2.5D Convolutional Neural Networks

#### A. RGBD

이미지\(RGB\)에서 사용한 CNN기법을 RGBD로 확장하려는 연구가 진행 되었다. \[17\], \[18\], \[19\], \[20\]

* 간단한 접근법은 D를 또 다른 채널로 간주하고 처리 하는 것이다. 
* 단점 \#1 : geometric information를 제대로 활용 못함 
* 단점 \#2 : integrate information across viewpoints하기 어려움 

```
[17] I. Lenz, H. Lee, and A. Saxena, “Deep learning for detecting robotic grasps,” in RSS, 2013.
[18] Richard Socher and Brody Huval and Bharath Bhat and Christopher D.Manning and Andrew Y. Ng, “Convolutional-Recursive Deep Learning for 3D Object Classification,” in NIPS, 2012.
[19] L. A. Alexandre, “3D object recognition using convolutional neural networks with transfer learning between input channels,” in IAS, vol. 301, 2014.
[20] N. Hoft, H. Schulz, and S. Behnke, “Fast semantic segmentation of RGBD scenes with gpu-accelerated deep neural networks,” in 37th Annual German Conference on AI, 2014, pp. 80–85.
```

#### B. LiDAR

* \[4\] propose a feature that locally describes scans with a 2.5D representation,

* \[21\] studies this approach in combination with a form of unsupervised feature learning.

* \[22\] propose an encoding that makes better use of the 3D information in the depth, but is still 2D-centric.

```
[4] A. Quadros, J. Underwood, and B. Douillard, “An occlusion-aware feature for range images,” in ICRA, May 14-18 2012.
[21] M. De Deuge, A. Quadros, C. Hung, and B. Douillard, “Unsupervised feature learning for classification of outdoor 3d scans,” in ACRA, 2013.
[22] S. Gupta, R. Girshick, P. Arbelaez, and J. Malik, “Learning rich features ´from RGB-D images for object detection and segmentation,” in ECCV, 2014.
```

### 2.3 3D Convolutional Neural Networks

비디오 분석에서는 3D CNN이 성공적으로 적용 되었다. \(\[23\], \[24\]\)

* 하지만 이때는 `시간 정보`가 3rd D로 작용하였다. 
* 알고림적으로 논문의 제안 방식과 비슷하지만, 사용되는 데이터 속성이 다르다. 

#### A. RGBD

* \[25\] uses an unsupervised volumetric feature learning approach as part of a pipeline to detect indoor objects.

  * This approach is based on `sparse coding`, which is generally slower than convolutional models. 

* \[26\] propose a generative 3D convolutional model of shape and apply it to RGBD object recognition, among other tasks.

```
[25] K. Lai, L. Bo, and D. Fox, “Unsupervised feature learning for 3D scene labeling,” in ICRA, 2014.
[26] Z. Wu, S. Song, A. Khosla, F. Yu, L. Zhang, X. Tang, and J. Xiao, “3d shapenets: A deep representation for volumetric shape modeling,” in CVPR, 2015.
```

#### B. LiDAR

* \[27\] is an early work that studies a3D CNN for use with LiDAR data with a binary classification task.

* \[28\], which introduced 3D CNNs for landing zone detection in UAVs.

  * Compared to this work, we tackle a more general objectre cognition task with 3D data from different modalities. 

We also study different representations of occupancy and propose techniques to improve performance when the data varies significantly in scale and orientation

```
[27] D. Prokhorov, “A convolutional learning system for object classification in 3-D lidar data,” IEEE TNN, vol. 21, no. 5, pp. 858–863, May 2010.
[28] D. Maturana and S. Scherer, “3D convolutional neural networks for landing zone detection from lidar,” in ICRA, 2015.
```

## 3. Approach

* 입력 : The input to our algorithm is a **point cloud segment**, 
  * which can originate from segmentation methods such as \[12\], \[29\],or a “sliding box” if performing detection. 

> The **segment** is usually given by the **intersection of a point cloud** with a **bounding box** and may include **background clutter**.

* 본 제안 기능 : 물체 분류 예측 `Our task is to predict an object class label for the segment.`

* 본 제안 요소\(2가지\) `Our system for this task has two main components:`

  * A **volumetric grid representing** our estimate of spatial occupancy, 
  * A **3DCNN** that predicts a class label directly from the occupancy grid. 

### 3.1 Volumetric Occupancy Grid

#### A. Occupancy grids \(\[30\], \[31\]\)

* **Represent** the state of the environment as a 3D lattice\(격차\) of random variables \(each corresponding to a voxel\) 
* **Maintain** a probabilistic estimate of their occupancy as a function of incoming sensor data and prior knowledge.

#### B. occupancy grids를 사용하는 이유\(2가지\)

1번째 이유

* they allow us to efficiently estimate **free**, **occupied** and **unknown space** from range measurements, even for measurements coming from different viewpoints and time instants.

* 제안 방식은 포인트 클라우드 처럼 `occupied space VS. free space`만 고려 하는 방식 보다 정보량이 풍부하다. 왜냐 하면 free and unknown space를 구분하는 것은 향후 중요한 정보가 될수 있기 때문이다.

  * `This representation is richer than those which only consider occupied space versus free space such as point clouds, as the distinction between free and unknown space can potentially be a valuable shape cue.`

2번째 이유

* they can be stored and manipulated with simple and efficient data structures. 

### 3.2 Reference frame and resolution

* In our volumetric representation, **each point \(x, y, z\)** is mapped to **discrete voxel coordinates \(i, j, k\)**.

  * 맵핑은 아래 3가지 요소에 Depend하다. The mapping is a uniform discretization but depends on the **origin**, **orientation** and **resolution **of the voxel grid in space.

  * 복셀화된 물체의 외관은 위 3가지가 중요한 요소를 끼치기 때문이다. . `The appearance of the voxelized objects depends heavily on these parameters.`

###### \[For the origin\]

* we assume it is given as an input, e.g.obtained by a segmentation algorithm or given by a sliding box.

###### \[For the orientation\]

* we assume that the z axis of the grid frame is approximately aligned with the direction of gravity.

* This can be achieved with an IMU or simply keeping the sensor upright.

* This still leaves a degree of freedom, the rotation around the z axis \(yaw\).

* If we defined a canonical orientation for each object and were capable of detecting this orientation automatically, it would be reasonable to always align the grid to this orientation.

* However, it is often non-trivial in practice to detect this orientation from sparse and noisy point clouds.

* In this paper we propose a simple alternative based on data augmentation, discussed in III-F.

###### \[For the resolution\]

we adopt two strategies, depending on the dataset.

* For our LiDAR dataset: we use a fixed spatial resolution, `e.g. a voxels of (0.1 m)^3`.

* For the other datasets: the resolution is chosen so the object of interest occupies a subvolume of `24 × 24 × 24` voxels.

> In all experiments we use a fixed occupancy grid of size `32 × 32 × 32` voxels.

The trade-off between these two strategies is that

* **in the first case**, we maintain the information given by the relative scale of objects `(e.g., cars and persons tend to have a consistent physical size)`; 
* **in the second case**, we avoid loss of shape information when the voxels are too small `(so that the object is larger than the grid)` or when the voxels are too large `(so that details are lost by aliasing)`.

### 3.3 Occupancy model

* Let $$\{z^t\}^T_{t=1}$$ be a sequence of range measurements that either hit \($$z^t = 1$$\) or pass through \($$z^t = 0$$\) a given voxel with coordinates \(i, j, k\).

* Assuming an ideal beam sensor model, we use 3D ray tracing \[32\] to calculate the number of hits and pass-throughs for each voxel.

* 3가지의 **occupancy grid models** 정의 `Given this information, we consider three different occupancy grid models to estimate occupancy:`

#### A. Binary occupancy grid

In this model, each voxel is assumed to have a binary state, occupied or unoccupied.

The probabilistic estimate of occupancy for each voxel is computed with log odds for numerical stability.

Using the formulation from \[31\], we update each voxel traversed by the beam as


$$
l^t_{ijk} = l^{t-1}_{ijk} + z^tl_{occ} + (1-z^t)l_{free}
$$


* $$l_{occ}$$: the log odds of the cell being occupied, \[33\]참고하여 1.38 설정 
* $$l_{free}$$: free given that the measurement hit or missed the cell, \[33\]참고하여 -1.38설정

Empirically we found that within reasonable ranges these parameters had little effect on the final outcome.

* The initial probability of occupancy is set to 0.5, or $$l^0_{ijk}=0$$

* In this case, the network acts on the log odd values $$l_{ijk}=0$$

#### B. Density grid

In this model each voxel is assumed to have a continuous density, corresponding to the probability the voxel would block a sensor beam.

> 자세한 내용 생략

#### C. Hit grid

This model only consider hits, and ignores the difference between unknown and free space.

> 자세한 내용 생략

### 3.4 3D Convolutional Network Layers

CNN을 사용한 3가지 이유 `There are three main reasons CNNs are an attractive option for our task.`

###### \[1번째 이유\]

* First, they can explicitly make use of the spatial structure of our problem.

* In particular, they can learn local spatial filters useful to the classification task.

* In our case, we expect the filters at the input level to encode spatial structures such as planes and corners at different orientations.

###### \[2번째 이유\]

* Second, by stacking multiple layers the network can construct a hierarchy of more complex features representing larger regions of space, eventually leading to a global label for the input occupancy grid. 

###### \[3번째 이유\]

* Finally, inference is purely feed-foward and can be performed efficiently with commodity graphics hardware.

![](http://i.imgur.com/yXb89IB.png)

###### \[Input Layer\]

* This layer accepts a fixed-size grid of I×J×K voxels. In this work, we use I = J = K = 32.

* Depending on the occupancy model, each value for each grid cell is updated from Equation 1\(Binary Occupancy grid model\), Equation 2\(Density Grid Model\) or Equation 3\(Hit Grid Model\).

* In all three cases we subtract 0.5 and multiply by 2, so the input is in the\(−1, 1\) range; no further preprocessing is done.

* While this work only considers scalar-valued inputs, our implementation can trivially accept additional values per cell, such as LiDAR intensity values or RGB information from cameras.

###### \[Convolutional Layers $$C(f, d, s)$$\]

* These layers accept four dimensional input volumes in which three of the dimensions are spatial, and the fourth contains the feature maps.

* The layer creates $$f$$ feature maps by convolving the input with $$f$$ learned filters of shape `d × d × d × f'`, where d are the spatial dimensions and `f'`is the number of input feature maps.

* Convolution can also be applied at a spatial stride `s`.

* The output is passed through a leaky rectified nonlinearity unit\(ReLU\) \[35\] with parameter 0.1.

###### \[Pooling Layers $$P(m)$$\]

* These layers down-sample the input volume by a factor of by m along the spatial dimensions by replacing each m × m × m non-overlapping block of voxel swith their maximum.

###### \[Fully Connected Layer $$FC(n)$$\]

* Fully connected layers haven output neurons.

* The output of each neuron is a learned linear combination of all the outputs from the previous layer,passed through a nonlinearity.

* We use ReLUs save for the final output layer, where the number of outputs corresponds to the number of class labels and a softmax nonlinearity is used to provide a probabilistic output.

### 3.5 Proposed architecture

* 이전 연구에서 LiDAR데이터를 가지고 적합한 모델을 찾기 위해 수백번의 실험을 진행 하였다. `in our previous work [28] we performed extensive stochastic search over hundreds of 3D CNN architectures on a simple classification task on simulated LiDAR data.`

```
[28] D. Maturana and S. Scherer, “3D convolutional neural networks for
landing zone detection from lidar,” in ICRA, 2015.
```

* Several of the best-performing networks had a small number of parameters in comparison to state of the art networks used for imagedata;

* \[7\] has around 60 million parameters, while the majority of our best models used less than 2 million.

* While it is difficult to compare these numbers meaningfully, given the vast differences in tasks and datasets, we speculate that volumetric classification for point clouds is in some sense a simpler task, as many of the factors of variation in image data \(perspective, illumination, viewpoint effects\) are diminished or not present.

* Guided by this precedent, our base model, VoxNet, is **C\(32, 5, 2\)−C\(32, 3, 1\)−P\(2\)−F C\(128\)−F C\(K\)**,

  * K is number of classes. 

* VoxNet is essentially a simpler version of the two-stage model reported in \[28\].

* The changes aimed to reduce the number of parameters and increase computational efficiency, making the network easier and faster to learn.

* The model has 921736 parameters, most of them from inputs to the first dense layer.

### 3.6 Rotation Augmentation and Voting

* 일관된 **orientation** 을 유지 하는것은 중요하다. `it is nontrivial(중대한) to maintain a consistent orientation of objects around their z axis.`

* 문제 해결을 위해 기존에는 **rotationally invariant**하도록 설게 되었다. `To counter this problem, many features for point clouds are designed to be rotationally invariant (e.g. [36], [37]).`

* 문제 해결을 위해 본 논문은 built-in된 대처 알고리즘은 없지만 다른 방법으로 문제를 해결 하였다. `Our representation has no built-in invariance to large rotations;`

  * **At training time**, we augment the dataset with by creating `n` copies of each input instance, each rotated 360◦/n intervals around the z axis. 
  * **At testing time**, we pool the activations of the output layer over all `n` copies. 
  * 본 논문에서 `n`값은 12 or 18. 

* 보팅방법과 비슷 : This can be seen as a **voting approach**, similar to how networks such as \[7\] average predictions over random crops and flips of the input image;

  * 다른점 : however, it is performed over an exhaustive sampling of rotations, not a random selection

* 제안 방식은 아래에서 영감을 받았다. This approach is inspired by the interpretation of convolution as weight sharing across translations; implicitly, we are sharing weights across rotations.

* 초반에는 Initial versions of this approach were implemented by max-pooling or mean-pooling the dense layers of the network during training in the same way as during test time.

* 추후 수정 하였다. However, we found that the approach described above yielded comparable results while converging noticeably faster.

### 3.7 Multiresolution Input

* LiDAR 데이터에서 탐지를 위해서는 $$0.2 m^3$$정도 Resolution가 필요 하다고 제안되고 있다. `Visual inspection of the LiDAR dataset suggested a(0.2 m^3) resolution preserves all necessary information for the classification, while allowing sufficient spatial context for most larger objects such as trucks and trees.`

* 우리가 세운 가설은 **좋은 해상도**는 판별력을 더 좋게 할수 있다. `However, we hypothesized that a finer resolution would help in discriminating other classes such as traffic signs and traffic lights, especially for sparser data.`

* 따라서 **Foveal **구조\[24\]를 참고 삼아 **multiresolution VoxNet**를 구현 하였다. `Therefore, we implemented a multiresolution VoxNet, inspired by the “foveal” architecture of [24] for video analysis.`

  * 이 모델에서는 두개의 동일한 VoxNet 네트워크에 서로 다른 해상도의 occupancy grids를 입력으로 하였다. `In this model we use two networks with an identical VoxNet architectures, each receiving occupancy grids at different resolutions`: $$0.1m^3$$and $$0.2m^3$$. 
  * 두 입력의 중심점은 같지만 `Both inputs are centered on the same location`, 
    * but the **coarser network** covers a **larger area** at low resolution 
    * while the **finer network** covers a **smaller area** at high resolution. 
  * 두 출력을 합치는 법 : `To fuse the information from both networks,` 
    * we concatenate the outputs of their respective FC\(128\) layers 
    * and connect them to a softmax output layer.

 \[24\] A. Karpathy, G. Toderici, S. Shetty, T. Leung, R. Sukthankar, and L. Fei-Fei, “Large-scale video classification with convolutional neural networks,” in CVPR, 2014.



### 3.8 Network training details

* Training of the network parameters is performed by **Stochastic Gradient Descent \(SGD\)** with momentum.

* The objective is the multinomial negative log-likelihood plus 0.001 times the L2 weight norm for regularization.

* SGD is initialized with a learning rate of

  * 0.01 for the LiDAR dataset 
  * 0.001 in the the other datasets. 

* The momentum parameter was 0.9.

* Batch size is 32.

* The learning rate was decreased by a factor of 10 each 8000 batches for the LiDAR dataset and each 40000 batches in the other datasets.

* Dropout regularization is added after the output of each layer.

* Convolutional layers were **initialized** with the method proposed by \[38\], whereas dense layers were initialized from a zero-mean Gaussian with σ = 0.01.

* Following common practices for CNN training, we augment the data by adding randomly perturbed copies of each instance.

  * The perturbed\(교란\) copies are generated dynamically during training and consist of randomly mirrored and shifted instances. 

* Mirroring is done by along the x and y axes; shifting is done between −2 to 2 voxels along all axes.

* 구현 언어 :  Our implementation uses a combination of C++ and Python.

* 라이브러리 : The Lasagne library was used to compute gradients and accelerate computations on the GPU.

* 학습 소요 시간 : The training process takes around 6 to 12 hours on our K40 GPU, depending on the complexity of the network.

## 4. EXPERIMENTS

To evaluate VoxNet we consider benchmarks with data from three different domains:

* LiDAR point clouds : Sydney Objects Dataset
* RGBD point clouds : NYUv2
* CAD models : ModelNet40

### 4.1 LiDAR

* Sydney데이터셋 설명 : labeled Velodyne LiDAR scans of 631 urban objects in 26 categories.

* Sydney데이터셋 선택 이유: We chose this dataset for evaluation as it provides labeled object instances and the LiDAR viewpoint, which is used to compute occupancy.

* When voxelizing the point cloud we use all points in a bounding box around the object, including background clutter.

* 평가 요소 : F1 값 `We report the average F1 score, weighted by class support, for a subset of 14 classes over four standard training/testing splits.`

* 데이터 증가 및 보팅 실시 : For this dataset we perform augmentation and voting with 18 rotations per instance.

### 4.2 CAD data

> 제외

### 4.3 RGBD data

> 제외


---

```
LiDAR + RGB + CAD
Dense 3D occupancy grids obtained from point clouds are processed with CNNs in VoxNet

```

```
- **voxelization **기법에 대한 다양한 연구도 진행 되었다. `Other authors have explored variations of voxelization methods including, `
    - binary occupancy grid, 
    - density grid, 
    - hitgrid. 

- VoxNet에서는 위 다양한 방식에 대한 테스트가 진행 되었다. `In VoxNet, Maturana and Scherer (2015) tested each voxelization model individually, to train 3D-CNN swith 32x32x32 grid inputs. `
    - To handle multi-resolution inputs, they trained two separate networks each receiving an occupancy grid with different resolution Parallel development of both multiview and volumetric CNNs has resulted in an empirical performance gap.
```









```
Maturana and Scherer have also employed volumetric (i.e., spatially 3D) representation of the 3D data to perform 3D object recognition [Maturana and Scherer 2015].+

- In the proposed VoxNet architecture, a volumetric occupancy grid of size 32×32× 32 voxels was at first generated from a point cloud’s segment that was then given as input to a CNN.
- The employed network was constructed using two convolutional (with 3D filters), one pooling, and two FC layers, while it was trained using SGD with momentum.
- An object class label was finally predicted for each seg-ment.
- Data from three different domains were used for evaluating VoxNet.
. LIDAR data point clouds
. RGB-D point clouds
. CAD models

```


```
A similar approach is VoxNet [24], which also uses binary voxel grids and a corresponding 3D CNN architecture.

```

```
The advantage of these approaches is that it can process different sources of 3D data, including LiDAR point clouds, RGB-D point clouds, and CAD models; we likewise follow this direction. [중요] 3DShapeNets & VoxNet = LiDAR 데이터에도 적용할수 있다는 장점이 있다.

```


```
Dense 3D occupancy grids obtained from point clouds are processed with CNNs in [8-Voxnet] and [9-Daniel2015a=Landingzone].+

With a minimum cell size of 0.1m, [8-Voxnet] reports a speed of 6ms on a GPU to classify a single crop with a grid-size of 32×32×32 cells.
Similarly, a processing time of 5ms per $$m^3$$ for landing zone detection is reported in [9].
With 3D point clouds often being larger than 60m × 60m × 5m, this would result in a processing time of $$60×60×5×5×10^{−3} = 90s$$ per frame, which does not comply with speed requirements typically encountered in robotics applications.
```


```
[16] introduced `Voxnet, a 3D CNN for 3D point cloud data and voxelized models, which performed significantly better than[27].
```

```
Recently CNNs have been applied to 3D shapes by representing them as 3D occupancy grids, and building generative [39-ShapeNet]or discriminative [26-VoxNet] networks.

```

```
VoxNet [13] introduces three different occupancy grids (32 × 32 × 32 voxels) that employ 3D ray tracing to compute the number of beams hitting or passing each voxel and then use that information to compute the value of each voxel depending on the chosen model: +

- a binary occupancy grid using probabilistic estimates,
- a density grid in which each voxel holds a value corresponding to the probability that it will block a sensor beam,
- a hit grid that only considers hits thus ignoring empty or unknown space.

The binary and density grids proposed by Maturana et al[13]. differentiate unknown and empty space, whilst the hit grid and the binary tensor do not.
```


```
Volumetric CNNs: [28-ShapeNet, 17-VoxNet, 18-VMCNN] are the pioneers applying 3D convolutional neural networks on voxelized shapes. However, volumetric representation is constrained by its resolution due to data sparsity and computation cost of 3D convolution.

```


```
[VoxNet (확장버젼)] boosted VoxNet

Sedaghat et al. [2016] modified VoxNet’s architecture in such a way that the object’s orientation was taken into account.
In their final model, the class labels were extracted directly from the orientation activations.


[boosted VoxNet] N. Sedaghat, M. Zolfaghari, and Th. Brox. 2016. Orientation-boosted voxel nets for 3D object recognition. CoRR abs/1604.03351 (2016).

```

```
[VoxNet (이전연구)] 3D convolutional neural networks for landing zone detection from lidar (Daniel2015a)


[Daniel2015a] propose a generative 3D convolutional model of shape and apply it to RGBD object recognition, among other tasks.
```
