# Didi Data Visualization 

![](https://github.com/jokla/didi_challenge_ros/raw/master/visualization.gif)

> Udacity에서 배포 하는 [데이터셋](http://academictorrents.com/details/76352487923a31d47a6029ddebf40d9265e770b5)에서만 제대로 동작 하며 KITTI파일을 ROS bag으로 변경시에는 에러 

## 1. 설치 

```
cd ~/catkin_ws/src   
git clone https://github.com/jokla/didi_challenge_ros.git
cd ~/catkin_ws
catkin_make

# Now source the setup.bash;   
source ~/catkin_ws/devel/setup.bash

# Check if ROS is able to find the package:  
roscd didi_challenge_ros
```

## 2. 실행 

```
 $ roslaunch didi_challenge_ros display_rosbag_rviz.launch rosbag_file:={rosbag.bag}
 ```
 
#### launch file 설명
`display_rosbag_rviz.launch` 파일의 역할 

```
<launch>

<!-- Usage: roslaunch didi_challenge_ros display_rosbag_rviz.launch rosbag_file:=/path/approach_1.bag  -->

# rosbag 반복 재생
<arg name="rosbag_file" default="my_file_1" />

<node pkg="rosbag" type="play" name="player" output="screen" args="-l $(arg rosbag_file) "/> 

# display_rviz.launch실행 
<include file="$(find didi_challenge_ros)/launch/display_rviz.launch"/>

</launch>

```

`display_rviz.launch` 파일의 역할 
  
``` 
<launch>

# Publishing the transformation between the link 'base_link' and 'velodyne'    
<node pkg="tf2_ros" type="static_transform_publisher" name="link1_broadcaster" args="1.9 0 1.6 0 0 0 1 base_link velodyne" />

# `display.rviz`설정 파일 이용하여 `RViz`실행 
<node name="rviz" pkg="rviz" type="rviz" args="-d $(find didi_challenge_ros)/launch/display.rviz" />

</launch>

```

