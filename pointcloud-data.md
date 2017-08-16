# The Point Cloud Data


## 1. 개요 

> [Ronny Restrepo](http://ronny.rest/tutorials/module/pointclouds_01/point_cloud_data/)

|The Point Cloud Data|이미지 데이터와 비교 |
|-|-|
|![](http://i.imgur.com/Bc13san.png)|![](http://i.imgur.com/smzFU5N.png)|



- 포인트 클라우드 데이터는 보통 `N x 3` Numpy 배열로 표현 된다. 
    - 각 N 줄은 하나의 점과 맵핑이 되며 
    - 3(x,y,z) 정보를 가지고 있다. 

- Lidar 센서에서 수집한 정보의 경우는 `reflectance`라는 정보가 추가되어 `N x 4` Numpy 배열이 된다. 
    - reflectance : 반사 시간 정보로 보면 된다. 


이미지 데이터
- 항상 양수 이다. 
- 기준점은 왼쪽 위부터 이다. 
- 좌표값은 정수(integer)이다. 

포인트 클라우드 데이터 
- 양수/음수 이다. 
- 좌표값은 real numbered이다. 
- The positive x axis represents forward.
- The positive y axis represents left.
- The positive z axis represents up.

## 2. Creating Birdseye View of Point Cloud Data

In order to create a birds eye view image, the relevant axes from the point cloud data will be the x and y axes.

![](http://i.imgur.com/cHsb48Y.png)

조심해야 할점 
- the x, and y axes mean the opposite thing.
- The x, and y axes point in the opposite direction.
- You have to shift the values across so that (0,0) is the smallest possible value in the image.


|- [Creating Birdseye View of Point Cloud Data 코드 및 설명(python)](https://gist.github.com/adioshun/12873804f472080c612e506310674797)|
|-|

> [참고] cpp로 작성한 코드 : [mjshiggins's github](https://github.com/mjshiggins/ros-examples)



## 3. Creating 360 degree Panoramic Views

- Project the `points in 3D` space into `cylindrical surface`

- LiDAR센서의 특징에 따라 설정값이 달라 진다. 
    - `h_res`: Horizontal resolution
    - `v_res`: vertical resolution

```python
# KTTI dataset = Velodyne HDL 64E 
## A vertical field of view of 26.9 degrees, at a resolution of 0.4 degree intervals. The vertical field of view is broken up into +2 degrees above the sensor, and -24.9 degrees below the sensor.
## A horizontal field of view of 360 degrees, at a resolution of 0.08 - 0.35 (depending on the rotation rate)
## Rotation rate can be selected to be betwen 5-20Hz.
## http://velodynelidar.com/docs/datasheet/63-9194%20Rev-E_HDL-64E_S3_Spec%20Sheet_Web.pdf

# Resolution and Field of View of LIDAR sensor
h_res = 0.35         # horizontal resolution, assuming rate of 20Hz is used 
v_res = 0.4          # vertical res
v_fov = (-24.9, 2.0) # Field of view (-ve, +ve) along vertical axis
v_fov_total = -v_fov[0] + v_fov[1] 
```

|- [Creating 360 degree Panoramic Views코드 및 설명(matplotlib)](http://ronny.rest/blog/post_2017_03_25_lidar_to_2d/)<br>- [Creating 360 degree Panoramic Views코드 및 설명(numpy)](http://ronny.rest/blog/post_2017_04_03_point_cloud_panorama/)|
|-|

## 4. 3D Visualization

### 4.1 Mayavi 이용 

- [Mayavi 홈페이지](http://docs.enthought.com/mayavi/mayavi/)

#### A. 설치 

- 설치 스크립트 : [Install Mayavi on Ubuntu](https://gist.github.com/ronrest/d778ee5d49c026ccee1dbec6bd5b3988)

#### B. 실행 코드 

```python
# ==============================================================================
#                                                                     VIZ_MAYAVI
# Input : kitti Raw Dataset 
# ==============================================================================
def viz_mayavi(points, vals="distance"):
    x = points[:, 0]  # x position of point
    y = points[:, 1]  # y position of point
    z = points[:, 2]  # z position of point
    # r = lidar[:, 3]  # reflectance value of point
    d = np.sqrt(x ** 2 + y ** 2)  # Map Distance from sensor

    # Plot using mayavi -Much faster and smoother than matplotlib
    import mayavi.mlab

    if vals == "height":
        col = z
    else:
        col = d

    fig = mayavi.mlab.figure(bgcolor=(0, 0, 0), size=(640, 360))
    mayavi.mlab.points3d(x, y, z,
                         col,          # Values used for Color
                         mode="point",
                         colormap='spectral', # 'bone', 'copper', 'gnuplot'
                         # color=(0, 1, 0),   # Used a fixed (r,g,b) instead
                         figure=fig,
                         )
    mayavi.mlab.show()
```

