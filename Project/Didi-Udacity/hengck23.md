# 

## Part 1 

https://medium.com/@hengcherkeng/part-1-didi-udacity-challenge-2017-car-and-pedestrian-detection-using-lidar-and-rgb-fff616fc63e8

### 1. Pre-processing

- 3D 사각형 영역을 Top-view형태의 8개 채널 별로 나눔 `I first covert a rectangular region of lidar 3d point cloud into a multi-channel(8 channels) top view image`
    - kitti dataset(2011_09_26_drive_0005_sync) 사용 


### 2. Training Net

- I learn to use tf.py_func() to create customized tf layer. For example, in the generation of +ve (red) and -ve (gray) anchor boxes training samples for the 3d proposal net:

## Part 2 

- 추가 작업 
    - add a “dummy” rgb image feature extraction net.
    
    - generate 3d proposals from top view and then project to rgb proposals again
    
    - add several customised op to tensorflow.
    
- SqueezeDet 적용 
    - In order to speedup development, I am now using an existing[1-SqueezeDet] rgb kitti car car detector to replace my “dummy” rgb feature extraction net.
    
## Part 3 

