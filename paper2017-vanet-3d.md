
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

### 1.1 기존 연구 

Vote3Deep isdeveloped in [5] for fast point cloud object detection from3D CNN in order to keep the key power of Lidar as distanceand objects 3D shapes and depth. 

The Kitti Vision BenchmarkSuite [6] offers raw Lidar and labeled objects from point cloudas well as RGB and Grayscale sequences images of driving.However, it does not offer any V2V type of message [11], [15]which offers various types of safety applications operating ona control channel of its 7 available channels operating over adedicated 75 MHz spectrum band around 5.9 GHz. 

The goalof this work is to merge the key features of Lidar in givingaccurate distances, camera with object textural details, andV2V beacons for the awareness of both hidden out-of-sight vehiclesor vehicles not observed by the two other means due tobad conditions (e.g., rainy or foggy weather). 

Our Frameworkrequires additional prior knowledge about selection of labeledpaired objects between the 3 types of data set that we want tocorrespond. 

Exploring the physical neighborhood correlationwithin these three datasets and their natural correspondences inthe 3D physical space, we cast the merging problem of thesethree sets of data as a semi-supervised manifold alignment.Given some clear correspondences between data points fromeach pair of data sets, we align (i.e., pair) the rest of thepoints between the camera-lidar and camera-V2V data sets.The problem is casted as an eigenvalue problem over a graphbasedcompounded Laplacian matrix. 

Once the mapping ofknown points is done, the other points from each data sets canbe easily added in aligned 3D environment, thus significantlyenriching the vehicle knowledge of its surroundings. 

Theremainder of this paper is organised as follows. 

The relatedwork is presented in Section II. 

Object recognition in scene ofthe kitti dataset are presented in III. 

Learning the Lidar objectsfrom Lidar point cloud scans in Kitti dataset are studied in IV.We present the manifold alignment formulation and solutionbetween the 3 Dimensional Lidar space, D camera Space,and 3D V2V becons in section V. 

BSM creation accordingto the Lidar recognized objects from Kitti suite, number ofrecognized objects per input type and the performance of thealignment process are illustrated in Section VI. 

Section VIIprovides conclusion and future work
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU0ODAwNDY1OV19
-->