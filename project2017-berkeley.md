# 3D Object Detection based on Lidar and Camera Fusion

- [홈페이지](http://msc.berkeley.edu/research/lidar-camera-fusion.html): 버클리 DeepDrive 센터 소속
- PM : [Masayoshi Tomizuka](http://www.me.berkeley.edu/people/faculty/masayoshi-tomizuka)
- Researcher : Kiwoo Shin, Zining Wang, Wei Zhan



## 1. ABOUT THE PROJECT

### 1.1 센서들의 장/단점 & 퓨전 필요성 

- 2D센서 장/단점 : 2D images from cameras provide rich texture descriptions of the surrounding, while depth is hard to obtain. 

- 3D센서 장/단점: On the other hand, 3D point cloud from Lidar can provide accurate depth and reflection intensity, but the solution is comparatively low. 

- 퓨전 필요성 : Therefore, 2D images and 3D point cloud are potentially supplementary to each other to accomplish accurate and robust perception, which is a prerequisite for autonomous driving.

### 1.2 퓨전시 고려사항 

Currently, there are several technical challenges in Lidar-camera fusion via convolutional neural network (CNN). 

- 라이다는 정해진 입력형태가 없음 `Unlike RGB images for cameras, there is no standard input form for CNN from Lidars. `

- 360도 데이터 Vs. 180도 전방 데이터 차이 `Processing is required before fusing the 3D omnidirectional point cloud with the 2D front view images. `

- 2D 이미지용 RPN은 3D에는 맞지 않음 `The current region proposal networks (RPN), adapted from typical image processing structures, generate proposals separately and are not suitable for learning based on Lidar-camera fusion. `

- Lidar-camera fusion enables accurate position and orientation estimation but the level of fusion in the network matters. 

Few works have been done on position estimation, and all existing works focus on vehicles.

### 1.3 본 프로젝트 설명 

In this project, our goal is to improve 3D object detection performance in driving environment by fusing 3D point cloud with 2D images via CNN. 

1. RPN적용 `The RPN is applied to multiple layers of the whole network so that obstacles with different sizes in the front view are considered. `

2. KITTI데이터를 전처리 하여 영향력 분석 `We will be preprocessing Lidar and camera data from the KITTI benchmark and comparing the influence of Lidar data processing schemes by examining the contribution of Lidar information in detection. `

3. 다른 **stereo-vision-based** & **fusion-based networks**와 후보영역 정확도에 대한 성능 비교 `We will compare the region proposal accuracy in the form of 2D or 3D bounding boxes with other stereo-vision-based and fusion-based networks. `

4. 실 주행차에 적용 `Finally, we will collect data from real world traffic, pre-process and label the collected data according to the defined input and output of the CNN.`