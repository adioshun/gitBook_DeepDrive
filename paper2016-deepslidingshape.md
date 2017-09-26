|논문명|Deep Sliding Shapes for Amodal 3D Object Detection in RGB-D Images
|-|-|
|저자(소속)|Shuran Song (Princeton)|
|학회/년도| CVPR 2016, [논문](http://dss.cs.princeton.edu/paper.pdf)|
|키워드|amodal, RPN, ORN |
|참고|[CVPR2016](https://www.youtube.com/watch?v=D-lDbS9NQ_0), [Youtube](https://www.youtube.com/watch?v=zzcipxzZP9E), [Homepage](http://dss.cs.princeton.edu/) |
|코드|[matlab](https://github.com/shurans/DeepSlidingShape)|

# Deep Sliding Shapes

목표 : amodal 3D object detection in RGB-D images
    - amodal : 완성된 물체가 아닌, Not Modal 
    
Deep Sliding Shapes, a 3D ConvNet    
- 입력 : 3D volumetric scene from a RGB-D image
- 출력 : 3D object bounding boxes
- 구성 
    - 3D Region Proposal Network (RPN) to learn objectness from geometric shapes
    - joint Object Recognition Network (ORN) to extract geometric features in 3D and color features in 2D
    
성능 : 기존 Sliding Shapes대비 13.8 in mAP and is 200x faster 

## 1. Introduction

We focus on the task of amodal 3D object detection in RGB-D images,
- which aims to produce an object’s 3D bounding box that gives real-world dimensions at the object’s full extent, regardless of truncation or occlusion

- However naively converting 2D detection results to 3D does not work well (see Table 3 and [10]).

###### sliding shapes

깊이 정보 활용을 위해 저자는 `sliding shapes`를 제안 하였으나 `hand-crafted` feature로 인해 제약이 있다. 
To make good use of the depth information, Sliding Shapes [25] was proposed to slide a 3D detection window in 3D space.
    - While it is limited by the use of `hand-crafted` features,

```
[25] S. Song and J. Xiao. Sliding Shapes for 3D object detection in depth images. In ECCV, 2014.
```

###### Depth RCNN 

Depth RCNN [10] takes a 2D approach: detect objects in the 2D image plane by treating depth as extra channels of a color image, then fit a 3D model to the points inside the 2D detected window by using ICP alignment.

```
[10] S. Gupta, P. A. Arbelaez, R. B. Girshick, and J. Malik. Aligning 3D models to RGB-D images of cluttered scenes. In CVPR, 2015
```


###### which representation is better for 3D amodal object detection, 2D or 3D? 

현재는 2D-Centric D-RCNN이 성능이 더 좋다. 하지만 이건 `2D representation`가 좋은게 아니라 2D Network 설계가 잘되어서 그런건 아닐까? `Currently, the 2D-centric Depth RCNN outperforms the 3D-centric Sliding Shapes. But perhaps Depth RCNN’s strength comes from using a well-designed deep network pre-trained with ImageNet, rather than its 2D representation.` 

향후 3D 모델이 잘 설계 되면 성능이 더 잘 나올수 있다. `Is it possible to obtain an elegant but even more powerful 3D formulation by also leveraging deep learning in 3D?`

---

![](https://i.imgur.com/7oMAaGv.png)

따라서, 본 논문에서는 we introduce Deep Sliding Shapes, a complete 3D formulation to learn object proposals and classifiers using 3D convolutional neural networks (ConvNets)

제안 1 : 3D Region Proposal Network (RPN) 
- RPN takes a 3D volumetric scene as input and outputs 3D object proposals (Figure 1).
- It is designed to generate amodal proposals for whole objects at two different scales for objects with different sizes

제안 2 : joint Object Recognition Network (ORN) 
- ORN to use a 2D ConvNet to extract image features from color, and a 3D ConvNet to extract geometric features from depth (Figure 2). 
- This network is also the first to regress 3D bounding boxes for objects directly from 3D proposals.

제안 방식은 3D의 정보를 Fully 이용하기 때문에 아래 `5가지 장점`이 있다. 

1. First, we can predict 3D bounding boxes without the extra step of fitting a model from extra CAD data. 
    - This elegantly simplifies the pipeline, accelerates the speed, and boosts the performance because the network can directly optimize for the final goal. 
    
2. Second, amodal proposal generation and recognition is very difficult in 2D, because of occlusion, limited field of view, and large size variation due to projection. 
    - But in 3D, because objects from the same category typically have similar physical sizes and the distraction from occluders falls outside the window, our 3D sliding-window proposal generation can support amodal detection naturally. 

3. Third, by representing shapes in 3D, our ConvNet can have a chance to learn meaningful 3D shape features in a better aligned space. 

4. Fourth, in the RPN, the receptive field is naturally represented in real world dimensions, which guides our architecture design. 

5. Finally, we can exploit simple 3D context priors by using the Manhattan world assumption to define bounding box orientations.

제안 방식이 3D를 이용하므로써 발생하는 `3가지 도전` 사항 및 해결책 

1. (계산 부하)First, a 3D volumetric representation requires much more memory and computation.
    - To address this issue, we propose to separate the 3D Region Proposal Network with a low-res whole scene as input, and the Object Recognition Network with high-res input for each object. 
    
2. Second, 3D physical object bounding boxes vary more in size than 2D pixel-based bounding boxes (due to photography and dataset bias) [16].
    - To address this issue, we propose a multi-scale Region Proposal Network that predicts proposals with different sizes using different receptive fields. 

3. (Missing Value)Third, although the geometric shapes from depth are very useful, their signal is usually lower in frequency than the texture signal in color images.
    - To address this issue, we propose a simple but principled way to jointly incorporate color information from the 2D image patch derived by projecting the 3D region proposal.

### 1.1. Related works

- 2D 이미지 분류관련 연구들 : RCNN [8], Fast RCNN [7], and Faster RCNN [18] 

- 2D amodal  이미지 분류관련 연구 : [14] further extended RCNN to estimate the amodal
box for the whole object

```
[14] A. Kar, S. Tulsiani, J. Carreira, and J. Malik. Amodal completion and size constancy in natural scenes. In ICCV, 2015
```
