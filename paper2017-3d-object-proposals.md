|논문명|3D Object Proposals for Accurate Object Class Detection
|-|-|
|저자(소속)|Xiaozhi Chen|
|학회/년도|TPAMI 2017,  [논문](https://arxiv.org/abs/1608.07711)|
|키워드| MV3D 저자,  |
|참고|[홈페이지](http://www.cs.toronto.edu/objprop3d/), [보충자료](http://www.cs.toronto.edu/objprop3d/3DOP_journal_suppl.pdf), [이전버젼(2015)](http://www.cs.toronto.edu/objprop3d/3dopNIPS15.pdf) |
|코드|[Download](http://www.cs.toronto.edu/objprop3d/downloads.php)|

# 3DOP

목표 : generating a set of 3D object proposals by exploiting stereo imagery

방법 : We formulate the problem as `minimizing an energy function` that encodes 
- object size priors
- placement of objects on the ground plane
- several depth informed features that reason about free space, point cloud densities and distance to the ground

Fusion하면 성능이 더 좋음 : Furthermore, we experiment also with the setting where `LIDAR information is available`, and show that using both LIDAR and stereo leads to the best result.

## 1. INTRODUCTION


물체 탐지 분야에서 CNN기반 `후보영역`방법을 이용하는 것[4-RCNN][5]은 `Sliding Window[3]`방식 보다 20%성능이 좋다. 

```
[3] P. F. Felzenszwalb, R. B. Girshick, D. McAllester, and D. Ramanan,“Object detection with discriminatively trained part based models,”PAMI, 2010.
[5] Y. Zhu, R. Urtasun, R. Salakhutdinov, and S. Fidler, “SegDeepM:Exploiting segmentation and context in deep neural networks for object detection,” in CVPR, 2015.
```

KITTI Dataset은 작고, 가려지거나(occluded), 잘린(truncated)부분이 많다. 따라서 PASCAL VOC에서 좋은 성능을 보인것도 그대로 사용하면 성능이 않좋다. 


In this paper, we propose a novel 3D object detection approach that exploits `stereo imagery` and `contextual information` specific to the domain of autonomous driving

연구 순서 

1. `We propose a 3D object proposal method that goes beyond 2D bounding boxes and is capable of generating highquality 3D bounding box proposals. `

2. We make use of the 3D information estimated from a stereo camera pair by placing 3D candidate boxes on the ground plane 

3. scoring them via 3D point cloud features. 

> 최종 결과를 3D point cloud값과 비교 

In particular, our `scoring function` encodes several depth informed features such as
- point densities inside a candidate box, 
- free space, 
- visibility
- object size priors
- height above the ground plane

학습절차는 Learning can be done using `structured SVM` [17] to obtain class-specific weights for these features. 

탐지 네트워크는 입력으로 3D 후보를 받아, 출력으로 3D BBox를 출력 한다. 
We also present a `3D object detection neural network` that takes 3D object proposals as input and predict accurate 3D bounding boxes. 

제안 네트워크는 최종적으로  The neural net exploits `contextual information` and uses a `multi-task loss` to jointly regress to bounding box coordinates and object orientation.

성능 : In particular, compared with the state-of-the-art RGB-D
method MCG-D [18], we obtain 25% higher recall with 2K
proposals
