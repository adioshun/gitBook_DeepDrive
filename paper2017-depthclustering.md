|논문명 |Efficient Online Segmentation for Sparse 3D Laser Scans |
| --- | --- |
| 저자\(소속\) | I. Bogoslavskyi\(\) |
| 학회/년도 | PFG2017, [논문](https://link.springer.com/article/10.1007%2Fs41064-016-0003-y) |
| Citation ID / 키워드 |Range Image, Clustering |
| 데이터셋(센서)/모델 |KITTI |
| 관련연구||
| 참고 |[Youtube](https://www.youtube.com/watch?v=xAAz3Zgkmy80), |
| 코드 |[python-ROS](https://github.com/PRBonn/depth_clustering) |



|년도|1st 저자|논문명|코드|
|-|-|-|-|
|2016|I. Bogoslavskyi|[Fast Range Image-Based Segmentation of Sparse 3D Laser Scans for Online Operation](http://www.ipb.uni-bonn.de/pdfs/bogoslavskyi16iros.pdf)||



# Efficient Online Segmentation for Sparse 3D Laser Scans


```
인지 시스템에서 사전-세그멘테이션은 이후 분석 작업을 위해 필수적인 요소 이다. `In most perception cues, a pre-segmentation of the current image or laser scan into individual objects is the first processing step before a further analysis is performed.`

본 논문에서는 바닦제거 + 물체 세그멘테이션을 다루고 있다. `In this paper, we present an effective method that first removes the ground from the scan and then segments the 3D data in a range image representation into different objects.`

본 논문에서는 2.5D range image를 이용하고 있다. `We explicitly avoid the computation of the 3D point cloud and operate directly on a 2.5D range image, which enables a fast segmentation for each 3D scan`
```


## 1 Introduction

인지 시스템에서 사전-세그멘테이션은 중요 하다. `Object segmentation from raw sensor data is especially relevant when mapping or operating in dynamic environments. In busy streets with cars and pedestrians, for example, the maps can be influenced by wrong data associations caused by the dynamic nature of the environment. A key step to enable a better reasoning about such objects and to potentially neglect dynamic objects during scan registration and mapping is the segmentation of the 3D range data into different objects so that they can be tracked separately, see (DEWAN et al., 2016)`

저채널(16ch)라이다 사용의 제약 `Sparser point clouds lead to an increased Euclidean distance between neighbouring points even if they stem from the same object. Thus, these sparse 3D points render it more difficult to reason about segments. The situation becomes even harder with the increase in distance between the object and the sensor.`

본 논문의 기여점 `The contribution of this paper is a robust method for separating ground from the rest of the scene and a fast and effective segmentation approach for 3D range data obtained from modern laser range finders such as Velodyne scanners.`

제안 바닥 제거 방법의 특징 : 곡선이 있거나, 평평하지 않아도 괜찮음, sub-sampling방법을 사용 안함 `To achieve the final segmentation, we first perform a robust ground separation which can detect ground fast and reliably. In contrast to several other approaches, the ground can have slight curvature and does not necessarily have to be entirely flat. We also do not use any kind of sub-sampling and decide for each pixel of the range image whether it belongs to ground or not. `

기존 연구에 바닥제거를 추가 하였음 `This paper extends our recently published conference paper on 3D range data segmentation (BOGOSLAVSKYI & STACHNISS, 2016). In this work, we added the robust ground removal and provide an extended experimental evaluation.`


## 2 Related Work

### 2.1 Segmenting objects from 3D point clouds

There is substantial amount of work that targets acquiring a global point cloud and segmenting it off-line.

Examples for such approaches are the works by ABDULLAH et al. (2014); ENDRES et al. (2009); GOLOVINSKIY
& FUNKHOUSER (2009); HEBEL & STILLA (2008); WANG & SHAN (2009).

These segmentation methods have been used on a variety of different data produced by 3D range sensors or 2D lasers in push-broom mode.

VELIZHEV et al. (2012) focus on learning the classes of the objects and detecting them in huge point clouds via a voting-based method.

These point clouds can be large, and the work by HACKEL et al. (2016) targets the runtime along with the quality of classification.

본논문의 차별점 : In contrast with these works, we focus on the segmentation of range data that comes from a 3D laser scanner such as a Velodyne that provides a 360 degree field of view in a single scan and is used for online operation on a mobile robot.
- Additionally, we target segmentation of a scene without the knowledge about the objects in it and without any prior
learning and not using complex features.


분석 논문 추천 : For a comprehensive analysis of methods that perform supervised scene segmentation we refer the reader to WEINMANN et al. (2015).


### 2.2 Ground removal

Ground removal is an often used pre-processing step and is therefore well-discussed in the literature.

RANSAC기반 방법 : There is a number of papers that use RANSAC for fitting a plane to the ground and removing points that are near this plane such as the work by OSEP ˇ et al. (2016).

시멘틱 세그멘테이션 방법 : Another prominent method of ground detection is a side-product of full semantic segmentation of the scene, where all parts of the scene get a semantic label.
- 바닥도 하나의 label로 분류됨 : The ground is then segmented as one class; for more details we refer the reader to the papers by HERMANS et al. (2014) and BANSAL et al. (2009).

높이 정보 이용 : A couple of approaches use a 2D-grid and analyse the heights of the points that fall into its bins, taking decisions about points being parts of the ground based on this information.

The decisions can be taken based on the inclination of lines between consecutive cells as in works by PETROVSKAYA &
THRUN (2008); LEONARD et al. (2008) or by analysing the height above the lowest local point as in works by GORTE et al. (2015); BEHLEY et al. (2013).

### 2.3 Segmentation techniques

Segmentation techniques for single scans without requiring additional information can be divided into three groups.


#### A. 3D domain

The first group, represented by the works by DOUILLARD et al. (2011,2014), performs the segmentation in the 3D domain by defining sophisticated features that explain the data in 3D or by removing the ground plane and segmenting the clouds with a variant of a nearest neighbour approach as shown by CHOE et al. (2012) and KLASING et al. (2008).

Feature-based approaches, while allowing for accurate segmentation, are often comparably time-consuming and may limit the application for online applications to a robot with substantial computational resources.

#### B. projecting 3D points onto a 2D grid positioned


The second group focuses on projecting 3D points onto a 2D grid positioned on the ground plane.

The segmentation is then carried out on occupied grid cells as in BEHLEY et al. (2013); HIMMELSBACH et al. (2010); KORCHEV et al. (2013); STEINHAUSER et al. (2008).

These algorithms are fast and suitable to run online.

Quite often, however, they have a slight tendency to under-segment the point clouds, i.e. multiple objects may be grouped as being one object if they are close to each other.

This effect often depends on the choice of the grid discretisation, so that the grid width may need to be tuned for individual environments.

Additionally, some of these approaches can suffer from under-segmenting objects in the vertical direction.


### C. range image

The third group of approaches performs the segmentation on a range image and our approach belongs to this group of techniques.

For example, MOOSMANN et al. (2009) and MOOSMANN (2013) use a range image to compute local convexities of the points in the point cloud.

In contrast to that, our approach avoids computing complex features and, thus, is easier to implement, runs very fast and produces comparable results.

We therefore believe that our approach is a valuable contribution to a vast and vibrant field of 3D point cloud segmentation, and consequently we will contribute our approach to the open source ROS community by providing the source code for our implementation.


### D. 그외 - RGBD

There are also several works (PYLVANAINEN et al., 2010; STROM et al., 2010) that perform segmentation on RGBD data acquired from a LIDAR registered with a camera.

Registering one or multiple cameras with the laser scanner requires a more sophisticated setup and the segmentation
becomes more demanding.

Using both cues may improve the results but it is seldom possible at speeds faster than the frame rate.

Therefore, we focus on segmenting unknown objects from pure 3D range data not requiring any additional visual or intensity information.

### E. 시각 정보외 데이터들 : 시간, tracking

Visual information is not the only information that aids segmentation. Temporal information and tracking are also shown to be useful to enhance the segmentation performance by FLOROS & LEIBE (2012) and TEICHMAN & THRUN (2012).

While the benefit of using the information about the moving objects is clear, we show that it is possible to perform a fast and meaningful segmentation on single scans even without relying on temporal integration.



## 3. Range Image based Ground Removal

기존 방식과 문제점
- A standard approach to ground removal simply discards all 3D points that are lower than the vehicle.
- While this approach may work in simple scenes, it fails if the vehicle’s pitch or roll angle is unequal to zero or if the ground is not a perfect plane.
- Using RANSAC-based plane fitting may improve the situation but even using this method,
- non-zero curvatures may remain a challenge and the operation can be time consuming.
제안 방식 & 생성 방법
- 제안 방식 : Most laser range scanners provide raw data in the form of individual range readings per laser beam with a time stamp and an orientation of the beam. This allows us to directly convert the data into a range image.
- 생성 방식
- The number of rows in the image is defined by the number of beams in the vertical direction, i.e., 16, 32 or 64 for the Velodyne scanners.
- The number of columns is given by the range readings per 360◦ revolution of the laser.
- Each pixel of such a virtual image stores the measured distance from the sensor to the object.

Raw데이터 제공 안 하는 장비 경우 `only provides a 3D point cloud per revolution and not the individual range measurements,`
- one can project the 3D points cloud onto a cylindrical image,
- compute the Euclidean distance per pixel, and proceed with our approach.


가정 사항 3가지 `For identifying the ground plane, we make three assumptions.`
- First, we assume that the sensor is mounted roughly horizontally on the mobile base/robot (this assumption can be relaxed, but the explanation would turn out to be more complex).
- Second, we assume that the curvature of the ground is low.
- Third, we assume that the robot observes the ground plane at least in some pixels of the lowest row of the range image (corresponding to the laser beam scans close to the ground close to the robot).


> 추후 논문 참고


## 4. Fast and Effective Segmentation Using Laser Range Images


The vertical resolution of the sensors has an impact on the difficulty of the segmentation problem.

For every pair of neighbouring points, one basically has to decide if the laser beams have been reflected by the same object or not.


본 논문에서는 range image를 사용 하였다. `In our approach, outlined in Fig. 4, we avoid the explicit creation of the 3D point cloud and perform our computations using a laser range image, in our case a cylindrical one for the Velodyne scanners. `

장점 두가지 `This has two advantages: `
- First, we can exploit the clearly defined neighbourhood relations directly in the range image and this makes the segmentation problem easier.
- Second, we avoid the generation of the 3D point cloud, which makes the overall approach faster to compute.

가정 사항 `We assume `
- the vehicle to move on the ground (see Fig. 1 for our setup) and
- we expect the sensor to be oriented roughly horizontally with respect to the wheels.
- Thus, we can quickly obtain an estimate of the ground plane by analysing the columns of such range image as described in Sec. 3.
- The ground is then removed from the range image.


주요 요소는 두개의 빔에서 반사된 정보가 같은 물체에서 온 것인가를 판단 하는 것이다. : The key component of our approach is the ability to estimate which measured points originate from the same object for any two laser beams.

방법은 angle-based measure를 이용하는것이다. 다음장에서 자세히 설명 하겠다. `To answer the question if two laser measurements belong to the same object, we use an angle-based measure, which is illustrated in Fig. 5 and is described in the following paragraphs.`

![](https://i.imgur.com/XK7X0Jp.png)
```
Fig. 5: 레이져가 물체에 도달시 각도 β가 특정값 θ이내이면 동일한 물체로 판단
- Left: example scene with two pedestrians, a cyclist and a car.
- Middle: Given that the sensor is in O and the lines OA and OB represent two laser beams,
- the points A and B spawn a line that estimates the surface of an object should they both belong to the same object.
- We make the decision about this fact based on the angle β.
- If β > θ, where θ is a predefined threshold, we consider the points to represent one object.
- Right: a top view on the pedestrians from the example scene.
- The green lines represent points with β > θ while the red one shows an angle that falls under the threshold and thus labels objects as different.

```

The left image of Fig. 5 shows an example scene with two people walking close to each other in front of a cyclist, who passes between them and a parked car.

This scene has been recorded using our Velodyne VLP-16 scanner.

The middle image shows an illustration of two arbitrary points A and B measured from the scanner located at O with the illustrated laser beams OA and OB.

Without loss of generality, we assume the coordinates of A and B to be in a coordinate system which is centred in O and the y-axis is oriented along the longer of two laser beams.

We define the angle β as the angle between the laser beam and the line connecting A and B in the point that is further away from the scanner (in our example that is A).

In practice, the angle β turns out to be a valuable piece of information to determine if the points A and B lie on the same object or not.

거리 정보를 알수 있음,이를 통해 β추출 가능 Given the nature of the laser range measurements, we know the distance ||OA|| as it corresponds to the first laser measurement as well as ||OB|| (second laser measurement).

We will call these range measurements d1 and d2 respectively. One can use this information to calculate β by applying trigonometric equations

![](https://i.imgur.com/b0rMuSH.png)


> 추가 설명 논문 참고, θ = 10◦ 로 사용


## 5. Experimental Evaluation

성능 평가 요소
- all computation can be executed fast, even on a single core of a mobile CPU with around 70 Hz,
- we can segment typical 3D range data obtained by mobile robots into meaningful segments,
- and the approach performs well on sparse data such as those obtained from a 16-beam Velodyne Puck scanner

비교 대상 `In our evaluation, we also provide comparisons to the`
- grid based segmentation method proposed by TEICHMAN & THRUN (2012) as used by BEHLEY et al.(2013) as well as to
- Euclidean clustering implemented in the point cloud library PCL.


### 5.1 Runtime

### 5.2 Segmentation Results

테스트 데이터
- For the 64-beam evaluation, we rely on the publicly available street scenes dataset by MOOSMANN (2013) and the KITTI dataset by GEIGER et al. (2013),
- while we recorded the 16-beam datasets using our robot in Bonn, Germany

테스트 설정 값
- grid : 0.05m ~ 1.25m
- 제안 : θ from 5◦ to 45◦




## 6 Conclusion

This paper presents a fast and easy to implement method for 3D laser range data segmentation including fast ground removal.

Instead of operating in the 3D space, our approach performs all computations directly on the range images.

This speeds up the segmentation of the individual range images and allows us to directly exploit neighbourhood relations.

It enables us to successfully segment even sparse laser scans like those recorded with a 16-beam Velodyne scanner.

We implemented and evaluated our approach on different publicly available and self-recorded datasets and provide comparisons to other existing techniques.

On a single core of a mobile i5 CPU, we obtain segmentation results at average frame rates between 74 Hz and 250 Hz and can run up to 667 Hz on an i7 CPU.

We will release our code that can either be used standalone with C++ or as a ROS module.

---


# [데모](https://github.com/PRBonn/depth_clustering)

