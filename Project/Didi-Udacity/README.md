![](http://i.imgur.com/Kmm1uwY.png)

> https://github.com/adioshun/Didi_challenge

## 1. 개요 

자율주행 차 개발의 주요 Task중 하나는 주변 상황을 이해 하는 것이다.

본 Challenge를 통해 참가자는 LIDA데이터와 Camera데이터를 활용하여 주변 상황을 인지 하여야 한다.

## 1.2 데이터셋 

[awesome-vehicle-datasets](https://github.com/hunjung-lim/awesome-vehicle-datasets/tree/master/vehicle/Didi-Challange)

## 1.3 주요 링크 

- [Homepage](https://www.udacity.com/didi-challenge), [Details #1](https://challenge.udacity.com), - [Details #2](http://www.yuchao.us/2017/04/didi-challenge.html)

- [Github](https://github.com/udacity/didi-competition)

- [Discussions-udacity](https://discussions.udacity.com/c/didi-udacity-challenge-2017)



# Getting Started Didi-Challenge

> https://github.com/udacity/didi-competition/blob/master/docs/GettingStarted.md

## 1. 개요 
Challenge 목표 : Detecting and locating obstacles in 3D space, [평가방법](https://github.com/udacity/didi-competition/tree/master/tracklets#metrics-and-scoring)


## 2. Dataset

학습 데이터는 [ROS bag](http://academictorrents.com/details/76352487923a31d47a6029ddebf40d9265e770b5) 파일로 제공됨 
- 1,2의 차이 살펴 보기(1은 Training), bag파일은 1번에 있음 

A bag contains the synchronized output of several ROS nodes.

vehicle bag
- Camera video
- Lidar point clouds
- GPS/IMU measurements

Obstacle bags 
- Front RTK GPS
- Back RTK GPS

###### [Tip] Convert `/velodyne_packets` to `/velodyne_points` ,[출처](https://github.com/udacity/didi-competition/blob/master/docs/GettingStarted.md#convert-velodyne_packets-to-velodyne_points)

일부 데이터셋에는 용량문제로 Velodyne point cloud(`published on the /velodyne_points ROS topic`) 데이터가 없을수 있음 

The LIDAR readings are represented in a compressed packet form (/velodyne_packets)

```bash
# Install the Velodyne package
sudo apt-get install ros-indigo-velodyne

# Run the conversion tool for the HDL-32E LIDAR unit that Udacity used to record the data
rosrun velodyne_pointcloud cloud_node _calibration:=/opt/ros/indigo/share/velodyne_pointcloud/params/32db.yaml

```
Now when you play a bag file with the `/velodyne_packets` topic, it will automatically get converted to a point cloud format and republished as `/velodyne_points`




## 3. 활용 소프트웨어 

- ROS : 데이터셋 추출 및 가공 

- RVIZ : [데이터 시각화](https://github.com/udacity/didi-competition/blob/master/docs/GettingStarted.md#display-data-in-rviz) 

- Autoware  : camera/LIDAR calibration.


---

## 2. Solution

### 2.1 omgteam
- [omgteam](https://github.com/omgteam/Didi-competition-solution): This repository is to provide visualization, calibration, detection ROS nodes.

### 2.2 hengcherkeng

- [part.1: Car and pedestrian Detection using Lidar and RGB](https://medium.com/@hengcherkeng/part-1-didi-udacity-challenge-2017-car-and-pedestrian-detection-using-lidar-and-rgb-fff616fc63e8)

- [part.2: Car and pedestrian Detection using Lidar and RGB](https://medium.com/@hengcherkeng/part-2-didi-udacity-challenge-2017-car-and-pedestrian-detection-using-lidar-and-rgb-bb8e28f6d987)

- [part.3: Car and pedestrian Detection using Lidar and RGB](https://medium.com/@hengcherkeng/part-3-didi-udacity-challenge-2017-car-and-pedestrian-detection-using-lidar-and-rgb-e86490774ec6)

- [part.4a: Car and pedestrian Detection using Lidar and RGB](https://medium.com/@hengcherkeng/part-4-didi-udacity-challenge-2017-car-and-pedestrian-detection-using-lidar-and-rgb-6f6a964b94b5)

- [part.4b: Car and pedestrian Detection using Lidar and RGB](https://medium.com/@hengcherkeng/part-4b-didi-udacity-challenge-2017-car-and-pedestrian-detection-using-lidar-and-rgb-9f8b910562fc)

- [hengck23's GitHub](https://github.com/hengck23/didi-udacity-2017)


### 2.3 Team Timelaps(markstrefford)

- [github](https://github.com/markstrefford/didi-sdc-challenge-2017)


### 2.4 experiencor

> 포인트 클라우드가 아닌 이미지에 3D Bbox 적용하는 방법 

- [3D Vehicle Detection for Self Driving Car](https://experiencor.github.io/sdc_3d.html)

- [Didi-Starter](https://github.com/experiencor/didi-starter)

- [Simple Solution](https://github.com/experiencor/didi-starter/tree/master/simple_solution)

### 2.5 Boston Team 

- [Multi-View 3D Object Detection Network for Autonomous Driving](https://github.com/bostondiditeam/MV3D), [정리](https://www.gitbook.com/book/adioshun/deep_drive/edit#/edit/master/papermultiview-3d-cnn/codemv3d.md?_k=xxci2s)

- [kitti](https://github.com/bostondiditeam/kitti)

- [matters pertaining to Robot Operating System (ROS)](https://github.com/bostondiditeam/ros)

### 2.6 MV3D_TF

https://github.com/adioshun/MV3D_TF

### 2.9 etc

- [lancejchen](https://github.com/lancejchen/didi-competition.git)

## 3. References

- [**List** of LIDAR Point Clouds and Deep Learning](https://bigsnarf.wordpress.com/2017/05/12/lidar-point-clouds-and-deep-learning/)


### 3.1 Article/Blog 

- ~~[Vehicle detection using LIDAR: EDA, augmentation and feature extraction](https://chatbotslife.com/vehichle-detection-using-lidar-eda-augmentation-and-feature-extraction-udacity-didi-challenge-4c95a0c28566)~~: 별 내용 없음 



- [explore_udacity_didi_data.ipynb](https://github.com/markstrefford/didi-sdc-challenge-2017/blob/master/explore_udacity_didi_data.ipynb)

### 3.2 Tutorial

#### A. Ronny Restrep

- [Lidar Data to 2D](http://ronny.rest/blog/post_2017_03_25_lidar_to_2d/)

- [Lidar Birds Eye Views](http://ronny.rest/blog/post_2017_03_26_lidar_birds_eye/)

- [ROS and ROS bags - Part1](http://ronny.rest/blog/post_2017_03_29_ros/)

- [ROS and ROS bags - Part2](http://ronny.rest/blog/post_2017_03_30_ros2/)

- [ROS and ROS bags - Part3](http://ronny.rest/blog/post_2017_03_30_ros3_and_lidar/)


## 4. Tools

### 4.1 ROS Viwer


- [redlinesolutions](https://github.com/redlinesolutions/Udacity-Didi-Challenge-ROSBag-Reader): ROSbag 비디오 파일 뷰어 구현물 

- [mjshiggins](https://github.com/mjshiggins/ros-examples): height-map

- <del>[RViz for DiDi challenge](https://github.com/jokla/didi_challenge_ros)</del>: jokla

- [Youtube](https://www.youtube.com/watch?v=RVFpwMAeBOA): a small tutorial how to visualize the given bag files in ROS., [[GitHub]](https://github.com/didi-challenge-team-khodro/data_analysis)


### 4.2 Docker

- [Karthikksamy-Teamsf4win](https://hub.docker.com/r/karthikksamy/teamsf4win/0): 

### 4.3 변환 툴 

- [KITT-2-ROSbag](https://github.com/tomas789/kitti2bag)

- [ROSbag-2-KITTI](https://github.com/udacity/didi-competition/tree/master/tracklets)

---

(kitti_download)[https://gist.github.com/adioshun/0554effff45e4f16fe4db7eb1c4712cc)