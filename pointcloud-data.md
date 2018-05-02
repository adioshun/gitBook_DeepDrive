# The Point Cloud Data

- [The PCD (Point Cloud Data) file format](http://pointclouds.org/documentation/tutorials/pcd_file_format.php)

```
# .PCD v.7 - Point Cloud Data file format
VERSION .7
FIELDS x y z rgb
SIZE 4 4 4 4
TYPE F F F F
COUNT 1 1 1 1
WIDTH 213
HEIGHT 1
VIEWPOINT 0 0 0 1 0 0 0
POINTS 213
DATA ascii
0.93773 0.33763 0 4.2108e+06
0.90805 0.35641 0 4.2108e+06
0.81915 0.32 0 4.2108e+06
0.97192 0.278 0 4.2108e+06
0.944 0.29474 0 4.2108e+06
0.98111 0.24247 0 4.2108e+06
0.93655 0.26143 0 4.2108e+06
0.91631 0.27442 0 4.2108e+06
0.81921 0.29315 0 4.2108e+06
0.90701 0.24109 0 4.2108e+06
0.83239 0.23398 0 4.2108e+06
0.99185 0.2116 0 4.2108e+06
0.89264 0.21174 0 4.2108e+06
```

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

> 참고 : Height의 Level별 값 추출 (Height as Channels), [Creating Height Slices of Lidar Data](http://ronny.rest/blog/post_2017_03_27_lidar_height_slices/)

In order to create a birds eye view image, the relevant axes from the point cloud data will be the x and y axes.

![](http://i.imgur.com/cHsb48Y.png)

조심해야 할점 
- the x, and y axes mean the opposite thing.
- The x, and y axes point in the opposite direction.
- You have to shift the values across so that (0,0) is the smallest possible value in the image.


|- [Creating Birdseye View of Point Cloud Data 코드 및 설명(python)](http://ronny.rest/blog/post_2017_03_26_lidar_birds_eye/), [gist](https://gist.github.com/adioshun/12873804f472080c612e506310674797)|
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


- 패키지 설치 
##### python2
- conda install -c anaconda mayavi

###### python3
- conda install -c clinicalgraphics vtk=7.1.0; pip install mayavi

> ImportError: Could not import backend for traits 
> - conda install -c conda-forge pyside=1.2.4 
> - {OR} conda install pyqt=4




```
sudo apt-get install vtk6 python-vtk
python -c "import vtk"
# cp -r /usr/lib/python2.7/dist-packages/vtk /opt/anaconda3/envs/python2_gpu/lib/python2.7/site-packages/
pip install mayavi
import mayavi.mlab as mlab
```




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

### 4.2 Matplotlib이용

#### A. 설치 

- 설치가 쉽지만, 느리고 3D를 충분히 표현하지 못한다. 

#### B. 실행 코드 

In order to prevent matplotlib from crashing your computer, it is recomended to only view a subset of the point cloud data. 

For instance, if you are visualizing LIDAR data, then you may only want to view one in every 25-100 points. Below is some sample code to get you started.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

skip = 100   # Skip every n points

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
point_range = range(0, points.shape[0], skip) # skip points to prevent crash
ax.scatter(points[point_range, 0],   # x
           points[point_range, 1],   # y
           points[point_range, 2],   # z
           c=points[point_range, 2], # height data for color
           cmap='spectral',
           marker="x")
ax.axis('scaled')  # {equal, scaled}
plt.show()
```

### 4.3 RViz이용 

> 참고 : [Roslaunch to visualize a rosbag file from Udacity (DiDi Challenge)](https://github.com/jokla/didi_challenge_ros)


## 5. ROS bag 파일 살펴 보기 


# Visualization 

## 1. PCD

[샘플 PCD Download](https://raw.github.com/PointCloudLibrary/data/master/tutorials/table_scene_lms400.pcd), [PCD File Format](http://www.jeffdelmerico.com/wp-content/uploads/2014/03/pcl_tutorial.pdf): slide 12









### 1.1 PCL viewer

`/usr/bin/pcl_viewer/{  }.pcd`


### 1.2 Jupyter

[point cloud visualization with jupyter/pcl-python/and potree](https://www.youtube.com/watch?v=s2IvpYvB7Ew)



### 1.4 Paraview 

[ParaView/PCL Plugin](https://www.paraview.org/Wiki/ParaView/PCL_Plugin)
- apt-get install paraview


### 1.5 3D Viewer

> [How to visualize a range image](http://pointclouds.org/documentation/tutorials/range_image_visualization.php#range-image-visualization)


Code Download : [range_image_visualization.cpp](https://gist.githubusercontent.com/adioshun/1ae4197af17f79f01f1ec3ec7c8f4bcb/raw/6ec7e03db63f0477688a66ae580c14795dec0803/range_image_visualization.cpp), [CMakeLists.txt](https://gist.githubusercontent.com/adioshun/1ae4197af17f79f01f1ec3ec7c8f4bcb/raw/6ec7e03db63f0477688a66ae580c14795dec0803/CMakeLists.txt)



```
mkdir range_image_visualization; cd range_image_visualization
vi range_image_visualization.cpp
vi CMakeLists.txt
mkdir build;cd build
cmake ..
make

# Test
wget https://raw.github.com/PointCloudLibrary/data/master/tutorials/table_scene_lms400.pcd
./range_image_visualization table_scene_lms400.pcd 

```

> Simple Version : [Cloud Viewer](http://pointclouds.org/documentation/tutorials/cloud_viewer.php#cloud-viewer)



### 1.6 Plot
> https://github.com/hunjung-lim/awesome-vehicle-datasets/blob/master/vehicle/kitti/KITTI%2BDataset%2BExploration.ipynb

```
from mpl_toolkits.mplot3d import Axes3D

f2 = plt.figure()
ax2 = f2.add_subplot(111, projection='3d')
# Plot every 100th point so things don't get too bogged down
velo_range = range(0, third_velo.shape[0], 100)
ax2.scatter(third_velo[velo_range, 0],
            third_velo[velo_range, 1],
            third_velo[velo_range, 2],
            c=third_velo[velo_range, 3],
            cmap='gray')
ax2.set_title('Third Velodyne scan (subsampled)')

plt.show()
```




---

## 2. 활용

예제

```python
import pcl
import numpy as np
p = pcl.PointCloud(np.array([[1, 2, 3], [3, 4, 5]], dtype=np.float32))
seg = p.make_segmenter()
seg.set_model_type(pcl.SACMODEL_PLANE)
seg.set_method_type(pcl.SAC_RANSAC)
indices, model = seg.segment()
```










