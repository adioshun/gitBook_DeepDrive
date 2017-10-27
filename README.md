# Deep Drive

## 1. List

* [Awesome : Autonomous Vehicles](https://github.com/takeitallsource/awesome-autonomous-vehicles)

- [Learning where to attend like a human driver](http://ieeexplore.ieee.org/document/7995833/): Intelligent Vehicles Symposium (IV), 2017 IEEE

### 1.1 2D CNN

### 1.2 Point Cloud

* [awesome-point-cloud-processing](https://github.com/mmolero/awesome-point-cloud-processing)
* [Paper Reading List : 3D Convolutional Neural Networks](http://davidstutz.de/3d-convolutional-neural-networks-a-reading-list/)

## 2. Paper

* \[Computer Vision for Autonomous Vehicles: Problems, Datasets and State-of-the-Art\]
* [Deep Semantic Segmentation for Automated Driving: Taxonomy, Roadmap and Challenges](https://arxiv.org/abs/1707.02432v2)

### 2.1 2D DNN2

* [MultiNet: Real-time Joint Semantic Reasoning for Autonomous Driving](https://arxiv.org/abs/1612.07695v1): classifi-
  cation, detection and semantic segmentation Task수행시 값을 공유 하여 `속도 향상`에 초점, 2016 
* [Deep convolutional neural networks for pedestrian detection](https://arxiv.org/abs/1510.03608v5): 보행자 탐지, 2016

### 2.2 Point Cloud

- [Object Classification using 3D Convolutional Neural Networks](http://publications.lib.chalmers.se/records/fulltext/249371/249371.pdf): 2016

* [OctNet: Learning Deep 3D Representations at High Resolutions](https://arxiv.org/abs/1611.05009v4): 2016~2017
* [Deep Semantic Classification for 3D LiDAR Data](https://arxiv.org/abs/1706.08355v1): 물체를 고정된, 움직이는, 움직일수 있는 것으로 3분류 
* Unsupervised Depth Estimation. [\[Garg, ECCV '16\]](http://arxiv.org/abs/1603.04992)
* Unified multi-scale CNN. \(KITTI: 8th car, 1st ped\) [\[Cai, ECCV '16\]](http://arxiv.org/abs/1607.07155) [\[Home\]](https://sites.google.com/site/zhaoweicai1989/) [\[Code\]](https://github.com/zhaoweicai/mscnn) [\[Video\]](https://www.youtube.com/watch?v=NQFCURgv_cY&feature=youtu.be)
* Subcategory-aware CNN. \(KITTI: 7th car, 3rd ped\)\) [\[Xiang, Arxiv '16\]](http://arxiv.org/abs/1604.04693) [\[Home\]](https://yuxng.github.io/)
* Exploit all layers. \(KITTI: 10th car, 5th ped\) [\[Yang, CVPR '16\]](http://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Yang_Exploit_All_the_CVPR_2016_paper.pdf) [\[Home\]](http://www.umiacs.umd.edu/~fyang/)
* 2D/3D Sensor Exploitation and Fusion for Enhanced Object Detection \(Similar to ours\) [\[Xu, CVPRW '14\]](http://www.cv-foundation.org/openaccess/content_cvpr_workshops_2014/W19/papers/Xu_2D3D_Sensor_Exploitation_2014_CVPR_paper.pdf)
* [3D Bounding Box Estimation Using Deep Learning and Geometry](https://arxiv.org/abs/1612.00496): \(Submitted on 1 Dec 2016 \(v1\), last revised 10 Apr 2017 \(this version, v2\)\)
* 3D Object Proposals for Accurate Object Class Detection [\[Chen, NIPS 15\]](http://papers.nips.cc/paper/5644-3d-object-proposals-for-accurate-object-class-detection) [\[Project\]](http://www.cs.toronto.edu/objprop3d/) [\[Code\]](http://www.cs.toronto.edu/objprop3d/downloads.php)
* Visual Object Recognition with 3D-Aware Features in KITTI Urban Scenes [\[Yebes, Sensors '15\]](http://www.mdpi.com/1424-8220/15/4/9228/htm)
* [Generalized Convolutional Neural Networks for Point Cloud Data](https://arxiv.org/abs/1707.06719v1): 2017
* [~~Instant Object Detection in Lidar Point Clouds~~](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7927715&tag=1)
* [Fast LIDAR-based Road Detection Using Fully Convolutional Neural Networks](https://arxiv.org/abs/1703.03613): 2017.03

#### A. Missing points

* [CNN-Based Object Segmentation in Urban LIDAR with Missing Points](http://ieeexplore.ieee.org/document/7785116/): 2016
* LIDAR point upsampling. [\[Schneider, Arxiv '16\]](https://arxiv.org/abs/1608.00753)
* Voting for Voting in Online Point Cloud Object Detection [\[Wang, RSS '15\]](http://www.roboticsproceedings.org/rss11/p35.pdf) [\[Project\]](http://mrg.robots.ox.ac.uk/vote3d/)

#### B. 3D point cloud to 2D

* ~~Vehicle Detection from 3D Lidar Using Fully Convolutional Network ~~[~~\[Li, RSS '16\]~~](http://www.roboticsproceedings.org/rss12/p42.pdf)

#### C. Multiview

* \[A Comparative Analysis and Study of Multiview CNN Models for Joint Object
  Categorization and Pose Estimation\]\([http://proceedings.mlr.press/v48/elhoseiny16.pdf](http://proceedings.mlr.press/v48/elhoseiny16.pdf)\): [추가자료](http://proceedings.mlr.press/v48/elhoseiny16-supp.pdf), 3D 데이터 관련 내용인지 재 확인 필요 

### 2.3 RGB-D

### 2.4 Fusion

* [A Survey of ADAS Technologies for the Future Perspective of Sensor Fusion](https://link.springer.com/chapter/10.1007/978-3-319-45246-3_13)
* [VANETs Meet Autonomous Vehicles: A Multimodal 3D Environment Learning Approach](https://arxiv.org/abs/1705.08624)

###### 2015~

* [Multi-Modal Obstacle Detection in Unstructured Environments with Conditional Random Fields](https://arxiv.org/abs/1706.02908): 2017.06
  * Unstructured Environments: 농장 
  * lidar + camera sensing using a conditional random field
* [Fusing LIDAR and images for pedestrian detection using convolutional neural networks](http://ieeexplore.ieee.org/abstract/document/7487370/): 2016.04
* Multiview random forest of local experts combining rgb and lidar data for pedestrian detection [\[Gonzalez, IV '15\]](https://scholar.google.de/scholar?q=Multiview Random Forest of Local Experts Combining RGB and LIDAR data  for Pedestrian Detection)

###### ~2014

* Pedestrian Detection Combining RGB and Dense LIDAR Data [\[Premebida, IROS '14\]](https://people.eecs.berkeley.edu/~carreira/papers/iros2014.pdf) [\[Project\]](http://home.isr.uc.pt/~cpremebida/IROS14/LaserVisionFusion.html) [\[Code\]](http://home.isr.uc.pt/~cpremebida/IROS14/Codes_CP_IROS2014.zip)
* [Radar/Lidar sensor fusion for car-following on highways](http://ieeexplore.ieee.org/abstract/document/6144918/): 2011

## 3. Article \(Post, blog, etc.\)

## 3. Tutorial \(Series, \)

## 4. Youtube

* [Tutorial : 3D Deep Learning](https://www.youtube.com/watch?v=8CenT_4HWyY): CVPR 2017, MVCNN, 3DCNN, Point Cloud, Meshes

## 6. Material \(Pdf, ppt\)

* [3D Object Representation  
  ](http://www.connellybarnes.com/work/class/2015/intro_gfx/lectures/17-3DObjectRepresentation.pdf)

* [ADAS \(Advanced Driving Assistance System\)](https://www.slideshare.net/yuhuang/advanced-driving-assistance-system): ppt 261, Baidu USA, 2017.04

### 6.2 Point Cloud

* [~~Synthesize for Learning: Joint analysis of 2D images and 3D shapes~~](http://ai.stanford.edu/~haosu/slides/3dv.pptx): ShapeNet \(3D Datasets\)

* [3D Deep Learning on Geometric Forms](http://ai.stanford.edu/~haosu/slides/NIPS16_3DDL.pptx): \[추천\] 3D 모델들에 대한 설명, 3D DL 설명

* [~~Scene Understanding with 3D Deep Networks~~](https://www.cs.princeton.edu/~funk/nips16.pdf): 3D Match, Deep Sliding Shapes, SSCNet\(Semantic Scene Completion\)

* [Learning 3D representations,disparity estimation, and structure from motion  
  ](http://3ddl.cs.princeton.edu/2016/slides/brox.pdf): FlowNet, DispNet, DeMoN

## 7. Implementation \(Project\)

* [PyDriver](https://github.com/lpltk/pydriver): Training and evaluating object detectors and classifiers in road traffic 

### 7.2

[~~Project: Development of AEB System for Pedestrian Protection \(4th year\)~~](https://github.com/nlkim0817/ProjAEB_4thYear)

* [Kaggle\_3D MNIST](https://www.kaggle.com/daavoo/3d-mnist): A 3D version of the MNIST database of handwritten digits

* [Awesome : Autonomous Vehicles](https://github.com/takeitallsource/awesome-autonomous-vehicles)



## 8. Research Group / Conference 

- [DeepDrive](https://deepdrive.berkeley.edu/project/3d-object-detection-based-lidar-and-camera-fusion): 버클리, 3D Object Detection based on Lidar and Camera Fusion

- [Improving 3D Perception for Object Detection, Classification and Localization using Fused Multimodal Sensors](http://cse.msu.edu/~gonza647/proj03.html): Michigan State University
  - Researcher : Saif Imran, Aaron Gonzalez, Mehmet Akif Alper

- IEEE Intelligent Vehicles Symposium : [2017](https://its.papercept.net/conferences/conferences/IV2017/program/IV2017_ContentListWeb_3.html)




---

|논문명 | |
| --- | --- |
| 저자\(소속\) | \(\) |
| 학회/년도 | IROS 2015, [논문]() |
| 키워드 | |
| 데이터셋(센서)/모델 | |
| 참고 | |
| 관련연구||
| 코드 | |



