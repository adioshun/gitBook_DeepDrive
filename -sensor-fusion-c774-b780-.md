C. Fusion

The architectures for sensor data fusion can be divided into centralized and decentralized fusion.

### 가. centralized fusion architecture

[137] T. De Laet, H. Bruyninckx, and J. De Schutter, “Shape-based online multitarget tracking and detection for targets causing multiple measurements: Variational Bayesian clustering and lossless data association,” IEEE Transactions on Pattern Analysis and Machine Intelligence,
vol. 33, no. 12, pp. 2477–2491, 2011.
[138] W. Li and H. Leung, “Simultaneous registration and fusion of multiple dissimilar sensors for cooperative driving,” IEEE Transactions on Intelligent Transportation Systems, vol. 5, no. 2, pp. 84–98, 2004.
[139] D. Huang and H. Leung, “An expectation-maximization-based interacting multiple model approach for cooperative driving systems,” IEEE Transactions on Intelligent Transportation Systems, vol. 6, no. 2, pp. 206–228, 2005.
[140] S. Chen, H. Leung, and l. Boss, “A maximum likelihood approach to joint registration, association and fusion for multi-sensor multi-target tracking,” in Proceedings of International Conference on Information Fusion, 2009, pp. 686–693.
[141] Z. Li, S. Chen, H. Leung, and E. Bosse, “Joint data association, registration, and fusion using EM-KF,” IEEE Transactions on Aerospace and Electronic Systems, vol. 46, no. 2, pp. 496–507, 2010.

### 나. decentralized fusion architecture
```
[142] N. N. Okello and S. Challa, “Joint sensor registration and track-to-track fusion for distributed trackers,” IEEE Transactions on Aerospace and Electronic Systems, vol. 40, no. 3, pp. 808–823, 2004.
[143] H. Zhu, H. Leung, and K. V. Yuen, “A joint data association, registration, and fusion approach for distributed tracking,” Information Sciences, vol. 324, pp. 186–196, 2015.
[144] M. Aeberhard, S. Schlichtharle, N. Kaempchen, and T. Bertram, ¨“Track-to-track fusion with asynchronous sensors using information matrix fusion for surround environment perception,” IEEE Transactions on Intelligent Transportation Systems, vol. 13, no. 4, pp. 1717–1726,
2012.
[145] R. O. Chavez-Garcia and O. Aycard, “Multiple sensor fusion and classification for moving object detection and tracking,” IEEE Transactions on Intelligent Transportation Systems, pp. 1–10, 2015.
```

---
이미지 + optical flow + LiDAR가 함꺼번에 합쳐져서 DNN에 입력으로 이용 RGB image,optical flow, and LiDAR range images are combined to forma six channel input to a deep neural network [20] for object detection.
동일 모델을 이용하여 joint representation학습에도 활용 The same network can also be used for different modalities to learn a joint representation [21].
```
[20] M. Giering, V. Venugopalan, and K. Reddy, “Multi-modal sensor registration for vehicle perception via deep neural networks,” in High Performance Extreme Computing Conference (HPEC), 2015 IEEE,Sept 2015, pp. 1–6.
[21] L. Castrejon, Y. Aytar, C. Vondrick, H. Pirsiavash, and A. Torralba,“Learning aligned cross-modal representations from weakly aligned data,” in 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), June 2016, pp. 2940–2949.
```


---

# Sensor Fusion 

## 1. List

## 2. Paper

- A comparative study of data fusion for RGB-D based visual recognition : A study of data fusion methods for RGB-D visual recognition can be found in Sanchez-Riera et al. [2016].


-  C. Lundquist, “Sensor fusion for automotive applications,” Ph.D. dissertation, Linkoping University, Link ¨ oping, 2011. ¨

-  N.-E. E. Faouzi, H. Leung, and A. Kurian, “Data fusion in intelligent transportation systems: Progress and challenges : A survey,” Information Fusion, vol. 12, no. 1, pp. 4 – 10, 2011.

- ~~[Object Detection and Tracking with Side Cameras and RADAR in an Automotive Context](http://www.mi.fu-berlin.de/inf/groups/ag-ki/Theses/Completed-theses/Master_Diploma-theses/2013/Hofmann/Master-Hofmann.pdf?1381479774)~~: 2013, 3장이 센서 퓨전 

- ~~[Object Detection and Classification by Decision-Level Fusion for Intelligent Vehicle Systems](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5298778/)~~: 2017, KITTI, 21p

- ~~[FUSION OF LIDAR 3D POINTS CLOUD WITH 2D DIGITAL CAMERA IMAGE](http://www.secs.oakland.edu/~li4/research/student/JuanLi2015.pdf)~~: 2015, 석사학위, 90p, 라이다+카메라 -> RGB-D 정보 획득하기, transformatio 논문

- ~~[Survey on Object Detection and Tracking Using Fusion Approach](https://www.ijircce.com/upload/2016/march/98_24_Survey.pdf)~~: 2016, 8P, 일반적 설명 

- ~~[A Survey of ADAS Technologies for the Future Perspective of Sensor Fusion](https://link.springer.com/chapter/10.1007/978-3-319-45246-3_13)~~: 2016, 일반적 설명

- FusionNet: A deep fully residual convolutional neural network for image segmentation in connectomics: 2016

- FuseNet: Incorporating Depth into Semantic Segmentation via Fusion-Based CNN Architecture: 2016, Depth Information, Semantic Segmentation, Depth Image, CNN, RGB





- ~~Multi-Sensor Fusion of Occupancy Grids based on Integer Arithmetic~~: Fusion 프레임워크 제안, 기본 익힌후 살펴 보기 

- Fusing LIDAR and Images for Pedestrian Detection using Convolutional Neural Networks, Schlosser

- Motion-based Detection and Tracking in 3D LiDAR Scans, Dewan


- ~~[Multiple Sensor Fusion and Classification for Moving Object Detection and Tracking](http://ieeexplore.ieee.org/document/7283636/)~~: 2015, 관련연구의 퓨전 레벨 부분만 참고 함

- [Object Perception for Intelligent Vehicle Applications:A Multi-Sensor Fusion Approach](https://hal.inria.fr/hal-01019527/document): 2014

- ~~[Sensor Modality Fusion with CNNs for UGV Autonomous Driving in Indoor Environments](http://cims.nyu.edu/~achoroma/NonFlash/Papers/SMF_CNN.pdf)~~: 2017, 모형 자동차, 카메라+라이다 연동, DNN 제안 

- [Acoustic/Lidar Sensor Fusion for Car Tracking in City Traffic Scenarios](http://www.drgoehring.de/bib/tadjine15fastzero/tadjine15fastzero.pdf)

- [Trends in Sensor and Data Fusion](http://www.ifp.uni-stuttgart.de/publications/phowo05/300roth.pdf): 2005

## 3. Article (Post, blog, etc.)

- ~~[Expert Advice: Sensor Fusion for Highly Automated Driving](http://gpsworld.com/expert-advice-sensor-fusion-for-highly-automated-driving/)~~: GNSS관련, 구체적 내용 없음 

- [Particle Filter Implementation](https://medium.com/@andrew.d.wilkie/self-driving-car-engineer-diary-9-898f075e888c): 하단 

- 추천 : [Tracking pedestrians for self driving cars](https://medium.com/towards-data-science/tracking-pedestrians-for-self-driving-cars-ccf588acd170)
- 추천 : [Tracking a self-driving car with high precision](https://medium.com/@priya.dwivedi/latest)



## 3. Tutorial (Series, )



## 4. Youtube

- [Vehicle Detection using LiDAR and Camera sensor Fusion](https://www.youtube.com/watch?v=V3cN5LrPr4M)

- [Why You Should Use The Kalman Filter Tutorial - Pokemon Example](https://www.youtube.com/watch?v=bm3cwEP2nUo)

## 6. Material (Pdf, ppt)

- ~~[Sensor Fusion and Calibration of Velodyne LiDAR and RGB Camera ](https://www.it4i.cz/wp-content/uploads/2014/11/RP7_Velas.pdf)~~: ppt

- [Sensor Fusion for Automotive Applications](http://users.isy.liu.se/en/rt/lundquist/Publications/Lundquist2011.pdf): 2011, 331p 

## 7. Implementation (Project)

- [Object Tracking with Sensor Fusion-based Extended Kalman Filter](https://github.com/JunshengFu/tracking-with-Extended-Kalman-Filter)

- [An extended Kalman Filter implementation in Python for fusing lidar and radar sensor measurements](https://github.com/mithi/fusion-ekf-python): 파이썬, 라이다+레이다. 

## 8. Research Group / Conference 

---
![](https://i.imgur.com/8Le2eVF.png)
[RADAR + LIDAR Sensor Fusion Processing Pipeline]
		
## NANODEGREE COURSE (Self-Driving Car Engineer - Sensor Fusion)


### LESSON 1 : Introduction and Sensors
Meet the team at Mercedes who will help you track objects in real-time with Sensor Fusion.

- ~~[Intuition of Kalman Filter for Self-Driving-Car Applications](https://medium.com/towards-data-science/intuition-of-kalman-filter-for-self-driving-car-applications-749b356e19db)~~ 



###  LESSON 2 : Kalman Filters
Learn from the best! Sebastian Thrun will walk you through the usage and concepts of a Kalman Filter using Python.

- [Sensor Fusion and Object Tracking using an Extended Kalman Filter Algorithm — Part 1](https://medium.com/@mithi/object-tracking-and-fusing-sensor-measurements-using-the-extended-kalman-filter-algorithm-part-1-f2158ef1e4f0) 
- [Sensor Fusion and Object Tracking using an Extended Kalman Filter Algorithm — Part 2](https://medium.com/@mithi/sensor-fusion-and-object-tracking-using-an-extended-kalman-filter-algorithm-part-2-cd20801fbeff)

- [Sensor Fusion Algorithms For Autonomous Driving: Part 1 — The Kalman filter and Extended Kalman Filter](https://medium.com/@wilburdes/sensor-fusion-algorithms-for-autonomous-driving-part-1-the-kalman-filter-and-extended-kalman-a4eab8a833dd)

- ~~[UDACITY SDCE Nanodegree Term 2: Kalman Filters for Sensor Fusion](https://medium.com/@ckyrkou/udacity-sdce-nanodegree-term-2-kalman-filters-for-sensor-fusion-1dde97ea628b)~~

- [Kalman Filter, Extended Kalman Filter, Unscented Kalman Filter](https://medium.com/@kastsiukavets.alena/kalman-filter-extended-kalman-filter-unscented-kalman-filter-dbbd929f83c5)
- [Kalman Filter: Predict, Measure, Update, Repeat.](https://medium.com/@tjosh.owoyemi/kalman-filter-predict-measure-update-repeat-20a5e618be66)
- [Make sense of Kalman Filter](https://medium.com/towards-data-science/make-sense-of-kalman-filter-c59fe5f8202f)
- [What is a Kalman filter and why is there an unscented version?](https://medium.com/@anthony_sarkis/what-is-a-kalman-filter-and-why-is-there-an-unscented-version-bc5f6e77c509)
- [How a Kalman filter works, in pictures](http://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/)
- [Udacity Self-Driving Cars: Extended Kalman Filters — my bits](https://medium.com/@tempflip/udacity-self-driving-cars-extended-kalman-filters-my-bits-99cbbaf65e3d)
- [Extended Kalman Filters for Dummies](https://medium.com/@serrano_223/extended-kalman-filters-for-dummies-4168c68e2117)

###  LESSON 3 : C++ Checkpoint
 - Are you ready to build Kalman Filters with C++? Take these quizzes to find out.


###  LESSON 4 : Lidar and Radar Fusion with Kalman Filters in C++
 - In this lesson, you'll build a Kalman Filter in C++ that's capable of handling data from multiple sources. Why C++? Its performance enables the application of object tracking with a Kalman Filter in real-time.


###  LESSON 5(Project) : Extended Kalman Filter Project
In this project, you'll apply everything you've learned so far about Sensor Fusion by implementing an Extended Kalman Filter in C++!
- [Udacity Self-Driving Car Nanodegree Project 6 — Extended Kalman Filter](https://medium.com/udacity/udacity-self-driving-car-nanodegree-project-6-extended-kalman-filter-c3eac16c283d)

- [SDC ND Project 1 — Finding Lane Lines With Kalman Filter](https://medium.com/@raul7/sdc-nd-project-1-finding-lane-lines-with-kalman-filter-15be077346af)

### LESSON 6 : Unscented Kalman Filters
While Extended Kalman Filters work great for linear motion, real objects rarely move linearly. With Unscented Kalman Filters, you'll be able to accurately track non-linear motion!

- [How the Unscented Kalman Filter Got Its Name](https://medium.com/self-driving-cars/how-the-unscented-kalman-filter-got-its-name-4f53fe2db739)

### LESSON 7(Project) : Unscented Kalman Filter Project
Put your skills to the test! Use C++ to code an Unscented Kalman Filter capable of tracking non-linear motion.

- [Udacity Self-Driving Car Nanodegree Project 7 — Unscented Kalman Filter](https://medium.com/@jeremyeshannon/udacity-self-driving-car-nanodegree-project-7-unscented-kalman-filter-ea8bef72a5c7)





