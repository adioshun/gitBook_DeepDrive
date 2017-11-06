# Vision-based SLAM((Simultaneous Localization And Mapping))

## 1. 개요 

영상 기반 항법 기술

- 맵이 필요 없는 항법(mapless) : 비주얼 서보잉(VS; visual servoing), 비주얼 오도메트리(VO; visual odometry)

- 맵을 기반으로 하는 항법(map-based)

  - 맵을 구성하는 항법(map-building) : 영상 기반 슬램(visual SLAM) 
 
  - 맵을 이용하는 항법(map-using)

### 1.1 정의 (영상정보를 기반으로 자율 항법기술)

#### A. 비주얼 서보잉
- 목표 이미지와 현재 이미지 사이의 피쳐 차이로부터 원하는 속도 입력을 계산하여 무인 로봇을 목표 자세로 유도하는 데 사용
- 주어진 영상 정보를 바탕으로 무인 시스템을 원하는 위치로 이동시키는 기법
- 획득한 영상정보를 바탕으로 현재 무인 시스템의 목표 속도를 계산하는 것

#### B. 비주얼 오도메트리
- 무인 시스템이 영상정보를 바탕으로 자신의 이동 궤적을 추정하는 기술로, 기존의 dead-reckoning 방식보다 정확성을 향상시
킬 수 있다
- 영상 정보를 바탕으로, 자기 자신의 이동 궤적을 추정하는 기술

#### C. 영상 기반 SLAM
- 무인 시스템이 영상 정보를 활용하여 미지의 환경에 대한 지도를 구축함과 동시에 자신의 위치를 결정해 나가는 기술로, 정확히 알지 못하는 환경에서 무인차량이나 무인기를 운용하는데 필수적



> SLAM : 이동 로봇이 자신의 **위치를 인식**하고 동시에 주변 환경에 대한 **지도를 작성**하는 것을 말한다.
> - 어떤 센서를 통해 주변 환경에 대한 정보를 얻느냐에 따라 다양한 종류의 SLAM이 존재
> - : 카메라를 이용하는 방법을 Visual SLAM이라고 함

 




 
### 1.2 역사 

- 1986년 국제 로봇공학 및 자동화 컨퍼런스에서 수학적 정의가 이루어졌다. 

- 1995년 국제 로봇공학 연구 심포지엄에서(International Symposium on Robotics Research)  SLAM이란 용어가 처음 등장했다. 

- 1998년 Davison 등[3]이 유럽 컴퓨터 비전 컨퍼런스에 다른 센서 없이 카메라만을 사용한 방법을 제시함으로써, 카메라를 3차원 위치 탐지기로 한 **비전 기반 SLAM**이 본격적으로 발전하게 되었다. 

- 1999년 Thrun [4]에 의해 칼만 필터 방법론에 기반한 확률적 접근으로 이론이 정립되었고, 

- 뒤를 이어 계산 복잡도, 데이터 조합, 구현 등에 관한 연구가 활발히 진행되었다. 

### 1.3 목적 

#### A. Localization 
- 위치 인식은 로봇이 '내가 어디에 있는가?'를 파악하는 문제이다. 

- 이것이 기존의 위치 추적 (pose tracking)과 다른 것은 SLAM의 경우 로봇의 초기 위치를 알 수 없기 때문이다. 
 - 낯선 곳에서 처음 눈을 뜬 사람과 마찬가지로 시야(이미지 프레임)에 들어오는 시각적 정보를 바탕으로 위치를 추정한다. 

- 사람은 거리나 방위에 대해 절대적인 감각을 가지고 있는 것이 아니라 상황에 따라 판단하므로 종종 착각을 하거나 길을 헤매기도 한다. 

- 로봇 역시 자신이 이동해 나가는 진행 방향과 경로를 주변 환경에 대해 상대적으로 계산한다. 그러므로 지도가 잘 만들어져야 자신의 위치를 정확히 파악할 수 있다. (그림 )

- 카메라 내부의 렌즈 특성 등을 포함하여 카메라의 회전 정도와 이동 거리를 계산하는 카메라 캘리브레이션 (Camera Calibration 또는 Camera Re-sectioning)의 문제는 컴퓨터 비전의 핵심 주제 중 하나이다. 

- 2차원의 이미지 프레임 상의 특징점들을 실제의 3차원 좌표와 매칭시켜 동차 좌표 (Homogeneous coordinates)를 적용한 투영 행렬 (Projection matrix)을 구한다. 

- SLAM에서는 카메라의 위치와 방향이 그대로 로봇 자신의 것이 되므로 Ego-motion estimation 또는 Self-calibration이라고 부르기도 한다. 

#### B. Mapping
- 지도 작성은 '세상이 어떻게 보이는가?'하는 문제에 대해 로봇이 센서를 가지고 수집한 정보들을 분석하여 답을 그려 나가는 과정이다. 

- 카메라를 센서로 사용하는 비전 기반 SLAM에서는 영상 처리 (image processing)의 필수 과정인 특징점 검출 (feature detections)을 통해 실제 공간에서는 하나의 점이라고 생각되는 각 이미지 프레임 상의 점들을 매칭한다. 

- 이때 각 이미지가 찍힌 위치, 즉 로봇의 위치 정보를 근거로 한다. 그러므로 위치 인식과 지도 작성의 문제는 상보적이다. 

- 다(多)시 점 기하학 (Multiple-view Geometry) [11]에 바탕을 두고 움직이는 물체의 구조를 알아내는 SfM (;Structure from Motion) 등 컴퓨터 비전의 3차원 복원 (3D Reconstruction) 기술은 보통 오프라인으로 진행되는 과정이었으나, SLAM에 적용되면서는 시시각각 변하는 위치 인식 정보와 더불어 결과가 나와야 하기 때문에 온라인으로 처리되어야 한다. 

- 그래서 컴퓨터의 계산 속도나 성능, 알고리즘의 복잡성, 정확도를 높이기 위한 최적화 등을 통해 효율을 높이는 것이 관건이다. 

- SLAM의 각 과정의 처리 속도는 현재 수 천 분의 일 초 (ms)로, 실시간을 지향한다. 


## 2. 기술 

### 2.1 기술 구성 

- SLAM 문제는 
 - 로봇의 상태, 즉 현재 위치와 자세(방위)를 나타내는 모션 모델 (motion model)과 
 - 카메라를 통해 들어온 이미지 상의 랜드마크들(landmarks)의 위치 정보를 나타내는 관측 모델 (observation model)로 구성된다. 

### 2.2 동작과정 
- 1. Markov process와 conditional Bayes rule을 적용하여 랜드마크의 관찰 결과로부터 다음 프레임에서의 모션 모델을 확률적으로 예측하고 (time-update), 
- 2. 이렇게 계산된 모션 모델과 지금까지 누적된 관찰 결과를 조합하여 랜드마크들의 다음 위치를 추정하여 관측 모델을 수정하는 (measurement update) 단계를 반복적으로 수행한다. (그림 )

> SLAM 문제는 무인 시스템에 가해진 입력과 주변 환경의 관측 값에 대한 확률 모델을 세우는 것에서부터 시작한다. 

#### A. 대표적인 해법 : EKF(extended kalman filter)SLAM이다

- 원리 : 무인 시스템의 운동방정식과 관측 모델 방정식을 현재 시점에서 선형화하여 시간 갱신(time update)와 측정치 갱신(measurement update)를 진행한다

- 문제점 #1: 거리가 먼 특징들의 경우 EKF모델에 쓰이는 불확실성을 설정하기가 어려웠으나, 
 - 해결법 : inverse-depth 개념이 도입되면서 모든 거리에 대한 불확실성을 가우시안 분포로 표현할 수 있게 되었다[28]. 
  - 해결법의 단점 : inverse-depth 표현법은 특징점의 좌표를 6개의변수로 나타내야하기 때문에 EKF 상태량 벡터의 크기를 2배로증가시키게 하였다. 

- 문제점 #2:  EKF기반의 SLAM에서는 관측 지점이 추가됨에 따라 상태량 벡터의 크기가 계속 증가하기 때문에계산을 거듭할수록 맵 구성 속도가 현저히 떨어진다. 

- 문제점 #3: 또한 추가된 관측 지점이 기존의 관측 지점과 일치하는지를 판별하는data association 문제에 대해서도 취약하다는 단점이 있다[29].

#### B. 최근 해법(2015) : Fast SLAM
FastSLAM은 EKF-SLAM의 느린 계산 속도에 대한 해결책으로 등장한 SLAM이다[29]. 

- 원리 :
 - Rao-blackwellization을 통해 무인시스템의 상태량을 샘플화한다. 
 - 여기서 각 샘플이 무인 시스템의 실제 위치 정보를 가진다는 가정을 추가하면, 무인 시스템관련 상태량의 확률 분포와 맵에 관한 상태량의 확률분포가 서로 독립이 된다. 
 - 결국 맵을 독립적인 가우시안들로 표현할 수있기 때문에 결합분포를 가졌던 이전에 비해 계산 속도가 비약적으로 증가하게 된다[30].



### 2.3 기술 구분 

#### A. 기존 SLAM

Davison [7]와 Nistér [8]는 카메라에서 수신된 신호와 로봇 자세의 불확정성을 가우시안 노이즈 (Gaussian uncertainty)로 가정하고 확장 칼만 필터 (extended Kalman filter)를 사용하여 비선형 모델의 상태를 선형적인 조합으로 추정하는 전통적인 SLAM의 방식에 접근하였다. 

#### B. 개선 SLMA (Vision based SLAM?)

Pupilli 등[9]은 입자 필터링 (Particle filter)을 사용하는 기존의 SLAM 방식에 3차원 모델을 마커로 한 컴퓨터 비전의 물체 추적 기술을 결합하여 성능을 향상시켰다. 

Eade 등 [23]은 모션 모델에는 입자 필터를 관측 모델에는 칼만 필터를 각기 적용하여 다중 데이터 조합 (multiple data association)을 가능케 한 FastSLAM [24]의 방법을 단일 카메라로 구현하여 계산량을 대폭 감소시킬 수 있음을 보여 주었다.

![](http://i.imgur.com/BJK1j7N.png)

---

# SfM

SfM 완전이해
- toy-sfm 코드를 통해 framework 을 완전이해하였다. 이 역시 앞으로 큰 자산이 될 듯. sfm에 best view select part 가 using sequential image 로 바뀌면 visual odometry 이고 여기에 loop closing module 이 붙으면 vSLAM이 된다!라는 간단한 핵심 파악. (물론 vSLAM의 경우 실제 모듈은 병렬적으로 즉 PTAM 적으로 구성되어야 함)

Structure from motion (SfM) is the process of estimating the 3-D structure of a scene from a set of 2-D images. This example shows you how to estimate the poses of a calibrated camera from two images, reconstruct the 3-D structure of the scene up to an unknown scale factor, and then recover the actual scale factor by detecting an object of a known size.

두장의 이미지를 이용하여 3D 정보를 출려 ㄱ하는것??

The Structure From Motion PipeLIne [Youtube)](https://www.youtube.com/watch?v=i7ierVkXYa8)
- 여러 사진(예:671)을 찍은다. 
- 각 사진에서 특징점을 추출 한다. 
- 사진들간의 특징점 연결선을 추출 한다. 

- [A Survey of Structure from Motion](https://arxiv.org/abs/1701.08493)ㅣ 2017

---

- [Augmented Reality And Vision-based SLAM 증강 현실과 비전 기반 슬램](http://metacups.blog.me/100088432677)

---


