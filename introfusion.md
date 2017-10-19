## Paper 

- Multi-Sensor Fusion of Occupancy Grids based on Integer Arithmetic

- Fusing LIDAR and Images for Pedestrian Detection using Convolutional Neural Networks, Schlosser

- Motion-based Detection and Tracking in 3D LiDAR Scans, Dewan

- [Learning Where to Attend Like a Human Driver](http://ieeexplore.ieee.org/document/7995833/)

- [Can we unify monocular detectors for autonomous driving
by using the pixel-wise semantic segmentation of CNNs?](https://arxiv.org/pdf/1607.00971.pdf)

- [Online vehicle detection using Haar-like, LBP and HOG feature based image classifiers with stereo vision preselection](http://ieeexplore.ieee.org/abstract/document/7995810/)

- [Feature-based lateral position estimation of surrounding vehicles using stereo vision](http://ieeexplore.ieee.org/document/7995811/)



---

## Overview of Environment Perception for IntelligentVehicles : [참고](http://eprints.whiterose.ac.uk/111149/1/Overview_paper_IEEE_ITS_2017.pdf)

#### B. Data association

Data association plays an important role in the multi-sensor multi-target systems. 

The algorithms of data association can be divided into 
- explicit data association algorithms 
- implicit data association algorithms [126].

##### 가. explicit data association

- the nearest neighbor (NN) algorithm [127]
- the multihypothesis tracking (MHT) approach [128]
- the probabilistic data association (PDA) approach [129]
- to the joint probability data association (JPDA) algorithms [130], [131]. 

##### 나. implicit data association

In contrast to explicit data association, implicit data association tracking approaches output a set of object hypotheses in an implicit way, such as 
- particle filtering [132], 
- probability hypothesis density (PHD) filtering [133]
- multi-target multi Bernoulli (MeMBer) filtering [134], [135], 
- labeled multi Bernoulli filtering [136].

#### C. Fusion 

The architectures for sensor data fusion can be divided into **centralized** and **decentralized** fusion. 

##### 가. centralized fusion architecture

Combining the overall system measurements, most of the data and information processing steps are performed at the fusion center in centralized fusion. 

In [137], a multi target detection and tracking approach for the case of multiple measurements per target and for an unknown and varying number of targets was proposed. 

In [138], [139], a joint sensor registration and fusion approach was developed for cooperative driving in intelligent transportation systems. 

In [140], [141], a multisensor and multitarget surveillance system was developed based on solving jointly the registration, data association and data fusion problems.

```
[137] T. De Laet, H. Bruyninckx, and J. De Schutter, “Shape-based online multitarget tracking and detection for targets causing multiple measurements: Variational Bayesian clustering and lossless data association,” IEEE Transactions on Pattern Analysis and Machine Intelligence,
vol. 33, no. 12, pp. 2477–2491, 2011.
[138] W. Li and H. Leung, “Simultaneous registration and fusion of multiple dissimilar sensors for cooperative driving,” IEEE Transactions on Intelligent Transportation Systems, vol. 5, no. 2, pp. 84–98, 2004.
[139] D. Huang and H. Leung, “An expectation-maximization-based interacting multiple model approach for cooperative driving systems,” IEEE Transactions on Intelligent Transportation Systems, vol. 6, no. 2, pp. 206–228, 2005.
[140] S. Chen, H. Leung, and l. Boss, “A maximum likelihood approach to joint registration, association and fusion for multi-sensor multi-target tracking,” in Proceedings of International Conference on Information Fusion, 2009, pp. 686–693.
[141] Z. Li, S. Chen, H. Leung, and E. Bosse, “Joint data association, registration, and fusion using EM-KF,” IEEE Transactions on Aerospace and Electronic Systems, vol. 46, no. 2, pp. 496–507, 2010.
```

##### 나. decentralized fusion architecture

For the decentralized fusion architecture, the fusion of tracks can be performed at the tracks level. 

In [142], based on equivalent measurements, a joint sensor registration and trackto-track
fusion approach was proposed. 

In [143], using a pseudo-measurement approach, a joint registration, association and fusion method at distributed architecture was developed.

In [144], using information matrix fusion, a track-to-track fusion approach was presented for automotive environment perception. 

Therefore, many heterogeneous sensor data can be fused for vehicle tracking [145].

```
[142] N. N. Okello and S. Challa, “Joint sensor registration and track-to-track fusion for distributed trackers,” IEEE Transactions on Aerospace and Electronic Systems, vol. 40, no. 3, pp. 808–823, 2004.
[143] H. Zhu, H. Leung, and K. V. Yuen, “A joint data association, registration, and fusion approach for distributed tracking,” Information Sciences, vol. 324, pp. 186–196, 2015.
[144] M. Aeberhard, S. Schlichtharle, N. Kaempchen, and T. Bertram, ¨“Track-to-track fusion with asynchronous sensors using information matrix fusion for surround environment perception,” IEEE Transactions on Intelligent Transportation Systems, vol. 13, no. 4, pp. 1717–1726,
2012.
[145] R. O. Chavez-Garcia and O. Aycard, “Multiple sensor fusion and classification for moving object detection and tracking,” IEEE Transactions on Intelligent Transportation Systems, pp. 1–10, 2015.
```

---
![](https://i.imgur.com/Nps3BBD.png)

버클리대 프로젝트 : [DeepDrive](https://deepdrive.berkeley.edu/project/3d-object-detection-based-lidar-and-camera-fusion)
RESEARCHERS : Kiwoo Shin, Zining Wang, Wei Zhan
