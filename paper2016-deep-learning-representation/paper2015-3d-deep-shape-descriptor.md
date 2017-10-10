|논문명|3D Deep Shape Descriptor|
|-|-|
|저자(소속)|Yi Fang ( New York University)|
|학회/년도| IEEE 2015, [논문](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7298845)|
|키워드|Yi2015,  |
|참고||
|코드||


# 3D Deep Shape Descriptor

논문 산출물
- we developed geometrically informative shape descriptor 
- new methods of defining **Eigen-shape descriptor** and **Fisher-shape descriptor**
to guide the training of a deep neural network.


제안된 SD의 특징 :  Our deep shape descriptor tends to maximize the inter-class margin
while minimize the intra-class variance


## 1. Introduction 

### 1.1 Background 

SD 정의 : Shape descriptor refers to an informative description that provides a 3D object with an identification as a member of some category.

좋은 3SD의 요구 사항 `3D shape descriptor poses several technical challenges,Therefore, effective solutions must be able to address the following issues.`

1. The high data complexity of 3D models [36, 8, 46, 9].
    - 3D geometric data is often featured as a highly complex and abstract representation for an object and with severe loss of critical descriptive information such as color, texture and appearance [6] to some extent.
    - The high data complexity in 3D model representation therefore presents great challenges in the development of a concise but geometrically informative description for efficient and real-time 3D shape analysis.

2. The structural variations present in 3D models [8, 46,17]. 
    - Many 3D objects contain dynamical units with their shape flexibility and variations play an essential role in certain types of functional processes. 
    - Therefore, the geometric structures of 3D models are often compounded by highly variable complexity causing large structural variations. 
    - For instance, 3D human models are dynamical units with different poses, and 3D protein models are functional units with their 3D shape flexibility playing an essential role in a variety of biological processes.

3. Noise, incompleteness, and occlusions, etc [17, 16].3D data are often noisy and incomplete after acquisition and meshing [36, 6]. 
    - A 3D model is composed of an unorganized sets of polygons that form “polygonsoups”. 
    - As stated in [36], a 3D model often contains missing, wrongly oriented, intersecting, disjoint,and /or overlapping polygons. 
    - For example, the classic model Utah teapot is missing its bottom and rim, and the Stanford Bunny has several holes along its base.
    
### 1.2 Related Works

위에서 언급한 3가지 사항에 대한 관련 연구들. 두가지 접근 방법으로 분류 가능 
1. develop better 3D shape signature and descriptor 
2. develop methods to automatically learn the 3D features

#### A. 3D shape signatures and descriptors

- 정의 : 3D shape **signature** and **descriptor** are succinct and compact** representations** of 3D object that capture the geometric essence of a 3D object[19]. 

> shape signature(SS) : a local description for a point on a 3D surface 
> shape descriptor(SD) :a global description for the entire shape. 


- **heat diffusion**에 기반한 SS와 SD가 3D를 표현하는데 효과적이다. `Shape signatures and descriptors, which are based on heat diffusion, have been proved to be very effective in capturing the geometric essence of 3D shapes. `

- **heat diffusion**에 기반하지 않는 SS/SD도 많이 제안 되었다. `On the other hand, a large amount of non-diffusion based shape features are also proposed in the literature`,
    - D2 shape distribution [36]
    - statistical moments [15]
    - Fourier descriptor[49, 42]
    - Light Field Descriptor [10]
    - Eigenvalue Descriptor[25], etc. 


- 최근 연구는 **diffusion **에 기반한것들이 대부분 이다. `Recent efforts on robust 3D shape feature development are mainly based on diffusion [45, 9, 41, 37].`


###### global point signature (GPS)[41]

- The global point signature (GPS)[41] uses `eigen value`s and `eigen functions` of the `Laplace-Beltrami` defined on a 3D surface to characterize points. 

###### Heat kernel signature (HKS) and wave kernel signature (WKS)

- Heat kernel signature (HKS) and wave kernel signature (WKS) [2, ?] have gained attention because of their multi-scale property and invariance toisometric deformations. 

>  단점 : GPS, HKS, WKS = point-based shape signatures -> **do not provide a global description** of the entire shape.

###### temperature distribution(TD)

- **A global shape descriptor**, named TD descriptor, is developed based on HKS information at a single scale [17] to represent the entire shape. 

- 제약 : it only describes the entire shape at one single scale resulting in an incomplete description of 3D objects [17]. 

- As indicated in [17] the selection of an appropriate scale is often not straightforward.

