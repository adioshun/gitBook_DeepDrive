
| 논문명 |VANETs Meet Autonomous Vehicles: A Multimodal 3D Environment Learning Approach |
| --- | --- |
| 저자\(소속\) | Yassine Maalej \(University of Idaho\) |
| 학회/년도 | arXiv 2017, [논문](https://arxiv.org/abs/1705.08624v1) |
| 키워드 | Yassine2017,  |
| 데이터셋(센서)/모델 | |
| 관련연구||
| 참고 | |
| 코드 | |

# VANET 

- we design a **multimodal framework** for object **detection**, **recognition** and **mapping** based on the fusion
of 
	- stereo camera frames
	- point cloud Velodyne Lidar scans,
	- Vehicle-to-Vehicle (V2V) Basic Safety Messages(BMS) exchanged using DSRC

- We merge the key features of rich texture descriptions of objects 
	- from 2D images, 
	- depth 
	- distance between objects provided by 3D point cloud 
	- awareness of **hidden vehicles** from BSMs’ 3D information


## I. INTRODUCTION

-  VANET & 자율주행 연구는 **separate worlds**, and barely affected one another despite the obvious relationships.

- 기존 연구 **Vote3Deep** is developed in [5] for fast point cloud object detection from 3D CNN in order to keep the key power of Lidar as distance and objects 3D shapes and depth. 

-  V2V type of message [11], [15]which 
	- offers various types of safety applications operating on a control channel of its 7 available channels operating over a dedicated 75 MHz spectrum band around 5.9 GHz. 

- 퓨젼이 논문 목적 `The goalof this work is to merge the key features of`
	-  **Lidar** in giving accurate **distances**, 
	-  **camera** with object **textural details**
	-  **V2V beacons** for the awareness of both **hidden** out-of-sight vehicles or vehicles **not observed** by the two other means due to bad conditions (e.g., rainy or foggy weather). 

- Exploring the physical neighborhood correlation within these three datasets and their natural correspondences inthe 3D physical space, we cast the merging problem of these three sets of data as a **semi-supervised** manifold alignment.

- Given some clear correspondences between data points from each pair of data sets, we align (i.e., pair) the rest of the points between the camera-lidar and camera-V2V data sets.

- The problem is casted as an eigenvalue problem over a graph based compounded Laplacian matrix. 

- Once the mapping of known points is done, the other points from each data sets can be easily added in aligned 3D environment, thus significantly enriching the vehicle knowledge of its surroundings. 

## RELATED WORK

- 자율 주행을 위해서는 **세그멘테이션이** 필수 적이다. 
	- semantic segmentation that labels each pixel in an image withthe 

- Techniques based on 
	- Markov RandomFields (MRF), 
	- Conditional Random Field (CRF) 
	- many graphical models are presented in [9], [14], [16] to guarantee the consistency of labeling of the pixels in the context ofthe overall image. 

In addition, the authors in [18], [12]and [7] developed various methods for presegmentation intosuperpixels or segment candidates that are used to extract thecategories and features characterizing individual segments andfrom combinations of neighboring segments. 

Alternatively,the authors in [13] attempted to create 3D reconstruction ofdynamic scenes by achieving a long-range spatio-temporalregularization in semantic video segmentation, since both thecamera and the scene are in motion. 

The developed idea isto integrate deep CNN and CRF to perform sharp pixel-levelboundaries of objects. 

To this end, deep learning has shownthe best performance in inferring objects from not previouslytrained or seen scenes. 

Joseph et al. 

[17] developed a generalpurpose object detection system characterized by a resolutionclassifier and the usage of a 2 fully connected networks that arebuilt on top of a 24 convolutional layers network. 

Additionally,a unified muti-scale deep CNN for real-time object detectionis developed in [4] with many sub-network detectors with multipleoutput layers for multiple object class recognition. 

Mostautonomous driving systems rely on Lidar, stereo cameras orradar sensors to achieve object detection, scene flow estimationof objects on roads and their key characteristics and influenceon driving decisions and steering commands. 

We present anaugmented scene flow understanding and object mapping byconsidering not only Lidar and cameras, but also DSRC-basedV2V beacons exchanged between vehicles.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjc1NDk2MzddfQ==
-->