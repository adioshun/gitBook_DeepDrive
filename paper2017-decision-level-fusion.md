| 논문명 | Object Detection and Classification by Decision-Level Fusion for Intelligent Vehicle Systems |
| --- | --- |
| 저자\(소속\) | Sang-Il Oh\(Catholic University\) |
| 학회/년도 | 2017, [논문](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5298778/), [석사학위논문](http://academic.naver.com/article.naver?doc_id=195223326) |
| 키워드 | Oh2017, Lidar+Image, object-detection,  decision-level fusion |
| 데이터셋(센서)/모델 | KITTI |
| 참고 |  |
| 코드 |  |

# Decision-Level Fusion

목적 
- Object detection :  performed for the localization of objects,
- Object classification : recognizes object classes from detected object regions.

In this paper, we propose a new **object-detection and classification method** using **decision-level fusion**. 

방법 

1. We fuse the classification outputs from independent unary classifiers(단항 분류기), 
	- unary classifiers, such as **3D point clouds** and **image data** using a convolutional neural network (CNN). 

2. The unary classifiers for the two sensors are the CNN with five layers, 
	- which use more than two pre-trained convolutional layers to consider local to global features as data representation. 

3. To represent data using convolutional layers, we apply region of interest (ROI) pooling to the outputs of each layer on the object candidate regions generated using object proposal generation to realize color flattening and semantic grouping for charge-coupled device and Light Detection And Ranging (LiDAR) sensors.


> unary classification(=one-class classification) = tries to identify objects of a specific class amongst all objects

## 1. Introduction

### 1.1 Two data-fusion scheme

- 데이터 퓨전은 크게 두 분류로 나누어 진다. 앞단 퓨젼 & 뒷단 퓨젼 `The data-fusion scheme is generally categorized into two types, namely early and late fusion. `

###### The early-fusion method 
- fuses two or more data by combining raw data or concatenating feature descriptors. 
- it often cannot handle incomplete measurements. 
- If one sensor modality becomes useless due to malfunctions, breakdown or severe weather conditions, its measurements will be rendered ambiguous. 

###### The late-fusion method 
- independently performs detection and classification from each sensor modality


- Subsequently, the classified outputs are fused at the decision level for final classification.

- decision-level 퓨전 장점 `By using the decision-level fusion scheme for the object detection and classification task, `
	- 센서가 제대로 동작 하지 않는 상황에 대처 가능 `we can prevent the autonomous driving system from becoming non-functional when information conflicts are introduced to more than one sensor. `
	- In addition, the reliability and plausibility of each sensor can be considered.
	
### 1.2  본 논문의 제안 

In this paper, we propose a new **object-detection** and **classification** method for a multi-layer LiDAR and a CCD sensor. 

- The contributions of this work are two-fold: 
	- (1) 후보영역 추전 방법 : an effective **object-region proposal generation** method
	- (2) 분류 정확도 향상을 위한 **퓨전** 방법 : a **decision-level fusion** method for accurate object classification.


- 기존 **object-region proposals**방법 
	- For the 3D pointcloud data from the LiDAR sensor : **supervoxel segmentation** and **region-growing** methods are used [6],
	- for the CCD sensor data : **color-flattening image segmentation** and **semantic grouping** methods are proposed  

> **Semantic grouping**정의 : a process in which tiny partitions extracted from segment generation agglomerate with one another to form meaningful object regions. 

- 제안 방식 
	- Our proposed **color flattening** is based on **L1 norm color transform** [8]. 
	- **Semantic grouping** is performed using our **own dissimilarity cost function** between the color-flattened and original images.

![](https://i.imgur.com/DlIqQnW.png)
```
Figure 1. Overview of our work. 
- Red arrows denote the processing of unary classifier for each sensor,
- Green arrows denote the fusion processing.
```

- 성능향상을 위해 서로 다른 센서의 unary classifiers 결과값을 decision level에서 CNN을 이용하여 합쳤다.` For accurate object classification, we combine the results from the unary classifiers of each sensor at the decision level using a convolutional neuralnetwork (CNN). `

- **unary classifiers**의 주 목적은 object proposals를 분류 하는 것이다. `The main objective of the unary classifiers is to accurately recognize the class of object proposals on each sensor modality. `

###### [기존 방식과의 비교]

- 기존의 물체 분류기들은 CNN 이용시 고정된 수의 출력 레이어를 마지막 Loss 레이어에 입력으로 사용하였다.  `Previous models of object category classification that used CNNs fed a fixed number of output layers into the final loss layer in their task. `
	- For example, all-passed output, which means the input is passed through all layers of networks, is widely used for feeding into the loss layer. 
	- 이 결과물은 일련의 풀링레이어를 통과 하면서 일부 정보를 잃게 된다. `For this output, however, little information loss might occur through the passing of several pooling layers. `

- 하지만 제안하는 CNN 모델은 convolutional layer에서 convolutional cube를 image representations로 생성한다. 
	- In contrast, the proposed CNN model, `(similar to unary classifiers)`, generates a **convolutional cube** from more than one **convolutional layer** of a pre-trained CNN model as **image representations**. 

- 후보영역 추출 후에 `From the extracted object proposals obtained from the proposal generations,`
	- convolutional cube에 ROI Pooling을 적용하여 분류기 네트워크에 입력 한다. 
    - 분류기 네트워크는 Fully-connected layers + a softmax layer로 구성되어 있따. 
    - **ROI pooling** is applied on the **convolutional cube** to feed them into a fine-tuned **classification network** comprising two convolutional layers, **two fully-connected layers** and a **softmax layer**.

##### [Fuse 방법]

- 이후 작업으로 결과`(Softmax result vectors +  their convolutional cube)`값 Fuse를 위해 Fusion CNN에 입력 한다. `Subsequently,to fuse the two detection and classification results of the LiDAR and CCD sensors, we feed the final softmax result vectors and their convolutional cube into the fusion CNN. `

- fusing the multi-sensor in the **decision level** makes it more **stable** when information **conflict occurs** in each modality when compared to **feature-level fusion **schemes.

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

###### [ objectness method ]
- The objectness method [20] measures the objectness score to distinguish whether a window region belongs to a background or an object.

###### [ category-independent method ]
- The category-independent method [21] extracts object regions using the graph-cut segmentation method and 
- then ranks them to select a well-represented object-region proposal among the overlapped proposals. 

###### [CPMC method]

- The CPMC method [22] ranks the plausibility of each segment to determine whether the foreground segments follow good object hypotheses or not. 

###### [selective search]

- The selective search [23] hierarchically segments an image using the color, texture and size of each segment. 

###### [EdgeBox]

- EdgeBox [24] extracts object proposals using edge segmentations. 

- In addition, it focuses on object boundaries for object-level proposals. 

###### [multi-scale combinatorial grouping method]

- The multi-scale combinatorial grouping method [26] segments an image in the hierarchical scale pyramids, 
- and all of the segmentation results are then applied into the combinatorial grouping.

###### [기타 ]

- Some previous works proposed the extraction of moving objects from video sequences [27–30] for traffic scenes. 

많은 제안들이 있지만, 차량 환경에서는 데이터의 양이 많기 떄문에 좀더 경량화된 후보영역 선출 방법이 필요 하다. `Because the amount of measured data in intelligent vehicle environments is larger than that in other applications, we need to design a new method to extract a smaller number of proposals than the previous methods.`

### 2.2 Object detection and classification

###### [AlexNet ]
- AlexNet [31] won the ImageNet classificationcompetition using CNN. 

###### [YOLO & faster R-CNN ]
- “You only look once” (YOLO) [35] and faster R-CNN [34] constructed a CNN architecture that simultaneously performs object proposal generations and class classifications to reduce the computational times. 

###### [Huang and Chen]
- Huang and Chen [28,29] proposed a variable-bandwidth network and a probabilistic neural network for traffic monitoring systems. 


### 2.3 Detection on multi-sensor modality

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

###### [ early fusion method]

- the measurements are fused by mapping them together,or by concatenation, or probabilistic fusion [41,44,45]. 

- 제약 : However, the early fusion method suffers from problems of **non-overlapping regions** and **uncertainties**. 

- 해결책 : To solve these problems, the **decision-level fusion method** is used as a **late fusion** method. 

```
41. González A., Villalonga G., Xu J., Vázquez D., Amores J., López A.M. Multiview random forest of local experts combining rgb and LiDAR data for pedestrian detection; Proceedings of the 2015 IEEE Intelligent Vehicles Symposium (IV); Seoul, Korea. 28 June–1 July 2015; pp. 356–361.
44. Cadena C., Košecká J. Semantic segmentation with heterogeneous sensor coverages; Proceedings of the 2014 IEEE International Conference on Robotics and Automation (ICRA); Hong Kong, China. 31 May–7 June 2014; pp. 2639–2645.
45. Russell C., Kohli P., Torr P.H., Torr P.H.S. Associative hierarchical crfs for object class image segmentation; Proceedings of the 2009 IEEE 12th International Conference on Computer Vision; Kyoto, Japan. 27 September–4 October 2009; pp. 739–746.
```

###### [Chavez-Garcia and Aycard]

- Chavez-Garcia and Aycard [46] proposed an evidential framework to improve the detection and tracking of moving objects by managing the uncertainty. 

###### [Cho et al]

- Cho et al. [43] independently extracted data features using target information from sensors and combined the entire target information for movement classification and tracking of moving objects.

###### [transferable belief model ]

- The transferable belief model was used to combine the sensor measurements by managing the uncertainty [47]. 

최근 연구에서 저자는**performance**과 **uncertainties**를 모두 고려 하였다. `In the present study, we use the CNN framework to jointly consider the classification performance of each sensor modality, as well as the uncertainties.`

## 3. Overview

Our method consistsof three phases: 
- (1) pre-processing; 
- (2) object-region proposal generation; 
- (3) classification of theobject-region proposals.

### 3.1 Pre-processing

- For the CCD image input, 
	- **color flattening** is performed,
	- 모노톤이 유용함 `which makes the image assume a monotonous color and is useful in obtaining desirable segmentation results.`

- For the point-cloud input, 
	- we transform the 3D point clouds into **3D occupancy voxel** spaces.
	- 노이즈 제거 `This transformation reduces the noise in the point clouds, `
	- i.e., only the obviously reflected point measurements are acquired.


### 3.2 Object-region proposal generation

> 2D`(color-flattened image)`, 3D`(supervoxels)` 입력 결과는 후보 영역들의 집합이다. 

#### A. Image

- 평탄화한 모노톤 이미지에 대하여 세그멘테이션 실시 `We perform segmentation of the color-flattened image.`
	- 결과가 만족 스럽지 않음 `However, the initial segmentation results are not satisfactory with respect to the detection of meaningful objects. `

- 그래서 추가 작업 실시 : Therefore, we perform **semantic grouping** using a dissimilarity cost function from the pixel values of both the color-flattened and original images. 
	- 이 결과는 **object-region proposals**이다.  `These results are the object-region proposals from the CCD sensor data.`

#### B. Point Cloud

- VCCS를 이용하여 **슈퍼복셀** 추출 `In the 3D occupancy voxel space, we extract the supervoxels using the voxel cloud connectivity segmentation (VCCS) [6]. `
	- VCCS uses a gradient-seeding methodology to segment point clouds.
	- 이 결과는 fine-level 세그먼트 이다.  `The resulting supervoxels are fine-level segments with a fixed size. `

- 추가적으로 region growing을 실시 하여 object-level 세그먼트 획득 `Subsequently, we perform region growing on the supervoxels to obtain object-level segments using the occupancy connectivity because the supervoxels do not express meaningful cues. `
	- 이결과는 **object-region proposals** 이다. `These results are the object-region proposals from the 3D point clouds.`


### 3.3 Classifying object proposals

> convolutional cube - ROI pooling - 물체 영역정보

- 여러 후보영역중에서 분류하기 위하여 unary classifiers를 통과한 결과들을 CNN을 이용하여 Fuse하였다. `To classify the object proposals, we fuse the classification results from the unary classifiers of the LiDAR and CCD sensors using CNN. `

- unary classifiers은 CNN으로 모델링 하였다. `The unary classifiers are modeled using CNN models with the same network architecture. `

- 제안된 CNN은 두 절차(**image representation** + **classification networks**)로 진행 된다. `The proposed CNN models are generated with two phases consisting of image representation and classification networks. `

###### [절차 1 : image representation]

- 입력 데이터를 Represent 하기 위하여 convolutional cube`(onvolutional layer로 구성됨)`를 추출 한다. `To represent the input data, we extract a convolutional cube that has more than one convolutional layer of pre-trainedCNN models. `

- 입력데이터의 convolutional cube에서 **ROI pooling**을 이용하여 물체 영역정보를 추출 한다. `From the convolutional cube of the input data, object regions from the object-proposal generations are extracted using ROI pooling. `

###### [절차 2 : classification networks]

-  후보 영역들에서 추출된 convolutional cube를 classification network로 입력 `the convolutional cube extracted from the proposal regions is fed into a classification network `

- classification network = two convolutional layers + two fully-connectedlayers + a softmax layer. 


- 결과를 Fuse하기 위해 새 CNN모델 제안 `To fuse the results from the two separate unary classifiers, we propose a CNN model `
	- that uses the **convolutional cube** and **softmax results** of the sensor modalities as input.

## 4. Pre-Processing

- 이미지 데이터 :L1 Norm-Based Color Flattening
- 포인트 클라우드 데이터 : The 3D Occupancy Voxel Spaces

### 4.1. L1 Norm-Based Color Flattening

- we generate a color-flattened image from CCD sensor image I.

- Our color flattening is based on the L1 image transform. 

- However, the color flattening based on the L1 image-transform method proposed by Bi et al. [8] was very costly. 

- Therefore, we propose a modified color-flattening L1 image transform by defining an energy function as follows:

### 4.2. The 3D Occupancy Voxel Spaces (노이즈 제거위해)

- the 3D point clouds can have many **noisy reflectance particles**. 

- If the given point clouds contain significant noise, erroneous object partitions will be generated in the segmentation task,i.e., the number of meaningless partitions will increase. 

- This incurs additional computational costs to achieve desirable segmented results. 

- To reduce the noise, 3D point clouds with adjacent positions are transformed to discrete 3D **occupancy voxel spaces**.

## 5. Object-Region Proposal Generation

### 5.1. Object-Region Proposal from the CCD Sensor

### 5.2. Object-Region Proposal from the LiDAR Sensor

## 6. Classifying Object-Region Proposals


### 6.1. Unary Classifier

- CNN의 특징중 하나는 representation 학습과 예측을 동시에 할수 있다는 것이다. `One of the benefits of the CNNs is the simultaneous direct learning of representation and estimation. `

![](https://i.imgur.com/HPzXqNR.png)


- 후보 영역을 classify하는데 사용하는 unary classifier를 제안 한다. `We propose a CNN architecture for accurate classification of the object proposals. Figure 4 shows the architecture of the unary classifier used to classify the object proposals presented in Section 5. `

- 자율 주행 부분에서 다양한 크기의 물체들이 존재 한다. Scale variations은 자차와의 거리에 영향을 받는다. `The objects of the driving scenes contain large variations in their scales. Scale variations can be introduced by distances from the ego-vehicle and/or inter (or intra) types of objects in driving scenes. `

- 그러나 이전의 CNN모델들은 마지막 레이어의 fixed output을 data representation으로 사용 하였다. `However, previous CNN models for detecting and classifying objects used the fixed output from the final layers of a model as a data representation. `

- 이런점 때문에 중요한 특징들이 convolution/pooling같은 레이어를 지나면서 사라졌다. `At this point, the fine features can be gradually ignored according to a passing layer, which includes some types of operations, such as convolution and pooling. `

- 특히 작은 바운딩 박스는 해상도가 낮기 때문에 레이어를 지나면서 특징값을 잃게 된다. `In particular, if a small bounding box has passed entire layers, feature losses may be introduced owing to its low resolution. `

- 이러한 작은 물체 특징을 이용하기 위해서 본 논문에서는 각 입력데이터를 이용하여 convolutional cube를 만들고 이것을 data representation으로 사용 하였다. ` Therefore, to use the features of small objects, as well as objects with moderate sizes, we construct a convolutional cube from each input data as a data representation. `

> convolutional cube 적용 이유 : 작은 물체특징 활용 

- convolutional cube는 HyperFeature와 마찬가지로 convolutional layers를 쌓음으로써 여러개의 convolutional output을  represents할수 있다. `The convolutional cube represents more than one convolutional output of some stacked convolutional layers, which is similar to HyperFeature [33]. `

- 각 convolutional layer의 출력값이 다르기 때문에 이를 고려하여야 하였다. `Because the sizes of the outputs from each convolutional layer vary, we should individually sample them by applying different sampling layers to the stack outputs of the convolutional layers. `

- convolutional cube보다 크기가 큰것들도 max pooling layers사용하여서 조절 하였다. `The subsampling for the outputs of the convolutional layers with sizes larger than that of the convolutional cube is generated by max pooling layers. `

- convolutional cube보다 크기가 작은것들도 deconvolutional layer를 사용하여서 업샘플링하였다. ` Meanwhile, a deconvolutional layer is used to up-sample the outputs of convolutional layers that are smaller than the size of the convolutional cube. `

- 이후 전체 결과에 대하여 **local response normalization**을 이용하여 normalize하였따. `Subsequently, local response normalization is used to normalize the entire output. `

- 결과적으로 동일한 크기의 입력 데이터의 convolutional cube를 획득하게 된다. `Consequently, we can obtain the convolutional cube of the input data with a uniform scale.`


- **region of the object proposal**은 ROI pooling을 이용하여서 convolutional cube에서 추출 된다. `The region of the object proposal presented in Section 5 is extracted from the convolutional cube of the input data using ROI pooling. `

- 이후 각 후보영역의 convolutional cube는 CNN에 입력되어 물체의 category가 분류 된다. `Then, the convolutional cube of each object proposal is fed into a small CNN to classify their object category. `
	- 이 CNN은 KITTI 데이터셋으로 파인튠된것이다. `This CNN is fine-tuned on a KITTI dataset. `

- 네트워크는 **max pooling layers** + **two fully-connected layers** + **one softmax layer**로 구성되어 있다. `The network comprises two convolutional layers with max pooling layers, two fully-connected layers and one softmax layer.`


### 6.2. Fusion Classifier


- Bounding box association: 분류 결과들을 Fuse하기 위해서는 object bounding boxes간의 **Association**을 찾아야 한다. ` To fuse the classification results extracted from each sensor datum, we need to find an association between the object bounding boxes. `

- 본 논문에서는 association을 BBA로 표현 하였다. `In this paper, we represent the association as basic belief assignment (BBA) [50,51].`

- The fusion of the classification results provided by each unary classifier leads us to benefit from the reliability by reducing the uncertainty.

![](https://i.imgur.com/yDLpTxk.png)

- Classifier for fusion results from unary classifiers: For the decision-level fusion,**object-proposal generations** and **classifications** are 
	- first independently run on each sensor modality. 
    - The next process is performed to fuse the decision results using a CNN model. 
    
- 퓨젼 분류기는 2개의 Culumn을 입력으로 받는다. The fusion classifier takes **two separate input columns** that include 
	- convolutional cubes and 
    - category probabilities of the softmax layers from each sensor modality. 

- 첫번째 Culumn의 입력은 각 센서의 convolutional cube이 concatenated된 convolutional cube이다. `The input of the first column is a convolutional cube in which the convolutional cubes from each sensor modality are concatenated. `

- 두개의 합성곱 레이어와 두개의 FCL을 지나면서 concatenated convolutional cube 은 2048D 벡터가 된다. `By passing two convolutional layers and two fully-connected layers, the concatenated convolutional cube becomes a 2048-dimensional vector. `
	- 이 벡터는 two-class probability vectors를 이용해서 concatenated된다. `This vector is concatenated using two-class probability vectors. `

- Subsequently, a 2054-dimensional vector (2048 + 3 + 3) is fed into two fully-connected layers and a binary class SVM for the final fusion classification.


## 7. Experimental Results 

![](https://i.imgur.com/pcCKDUH.png)

- 차량 탐지 Recall
	- CCD만 88.4%
    - Lidar만 71.8%
    - Fution 90.8%

---
DST has previously been used in perception as a pre-processing information fusion step to a CNN to achieve both semantic image labeling as in [25] and object detection and classification as in [16-DL-Fusion].
[25] presents a custom, 4-layer CNN,
while [16] utilizes a pre-trained VGG-16 network for each sensor.


---
- Unary classification(=one-class classification) :여러 object중에서 특정 class에 속하는 object만 선택 `tries to identify objects of a specific class amongst all objects, `
	- by learning from a training set containing only the objects of that class. 

- Multi classification : 여러 class중에서 어느 class에 속하는지 선택 `tries to distinguish between two or more classes `
	- by training set containing objects from all the classes. 

- "One-class learning, or unsupervised SVM, aims at separating data from the origin......."

- To build a callsifier only with the knowledge of a target class

- An example is the classification of the operational status of a nuclear plant as 'normal':[1] In this scenario, there are few, if any, examples of catastrophic system states; only the statistics of normal operation are known. 

- 단일 분류는 오직 하나의 타겟 클래스 만을 이용해 분류기를 만들며, 

- 분류 결과가 해당 클래스에 속하는지 아닌지에 따라 양(positive) 또는 음(negative)으로 판별한다.

- 일반적으로 단일 분류 문제는 비교할 수 있는 다른 클래스가 없어서 타겟 클래스의 고유 특성을 알기가 모호하다는 점 때문에 다중 분류 문제보다 어렵다.

> 정인교, Hyper-Rectangles를 이용한 단일 분류기 설계, 2015

> A Survey of Recent Trends in One Class Classification, 2010 [[다운로드]](https://cs.uwaterloo.ca/~s255khan/files/occ_survey09.pdf)
