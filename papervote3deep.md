| 논문명 | Vote3Deep: Fast Object Detection in 3D Point Clouds Using Efficient Convolutional Neural Networks |
| --- | --- |
| 저자\(소속\) | Martin Engelcke, D. Z. Wang \(옥스포드\) |
| 학회/년도 | Sep 2016~Mar 2017, ICRA2017, [논문](https://arxiv.org/abs/1609.06666) |
| 키워드 | Martin2017, Missing Point  |
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

> 3D 데이터의 희박한 밀도를 역으로 이용하는 논문들 

An alternative approach that **takes advantage** of sparse representations can be found in \[10\] and \[11\], in which sparse convolutions are applied to comparatively small 2D and 3D crops respectively.

While the convolutional kernels are only applied at sparse feature locations, the presented algorithm still has to consider neighbouring values which take a value of either zero or a constant bias, leading to unnecessary operations and memory consumption.

Another method for performing sparse convolutions is introduced in \[12\] who make use of “permutohedral lattices”, but only consider comparatively small inputs, as opposed to our work.

```
[10] B. Graham, “Spatially-sparse convolutional neural networks,” arXiv Preprint arXiv:1409.6070, pp. 1–13, 2014
[11] “Sparse 3D convolutional neural networks,” arXiv preprint arXiv:1505.02890, pp. 1–10, 2015.
[12] V. Jampani, M. Kiefel, and P. V. Gehler, “Learning Sparse High Dimensional Filters: Image Filtering, Dense CRFs and Bilateral Neural Networks,” in IEEE Conf. on Computer Vision and Pattern Recognition (CVPR), 2016
```

### 2.4 biomedical image analysis 

> 의료 데이터 분석에 쓰임


## 3. METHODS

본 장에서는 sparse 3D를 입력으로 하여 물체 탐지 하는 방법에 대하여 살펴 본다. `This section describes the application of convolutionalneural networks for the prediction of detection scores from sparse 3D input grids of variable sizes. `

###### [sparse 3D grid & Feature Vector]

- 포인트 클라우드는 입력으로 **sparse 3D grid**를 취한다. `As the input to the network, a point cloud is discretised into a sparse 3D grid as in [5]. `
	- 각 셀은 non-zero number를 가진다. 특징벡터는 통계처리후 값이 입력된다. `For each cell that contains a non-zero number of points, a feature vector is extracted based on the statistics of the points in the cell. `

- 특징 벡터는 **이진 occupancy 값**, **반사값의 평균, 편차**, **three shape factors 값**이다. `The feature vector holds a binary occupancy value, the mean and variance of the reflectance values and three shape factors.` 

- sparse representation가 되는 빈 공간은 저장 되지 않는다. `Cells in empty space are not stored which leads to a sparse representation.`

###### [제안 방식의 동작 과정 Overview ]

- 제안 방식은 **투표**방식을 **원래의 3D representation**에 적용하여 **새로운 sparse 3D representation**을 생성한다. `We employ the voting scheme from [5] to perform a sparse convolution across this native 3D representation, followed by a ReLU non-linearity, which returns a new sparse 3D representation. `


- 이 절차는 반복적으로 진행되며 예측된 탐지 점수(detection scores)도 같이 누적된다. `This process can be repeated and stacked as in a traditional CNN, with the output layer predicting the detection scores.`


- [5]와 동일하게 CNN은 N개의 다른 회전 각도에 적용된다. `Similar to [5], a CNN is applied to a point cloud at N different angular orientations in N parallel threads to handle objects at different orientations at a minimal increase in computation time. `

- 중복 탐지는 NMS로 가지치기 된다. `Duplicate detections are pruned with non-maximum suppression (NMS) in 3D space. `
	- NMS in 3D is better able to handle objects that are behind each other as the 3D bounding boxes overlap less than their 2D projections.

- 가정 사항 및 제약 = **fixed-size bounding box**
	- Based on the premise that bounding boxes in 3D spaceare similar in size for object instances of the same class, 
    - we assume a fixed-size bounding box for each class, whiche liminates the need to regress the size of a bounding box.

- We select 3D bounding box dimensions for each class of interest based on the 95th percen tile ground truth bounding box size over the training set.

- The receptive field of a network should be at least as large as the bounding box of an object, but not excessively large which would waste computation time. 

- We therefore employ several class-specific networks which can be run in parallel at test time, each with a different total receptive field size depending on the object class. 

- In principle, it is possible to compute detection scores for multiple classes with a singlenetwork; a task left for future work.

### 3.1 Sparse Convolutions via Voting

- 조밀한 3D CNN을 포인트 클라우드에 적용하면 ` multiplications by zero`연산으로 인해 대부분의 시간이 소모 된다. 더구나, 3rd 공간 연산으로 인해 2D에 비하여 더 연산 부하가 걸린다. `When running a dense 3D convolution across a discretised point cloud, most of the computation time is wasted as the majority of operations are multiplications by zero. The additional third spatial dimension makes this process even more computationally expensive compared to 2D convolutions, which form the basis of image-based CNNs.`

- 이점에 착안하여 3D features가 non-zero인것에서만 연산을 수행하는 feature-centric voting scheme[5]가 제안 되었다. `Using the insight that meaningful computation only takes place where the 3D features are non-zero, [5] introduce a feature-centric voting scheme. `


- 이 **알고리즘의 기본**은 : The basis of this algorithm is the idea of letting each non-zero input feature vector cast a set of votes, weighted by the filter weights, to its surrounding cells in the output layer, as defined by the receptive field of the filter. 
	- The **voting weights** are obtained by flipping the convolutional filter kernel along each spatial dimension. 

The final convolution result is obtained by accumulating the votes falling into each cell of the output (Fig. 2).

![](https://i.imgur.com/IHaeN8w.png)
```
[Fig. 2. An illustration of the voting procedure on a sparse 2D example input
without a bias.]
- The voting weights are obtained by flipping the convolutional weights along each dimension. 
- Whereas a standard convolution applies the filter at every location in the input, the equivalent voting procedure only needs to be applied at each non-zero location to compute the same result.
- Instead of a 2D grid with a single feature, Vote3Deep applies the voting procedure to 3D inputs with several feature maps. 
- For a full mathematical justification, the reader is referred to [5]. Best viewed in colour.
```

This procedure can be formally stated as follows. 
- Without loss of generality, assume we have one 3D convolutional filter with odd-valued kernel dimensions in network layer $$c$$, operating on a single input feature, with the filter weights denoted by $$w^c \in \Re^{(2I+1)\times(2J+1)\times(2K+1)}$$

Then, for an input grid $$h^{c−1} \in \Re^{L \times M \times N}, the convolution result at location
$$(l, m, n)$$ is given by:

![](https://i.imgur.com/WIeqRi1.png)

- $$b^c$$ : is a bias value applied to all cells in the grid. 

This operation needs to be applied to all $$L × M × N$$ locations
in the input grid for a regular dense convolution. 

In contrast to this, given the set of cell indices for all of the non-zero
cells $$ \Phi = \left\{\left(l,m,n\right)\forall h^{c-1}_{l,m,n} \ne 0 \right\} $$

the convolution can be recast as a feature-centric voting operation, with each input
cell casting votes to increment the values in neighbouring cell locations according to:

![](https://i.imgur.com/me1dr1w.png)

which is repeated for all tuples $$(l,m,n) \in \Phi $$ and where $$\{i,j,k \in Z \mid i \in \[-I,I\], j \in \[-J, J\], k \in \[-K, K\] \}$$

**Voting**의 결과물은 ReLU를 통과 하여 양수가 아닌것들은 버려진다. `The voting output is passed through a ReLU non-linearity which discards non-positive features as described in the next subsection. `


Crucially, the biases are constrained to be nonpositive as a single positive bias would return an output grid in which almost every cell is occupied with a feature vector, hence eliminating sparsity. 

The bias $$b^c$$ therefore only needs to be added to each non-empty output cell.

With this sparse voting scheme, the filter only needs to be applied to the occupied cells in the input grid, rather than convolved over the entire grid. 

더 자세한 알고리즘 내용은 [5]에 기술 되어 있다. `The algorithm is described in more detail in [5], including formal proof that feature-centric voting is equivalent to an exhaustive convolution`



### 3.2 Maintaining Sparsity with ReLUs


> 추후 확인 

## 4. TRAINING

-  고정된 B.Box를 사용하기 때문에 바로 적용하기 쉽다. `Due to the use of fixed-size bounding boxes, networks can be directly trained on 3D crops of positive and negative examples whose dimensions equal the receptive field size specified by the architecture.`

- Negative training examples are obtained by performing hard negative mining periodically after a fixed number of training epochs. 

- 이진 분류기를 사용하며 Loss로는 **linear hinge loss**를 채택 하였다. `The class-specific networks are binary classifiers and we choose a linear hinge loss for training due to its maximum margin property.`


### 4.1 Linear Hinge Loss


### 4.2 L1 Sparsity Penalty

## 5. EXPERIMENTS


### 5.1 Dataset 

- KITTI 사용 
- We only use the 3D point cloud data to train and test the models.

### 5.2 Evaluation

### 5.3  Training






