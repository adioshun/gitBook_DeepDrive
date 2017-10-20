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

### 1.1 Two data-fusion scheme
The data-fusion scheme is generally categorized into two types, namely early and late fusion. 

###### The early-fusion method 
- fuses two or more data by combining raw data or concatenating feature descriptors. 
- it often cannot handle incomplete measurements. 
- If one sensor modality becomes useless due to malfunctions, breakdown or severe weather conditions, its measurements will be rendered ambiguous. 

###### The late-fusion method 
- independently performs detection and classification from each sensor modality


Subsequently, the classified outputs are fused at the decision level for final classification.

By using the decision-level fusion scheme for the object detection and classification task, 
	- we can prevent the autonomous driving system from becoming non-functional when information conflicts are introduced to more than one sensor. 

In addition, the reliability and plausibility of each sensor can be considered.

### 1.2  본 논문의 제안 

In this paper, we propose a new object-detection and classification method for a multi-layer LiDAR and a CCD sensor. 

- The contributions of this work are two-fold: 
	- (1) an effective **object-region proposal generation** method
	- (2) a **decision-level fusion** method for accurate object classification.


- 기존 **object-region proposals**방법 
	- For the 3D pointcloud data from the LiDAR sensor : **supervoxel segmentation** and **region-growing** methods are used [6],
	- for the CCD sensor data : **color-flattening image segmentation** and **semantic grouping** methods are proposed  

- **Semantic grouping**정의 : a process in which tiny partitions extracted from segment generation agglomerate with one another to form meaningful object regions. 

- 제안 방식 
	-  Our proposed color flattening is based on L1 norm color transform [8]. 
	- Semantic grouping is performed using our own dissimilarity cost function between the color-flattened and original images.

![](https://i.imgur.com/DlIqQnW.png)
```
Figure 1. Overview of our work. 
- Red arrows denote the processing of unary classifier for each sensor,
- Green arrows denote the fusion processing.
```

- 성능향상을 위해 서로 다른 센서의 unary classifiers 결과값 CNN을 이용하여 합쳤다.` For accurate object classification, we combine the results from the unary classifiers of each sensor at the decision level using a convolutional neuralnetwork (CNN). `

- **unary classifiers**의 주 목적은 object proposals를 분류 하는 것이다. `The main objective of the unary classifiers is to accurately recognize the class of object proposals on each sensor modality. `

- 네트워크를 통과한 결과물은 Loss layer에 입력으로 사용된다. `Previous models of object category classification that used CNNs fed a fixed number of output layers into the final loss layer in their task. `
	- For example, all-passed output, which means the input is passed through all layers of networks, is widely used for feeding into the loss layer. 

- 이 결과물은 일련의 풀링레이어를 통과 하면서 일부 정보를 잃게 된다. `For this output, however, little information loss might occur through the passing of several pooling layers. `

- 반대로, In contrast, the proposed CNN model, similar to unary classifiers, generates a convolutional cube from more than one convolutional layer of a pre-trained CNN model as image representations. 

- From the extracted object proposals obtained from the proposal generations, ROI pooling is applied on the convolutional cube to feed them into a fine-tuned classification network comprising two convolutional layers, two fully-connected layers and a softmax layer. 

- 이후 작업으로 결과값 Fuse를 위해 Fusion CNN에 입력 한다. `Subsequently,to fuse the two detection and classification results of the LiDAR and CCD sensors, we feed the final softmax result vectors and their convolutional cube into the fusion CNN. `

By fusing the multi-sensor modalities, the detection and classification failures can be compensated. 

In addition, fusing the multi-sensor in the decision level makes it more stable when information conflict occurs in each modality when compared to feature-level fusion schemes.

## 2. Related Work

### 2.1 Object-proposal generation

- The object detection and classification tasks can be divided into **object-region proposal generation** and **proposal region classification**. 

- 대안 중 하나는 **슬라이딩 윈도우** 방식 이다. `To extract the object-region proposals, one possible approach is to use the sliding-window method. `
	- 많은 분야에서 사용 되어 왔다. `The sliding window has been used in a wide range of detection tasks for faces [5,10–12], pedestrians [13–17] and cars [18,19].`
	- 단점은 너무 많은 후보 영역을 생성 한다. `Although the sliding window can search whole image regions (i.e., the recall rate is 100%), it generates a very large number of proposals (e.g., approximately 100,000 from a 640×480 image).`

- 단점`(많은 후보영역)` 해결을 위해 다양한 방법들이 제안 되었다. `To reduce the number of object-region proposals, new approaches have been proposed,namely` 
	- objectness [20], 
	- category-independent object proposals (CIOP) [21], 
	- constrained parametricmin-cuts (CPMC) [22], 
	- selective search [23], 
	- EdgeBox [24], 
	- BInarized Normed Gradients (BING) [25]
	- multi-scale combinatorial grouping (MCG) [26]. 

###### []
The objectness method [20] measures the objectness score to distinguish whether a window region belongs to a background or an object.The category-independent method [21] extracts object regions using the graph-cut segmentationmethod and then ranks them to select a well-represented object-region proposal among the overlappedproposals. 

###### []

The CPMC method [22] ranks the plausibility of each segment to determine whether theforeground segments follow good object hypotheses or not. 

###### []

The selective search [23] hierarchicallysegments an image using the color, texture and size of each segment. 

###### []

EdgeBox [24] extracts objectproposals using edge segmentations. 

In addition, it focuses on object boundaries for object-levelproposals. 

The multi-scale combinatorial grouping method [26] segments an image in the hierarchicalscale pyramids, and all of the segmentation results are then applied into the combinatorial grouping.Some previous works proposed the extraction of moving objects from video sequences [27–30] fortraffic scenes. 

Because the amount of measured data in intelligent vehicle environments is larger than that in other applications, we need to design a new method to extract a smaller number of proposalsthan the previous methods.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTIxNzUxNDI4XX0=
-->