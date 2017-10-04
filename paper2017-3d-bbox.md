|논문명|3D Bounding Box Estimation Using Deep Learning and Geometry
|-|-|
|저자(소속)|Arsalan Mousavian (GMU)|
|학회/년도| 2016~2017, [논문](https://arxiv.org/pdf/1612.00496.pdf)|
|키워드|KITTI,Pascal 3D+, 카메라 1대, 2D이미지에 3D BBox 적용하기|
|참고|[3D Vehicle Detection](https://experiencor.github.io/sdc_3d.html), [Github](https://github.com/experiencor/didi-starter/tree/master/simple_solution)|
|코드|[Keras](https://github.com/experiencor/image-to-3d-bbox)|

![](https://camo.githubusercontent.com/50a2bca55a388423aab8e8de8345e04d79a2f283/68747470733a2f2f6a2e676966732e636f6d2f7a6d574b6a4f2e676966)


# Deep3DBox

목적 : 3D object detection and pose estimation from a single image

- The first network : output estimates the 3D object orientation using a novel hybrid discrete-continuous loss, which significantly outperforms the L2 loss. 

- The second : output regresses the 3D object dimensions, which have relatively little variance compared to alternatives and can often be predicted for many object types. 

## 1. Introduction

3D object detection recovers both the 6 DoF pose and the dimensions of an object from an image. 

> 6자유도(degrees of freedom, 6DOF) 중 3자유도는 Position(위치)이며 나머지 3자유도는 Orientation(자세)이라 한다


목적 : we propose a method that estimates 
- the pose $$(R, T) \in SE(3)$$ 
- the dimensions of an object’s 3D bounding box 
from a **2D bounding box** and the **surrounding image** pixels.

our method is based on several important insights
- We show that a novel MultiBin discrete continuous formulation of the orientation regression significantly outperforms a more traditional L2 loss. 
- Further constraining the 3D box by regressing to vehicle dimensions proves especially effective, since they are relatively low variance and result in stable final 3D box estimates.

We introduce three additional performance metrics measuring the 3D box accuracy: 
- distance to center of box, 
- distance to the center of the closest bounding box face, 
- the overall bounding box overlap with the ground truth box, measured using 3D Intersection over Union (3D IoU) score.

In summary, the main contributions of our paper include:

1. A method to estimate an object’s full **3D pose** and **dimensions** from a 2D bounding box using the constraints provided by projective geometry and estimates of the object’s orientation and size regressed using a deep CNN. 
    - In contrast to other methods, our approach does not require any preprocessing stages or 3D object models. 
2. A novel discrete-continuous CNN architecture called **MultiBin** regression for estimation of the object’s orientation. 
3. Three n**ew metrics **for evaluating 3D boxes beyond their orientation accuracy for the KITTI dataset. 
4. An experimental evaluation 
5. Viewpoint evaluation on the Pascal 3D+ dataset..

## 2. Related Work


## 3. 3D Bounding Box Estimation

In order to leverage the success of existing work on 2D object detection for 3D bounding box estimation, we use the fact that the perspective projection of a 3D bounding box should fit tightly within its 2D detection window. 

We  assume that the 2D object detector has been trained to produce boxes that correspond to the bounding box of the projected 3D box
