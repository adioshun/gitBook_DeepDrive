![](https://i.imgur.com/OPatJnW.png)
# List 

[Awesome Autonomous Vehicles](https://github.com/takeitallsource/awesome-autonomous-vehicles)

[Bookmark of 3D CNN Rearch](https://github.com/NotAndOr/bookmarks/blob/master/20170203.md)

# Project

[Project: Development of AEB System for Pedestrian Protection (4th year)](https://github.com/nlkim0817/ProjAEB_4thYear)

# Post/Article
- [3D Convolutional Neural Networks — A Reading List](http://davidstutz.de/3d-convolutional-neural-networks-a-reading-list/)

# Material 

- [Synthesize for Learning:Joint analysis of 2D images and 3D shapes](http://ai.stanford.edu/~haosu/slides/3dv.pptx)

- [3D Deep Learning on Geometric Forms](http://ai.stanford.edu/~haosu/slides/NIPS16_3DDL.pptx)

- [Scene Understanding with 3D Deep Networks](https://www.cs.princeton.edu/~funk/nips16.pdf): 

- [Learning 3D representations,disparity estimation, and structure from motion](http://3ddl.cs.princeton.edu/2016/slides/brox.pdf): FlowNet, DispNet, DeMoN

- [Scene Understanding with 3D Deep Networks](http://3ddl.cs.princeton.edu/2016/slides/funkhouser.pdf)

## 참고 논문

- Unsupervised Depth Estimation. [[Garg, ECCV '16]](http://arxiv.org/abs/1603.04992)

- LIDAR point upsampling. [[Schneider, Arxiv '16]](https://arxiv.org/abs/1608.00753)

- Unified multi-scale CNN. (KITTI: 8th car, 1st ped) [[Cai, ECCV '16]](http://arxiv.org/abs/1607.07155) [[Home]](https://sites.google.com/site/zhaoweicai1989/) [[Code]](https://github.com/zhaoweicai/mscnn) [[Video]](https://www.youtube.com/watch?v=NQFCURgv_cY&feature=youtu.be)

- Subcategory-aware CNN. (KITTI: 7th car, 3rd ped)) [[Xiang, Arxiv '16]](http://arxiv.org/abs/1604.04693) [[Home]](https://yuxng.github.io/)

- Exploit all layers. (KITTI: 10th car, 5th ped) [[Yang, CVPR '16]](http://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Yang_Exploit_All_the_CVPR_2016_paper.pdf) [[Home]](http://www.umiacs.umd.edu/~fyang/)

- 2D/3D Sensor Exploitation and Fusion for Enhanced Object Detection (Similar to ours) [[Xu, CVPRW '14]](http://www.cv-foundation.org/openaccess/content_cvpr_workshops_2014/W19/papers/Xu_2D3D_Sensor_Exploitation_2014_CVPR_paper.pdf)
 

- [A Comparative Analysis and Study of Multiview CNN Models for Joint Object
Categorization and Pose Estimation](http://proceedings.mlr.press/v48/elhoseiny16.pdf): [추가자료](http://proceedings.mlr.press/v48/elhoseiny16-supp.pdf)

- [3D Bounding Box Estimation Using Deep Learning and Geometry](https://arxiv.org/abs/1612.00496): (Submitted on 1 Dec 2016 (v1), last revised 10 Apr 2017 (this version, v2))
+ 3D Object Proposals for Accurate Object Class Detection [[Chen, NIPS 15]](http://papers.nips.cc/paper/5644-3d-object-proposals-for-accurate-object-class-detection) [[Project]](http://www.cs.toronto.edu/objprop3d/) [[Code]](http://www.cs.toronto.edu/objprop3d/downloads.php)
+ Multiview random forest of local experts combining rgb and lidar data for pedestrian detection [[Gonzalez, IV '15]](https://scholar.google.de/scholar?q=Multiview%20Random%20Forest%20of%20Local%20Experts%20Combining%20RGB%20and%20LIDAR%20data%20%20for%20Pedestrian%20Detection)
+ Voting for Voting in Online Point Cloud Object Detection [[Wang, RSS '15]](http://www.roboticsproceedings.org/rss11/p35.pdf) [[Project]](http://mrg.robots.ox.ac.uk/vote3d/)
+ Pedestrian Detection Combining RGB and Dense LIDAR Data [[Premebida, IROS '14]](https://people.eecs.berkeley.edu/~carreira/papers/iros2014.pdf) [[Project]](http://home.isr.uc.pt/~cpremebida/IROS14/LaserVisionFusion.html) [[Code]](http://home.isr.uc.pt/~cpremebida/IROS14/Codes_CP_IROS2014.zip)
+ Vehicle Detection from 3D Lidar Using Fully Convolutional Network [[Li, RSS '16]](http://www.roboticsproceedings.org/rss12/p42.pdf)
+ Visual Object Recognition with 3D-Aware Features in KITTI Urban Scenes [[Yebes, Sensors '15]](http://www.mdpi.com/1424-8220/15/4/9228/htm)


### 1. 3D DL 

[Instant Object Detection in Lidar Point Clouds](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7927715&tag=1)

[Fast LIDAR-based Road Detection Using Fully Convolutional Neural Networks](https://arxiv.org/abs/1703.03613): 2017.03

### 2. Fusion 

[Fusing LIDAR and images for pedestrian detection using convolutional neural networks](http://ieeexplore.ieee.org/abstract/document/7487370/): 2016.04


[RegNet: Multimodal sensor registration using deep neural networks](http://ieeexplore.ieee.org/document/7995968/#full-text-section): 2017.06, LiDAR + monocular camera, 

[Multi-Modal Obstacle Detection in Unstructured Environments with Conditional Random Fields](https://arxiv.org/abs/1706.02908): 2017.06
- Unstructured Environments: 농장 
- lidar + camera sensing using a conditional random field

### 3. RNN/RL

[3DCNN-DQN-RNN: A Deep Reinforcement Learning Framework for Semantic Parsing of Large-scale 3D Point Clouds](https://arxiv.org/abs/1707.06783): 2017.07, 3D CNN + RNN + DQN

# Datasets
- Princeton Shape Benchmark (PSB) [Shilane et al. 2004] 

- Engineering Shape Benchmark (ESB) [Jayanti et al. 2006]

- PSB [Shilane et al. 2004]

- National Taiwan University (NTU) dataset [Chen et al. 2003] 

- SHREC’09 [Godil et al. 2009]

- [Semantic3D.net: A new Large-scale Point Cloud Classification Benchmark](https://arxiv.org/abs/1704.03847): 2017.04, Datasets, 도시, four billion~

# Workshop

[3D DeepLearning at NIPS2016](http://3ddl.cs.princeton.edu/2016/): 발표 자료 목록/자료 포

[Geometry Meets Deep Learning ECCV 2016 Workshop](https://sites.google.com/site/deepgeometry/)

---
![](https://i.imgur.com/EZp7gs1.png)

- [ModelNet](http://modelnet.cs.princeton.edu/): 프린스톤대, 127,915 CAD Models, 662 Object Categories, 10 Categories with Annotated Orientation


---
[3D Vehicle Detection](https://experiencor.github.io/sdc_3d.html)

1. Detect 2D BBoxes of other vehicles visible on CAMERA frame. This can be achieved by YOLOv2 or SqueezeDet. It turns out that SqueezeDet works better for this job and is selected.

2. Determine the dimension and the orientation of detected vehicles. As demonstrated in [https://arxiv.org/abs/1612.00496], dimension and orientation of other vehicles can be regressed from the image patch of corresponding 2D BBoxes.

3. Determine the location in 3D of detected vehicles. This can be achived by localizing the point cloud region whose projection stays within the detected 2D BBoxes.


---

https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=3D_CNN_Trend.xml#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D0B6Ry8c3OoOuqVUh1b2tyc2lhMEE%26export%3Ddownload



---

+ KITTI [[Link]](http://www.cvlibs.net/datasets/kitti/)
	+ Stereo, Lidar, GPS		
	+ Classes: Car, Pedestrian, Cyclist
	+ GT: Bounding box
+ Cityscapes [[Link]](https://www.cityscapes-dataset.com/)
	+ Stereo, Timestamp		
	+ Groups: flat, human, vehicle, construction, object, nature, sky, void
	+ GT: Dense pixel-level annotations 
+ Virtual KITTI [[Link]](http://www.xrce.xerox.com/Research-Development/Computer-Vision/Proxy-Virtual-Worlds)
	+ Mono (forward / 15-deg-right, 15-deg-left)
	+ Classes: Car, Pedestrian, Cyclist
	+ GT: Bounding box, Instance-level pixel annotations, Optical-flow, Depth	
	+ Weather conditions: morning, sunset, overcast, fog, rain
+ Synthia [[Link]](http://synthia-dataset.net/)
	+ 8 RGB (form binocular 360 deg), 8 depth sensors
	+ Classes: misc, sky, building, road, sidewalk, fence, vegetation, pole, car, sign, pedestrian, cyclist, lanemarking
	+ GT: Instance-level pixel annotations
	+ Seasons: winter, fall, spring, summer
	+ Lightings: dynamic light, shadows, day-time, rain, night-time





