- [Youtube](https://www.youtube.com/watch?v=8CenT_4HWyY) : 3시간 22분 , [자료](http://3ddl.stanford.edu/)


# Opening remark and overview of 3D deep learning [[pdf]](http://3ddl.stanford.edu/CVPR17_Tutorial_Overview.pdf)

## 1. 3D Deep Learning Tasks 

![](https://i.imgur.com/AlmQPZC.png)

### 1.1. 3D Geometry Anaysis

![](https://i.imgur.com/Db2NhIu.png)

### 1.2. 3D Assisted Image Analysis

![](https://i.imgur.com/NY2wwBR.png)

### 1.3. 3D Synthesis
![](https://i.imgur.com/kccad3b.png)


## 2. 3D representations

### A. Rasterized form (Regular grids)
- Multi-view images
- Volumetric

> CNN을 바로 적용 할수 있음, 몇가지 Challenges 있음 

### B. Geometric form(irregular) 
- Polygonal mesh
- Point cloud
- Primitive-based CAD models 

> CNN을 바로 적용 할수 없음, 새 딥러닝 Architecture 개발 필요 

![3D Deep learning algorithms by representation](https://i.imgur.com/qQxYXrb.png)
3D Deep learning algorithms by representation 

---

# Deep learning on regular structures 

## 1. Multi-view representation

- Convert irregular (3D) to regular (images)

- Circumvent any geometric representation artifacts (non-manifold geometry, polygon soups, no interior)

- Leverage pre-trained image-based CNNs Empty inside!

- Similarly to humans, analyze what can be seen: combine surface information from multiple views 



### 1.1 Deep Learning on Multi-view Representation

#### A. 3D Classification 

- Hang Su, Multi-view Convolutional Neural Networks for 3D Shape Recognition: Feature + Linear Classification 

- Issues:
    - What viewpoints to select? In particular, where shall we place the
camera in a scene?
    - What if the input is noisy and incomplete? e.g., point cloud
   

#### B. Segmentation 

- Evangelos Kalogerakis, 3D Shape Segmentation with Projective Convolutional Networks, CVPR 2017

- Challenges:
    - View-based network does not process invisible points
    - View-based representations have redundancy
    - Slow to train (~week for a few hundreds of shapes)
    - Aggregating view representations via max-pooling may lose information

#### C. Reconstruction 

- 3D Shape Reconstruction from Sketches via Multi-view Convolutional Networks”, arxiv 2017


### 1.2 Key challenges for multi-view representation

- Fusing information across viewpoints is not incorporated in the network (not trivial)
- “Cannot see through the surface”
- Less redundancy than producing a surface for every possible continuous viewing
 angle, yet surfaces across different viewpoints may not be consistent.

## 2. Volumetric Representation