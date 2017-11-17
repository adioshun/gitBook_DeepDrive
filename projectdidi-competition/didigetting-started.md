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
