| 논문명 | PointNet: A 3D Convolutional Neural Network for real-time object class recognition |
| --- | --- |
| 저자\(소속\) |A. Garcia-Garcia \(\) |
| 학회/년도 | IJCNN 2016, [논문](http://ieeexplore.ieee.org/document/7727386/) |
| 키워드 | PointNet3D2016,  |
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

2.5D 데이터에 CNN을 적용하려는 연구가 시작 되었다. 깊이 정보를 또다른 채널로 인식 하는 것이다. `Due to the successful applications of the CNNs to 2D image analysis, several researchers decided to take the same approach for 2.5D data, treating the depth channel as an additional one together with the RGB ones [10]–[12]. `
- 이건 단순히 입력으로 4채널을 받는것 뿐이다. `These methods simply extend the architecture to take four channels – matrices – as input instead of the three featured by RGB images. `
- 이건 아직 3D의 geometric 정보를 이용하지 않는 **이미지 기반** 접근법이다. `This is still a image-based approach which does not fully exploit the geometric information of 3D shapes despite its straightforward implementation. `

최근에는 3D의 정보를 이용하는 연굳Apart from 2.5D approaches, specific architectures to learn from volumetric data, which make use of pure 3D convolutions, have been recently developed. 

Those architectures are commonly referred as 3DCNNs and their foundations are the same as the 2D or 2.5D ones, but the
nature of the input data is radically different. 

Since volumetric data is usually quite dense and hard to process, most of the successful 3DCNNs resort to a more compact representation of the 3D space: the occupancy grids. 

VoxNet [13] and 3D ShapeNets [14] make extensive use of this representation.
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjIwNzg5MTk2XX0=
-->