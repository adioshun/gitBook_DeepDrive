|논문명|SqueezeSeg: Convolutional Neural Nets with Recurrent CRF for Real-Time Road-Object Segmentation from 3D LiDAR Point Cloud|
|-|-|
|저자(소속)|Bichen Wu (Berkeley)|
|학회/년도| arXiv 2017, [논문](https://arxiv.org/abs/1710.07368v1)|
|키워드| |
|참고|[Youtube](https://www.youtube.com/watch?v=Xyn5Zd3lm6s)|
|코드||


# SqueezeSeg

- 입력 : 3D LiDAR -> In this paper, we address semantic segmentation of road-objects from 3D LiDAR point clouds. 

In particular, wewish to detect and categorize instances of interest, such as cars,pedestrians and cyclists. 

We formulate this problem as a pointwiseclassification problem, and propose an end-to-end pipelinecalled SqueezeSeg based on convolutional neural networks(CNN): the CNN takes a transformed LiDAR point cloud asinput and directly outputs a point-wise label map, which isthen refined by a conditional random field (CRF) implementedas a recurrent layer. 

Instance-level labels are then obtained byconventional clustering algorithms. 

Our CNN model is trainedon LiDAR point clouds from the KITTI [1] dataset, and ourpoint-wise segmentation labels are derived from 3D boundingboxes from KITTI. 

To obtain extra training data, we built aLiDAR simulator into Grand Theft Auto V (GTA-V), a popularvideo game, to synthesize large amounts of realistic trainingdata. 

Our experiments show that SqueezeSeg achieves highaccuracy with astonishingly fast and stable runtime (8.7 ±0.5 ms per frame), highly desirable for autonomous drivingapplications. 

Furthermore, additionally training on synthesizeddata boosts validation accuracy on real-world data. 

Our sourcecode and synthesized data will be open-sourced.
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjEzNzc2MTE5XX0=
-->