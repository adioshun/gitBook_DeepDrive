# 3D Object Representations

![](https://i.imgur.com/OPatJnW.png)
- Raw data : **Point cloud**, Range image(eg.Kinect), Polygon soup,
  - Point cloud represents shapes as a collection of unordered 3d coordinates.
- Surfaces : **Mesh**, Subdivision, Parametric, Implicit
  - Polygonal mesh describes a shape by a set of polygonal faces.
- Solids : **Voxels**, BSP tree, CSG, Sweep, 
  - Volumetric representation encodes a shape as 3d volumetric occupancy
- High-level structures : Scene graph, Skeleton, Application specific

> [3D Object Representation](http://www.connellybarnes.com/work/class/2015/intro_gfx/lectures/17-3DObjectRepresentation.pdf): 각 분류에 대한 상세 이미지 및 설명 포함 

### RNN/RL

[3DCNN-DQN-RNN: A Deep Reinforcement Learning Framework for Semantic Parsing of Large-scale 3D Point Clouds](https://arxiv.org/abs/1707.06783): 2017.07, 3D CNN + RNN + DQN

---

# Datasets
- Princeton Shape Benchmark (PSB) [Shilane et al. 2004] 

- Engineering Shape Benchmark (ESB) [Jayanti et al. 2006]

- PSB [Shilane et al. 2004]

- National Taiwan University (NTU) dataset [Chen et al. 2003] 

- SHREC’09 [Godil et al. 2009]

- [Semantic3D.net: A new Large-scale Point Cloud Classification Benchmark](https://arxiv.org/abs/1704.03847): 2017.04, Datasets, 도시, four billion~




---

## Workshop

[3D DeepLearning at NIPS2016](http://3ddl.cs.princeton.edu/2016/): 발표 자료 목록/자료 포

[Geometry Meets Deep Learning ECCV 2016 Workshop](https://sites.google.com/site/deepgeometry/)

---

## LeaderBoard

### KITTI
![](https://i.imgur.com/WZ7rb9q.png)

### ModelNet 
![](https://i.imgur.com/EZp7gs1.png)

- [ModelNet](http://modelnet.cs.princeton.edu/): 프린스톤대, 127,915 CAD Models, 662 Object Categories, 10 Categories with Annotated Orientation

### [Generalized Convolutional Neural Networks for Point Cloud Data](https://arxiv.org/pdf/1707.06719v1.pdf)

![](https://i.imgur.com/6oAJmnx.png)

### [3D Object Proposals using Stereo Imagery for Accurate Object Class Detection](https://arxiv.org/pdf/1608.07711.pdf), 2017

![](https://i.imgur.com/a0WmMQb.png)


### [Deep Learning Advances in Computer Vision with 3D Data: A Survey](http://dl.acm.org/citation.cfm?id=3042064)

![](https://i.imgur.com/i64SI7G.png)

---
[3D Vehicle Detection](https://experiencor.github.io/sdc_3d.html)

1. Detect 2D BBoxes of other vehicles visible on CAMERA frame. This can be achieved by YOLOv2 or SqueezeDet. It turns out that SqueezeDet works better for this job and is selected.

2. Determine the dimension and the orientation of detected vehicles. As demonstrated in [https://arxiv.org/abs/1612.00496], dimension and orientation of other vehicles can be regressed from the image patch of corresponding 2D BBoxes.

3. Determine the location in 3D of detected vehicles. This can be achived by localizing the point cloud region whose projection stays within the detected 2D BBoxes.


---

https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=3D_CNN_Trend.xml#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D0B6Ry8c3OoOuqVUh1b2tyc2lhMEE%26export%3Ddownload



--- 

## Terms

a 3D voxel grid where each voxel was a binary variable indicating whether it belonged to the 3D shape or it was empty space

Volumetric representation, where the 3D object is discretized spatially as binary voxels (1 if the voxel is occupied and 0 otherwise. )



