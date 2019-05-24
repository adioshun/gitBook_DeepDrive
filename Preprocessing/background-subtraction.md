[CHANGE DETECTION OF MOBILE LIDAR DATA USING CLOUD COMPUTING](https://pdfs.semanticscholar.org/8aa4/f28b325a73bb3168cef1d40851caf0b74948.pdf): 2016


## occupancy grid map기반 

**occupancy grid map** 을 이용하면 움직이는 물체사이에서 고정된 물체를 찾을수 있다. `The occupancy grid map allows to identify static objects from moving objects. `
- It has been intensively used for detecting the surroundings of a vehicle in order to monitor and predict the movement of other road users.


## octree 기반 

> [Quadtrees and Octrees](https://www.i-programmer.info/programming/theory/1679-quadtrees-and-octrees.html?start=1)

[background subtraction of pointcloud](https://answers.ros.org/question/36272/background-subtraction-of-pointcloud/): ROS QnA



---



## 2012-Lidar-Based-MOT-system-with-Dyanamic-modeling

2.2.2.1 Background subtraction

Background subtraction techniques have been widely used for detecting moving objects from static cameras [23]. 

```
[23] M. Piccardi, “Background subtraction techniques: A review,” IEEE International Conference on Systems, Man and Cybernetics, 2004, pp. 3099–3104
```

One approach, presented by Fod et,al., considers the different features provided by LIDAR within a background model based on range information [24]. 

```
[24] A. Fod, A. Howard, and M. J. Mataric, “Laser-based people tracking,” IEEE International Conference on Robotics and Automation, Washington DC, May, 2002, pp. 3024–3029
```

In order to simultaneously detect moving targets and maintain the position of stationary objects, an occupancy grid map is employed to detect moving objects [25]. 

```
[24] A. Fod, A. Howard, and M. J. Mataric, “Laser-based people tracking,” IEEE International Conference on Robotics and Automation, Washington DC, May, 2002, pp. 3024–3029
```

The grid-based map technique has been widely used in Simultaneous Localization and Mapping (SLAM) for representing complex outdoor environments (Figure 2.1) [7, 35, 59]. 


```
[7] C. C. Wang, “Simultaneous localization, mapping and moving object tracking,” PhD thesis, The Robotics Institute, Carnegie Mellon University, Pittsburgh, PA, Apr. 2004
[35] T. D. Vu, O. Aycard, and N. Appenrodt, “Online localization and mapping with moving object tracking in dynamic outdoor environments,” IEEE Intelligent Vehicles Symposium, Istanbul, Turkey, June 2007
[59] T. D. Vu and O. Aycard, “Laser-based detection and tracking moving objects using data-driven markov chain monte carlo,” IEEE International Conference on Robotics and Automation, Kobe, Japan, May 2009

```


Due to the few features extracted from LIDAR data, by building motion-map and stationary-map separately, Wang showed this approach is more robust than a feature-based approach (Figure 2.1) [7].


---

## 2010-Tracking People with a 360 degreelidar

- 본 논문에서는 separate occupancy grid를 static objects로 populating함으로써 배경을 제거 하였다. `We perform 3D background subtraction by populating a separate occupancy grid with static objects. `

- The cells of the occupancy grid form our background mask.

- 각 셀은 최근 occupancy를 기록하고 있다. `Each 3D cell also includes a history buffer that records its recent occupancy, represented as a string of bits (eight bits in our implementation). `

- 절차
  1. Initially all cells are marked as empty and all bits are set to zero.
  2. Periodically we sample a frame of lidar data, and for each voxel in the frame we calculate which cell of the background mask it occupies.
  3. For each occupied cell, we set the highest order bit.
  4. Before sampling another frame, the background mask is aged, so that the lowest order bits of each cell’s mask are shifted one place.  


- To determine which cells represent the static background, each cell in the scene’s background mask is examined.

- A cell is marked as static background if a majority of its bits are set.

- A persistently empty space will have all bits in its cell mask unset.

- After sampling a minimum number of periodic frames, the learned background mask is applied continuously as a filter for future frames.

- A point in subsequent frames is discarded if it occupies a background cell.

> 이 방법을 통해 90%까지 입력 데이터를 줄일수 있다. `In practice, this approach reduces the lidar input data by as much as 90% (Figure 4). `

- 이 방식은 부가적인 효과도 있다. `This approach yields other benefits as well. `
   - First, it greatly simplifies segmentation, since most of points that are not marked as background are usually objects of interest.
    - Segmenting people standing near walls is much simpler when the walls are removed.
   - Second, transient artifacts such as lidar shadows are automatically removed without further processing.




--- 
## 2014-Confidence-Based-PedestrianTracking

In our approach, 
1. we first insert the 3D data into a three-dimensional grid with a resolution of $$0.1 × 0.1 × 0.1m^3$$ per cell. 
2. Afterwards, the cells are sorted according to their height(computed from the highest and the lowest point in each cell) from high to low. 
3. Each of those candidate cell is not only classified wrt. the contained points, but also wrt. the neighboring cells. 
4. A sliding window with a height threshold is used to calculate the absolute difference between the highest and the lowest point among all point of the current cell and in addition all points of neighboring cell. 
5. Based on the resulting values, a cell is classified as Empty, Ground or Obstacle

