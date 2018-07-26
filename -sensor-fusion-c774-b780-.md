- scene-level탐지 및 분류를 위해서 다양한 센서 정보가 사용된다. ` In particular, for the scene-level detection and classification tasks, various sensor modalities are used. `
	- 실내용 : The RGB-depth sensor is widely used for **indoor scene** recognition [36–38]
	- 실외용: LiDAR-stereo vision [39,40], LiDAR-CCD [41], LiDAR-radar [42] and LiDAR-radar-stereo vision [43] are used for **outdoor scenes**. 

- The fusion methods are divided into two categories, namely **early** and **late** fusion. 

```
36. Henry P., Krainin M., Herbst E., Ren X., Fox D. RGB-D mapping: Using depth cameras for dense 3D modeling of indoor environments; Proceedings of the 12th International Symposium on Experimental Robotics (ISER. Citeseer); New Delhi and Agra, India. 18–21 December 2010.
37. Gupta S., Arbelaez P., Malik J. Perceptual organization and recognition of indoor scenes from RGB-D images; Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition; Portland, OR, USA. 23–28 June 2013; pp. 564–571.
38. Munera E., Poza-Lujan J.L., Posadas-Yagüe J.L., Simó-Ten J.E., Noguera J.F.B. Dynamic reconfiguration of a rgbd sensor based on qos and qoc requirements in distributed systems. Sensors. 2015

39. Adarve J.D., Perrollaz M., Makris A., Laugier C. Computing occupancy grids from multiple sensors using linear opinion pools; Proceedings of the 2012 IEEE International Conference on Robotics and Automation (ICRA); St. Paul, MN, USA. 14–18 May 2012; pp. 4074–4079.
40. Oh S.I., Kang H.B. Fast Occupancy Grid Filtering Using Grid Cell Clusters From LiDAR and Stereo Vision Sensor Data. IEEE Sens. J. 2016;16:7258–7266. doi: 10.1109/JSEN.2016.2598600. [Cross Ref]

41. González A., Villalonga G., Xu J., Vázquez D., Amores J., López A.M. Multiview random forest of local experts combining rgb and LiDAR data for pedestrian detection; Proceedings of the 2015 IEEE Intelligent Vehicles Symposium (IV); Seoul, Korea. 28 June–1 July 2015; pp. 356–361.

42. Nuss D., Yuan T., Krehl G., Stuebler M., Reuter S., Dietmayer K. Fusion of laser and radar sensor data with a sequential Monte Carlo Bayesian occupancy filter; Proceedings of the 2015 IEEE Intelligent Vehicles Symposium (IV); Seoul, Korea. 28 June–1 July 2015; pp. 1074–1081.
43. Cho H., Seo Y.W., Kumar B.V., Rajkumar R.R. A multi-sensor fusion system for moving object detection and tracking in urban driving environments; Proceedings of the 2014 IEEE International Conference on Robotics and Automation (ICRA); Hong Kong, China. 31 May–7 June 2014; pp. 1836–1843.
```
---

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

* [A Survey of ADAS Technologies for the Future Perspective of Sensor Fusion](https://link.springer.com/chapter/10.1007/978-3-319-45246-3_13)
* [VANETs Meet Autonomous Vehicles: A Multimodal 3D Environment Learning Approach](https://arxiv.org/abs/1705.08624)

* [Multi-Modal Obstacle Detection in Unstructured Environments with Conditional Random Fields](https://arxiv.org/abs/1706.02908): 2017.06
  * Unstructured Environments: 농장 
  * lidar + camera sensing using a conditional random field
* [Fusing LIDAR and images for pedestrian detection using convolutional neural networks](http://ieeexplore.ieee.org/abstract/document/7487370/): 2016.04
* Multiview random forest of local experts combining rgb and lidar data for pedestrian detection [\[Gonzalez, IV '15\]](https://scholar.google.de/scholar?q=Multiview Random Forest of Local Experts Combining RGB and LIDAR data  for Pedestrian Detection)

* Pedestrian Detection Combining RGB and Dense LIDAR Data [\[Premebida, IROS '14\]](https://people.eecs.berkeley.edu/~carreira/papers/iros2014.pdf) [\[Project\]](http://home.isr.uc.pt/~cpremebida/IROS14/LaserVisionFusion.html) [\[Code\]](http://home.isr.uc.pt/~cpremebida/IROS14/Codes_CP_IROS2014.zip)
* [Radar/Lidar sensor fusion for car-following on highways](http://ieeexplore.ieee.org/abstract/document/6144918/): 2011



- A comparative study of data fusion for RGB-D based visual recognition : A study of data fusion methods for RGB-D visual recognition can be found in Sanchez-Riera et al. [2016].


-  C. Lundquist, “Sensor fusion for automotive applications,” Ph.D. dissertation, Linkoping University, Link ¨ oping, 2011. ¨

-  N.-E. E. Faouzi, H. Leung, and A. Kurian, “Data fusion in intelligent transportation systems: Progress and challenges : A survey,” Information Fusion, vol. 12, no. 1, pp. 4 – 10, 2011.



- ~~[Object Detection and Classification by Decision-Level Fusion for Intelligent Vehicle Systems](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5298778/)~~: 2017, KITTI, 21p

- ~~[FUSION OF LIDAR 3D POINTS CLOUD WITH 2D DIGITAL CAMERA IMAGE](http://www.secs.oakland.edu/~li4/research/student/JuanLi2015.pdf)~~: 2015, 석사학위, 90p, 라이다+카메라 -> RGB-D 정보 획득하기, transformatio 논문



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



## 8. Research Group / Conference 





