|논문명|Computer Vision for Autonomous Vehicles: Problems, Datasets and State-of-the-Art
|-|-|
|저자(소속)||
|학회/년도| 2017 [논문](https://arxiv.org/abs/1704.05519v1)|
|키워드||
|참고|[홈페이지](http://www.cvlibs.net/projects/autonomous_vision_survey/), [CVPR 2016(1:02)](https://www.youtube.com/watch?v=n8T7A3wqH3Q&feature=share)|
|코드||


- ~~[A REVIEW OF POINT CLOUDS SEGMENTATION AND CLASSIFICATION ALGORITHMS](https://www.int-arch-photogramm-remote-sens-spatial-inf-sci.net/XLII-2-W3/339/2017/isprs-archives-XLII-2-W3-339-2017.pdf)~~: 딥러닝 외 방식들 (Edge based, Region growing, Model fitting, Hibrid method, Hirarchical clustering, k-mean clustering)


# Survey 

Recognition, reconstruction, motion estimation, tracking, scene understanding and end-to-end learning

![](https://i.imgur.com/f5mYsf1.png)

자율 주행차가 아직까지 먼 미래의 이야기인 이유

1. First, autonomous systems which operate in complex dynamic environments require artificial intelligence which generalizes to unpredictable situations and reasons in a timely manner. 
2. Second, informed decisions require accurate perception, yet most of the existing `computer vision systems` produce errors at a rate which is not acceptable for autonomous navigation.

> 본 논문은 2번째 이유인 CV에 초점을 둔다. 

기존 Survey 논문들 

- Winner et al. (2015) explains in detail systems for `active safety and driver assistance`, considering both their structure and their function. 
    - Their focus is to cover all aspects of driver assistance systems and the chapter about machine vision covers only the most basic concepts of the autonomous vision problem. 
- Klette (2015) provide an overview over `vision-based driver assistance systems`. 
    - They describe most aspects of the perception problem at a high level, 
    - but do not provide an in-depth review of the state-of-the-art in each task as we pursue in this paper. 
- Zhu et al. (2017) provide an overview of environment perception for intelligent vehicles, focusing on `lane detection`, `traffic sign/light recognition` as well as `vehicle tracking`.


```
Winner, H., Hakuli, S., Lotz, F., Singer, C., Geiger, A. et al. (2015). Handbook of Driver Assistance Systems . Springer Vieweg.
Klette, R. (2015).Vision-based Driver Assistance Systems .  Technical Report CITR, Auckland, New Zealand.
Zhu, H., Yuen, K. V., Mihaylova, L., & Leung, H. (2017).   Overview of en-vironment  perception  for  intelligent  vehicles. IEEE  Trans.  on  Intelligent Transportation Systems (TITS),PP , 1–18.
```

## 1. History of Autonomous Driving 

## 1.1 Autonomous Driving Projects

### A. PROMETHEUS project
started 1986 in Europe and involved more than 13 vehicle manufacturers, several research units from governments and universities of 19 European countries. 

### B. Navlab (CMU)
One of the first projects in the United States was Navlab Thorpe et al. (1988)  by  the  Carnegie  Mellon  University  which  achieved  a major milestone in 1995,


### C. etc.

> 약 1page에 걸쳐서 다른 프로젝트들 소개 

### 1.2 Autonomous Driving Competitions

#### A. The European Land Robot Trial (ELROB)

## 2. Datasets & Benchmarks

### 2.1 Real-World Datasets

#### A. Stereo and 3D Reconstruction


#### B. Optical Flow

#### C. Object Recognition and Segmentation

- ImageNet (Deng et al. (2009))
- PASCAL VOC (Everingham et al. (2010))
- Microsoft  COCO  (Lin  et  al.  (2014))
- Cityscapes  (Cordts  et  al. (2016))
- TorontoCity (Wang et al. (2016)) 

#### D. Tracking


#### E. Aerial  Image  Datasets

#### F. Autonomous Driving

- KITTI Vision Benchmark
- Cityscapes Datase
- TorontoCity benchmark

#### G. Long-Term Autonomy

Maddern et al. (2016). They collected images, LiDAR and GPS data while traversing 1,000 km in central Oxford in the UK during one year.  

This allowed them to capture large variations in scene appearance due to  illumination,  weather  and  seasonal  changes,  dynamic objects, and constructions.  

Such long-term datasets allow for in-depth investigation of problems that detain the realization of autonomous vehicles such as localization in di erent times of the year.
 
```
Maddern, W., Pascoe, G., Linegar, C., & Newman, P. (2016).  1 year, 1000km: The oxford robotcar dataset. International Journal of Robotics Research (IJRR) , 
```

### 2.2. Synthetic Data (가상 데이터)

> 실생활 데이터를 Pixel 수준으로 Labeling하는것은 어렵다. 하지만, 게임등으로 습득 하는것은 쉽다. 


#### A. MPI Sintel

#### B. Flying Chairs and Flying Things

#### C. Game Engines

## 3. Cameras Models & Calibration

## 4. Representations

