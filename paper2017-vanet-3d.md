
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
	- many graphical models are presented in [9], [14], [16] to guarantee the consistency of labeling of the pixels in the context of the overall image. 

```
[9] Xuming He and Richard S. Zemel. Learning hybrid models for image annotation with partially labeled data. In D. Koller, D. Schuurmans, Y. Bengio, and L. Bottou, editors, Advances in Neural Information Processing Systems 21, pages 625–632. Curran Associates, Inc., 2009.
[14] L. Ladicky, C. Russell, P. Kohli, and P. H. S. Torr. Associative ´hierarchical crfs for object class image segmentation. In 2009 IEEE 12th International Conference on Computer Vision, pages 739–746, Sept 2009.
[16] Daniel Munoz, J Andrew Bagnell, and Martial Hebert. Stacked hierarchical labeling. In European Conference on Computer Vision, pages 57–70. Springer, 2010.
```

- In addition, the authors in [18], [12]and [7] developed various methods for 
	- **presegmentation** into **superpixels** 
	-  segment candidates that are used to extract the categories and features characterizing individual segments and from combinations of neighboring segments. 

```
[18] Joseph Tighe and Svetlana Lazebnik. Superparsing: Scalable nonparametric image parsing with superpixels. In Proceedings of the 11th European Conference on Computer Vision: Part V, ECCV’10, pages 352–365, Berlin, Heidelberg, 2010. Springer-Verlag.
[12] M. P. Kumar and D. Koller. Efficiently selecting regions for scene understanding. In 2010 IEEE Computer Society Conference on Computer Vision and Pattern Recognition, pages 3217–3224, June 2010.
[7] S. Gould, R. Fulton, and D. Koller. Decomposing a scene into geometric and semantically consistent regions. In 2009 IEEE 12th International Conference on Computer Vision, pages 1–8, Sept 2009
```


- Alternatively,the authors in [13] attempted to **create 3D reconstruction** of dynamic scenes by achieving a long-range spatio-temporal regularization in semantic video segmentation, since both the camera and the scene are in motion. 
	- The developed idea is to integrate deep CNN and CRF to perform sharp pixel-level boundaries of objects. 
	- To this end, deep learning has shown the best performance in inferring objects from not previously trained or seen scenes. 

```
[13] Abhijit Kundu, Vibhav Vineet, and Vladlen Koltun. Feature space optimization for semantic video segmentation. In CVPR, 2016.
```

- Joseph et al. [17-YOLO] developed a general purpose object detection system characterized by a resolution classifier and the usage of a 2 fully connected networks that are built on top of a 24 convolutional layers network. 

- Additionally,a unified muti-scale deep CNN for real-time object detectionis developed in [4] with many sub-network detectors with multiple output layers for multiple object class recognition. 

```
[4] Zhaowei Cai, Quanfu Fan, Rogerio Schmidt Feris, and Nuno Vascon- celos. A unified multi-scale deep convolutional neural network for fast object detection. CoRR, abs/1607.07155, 2016.
```

- 씬 플로우도 중요 하다. Most autonomous driving systems rely on Lidar, stereo cameras or radar sensors to achieve object detection, **scene flow estimation** of objects on roads and their key characteristics and influence on driving decisions and steering commands. 

- We present an augmented **scene flow** understanding and **object mapping** by considering not only Lidar and cameras, but also DSRC-basedV2V beacons exchanged between vehicles.

## 3. ADAPTED DARKNET’S CONVOLUTIONAL NEURAL NETWORK AND KITTI FRAME TESTING

- YOLO의 Anchor Boxes개념을 도입 하였다. `Inspired by CNN developed in [17-YOLO], we propose to exploi tthe feature of Anchor Boxes `
	-  Anchor Boxes = that predict the coordinates of the bounding boxes around recognized objects to find their pixel adjacency directly from the fully connected layers

- 하지만, 정확도가 별로 좋지 않다. 

Unfortunately, this is not an accurate measure since objects might be overlapped and consequently the distance in pixels does not have any significance. 

For this purpose, we introducethat a paired labeled point between camera and Lidar is thefarthest object in the Lidar scan and the farthest one beingdetected in the background of the image. 


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg4Mzc1MjY4M119
-->