# [Didi-Udacity Self Driving Car Challenge 2017](https://github.com/hb0702/Didi_Challenge_2017_ROS)

![](https://github.com/hb0702/Didi_Challenge_2017_ROS/raw/master/ref_script/ped.gif)




## Pedestrian detection
Cluster 3D Points using region growing clustering of depth map grid cells
Filter out clusters with width and depth
Select most probable cluster
Track selected cluster

## Car detection
Cluster 3D Points using region growing clustering of depth map grid cells
Filter out clusters with width and depth
Project clustered points on 360 degree panoramic view
Predict boxes with pre-trained deep neural network
Cluster boxes and select most probable box
Track selected box