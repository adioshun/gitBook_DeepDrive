|논문명|SqueezeSeg: Convolutional Neural Nets with Recurrent CRF for Real-Time Road-Object Segmentation from 3D LiDAR Point Cloud|
|-|-|
|저자(소속)|Bichen Wu (Berkeley)|
|학회/년도| arXiv 2017, [논문](https://arxiv.org/abs/1710.07368v1)|
|키워드| |
|참고|[Youtube](https://www.youtube.com/watch?v=Xyn5Zd3lm6s)|
|코드||


# SqueezeSeg

- 입력 : 3D LiDAR -> Segmentation `In this paper, we address semantic segmentation of road-objects from 3D LiDAR point clouds. `

- We formulate this problem as a **point wise classification problem**

- propose an end-to-end pipeline called **SqueezeSeg** based on convolutional neural networks(CNN): 

- 입력 : LiDAR Point cloud -> 출력 : point-wise label map -> refined -> Instance-level labels
-  the CNN takes a transformed **LiDAR point cloud** as input and directly outputs a **point-wise label map**,
	-  which is then refined by a **conditional random field (CRF)** implemented as a recurrent layer. 
	- **Instance-level labels** are then obtained by conventional clustering algorithms. 

- GTA-V를 이용하여서 가상 데이터 획득 `To obtain extra training data, we built a LiDAR simulator into Grand Theft Auto V (GTA-V), a popular video game, to synthesize large amounts of realistic training data. `

> 실시간 적용이 가능한 속도 이다. `Our experiments show that SqueezeSeg achieves high accuracy with a stonishingly fast and stable runtime (8.7 ±0.5 ms per frame), highly desirable for autonomous driving applications. `

> [8.3ms/F = 120 FPS](https://steamcommunity.com/app/346110/discussions/0/530646715638737020/)

## I. INTRODUCTION

- LiDAR는 자율 주행차에서 중요한 센서이다. 본 논문은 3D LiDAR를 이용하여서 도로위 물체 세그멘테이션을 목표로 한다. `LiDAR based perception tasks have attracted significant research attention. In this work, we focus on road-object segmentation using(Velodyne style) 3D LiDAR point clouds. `

- 기존 접근방법은 아래와 같은 단계로 진행 된다. `Previous approaches comprise or use parts of the following stages: `
	- Remove the ground, 
	- cluster the remaining points into instances, 
	- extract (hand-crafted) features from each cluster, 
	- and classify each cluster based on its features.

- 기존 접근 방법들의 문제점 `This paradigm, despite its popularity [2], [3], [4], [5], has several disadvantages: `
	- 단점 1 : Ground segmentation in the above pipeline usually relies on **hand-crafted features** or **decision rules** 
		- some approaches rely on a scalar threshold [6] and others require more complicated features such as surface normals [7] or invariant descriptors [4], 
		- all of which may **fail to generalize** and the latter of which require significant preprocessing. 
	- 단점 2: **Multi-stage pipelines** see aggregate effects of **compounded errors**, and classification or clustering algorithms in the pipeline above are **unable to leverage context**, most importantly the immediate surroundings of an object. 
	- 단점 3: Many approaches for ground removal rely on **iterative algorithms** 
		- `such as RANSAC (random sampleconsensus) [5], GP-INSAC (Gaussian Process IncrementalSample Consensus) [2], or agglomerative clustering [2]`. 
		- The **runtime** and **accuracy** of these algorithmic components depend on the quality of random initializations and, therefore,can be **unstable.** 

- 새로운 제안 `We takean alternative approach: `
	- 딥러닝을 이용하여 특징 추출 `use deep learning to extract features,`
	- 싱글 파이프라인을 이용하여 반복 알고리즘 회피 `develop a single-stage pipeline and thus sidestep iterative algorithms.`

- 제안 방법은 아래에 기반 하고 있다. `In this paper, we propose an end-to-end pipeline based on `
	- convolutional neural networks (CNN) 
	- conditional random field (CRF). 

- CNN에 3D 를 적용하기 위하여 수정 하였따. `To apply CNNs to 3D LiDAR point clouds, we designed a CNN that `
	- 입력으로 ... accepts transformed **LiDAR point clouds** 
	- 출력으로 ... outputs a **point-wise map of labels**, which is further refined by a CRF model. 
	- 분류 작업으로 ... **Instance-level labels** are then obtained by applying conventional clustering algorithms `(such asDBSCAN)` on points within a category. 

- 3D 데이터를 2D에 입력 하기 위하여 `To feed 3D point clouds to a 2D CNN, `
	- we adopt a **spherical projection** to transform sparse, irregularly distributed 3D point clouds to dense, 2D grid representations. 

> 2D CNN을 쓰는건가? 

- 제안 모델은 SqueezeNet을 기반으로 하였으며 임베디드 시스템에서 동작 할수 있도록 속도를 높이고 메모리 부하를 줄였다. `The proposed CNN model draws inspiration from SqueezeNet [12] and is carefully designed to reduce parameter size and computational complexity, with an aim to reduce memory requirements and achieve real-time inference speed for our target embedded applications. `

- CRF모델은 RNN모듈로 reformulated 하여 CNN과 함께 동작 한다. `The CRF model is reformulated as a recurrentneural network (RNN) module as [11] and can be trained end-to-end together with the CNN model. `

- 시뮬레이션 가상  데이터를 이용하니 validation  정확도가 올라가는 것을 추가적으로 확인 하였따. 
	- We additionally find that **supplanting** our dataset with **artificial, noise-injected simulation data** further boosts **validation accuracy** on realworld data.

## 2. RELATED WORK

### 2.1 Semantic segmentation for 3D LiDAR point clouds

- Previous work saw a wide range of granularity in LiDAR segmentation, handling anything from specific components to the whole pipeline. 

- [7-2009] proposed **mesh based** ground and object segmentation relying on **local surface convexity** conditions. 

- [2-2011] **summarized** several approaches based on **iterative algorithms** such as RANSAC (random sample consensus)and GP-INSAC (gaussian process incremental sampleconsensus) **for ground removal**. 

- Recent work also focused on algorithmic efficiency. 

- [5] proposed efficient algorithms for **ground segmentation** and **clustering** 

```
[5] D. Zermas, I. Izzat, and N. Papanikolopoulos, “Fast segmentation of 3d point clouds: A paradigm on lidar data for autonomous vehicle applications,” in Robotics and Automation (ICRA), 2017 IEEE International
Conference on. IEEE, 2017, pp. 5067–5073
```

- [13] bypassed ground segmentation to directly extract foreground objects.

```
[13] M.-O. Shin, G.-M. Oh, S.-W. Kim, and S.-W. Seo, “Real-time and accurate segmentation of 3-d point clouds based on gaussian process regression,” IEEE Transactions on Intelligent Transportation Systems, 2017.
```

- [4] expanded its focus to the whole pipeline, including segmentation, clustering and classification. 
	- It proposed to directly classify point patches into background and foreground objects of different categories then use EMST-RANSAC [5]to further cluster instances

```
[4] D. Z. Wang, I. Posner, and P. Newman, “What could move? finding cars, pedestrians and bicyclists in 3d laser data,” in Robotics and Automation (ICRA), 2012 IEEE International Conference on. IEEE,2012, pp. 4038–4044.
```

### 2.2 CNN for 3D point clouds

- CNN approaches consider LiDAR point clouds in either **two** or **three** dimensions. 

#### A. 2D로 간주 

- Work with **two-dimensional** data considers **raw images** with
	-  **projections** of LiDAR point clouds top-down [14]  
	- -  **projections** of LiDAR point clouds from a number of other views [15].

```
[14] L. Caltagirone, S. Scheidegger, L. Svensson, and M. Wahde, “Fast lidar-based road detection using fully convolutional neural networks.” in Intelligent Vehicles Symposium (IV), 2017 IEEE. IEEE, 2017, pp.
1019–1024.
[15] X. Chen, H. Ma, J. Wan, B. Li, and T. Xia, “Multi-view 3d object detection network for autonomous driving,” arXiv preprint arXiv:1611.07759, 2016.
```

#### B. 3D로 간주 

- Other work considers **three-dimensional** data itself, **discretizing** the space into **voxels** and engineering features such as **disparity**, **mean**, and **saturation** [16]. 

- Regardless of data preparation, deep learning methods consider end-to-end models that leverage 2D convolutional [17] or 3D convolutional [18] neural networks.

```
[16] J. Schlosser, C. K. Chow, and Z. Kira, “Fusing lidar and images for pedestrian detection using convolutional neural networks,” in Robotics and Automation (ICRA), 2016 IEEE International Conference on.
IEEE, 2016, pp. 2198–2205.
[17] B. Li, T. Zhang, and T. Xia, “Vehicle detection from 3d lidar using fully convolutional network,” arXiv preprint arXiv:1608.07916, 2016.
[18] D. Maturana and S. Scherer, “3d convolutional neural networks for landing zone detection from lidar,” in Robotics and Automation (ICRA), 2015 IEEE International Conference on. IEEE, 2015, pp.
3471–3478.
```


### 2.3 Semantic Segmentation for Images

### 2.4 Data Collection through Simulation

## 3. METHOD DESCRIPTION

### 3.1 Point Cloud Transformation

### 3.2 Network structure

### 3.3 Conditional Random Field

### 3.4 Data collection

## 4. EXPERIMENTS
<!--stackedit_data:
eyJoaXN0b3J5IjpbODU2NDE0NTQ0XX0=
-->