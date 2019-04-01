|논문명 |Pedestrian Detection and Tracking Using Three-dimensional LADAR Data |
| --- | --- |
| 저자\(소속\) | Luis E. Navarro-Serment\(Carnegie Mellon University\) |
| 학회/년도 | 2010, [논문](https://www.ri.cmu.edu/pub_files/2009/7/navarro_et_al_fsr_09.pdf) |
| Citation ID / 키워드 |SICK |
| 데이터셋(센서)/모델 |Demo III XUV |
| 관련연구||
| 참고 | |
| 코드 |  |



|년도|1st 저자|논문명|코드|
|-|-|-|-|
|||||




# Pedestrian Detection and Tracking Using Three-Dimensional LADAR Data

The algorithm uses geometric and motion features to recognize human signatures

## 1 INTRODUCTION

과거 연구 

### 1.1 평면
In our group, we have developed detection and tracking systems using SICKTM laser line scanners; 
- 평면에서 잘 동작 `these implementations work well in situations where the ground is relatively flat [5]. `
- However, a 3D LADAR captures a more complete representation of the environment and the objects
within it. 

비 평면에서도 잘 동작 : In [6], we presented an algorithm that detects pedestrians from 3D data.
- Its main improvement over the version with 2D data was that it constructs a ground elevation map, and uses it to eliminate ground returns. 
- This allows pedestrian detection even when the surrounding ground is uneven. 

### 1.2 분류 문제 

움직임 크기 등으로 분류 `To classify the humans the algorithm uses motion, size, and noise features. `

동적인 물체는 잘 판단, 정적 물체 에러 많음 `Persons are classified well as long as they are moving. However, there are still too many false positives when classifying stationary humans.`


본 연구를 통해 정적 물체도 잘 탐지 할수 있음 

## 2 RELATED WORK

### 2.1

> 2D 거리 기반 단순한 특징 이용

The approach reported in [1] applies AdaBoost to train a strong classifier from simple features of groups of neighboring points. 

This work focuses on 2D range measurements. 

### 2.2

> 3D 정보 surface density function이용 

Examples using three-dimensional data include [4], where 3D scans are automatically clustered into objects
and modeled using a surface density function. 

A Bhattacharya similarity measure is optimized to register subsequent views of each object enabling
good discrimination and tracking, and hence detection of moving objects.

### 2.3

> 스트레오 비젼을 이용하여 3D pointcloud 생성 

In [3], the authors describe a pedestrian detection system which uses stereo vision to produce a 3D point cloud, and then classifies the cloud according to the point shape distribution considering the first two central moments of the 2D projections using a naive Bayes classifier. 

Motion is also used as a cue for human detection.

### 2.4 

> 3D lidar + inrared video 퓨젼 

In [8] the authors report an algorithm capable of detecting both stationary and moving humans. 

Their approach uses multi-sensor modalities including 3D LADAR and long wave infrared video (LWIR). 

### 2.5


Similarly, in [9] the same research group presents a technique for detecting humans that combines the use of 3D LADAR and visible spectrum imagery. 

In both efforts the authors employ a 2D template to extract features from the shape of an object. 

Among other differences, as opposed to our work, they extract a shape template from the projection in only one plane, and compute a measure of how uniformly distributed the returns are across the template. 

## 3 ALGORITHM DESCRIPTION

1. we do object detection and tracking in a 2D data subset first, 
2. and then use the object’s position and size information to partition the set of 3D measurements into smaller groups, for further analysis.

### 3.1 Projection into 2D Plane


특정한 높이를 기준으로 3D -> 2D로 변형 `we initially isolate a 2D virtual slice, which contains only points located at a certain height above ground.`


The ground elevation is stored in a scrolling grid that contains accumulated LADAR points and is centered at the vehicle’s current position. 

포인트는 age정보로 가중치를 주며 최근 일수록 가중치가 크다. `The points are weighted by age, more recent points have a heigher weight. `

The mean and standard deviation of the heights of all scan points that are inside each cell are computed, and the elevation is then calculated by subtracting one standard deviation from the average height of all the points in the cell. 

중심 아이디어 : The key properties of this simple algorithm are that mean and standard deviations can be calculated recursively, and that the elevation is never below the lowest point while still having about 80% of the points above ground.


The system adapts to different environments by varying the shape of the sensing plane i.e., by adjusting the height of the slice from which points are projected onto a two-dimensional plane. 


가짜 데이터 처리 : Spurious measurements produced by ground returns are avoided by searching for measurements at a constant height above the ground. 

Since our research was done in an open outdoor environment, we did not encounter overhanging structures like over paths or ceilings. 

These might be topics of future research.

### 3.2 Motion Features


After detecting and tracking objects using the virtual scan line we can compute a Motion Score (MS).

The MS is a measure of how confident the algorithm is that the detected object is a human, based on four motion-related variables: 
- the object’s size, 
- the distance it has traveled, 
- and the variations in the object’s size and velocity. 

The size test discriminates against large objects like cars and walls. 

The distance traveled test discriminates against stationary objects like barrels and posts. 

The variation tests discriminate against vegetation, since their appearance changes a lot due to their porous and flexible nature. 

The individual results of these tests are scored, and then used to calculate the MS. 

A detailed description of each test and all parameters involved is presented in [6].


### 3.3 Geometric Features

고정 물체 탐지를 위해서 2D로 추적된 물체의 geometric features를 계산 한다. 계산값은 분류기에 전달 되어 사람인지 아닌지 판단 한다. `To discriminate against static structures, we compute a group of distinguishing geometric features from the set of points belonging to each object being tracked in 2D, and then feed these features to a classifier, which determines whether the object is a human or not.`

![](https://i.imgur.com/NxZtEeb.png)

#### A. 데이터 수집 : Fig. 2(a)

- As shown in Fig. 2(a), the process starts when a point cloud is read from the sensor. 
 - We define `Zj = {x1, x2, . . . , xN }` as the set of N points contained in a frame collected at time `tj` , 
 - whose elements are represented by Cartesian coordinates x = (x, y, z). 

- 색상은 높이 이다. The points corresponding to one frame are shown, and are colored according to their height above ground. 

#### B. extract a 2D virtual slice : Fig. 2(b)

- 계산 부하를 줄이기 위해 2D V-Slice 생성 `To avoid the computational cost of processing the entire point cloud, we extract a 2D virtual slice, as described in Section 3.1 (Fig. 2(b)).` 

#### C. 후보 추출 : Fig. 2(c).

- [6]의 제안방식을 활용하여 추적 물체의 위치, 속도, 크기 측정 `For each object being tracked, its position, velocity, and size are estimated using the algorithm described in [6]. `
 - 이 정보를 이용하여 MS 값 계산 `These values are used to compute the MS. `

- 사람으로 예상 되는 점들만 남김 The object’s position and size information are used to isolate, from the original point cloud, only those
points corresponding to potential humans, as shown in Fig. 2(c). 
 - 추출된 점들을 M으로 표기 At this point, we have a collection of `M` sets `{S1, S2, . . . , SM}`, where `Si∈{1,2,...,M} ⊂ Zj` .


#### 특징 벡터 추출 : Figs. 2(d) - (e)
A feature vector is computed from each of these sets (Figs. 2(d) - (e)), and then fed to a classifier that determines for each object whether it is a human or not, Fig. 2(f).


- 각 물체별로 결정이 이루어짐 `This decision is made for each object, and is based on the most recent set of points collected from the sensor. `
 
- 분류기는 MS계산시 사용한 정보도 고려하여 분류 한다. `The classifier also takes into account the information used to calculate the MS; this is described in a subsequent section.`

- A set of features is computed with the purpose of extracting the most informative signatures of a human in an upright posture from the 3D data.

- 다리가 사람을 구분하는 중요 요소 이므로 다리 부분부터 계산 한다. `The legs are particularly distinctive of the human figure, so the algorithm computes statistical descriptions from points located around the legs. `

- 비슷한 descriptions를 이용하여 몸통을 계산한다. `Similar descriptions are computed from the trunk area, representing the upper body.`

- Additionally, the moment of inertia tensor is used to capture the overall distribution of all points. 

- Finally, to include the general shape of the human figure, we compute the normalized 2D histograms on two planes aligned with the gravity vector.


#### A. Feature Extraction

![](https://i.imgur.com/P0hIA57.png)

- 특정 물체K의 포인트를 `S_k`라고 간주 하자. : Let `S_k = {x1, x2, . . . , xn}` be the set of points belonging to the object `k`, whose elements are represented by Cartesian coordinates x = (x, y, z). 

- 특징은 S_K를 기반으로 계산된다. : A set of suitable features is computed from `Sk`, as depicted in Fig. 2(d), which constitutes a profile of the object.

- 통계적 패턴 정보를 찾기 위하여 모든 S_k에 대하여 PCA를 실시 한다. ` We begin by performing Principal Component Analysis (PCA) using all the elements of `Sk`, to identify the statistical patterns in the three-dimensional data (see Fig. 3). `

- This involves the subtraction of the mean `m` from each of the three data dimensions. 

- 이 zero mean으로 된 새 데이터셋에서 아래 두 정보를 계산 한다. ` From this new data set with zero mean, we calculate`
 - the covariance matrix  `Σ ∈ <3×3`, and 
 - the normalized moment of inertia tensor `M ∈ <3×3`, treating all points as unit point masses:

![](https://i.imgur.com/kZL2TaV.png)

- 각 Feature에 대하여 6개의 element를 사용한다. Since both `Σ` and `M` are symmetric, we only use 6 elements from each as features.

- PCA의 결과물은 3쌍의 고유벡터와 고유값이다. `과 Resulting from the PCA are three pairs of eigenvectors and eigenvalues, sorted according to decreasing eigenvalue. `
 - Call these eigenvectors `e1`, `e2`, `e3`, with their corresponding eigenvalues `λ1 > λ2 > λ3`. 

- 사람은 서 있다고 가정하기 때문에 `We assume that a pedestrian is in an upright position`, 
 - so the principal component `e1` is expected to be vertically aligned with the person’s body1. 

Together with the second largest component `e2`, it forms the main plane (Fig.3, center top), and also forms the secondary plane with the smallest component, e3 (Fig.3, center bottom). 

- 다음으로 원본 값을 두 representations으로 변형 한다. : We then transform the original data into two representations using each pair of components `e1`, `e2` and `e1`, `e3`, from which we proceed to compute additional features (the third possible representation, i.e. using the two smallest components e2, e3, is not used).

We focus on the points included in the main plane, to analyze the patterns that would correspond to the legs and trunk of a pedestrian, as shown in Fig 3, center top. 

These zones are the upper half, and the left and right lower halves. 

After separating the points into these zones, we calculate the covariance matrix (in 2D) over the transformed points laying inside each zone.

This results in 9 additional features (3 unique values from each zone).

Finally, we compute the normalized 2D histograms for each of the two principal planes (Fig. 3, right), to capture the shape of the object. 

We use `14×7` bins for the main plane, and `9×5` for the secondary plane. 

Each bin is used as a feature, so there are 143 features representing the shape. 

A total of 164 geometric features are determined for each object.

### 3.4 Human Detection

분류기는 독립된 두개의 SVM으로 구성된다. `A classifier (Fig. 2(f)), composed of two independent Support Vector Machines (SVM) [2], determines for each object whether it is human or not. `

#### A. 첫번째 SVM

- S_k에서 바로 계산된 164 geometric features를 입력으로 받아 사람과 비슷한 모양인지를 계산한다.  
 - `The first classifier is a SVM that receives the vector of 164 geometric features computed directly from Sk, and scores how closely the set matches a human shape. `
 - 이 계산값을 GS라고 부른다. `We call this the Geometric Score (GS). `
 - 정적 보행자 탐지에도 효과적이다. `The GS is particularly effective for detecting static pedestrians. `

- MS를 결정하는 Feature들은 물체의 모션 정보를 가지고 있다. `Similarly, the features used to determine the MS  contain valuable information about the motion of the target. `
 - MS : object’s size, the distance it has traveled, and the corresponding size and motion noises

#### B. 두번째 SVM

- GS+MS를 입력으로 받아 결과로 `distance to the decision surface of the SVM`를 출력 한다. 
 - Together with the GS, these features are fed to a second SVM, whose output represents the distance to the decision surface of the SVM. 

- 신뢰도를 계산 하는데 사용된다. 
 - The Strength of Detection (SOD), the total measure of how strongly the algorithm rates the object as being a human, is calculated as the logistic function of the distance to the decision surface. 

- 각 물체 별로 계산 된다. This number is reported for each object. 

- 만약 GS가 계산되지 않으면 MS값이 신뢰도(SOD)로 제공된다. 
 - If the GS cannot be computed (e.g. insufficient data from a distant target, or violation of the upright position assumption), then the MS is reported as the SOD for that object.


#### A. Training

We trained the GS classifier using a combination of simulated and real examples. 

Because it is impossible to collect enough real data to evaluate perception algorithms in all possible situations, we have created a simulator capable of producing synthetic examples of sensor data. 

The simulator uses a ray tracing engine to generate a set of ray intersections between sensor and the objects in the scene to simulate. 

This information is then used to produce synthetic LADAR measurements according to a set of parameters for a particular sensor, as shown in Fig. 4. 

We trained the GS classifier using over 3500 examples (27.4% humans, 72.6% non-humans). 

The human set included 62% of simulated examples. 

The second classifier was trained using only real examples, since the motion and size noises used to determine the MS are of a dynamic nature and consequently harder to simulate efficiently (over 46000 examples: 6% humans, 94% non-humans).

We trained both SVMs using a five-fold cross validation procedure. 

We found that both radial basis function (RBF) and polynomial kernels resulted in similar levels of classification performance. 

After multiple tests, we determined that a RBF kernel was the best for the calculation of the GS, while a polynomial kernel was preferred for the second classifier.



## 4 EXPERIMENTAL RESULTS


## 5 CONCLUSION

We described a pedestrian detection and tracking system using only three dimensional data. 

The approach uses geometric and motion features to recognize human signatures, and clearly improves the detection performance achieved in our previous work. 

The set of features used to determine the human and motion scores was designed to detect humans in upright positions.

To increase the robustness of detection of humans in other postures, in future research we will investigate ways of extracting signatures from the point cloud that are highly invariant to deformations of the human body.









