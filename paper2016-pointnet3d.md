| 논문명 | PointNet: A 3D Convolutional Neural Network for real-time object class recognition |
| --- | --- |
| 저자\(소속\) |A. Garcia-Garcia \(\) |
| 학회/년도 | IJCNN 2016, [논문](http://ieeexplore.ieee.org/document/7727386/) |
| 키워드 | PointNet3D2016, 분류  |
| 데이터셋(센서)/모델 |ModelNet(RGB-D)  |
| 참고 |  |
| 코드 |  |

# PointNet3Deep

PointNet제안 : A new approach inspired by `VoxNet` and `3D ShapeNets`, 

개선 방법 :  
- Using density **occupancy grids representations** for the input data,
- Integrating them into a supervised **Convolutional Neural Network architecture**.


## 1. INTRODUCTION

대부분의 연구는 Handcrafted Local Feature 를 사용 하였따. `The vast majority of 3D object recognition methods [2] are typically based on hand-crafted local feature descriptors[3]. `

기존 방식의 Pipe-line `These kinds of approaches rely on specific pipelines [4] consisting of `
- a keypoint detection phase, 
- followed by the computation of descriptors at those characteristic regions, 
- finally they are classified to determine the possible object represented by those descriptors. 

분류 문제 해결 법 : 거리 기반 or 머신러닝 알고리즘 `That classification is performed by using distance metrics or machine learning algorithms, e.g.,`
- Support Vector Machines (SVMs) [5], 
- random forests [6],
- neural networks, which are trained with object datasets.

문제점 : 도메인 지식 필요, 완벽하지 않음 `handcrafting feature descriptors requires domain expertise and remarkable engineering and theoretical skills, and even fulfilling both requirements they are still far from perfection. `

본 논문의 기여도  `Its contribution is twofold:` 
- a novel way for representing the input data, which is based on **point density occupancy grids**, 
- its integration into a **CNN specifically** tuned for the aforementioned purpose.

## 2. RELATED WORK

### 2.1 2.5D 연구
2.5D 데이터에 CNN을 적용하려는 연구가 시작 되었다. 깊이 정보를 또다른 채널로 인식 하는 것이다. `Due to the successful applications of the CNNs to 2D image analysis, several researchers decided to take the same approach for 2.5D data, treating the depth channel as an additional one together with the RGB ones [10]–[12]. `
- 이건 단순히 입력으로 4채널을 받는것 뿐이다. `These methods simply extend the architecture to take four channels – matrices – as input instead of the three featured by RGB images. `
- 이건 아직 3D의 geometric 정보를 이용하지 않는 **이미지 기반** 접근법이다. `This is still a image-based approach which does not fully exploit the geometric information of 3D shapes despite its straightforward implementation. `

```
[10] R. Socher, B. Huval, B. Bath, C. D. Manning, and A. Y. Ng, “Convolutional-recursive deep learning for 3d object classification,” in Advances in Neural Information Processing Systems, 2012, pp. 665–673.
[11] L. A. Alexandre, “3d object recognition using convolutional neural networks with transfer learning between input channels,” in Proc. the 13th International Conference on Intelligent Autonomous Systems, 2014.
[12] I. Lenz, H. Lee, and A. Saxena, “Deep learning for detecting robotic grasps,” The International Journal of Robotics Research, vol. 34, no. 4-5, pp. 705–724, 2015.
```

### 2.2 3D 연구 

최근에는 3D의 정보를 이용하는 연구도 진행 되었다. `Apart from 2.5D approaches, specific architectures to learn from volumetric data, which make use of pure 3D convolutions, have been recently developed. `
- 이방식은 **3DCNN**라고 불리우며 근본은 2D, 2.5D방식과 같지만 **입력 데이터**의 속성이 다르다. `Those architectures are commonly referred as 3DCNNs and their foundations are the same as the 2D or 2.5D ones, but the nature of the input data is radically different. `

volumetric 데이터는 처리량이 많기 때문에 좀더 컴팩트한 표현방식`(representation )`으로 바꾸어서 진행 한다. `Since volumetric data is usually quite dense and hard to process, most of the successful 3DCNNs resort to a more compact representation of the 3D space: `
- the occupancy grids. 
- VoxNet [13] and 3D ShapeNets [14] make extensive use of this representation.

### 2.3 3DCNN

3DCNNs방식은 인기를 얻기 시작한다.  `Those 3DCNNs are slowly overtaking other approaches when applying object recognition to complete 3D scenes [15-DeepSlidingShape].`

이유 두가지 `This progress has been mainly enabled by two factors: `
- 데이터셋 증가 `The substantial growth in the number of 3D models available online through repositories, `
- 컴퓨팅 파워 증가 `The reduction of training times thanks to frameworks and libraries which exploit the power of massively parallel architectures for this kind of tasks. `

하지만, 3D데이터는 받지만 라벨링 된 데이터는 적다. `On the one hand, there exist many collections of 3D models, but they tend to be small and usually lack annotations and other useful information for training this kind of deep architectures. `

반대로 2D 데이터는 좋은 데이터가 많다. `In contrast, 2D approaches have taken advantage of the numerous and high-quality datasets that already exist such as ImageNet[9], LabelMe [16], and SUN [17]. `

그래서 최근 3D데이터셋 증가를 위해 많은 노력이 있었다. **ModelNet**  & **ShapeNets**  `During the last years,researchers have unified efforts to create large-scale annotated 3D datasets inspired by the success of the 2D counterparts. The most popular 3D datasets which have revamped data driven solutions – for computer vision in general, and object recognition in particular – are the Princeton ModelNet [14],and ShapeNets [18] datasets. `

하드웨어와 딥러닝 프레임워크 발전도 있다. `On the other hand, the creationof deep learning frameworks such as Caffe [19], Theano [20],Torch [21], or TensorFlow [22], which allow researchers to easily express and launch their architectures and accelerate thetraining calculations with Graphics Processing Units (GPUs)by using CUDA or OpenCL, has enabled quick prototypingand testing. `

Both facts have turned out to be crucial for the development of the field.

```
[15] S. Song and J. Xiao, “Deep sliding shapes for amodal 3d object detection in rgb-d images,” arXiv preprint arXiv:1511.02300, 2015.
```


## 3. Approach 

제안 방식The proposed system takes a point cloud of an object as an input and predicts its class label. 
- 입력 : Point Cloud
- 출력 : Class label

> 단순 이미지 분류는 의미 없은 전체 이미지에서 물체를 탐지하고 해당 물체를 분류 하여야 함

In this regard, the proposal is two fold: 
- a volumetric grid based on point density to estimate spatial occupancy inside each voxel, 
- a pure 3DCNN which is trained to predict object classes. 

###### [The occupancy grid]
– inspired by VoxNet [13] occupancy models based on probabilistic estimates 
– provides a compact representation of the object’s 3D information from the point cloud. 

That grid is fed to the CNN architecture, which in turn computes a label for that sample, i.e., predicts the class of the object.

This architecture was implemented using the Point Cloud Library (PCL) [23] – which contains state-of-the-art algorithms for 3D point cloud processing – and Caffe [19], a deeplearning framework developed and maintained by the BerkeleyVision and Learning Center (BVLC) and an active community of contributors on GitHub 1. 

This BSD-licensed C++ libraryallows us to design, train, and deploy CNN architecturesefficiently, mainly thanks to its drop-in integration of NVIDIAcuDNN [24] to take advantage of GPU acceleration.

### 3.1 Occupancy Grid

정의 
- Occupancy grids [25] are data structures which allow us to obtain a compact representation of the volumetric space.
- They stand between meshes or clouds, which offer rich but large amounts of information, and voxelized representations with packed but poor information. 

At that midpoint, **occupancy grids** provide considerable shape cues to perform learning, while enabling an efficient processing of that information thanks to their array-like implementation.

최근 3D DL구조들은 occupancy grids를 사용하는 사례가 증가 하고 있다. `Recent 3D deep learning architectures make use of occupancy grids as a representation for the input data to be learned or classified. `

```
[25] S. Thrun, “Learning occupancy grid maps with forward sensor models,”Autonomous robots, vol. 15, no. 2, pp. 111–127, 2003.
```

#### A. 3D ShapeNets

3D ShapeNets [14] is a Convolutional Deep Belief Network (CDBN) which represents a 3D shape as a 30 × 30 × 30 binary tensor in which a one indicates that a voxel intersects the mesh surface, and a zero represents empty space. 

#### B. VoxNet 

VoxNet [13] introduces three different occupancy grids (32 × 32 × 32 voxels) that employ 3D ray tracing to compute the number of beams hitting or passing each voxel and then use that information to compute the value of each voxel depending on the chosen model: 
- a binary occupancy grid using probabilistic estimates, 
- a density grid in which each voxel holds a value corresponding to the probability that it will block a sensor beam, 
- a hit grid that only considers hits thus ignoring empty or unknown space. 

The binary and density grids proposed by Maturana et al[13]. differentiate unknown and empty space, whilst the hit grid and the binary tensor do not.

```
[13] D. Maturana and S. Scherer, “Voxnet: A 3d convolutional neural network for real-time object recognition.” IROS, 2015.
```

최근까지는 VoxNet’s 의occupancy grid가 가장 좋은 성능을 보이고 있다. ` Currently, VoxNet’s occupancy grid holds the best accuracy in the ModelNet challenge for the 3D-centric approaches described above. `

However, ray tracing grids considerably harmed performance in terms of execution time so that other approaches must be considered for a real-time implementation.

In that very same work, the authors show that hit grids performed comparably to other approaches while keeping alow complexity to achieve a reduced runtime.

In this regard, we propose an occupancy grid inspired by the aforementioned successes but aiming to maintain a reason able accuracy while allowing a real-time implementation. 

In ourvolumetric representation, each point of a cloud is mapped toa voxel of a fixed-size occupancy grid. 

Before performing thatmapping, the object cloud is scaled to fit the grid. 

Each voxelwill hold a value representing the number of points mappedto itself. 

At last, the values held by each cell are normalized.Figure 1 shows the proposed occupancy grid representationfor a sample object.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg0MDUwMjQ2M119
-->