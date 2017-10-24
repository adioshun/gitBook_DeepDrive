# 3D Object Representations

![](https://i.imgur.com/OPatJnW.png)
- Raw data : **Point cloud**, Range image(eg.Kinect), Polygon soup,
  - Point cloud represents shapes as a collection of unordered 3d coordinates.
- Surfaces : **Mesh**, Subdivision, Parametric, Implicit
  - Polygonal mesh describes a shape by a set of polygonal faces.
- Solids : **Voxels**, BSP tree, CSG, Sweep, 
  - Volumetric representation encodes a shape as 3d volumetric occupancy
- High-level structures : Scene graph, Skeleton, Application specific

> [3D Object Representation](http://www.connellybarnes.com/work/class/2015/intro_gfx/lectures/17-3DObjectRepresentation.pdf): 각 분류에 대한 상세 이미지 및 설명 포함, [Youtube](https://youtu.be/prwm9jTpths?t=11m23s) 


## 1. shape descriptor
- motivation : challenge of shape matching
- 정의 : a structured abstraction of a 3D model that captures salient(가장 뚜렷한) shape information
- 활용 : So that rather than comparing two models directly, the two models are compared by comparing their shape descriptors. 


![](https://i.imgur.com/xW0AyYM.png)


어떤 shape descriptor를 이용하여 retrieval할지 선택시 고려할점 
- what kind of models can be represented by the shape descriptor?
  - What can you represent?
- What type of shape information is captured by the descriptor?
  - given a shape descriptor, how much of the model information can we get back?
  - What are you representing?


> genus 0 : 가운데에 구멍이 뚫린 원통 같은 것에 붙이는 위상학적 '번호' 라고 할 수 있죠. 구형은 genus 0, 도넛은 genus 1 이 되죠.. 위상적으로 동형인 물체들은 반드시 종수가 같기 때문



- shape matching Challenge
  - shape descriptors can be matched across these different transformations(translation, scale, or rotation).
  - partial shape matching


## 2. Representation 
- the different ways that a shape descriptors can be used to represent a model.
- 종류 
  - Volumetric Representations
  - Surface Representations
    - Spherical Parameterization​
    - Extended Gaussian Image​
    - Shape Histograms (Sectors + Shells)​
    - Gaussian EDT​
  - View-Based Representations
    - Spherical Extent Function​
    - Light Field Descriptor​


![](https://i.imgur.com/ITSs925.png)

### 2.1 Volumetric Representations
Perhaps the most direct way to compare two models is to measure how much they overlap.

This notion of shape similarity can be encoded in a shape descriptor that represents a model by a regularly sampled three-dimensional array, where the value of a 3D point is either one or zero, depending on whether it is interior to the model or exterior to it.

The advantage of this representation it that it is invertible (up to the resolution of the sampling) so that no information is lost in representing a 3D model by this type of shape descriptor.

Furthermore, this type of representation has the advantage that the similarity between two shape descriptors corresponds to the size of the overlap between the two models as desired.

Thus, using the shape descriptor we have the advantage of a vector-based representation that allows for efficient matching, and we also satisfy the property that the difference between two descriptors gives a direct and meaningful measure of the geometric similarity of the underlying models.

While this shape descriptor satisfies a number of desirable properties – providing an invertible representation of a 3D model a vector that gives rise to a meaningful shape metric, it is often impractical to use in retrieval settings. 

In particular, the shape descriptor depends on the ability to identify whether a particular point is interior or exterior to the model. 

Thus, it can only be applied to water-tight meshes.

Since in practice, we often want to match models that have boundaries and cracks with no well defined interior, this type of shape descriptor end up being too limiting.

### 2.2 Surface Representations​


### 2.3 View-Based Representation 

- shape descriptors that seek to capture information about how humans see the model.

- In these approaches, a viewer is placed at different locations on the view sphere and a shape descriptor is built from information gathered from these aggregate views


#### A. Spherical Extent Function 

This shape descriptor is obtained by placing viewers at different points on the view sphere, and computing the distance to the first point that the viewer would see when looking at the origin.

This shape descriptor is no longer invertible, because it only considers the distance to the first point of intersection, ignoring all subsequent points of intersection.


#### B. Light Field Descriptor 

The last shape descriptor that we will consider is similar to the Spherical Extent Function in that it computes a model representation by placing viewers at different locations on the view sphere. 

However, instead of computing a single pixel depth image at each view position, this approach computes a 2D image at each point, representing a model by a collection of 2D snapshots.

The Light Field descriptor is then obtained by extracting the silhouette and the interior of each image and using those for matching. 

Thus, while the Light Field Descriptor is not completely invertible, we can use it to extract the visual hull of the model, giving rise to a reasonable approximation of a model’s shape, for models that do not have too much depth complexity.

## 3. 결론

![](https://i.imgur.com/8zdfu4c.png)

To summarize, in this part of the lecture we have reviewed a number of existing shape descriptors and showed how they assist in the task of shape matching.

- We saw that because of its dependence on differential properties of the surface, the **Extended Gaussian Image** becomes unstable in the presence of noise.

- We saw that the **Gaussian EDT** provides a method for distributing the surface of a model across 3D space without blurring out the model details.

- We saw that while it is generally difficult to obtain a spherical parameterization of a 3D model, the Spherical Extent Function, provides a method for computing the star-shaped hull of an arbitrary model, giving a method to approximate arbitrary genus models by genus-0 models.

- And we saw how by transforming the challenge of 3D shape matching to the domain of 2D image matching, the Light Field Descriptor could take advantage of the fact that certain matching problems are easier to solve in 2D then they are in 3D.


> https://www.slideshare.net/secret/Ls3Y0t8O7jat80

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


![](https://i.imgur.com/hAfHmk1.png)
메모리 사용량 

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



