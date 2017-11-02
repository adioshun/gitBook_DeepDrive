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

- 기존 접근 방법들의 문제점 This paradigm, despite its popularity [2], [3], [4], [5], has several disadvantages: 

a) Ground segmentation in the above pipeline usually relies on hand-crafted features or decisionrules – some approaches rely on a scalar threshold [6] andothers require more complicated features such as surfacenormals [7] or invariant descriptors [4], all of which mayfail to generalize and the latter of which require signifi-cant preprocessing. 

b) Multi-stage pipelines see aggregateeffects of compounded errors, and classification or clusteringalgorithms in the pipeline above are unable to leveragecontext, most importantly the immediate surroundings ofan object. 

c) Many approaches for ground removal relyon iterative algorithms such as RANSAC (random sampleconsensus) [5], GP-INSAC (Gaussian Process IncrementalSample Consensus) [2], or agglomerative clustering [2]. 

Theruntime and accuracy of these algorithmic components dependon the quality of random initializations and, therefore,can be unstable. 

This instability is not acceptable for manyembedded applications such as autonomous driving. 

We takean alternative approach: use deep learning to extract features,develop a single-stage pipeline and thus sidestep iterativealgorithms.In this paper, we propose an end-to-end pipeline basedon convolutional neural networks (CNN) and conditionalrandom field (CRF). 

CNNs and CRFs have been successfullyapplied to segmentation tasks on 2D images [8], [9], [10],[11]. 

To apply CNNs to 3D LiDAR point clouds, we designeda CNN that accepts transformed LiDAR point clouds andoutputs a point-wise map of labels, which is further refinedby a CRF model. 

Instance-level labels are then obtainedby applying conventional clustering algorithms (such asDBSCAN) on points within a category. 

To feed 3D point clouds to a 2D CNN, we adopt a spherical projection totransform sparse, irregularly distributed 3D point clouds todense, 2D grid representations. 

The proposed CNN modeldraws inspiration from SqueezeNet [12] and is carefullydesigned to reduce parameter size and computational complexity,with an aim to reduce memory requirements andachieve real-time inference speed for our target embeddedapplications. 

The CRF model is reformulated as a recurrentneural network (RNN) module as [11] and can be trainedend-to-end together with the CNN model. 

Our model istrained on LiDAR point clouds from the KITTI dataset [1]and point-wise segmentation labels are converted from 3Dbounding boxes in KITTI. 

To obtain even more training data,we leveraged Grand Theft Auto V (GTA-V) as a simulator toretrieve LiDAR point clouds and point-wise labels.Experiments show that SqueezeSeg achieves high accuracyand is extremely fast and stable, making it suitablefor autonomous driving applications. 

We additionally findthat supplanting our dataset with artificial, noise-injectedsimulation data further boosts validation accuracy on realworlddata.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTk5NzAzNDY0MV19
-->