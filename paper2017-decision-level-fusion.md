| 논문명 | Object Detection and Classification by Decision-Level Fusion for Intelligent Vehicle Systems |
| --- | --- |
| 저자\(소속\) | Sang-Il Oh\(Catholic University\) |
| 학회/년도 | 2017, [논문](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5298778/), [석사학위논문](http://academic.naver.com/article.naver?doc_id=195223326) |
| 키워드 |  object-detection, classification, decision-level fusion |
| 데이터셋(센서)/모델 | KITTI |
| 참고 |  |
| 코드 |  |

# Decision-Level Fusion

목적 
- Object detection :  performed for the localization of objects,
- Object classification : recognizes object classes from detected object regions.

In this paper, we propose a new **object-detection and classification method** using **decision-level fusion**. 

방법 
1. We fuse the classification outputs from independent unary classifiers, 
	- unary classifiers, such as 3D point clouds and image data using a convolutional neural network (CNN). 
2. The unary classifiers for the two sensors are the CNN with five layers, 
	- which use more than two pre-trained convolutional layers to consider local to global features as data representation. 
3. To represent data using convolutional layers, we apply region of interest (ROI) pooling to the outputs of each layer on the object candidate regions generated using object proposal generation to realize color flattening and semantic grouping for charge-coupled device and Light Detection And Ranging (LiDAR) sensors.

## 1. Introduction


The data-fusion scheme is generally categorized into two types, namely early and late fusion. 

###### The early-fusion method 
	- fuses two or more data by combining raw data or concatenating feature descriptors. 
	- it often cannot handle incomplete measurements. 
	- If one sensor modality becomes useless due to malfunctions, breakdown or severe weather conditions, its measurements will be rendered ambiguous. 
- The late-fusion method 
	- independently performs detection and classification from each sensor modality


Subsequently, the classified outputs
are fused at the decision level for final classification. By using the decision-level fusion scheme for the
object detection and classification task, we can prevent the autonomous driving system from becoming
non-functional when information conflicts are introduced to more than one sensor. In addition,
the reliability and plausibility of each sensor can be considered.


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyNTM3ODM5NzBdfQ==
-->