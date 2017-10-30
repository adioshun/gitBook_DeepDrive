|논문명|SqueezeDet: Unified, Small, Low Power Fully Convolutional Neural Networks for Real-Time Object Detection for Autonomous Driving|
|-|-|
|저자(소속)|Bichen Wu(버클리)|
|학회/년도|Bichen2016, CVPR 2017, [논문](https://arxiv.org/abs/1612.01051)|
|키워드|KITTI, [YOLO](https://adioshun.gitbooks.io/semantic-segmentation/content/2015yolo.html) + [SqueezeNet](https://adioshun.gitbooks.io/semantic-segmentation/content/2017squeezenet.html)|
|참고|[정리](https://theintelligenceofinformation.wordpress.com/2017/03/02/introducing-squeezedet-low-power-fully-convolutional-neural-network-framework-for-autonomous-driving/)|
|Code|[TF](https://github.com/BichenWuUCB/squeezeDet), [TF /wKITTI](https://github.com/fregu856/2D_detection/blob/master/README.md),  [Docker](https://hub.docker.com/r/lorenagdl/squeezedet/)|


# SqueezeDet

자율주행용 물체 탐지 요구 사항 
- realtime inference speed to guarantee prompt vehicle control
- small model size 
- energy efficiency to enable embedded system deployment

차별점 : In our network we use convolutional layers not only to extract feature maps, but also as the output layer to compute bounding boxes and class probabilities. 

빠른 이유 : The detection pipeline of our model only contains a **single forward pass** of a neural network, thus it is extremely fast.

## 1. Introduction 


이미지 데이터는 중요한 요소중 하나이다.

### 1.1 자율주행용 물체 탐지 요구 사항 

Autonomous driving some **basic requirements** for image object detectors 
- Accuracy:  the detector ideally should achieve **100% recall** with **high precision** on objects of interest. 
- Speed: The detector should have real-time or faster inference speed to reduce the latency of the vehicle control loop. 
- Small model size: As discussed in [16], smaller model size brings benefits of more efficient distributed training, less communication overhead to export new models to clients through wireless update, less energy consumption and more feasible embedded system deployment.
- Energy efficiency: Desktop and rack systems may have the luxury of burning 250W of power for neural network computation, but embedded processors targeting automotive market must fit within a much smaller power and energy envelope.


### 1.2 Pipeline

> The detection pipeline of SqueezeDet is inspired by [21]

1. first, we use stacked convolution filters to extract a high dimensional, low resolution feature map for the input image. 
2. Then, we use ConvDet, a convolutional layer to take the feature map as input and compute a large amount of object bounding boxes and predict their categories. 
3. Finally, we filter these bounding boxes to obtain final detections. 

기본 구조는  SqueezeNet [16]에서 따왔다. 
- SqueezeNet  = AlexNet level imageNet accuracy with a model size of < 5MB that can be further compressed to 0.5MB

```
[21] J. Redmon, S. K. Divvala, R. B. Girshick, and A. Farhadi. You only look once: Unified, real-time object detection. In CVPR, 2016.
[16] F. N. Iandola, S. Han, M. W. Moskewicz, K. Ashraf, W. J. Dally, and K. Keutzer. SqueezeNet: Alexnet-level accuracy with 50x fewer parameters and <0.5mb model size. arXiv:1602.07360, 2016
```

- Small model size: Model size : ~ 8MB
- Speed: Inference속도는 57.2 FPS이다. (입력: 1242x375)
- Energy efficiency(전력 소모) : 1.4J of energy per image (TITAN X GPU, Faster RCNN보다 84배 적음)
- Accuracy: cyclist detection에서는 최고 성능 보임 (차량 탐지는??) 

## 2. Related Work

### 2.1. CNNs for object detection

#### A. Hand-crafted Features

From 2005 to 2013, various techniques were applied to advance the accuracy of object detection on datasets such as PASCAL [7]. In most of these years, versions of HOG+SVM [5] or DPM [8] led the state-of-art accuracy on these datasets

#### B. R-CNN

However, in 2013, Girshick et al. proposed Region-based Convolutional Neural Networks (RCNN)[11], which led to substantial gains in object detection accuracy. 
    
The R-CNN approach begins 
- by identifying region proposals (i.e. regions of interest that are likely to contain objects) and 
- then classifying these regions using a CNN. 

단점 : One disadvantage of R-CNN is that it computes the CNN independently on each region proposal, leading to time-consuming (≤ 1 fps) and energy-inefficient (≥ 200 J/frame) computation. 

해결책 : To remedy this, Girshick et al. experimented with a number of strategies to amortize computation across the region proposals [13, 17, 10], culminating in Faster R-CNN [22].


#### C. R-FCN

An other model, R-FCN, is fullyconvolutional and delivers accuracy that is competitive with
R-CNN, but R-FCN is fully-convolutional which allows it to amortize more computation across the region proposals

#### D. Vehicle Detection 

[2] modified the CNN architecture to use shallower networks to improve accuracy. 
 
[3, 26] on the other hand focused on generating better region proposals. 

```
[2] K. Ashraf, B. Wu, F. N. Iandola, M. W. Moskewicz, and K. Keutzer. Shallow networks for high-accuracy road objectdetection. arXiv:1606.01561, 2016.
[3] Z. Cai, Q. Fan, R. Feris, and N. Vasconcelos. A unified multi-scale deep convolutional neural network for fast object detection. In ECCV, 2016.
[26] Y. Xiang, W. Choi, Y. Lin, and S. Savarese. Subcategoryaware convolutional neural networks for object proposals and detection. arXiv:1604.04693, 2016.
```
#### E. YOLO : real-time speed

- Region proposals are a **cornerstone** in all of the object detection methods that we have discussed so far. 

- However, in YOLO (You Only Look Once) [21], region proposition and classification are integrated into one single stage. 

### 2.2. Small CNN models

Given the **same level of accuracy**, it is often beneficial to **develop smaller CNNs** (i.e. CNNs with fewer model parameters), as discussed in [16]. 

- AlexNet model : 240MB of parameters, 80% top-5 accuracy on ImageNet.
- VGG-19 model :575MB of parameters, 87% top-5 accuracy on ImageNet. 
- SqueezeNet [16] model : 4.8MB of parameters, **AlexNet-level** accuracy on ImageNet. 
- GoogLeNetv[25] model : 53MB of parameters, **VGG-19-level** accuracy on ImageNet


### 2.3 Fully convolutional networks

- Fully-convolutional networks (FCN) were popularized by Long et al., who applied them to the **semantic segmentation** domain [20]. 

```
[20] J. Long, E. Shelhamer, and T. Darrell. Fully convolutional networks for semantic segmentation. In CVPR, 2015.
```

- FCN의 마지막 레이어는 **Vector**방식이 아니라 **그리드** 방식이다. `FCN defines a broad class of CNNs, where the output of the final parameterized layer is a grid rather than a vector.`

- 그리드 방식은 픽셀단위 예측시 사용할수 있으므로 세그멘테이션에 유용한다. `This is useful in semantic segmentation, where each location in the grid corresponds to the predicted class of a pixel.`

- FCN은 다른 분야에도 사용 된다. `FCN models have been applied in other areas as well.`

- 예를 들어 분류 문제에서 기존에는 **Fully Connected Layer**를 써서  **1차원 벡터**로 Class의 확률을 표현 하였ㅏ. `To address the image classification problem, a CNN needs to output a 1-dimensional vector of class probabilities. One common approach is to have one or more fully connected layers, which by definition output a 1D vector– 1×1×Channels (e.g. [18, 23]). `

```
[18] A. Krizhevsky, I. Sutskever, and G. E. Hinton. ImageNet Classification with Deep Convolutional Neural Networks. In NIPS, 2012.
[23] K. Simonyan and A. Zisserman. Very deep convolutional networks for large-scale image recognition. arXiv:1409.1556, 2014.
```

- 하지만, 새 방법은 **Convolutional Layer**를 써서** Grid형태**의 아웃을을 생성하고 average-pooling으로 **다운 샘플링** 하여 **1차원 벡터**로 Class의 확률로 표현 할수 있다. `However, an alternative approach is to have the final parameterized layer be a convolutional layer that outputs a grid (H×W×Channels), and to then use average-pooling to downsample the grid to 1×1×Channels to a vector of produce class probabilities(e.g. [16, 19]). `

```
[16] F. N. Iandola, S. Han, M. W. Moskewicz, K. Ashraf, W. J. Dally, and K. Keutzer. SqueezeNet: Alexnet-level accuracy with 50x fewer parameters and <0.5mb model size. arXiv:1602.07360, 2016.
[19] M. Lin, Q. Chen, and S. Yan. Network in network. In ICLR, 2014.
```

- R-FCN 방법이 Fully convolutional networks을 사용한것이다. `Finally, the R-FCN method that we mentioned earlier in this section is a fully-convolutional network.`


## 3. Method Description

### 3.1. Detection Pipeline

- YOLO의 SSD`(single-stage detection)` pipeline을 채택 하였다. `Inspired by YOLO [21], we also adopt a single-stage detection pipeline : region proposition and classification is performed by one single network simultaneously. `



###### [1단계]
- 입력된 이미지에서 low-resolution, high dimensional **feature map** 추출

###### [2단계]

- Feature map을 **ConvDet layer**에 입력 

- Compute **bounding boxes** centered around W × H uniformly distributed spatial grids. 
  - Here, `W` and `H` are number of grid centers along horizontal and vertical axes.

![](https://i.imgur.com/enbAgkK.png)
```
[Figure 1. SqueezeDet detection pipeline.]
- A convolutional neural network extracts a feature map from the input image and feeds it into the ConvDet layer. 
- The ConvDet layer then computes bounding boxes centered around W × H uniformly distributed grid centers.
- Each bounding box is associated with 1 confidence score and C conditional class probabilities. 
- Then, we keep the top N bouding boxes with highest confidence and use NMS to filter them to
get the final detections.
```


- Each bounding box is associated with `C + 1` values
 - `C` : **number of classes** to distinguish, 
 - `extra 1`: for the **confidence score**

### 3.2 confidence score

- how likely does the bounding box actually contain an object
- A high confidence score = a high probability that an object of interest does exist and that the overlap between the predicted bounding box and the ground truth is high. 

- YOLO같은 confidence score 사용 : $$Pr(Object) \times IOU^{Pred}_{truth}$$

- The other `C` scalars represents the conditional class probability distribution given that the object exists within the bounding box.

- More formally, we denote the conditional probabilities as $$Pr(class_c \mid Object), c \in [1,C]$$

- We assign the label with the highest conditional probability to this bounding box and we use

$$max_c Pr (Class_c \mid Object) \times Pr(Object) \times IOU^{Pred}_{truth} $$

- as the metric to estimate the confidence of the bounding box prediction.

- Finally, we keep the top `N` bounding boxes with the highest confidence and use Non-Maximum Suppression (NMS) to filter redundant bounding boxes to obtain the final detections. 

- During inference, the entire detection pipeline consists of only **one forward pass** of one neural network with minimal post-processing.


### 3.2. ConvDet

- SqueezeDet의 기본 방법은 YOLO에서 가져 왔지만, `ConvDet layer`을 사용함으로써 YOLO보다 적은 model parameters를 가지고도 tens-of-thousands of region proposals을 생성 할수 있다. 

- ConvDet은 학습을 통해 **bounding box 좌표** 와 **class probabilities** 출력하는 중요한 합성곱 레이어이다. 

- **sliding window**처럼 Feature Map에 동작한다. `It works as a sliding window that moves through each spatial position on the feature map.`
 - At each position, it computes $$K × (4 + 1 + C)$$ values that encode the bounding box predictions. 
 - Here, K is the number of reference bounding boxes with pre-selected shapes. 

- Using the notation from [22], we call these reference bounding boxes as `anchor`. 

- Each position on the feature map corresponds to a grid center in the original image, so each anchor can be described by `4 scalars` as $$(\hat{x}_i, \hat{y}_j, \hat{w}_k, \hat{h}_k), i \in [1,W], j \in [1,H], k \in [1,K]$$. 
 - $$\hat{x}_i, \hat{y}_j$$ are spatial coordinates of the reference grid center (i, j).
 - $$\hat{w}_k, \hat{h}_k$$ are the width and height of the `k-th` reference bounding box

- We used the method described by [2] to select reference bounding box shapes to match the data distribution.

- For each anchor (i, j, k), we compute 4 relative coordinates $(\delta x_{ijk}, \delta y_{ijk}, \delta w_{ijk}, \delta h_{ijk})$ to transform the anchor into a predicted bounding box, as shown in Fig. 2. 

![](https://i.imgur.com/ZqiWmfJ.png)
```
[Figure 2. Bounding box transformation.]
- Each grid center has K anchors with pre-selected shapes. 
- Each anchor is transformed to its new position and shape using the relative coordinates computed by the ConvDet layer. 
- Each anchor is associated with a confidence score and class probabilities to predict the category of the object within the bounding box
```
Following [12], the transformation is described by
![](https://i.imgur.com/IKyjIB6.png)

-  $$ x^P_i, y^P_j, w^P_k, h^P_k $$  : predicted bounding box coordinates.

- the other **C + 1** outputs for each anchor encode the **confidence score**
	- for this prediction and conditional class probabilities.

- ConvDet은 Faster-RCNN RPN의 마지막 레이어와 비슷 하다. `ConvDet is similar to the last layer of RPN in Faster RCNN [22].`

-  다른점은 RPN은 Weak Detector이다. `The major difference is that, RPN is regarded as a “weak” detector`
	- “weak” detector is **only responsible** for detecting whether an object exists and generating bounding box proposals for the object. 
	- The classification is handed over to **fully connected layers**, which are regarded as a **“strong” classifier**. 
	- But in fact, **convolutional layers** are “**strong**” enough to detect, localize, and classify objects at the same time.

> For simplicity, we denote the **detection layers of YOLO** [21] as **FcDet** `(only counting the last two fully connected layers)`. 

- 둘의 차이점 : Compared with FcDet, the ConvDet layer has orders of magnitude fewer parameters and is still able to generate more region proposals with higher spatial resolution.

The comparison between ConvDet and FcDet is illustrated in Fig. 3.

|![](https://i.imgur.com/TRRVSzl.png)|![](https://i.imgur.com/UWKNLm1.png)|![](https://i.imgur.com/jLNUGZ8.png)|
|-|-|-|
|Last layer of Region Proposal Network (RPN)|The ConvDet layer|The detection layer of YOLO [21]|
| is a 1x1 convolution with K × (4 + 1) outputs. <BR>4 is the number of relative coordinates, and 1 is the confidence score. <BR>It’s only responsible for generating region proposals. | is a Fw × Fh convolution with output size of K × (5 + C). <BR>It’s responsible for both computing bounding boxes and classifying the object within. | contains 2 fully connected layers. |
|The parameter size for this layer is $$Ch_f × K × 5$$ |The parameter size for this layer is $$F_wF_hCh_fK(5 + C)$$|The first one is of size $$W_fH_fCh_fF_{fc1}$$ <BR> The second one is of size $$F_{fc1}W_oH_oK(5 + C)$$|
```
[Figure 3. Comparing RPN, ConvDet and the detection layer of YOLO [21].]
- Activations are represented as blue cubes and layers (and their parameters) are represented as orange ones. 
- Activation and parameter dimensions are also annotated.
```

![](https://i.imgur.com/e6k6rHe.png)
```
Table 1. Comparison between RPN, ConvDet and FcDet. 
- RP stands for region proposition. cls stands for classification.
```

- Assume that the input **feature map** is of size ($W_f , H_f , Ch_f$ ), 
	- $W_f$ is the width of the feature map, 
	- $H_f$ is the height, 
	- $Ch_f$ is the number of input **channels** to the detection layer. 

-  ConvDet’s 필터`(filter)` 넓이`(width)` as $F_w$ and 높이`(height)` as $F_h$. 

- 적절한 패팅과/Striding을 사용하여 ConvDet의 출력은 Feature Map과 같도록 유지 된다. `With proper padding/striding strategy, the output of ConvDet keeps the **same spatial dimension** as the feature map. `
- 각 reference grid의 출력을 계산하기 위해 필요한 파라미터수 `To compute K × (4 + 1 + C) outputs for each reference grid, the number of parameters required by the ConvDet layer is` 
	- $F_wF_hCh_fK(5 + C).$

#### FcDet layer
- FcDet layer구성 : 2개의 FCL `The FcDet layer described in [21-YOLO] is comprised of two fully connected layers. `

- Using the same notation for the input feature map and assuming the number of outputs of the $fc1$ layer is $F|{fc1|$, then the number of parameters in the $fc1$ layer is $W_fH_fCh_fF_{fc1}$. 

- The second fully connected layer in [21] generates C class probabilities as well as K×(4+1) bounding box coordinates and confidence scores for each of the $W_o × H_o$ grids. 

- Thus, the number of parameters in the fc2 layer is $F_{fc1}W_oH_o(5K + C)$. 

- The total number of parameters in these two fully connected layers is $F_{fc1}(W_fH_fCh_f + W_oH_o(5K + C))$.

- In [21], the input feature map is of size 7x7x1024.

- $F_{fc1}$ = 4096, K = 2, C = 20, $W_o$ = $H_o$ = 7, thus the total number of parameters required by the two fully connected layers is approximately 212 × 106 . 

- If we keep the feature map sizes, number of output grid centers, classes, and anchors the same, and use 3x3 ConvDet, it would only require 3×3×1024×2×25 ≈ 0.46×106 parameters, which is 460X smaller than $FcDet$. 

- The comparison of RPN, ConvDet and FcDet is illustrated in Fig. 3 and summarized in Table 1.

### 3.3. Training protocol

- Faster R-CNN은 4단계 학습이 필요 하지만, SqueezeDet은 YOLO처럼 End-to-End 학습이 가능하다. `Unlike Faster R-CNN [22], which deploys a (4-step) alternating training strategy to train RPN and detector network, our SqueezeDet detection network can be trained end-to-end, similarly to YOLO [21].`

-  Detection + Localization + Classification을 위한 **multi-task loss function**을 정의 하였다. `To train the ConvDet layer to learn detection, localization and classification, we define a multi-task loss function:`

![](https://i.imgur.com/6w12vTT.png)

#### A. The first part 

- 첫 부분은 BBox 리그레이션 관련 부분이다. `The first part of the loss function is the bounding box regression.`
- $(\delta x_{ijk}, \delta y_{ijk}, \delta w_{ijk}, \delta h_{ijk})$ corresponds to the relative coordinates of **anchor-k** located at grid center-(i, j).
- They are outputs of the ConvDet layer. 

- ground truth bounding box계산 : The ground truth bounding box $\delta G_{ijk}$ or $(\delta G_{ijk}, \delta G_{ijk}, \delta G_{ijk}, \delta G_{ijk})$ is computed as:

![](https://i.imgur.com/tKgW0Rk.png)

- Note that Equation 3 is essentially the inverse transformation of Equation 1.

- $(x^G, y^G. w^G, h^G)$ are coordinates of a ground truth bounding box. 

- 학습시, During training, we compare ground truth bounding boxes with all anchors and assign them to the anchors that have the largest overlap (IOU) with each of them. 
	- 그 이유는, The reason is that we want to select the “closest” anchor to match the ground truth box such that the transformation needed is reduced to minimum.


- $I_{ijk}$ evaluates to 
	- `1` if the k-th anchor at position-(i, j) has the largest overlap with a ground truth box, and to 
	- `0` if no ground truth is assigned to it. 
- This way, we only include the loss generated by the “responsible” anchors. 
- As there can be multiple objects per image, we normalize the loss by dividing it by the number of objects.

#### B. The second part

- The second part of the loss function is confidence scorere gression. 

- $\gamma_{ijk}$ is the output from the ConvDet layer, 
	- representing the predicted confidence score for anchor-k at position-(i, j). 

- $\gamma^G_{ijk}$ is obtained by computing the IOU of the predicted bounding box with the ground truth bounding box. 

- Same as above, we only include the loss generated by the anchor box with the largest overlap with the ground truth. 

- For anchors that are not “responsible” for the detection, we penalize their confidence scores with the $\barI_{ijk} \gamma^2_{ijk}$ term, where $\barI_{ijk}= 1 - I_{ijk}$. 

- Usually, there are much more anchors that are not assigned to any object. 

- In order to balance their influence, we use $\lambda^+_{conf}$ and $\lambda^−_{conf}$ to adjust the weight of these two loss components. 

- By definition, the confidence score’s range is [0, 1]. 

- To guarantee that $\gamma_{ijk}$  falls into that range, we feed the corresponding ConvDet output into a sigmoid function to normalize it.


#### C. The last part

- The last part of the loss function is just cross-entropy loss for classification. 
	- $l^G_c \in \{0, 1\}$ is the ground truth label 
	- $p_c \in \[0, 1\], c \in \[1, C\]$ is the probability distribution predicted by the neural net. 

- We used softmax to normalize the corresponding ConvDet output to make sure that $p_c$ is ranged between [0, 1].

#### D. The hyper-parameters

- The hyper-parameters in Equation 2 are selected empirically. 

- In our experiments, we set $\lambda_{bbox}$ = 5, $\lambda^+_{conf}% = 75, $\lambda^-_{conf}$ = 100. 

- This loss function can be optimized directly using back-propagation.

### 3.4. Neural Network Design
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTEyNjE2Mzg2MV19
-->