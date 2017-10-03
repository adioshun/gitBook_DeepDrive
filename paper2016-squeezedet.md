|논문명|SqueezeDet: Unified, Small, Low Power Fully Convolutional Neural Networks for Real-Time Object Detection for Autonomous Driving|
|-|-|
|저자(소속)|Bichen Wu(버클리)|
|학회/년도|CVPR 2017, [논문](https://arxiv.org/abs/1612.01051)|
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


#### E. YOLO : real-time speed

Region proposals are a **cornerstone** in all of the object detection methods that we have discussed so far. 

However, in YOLO (You Only Look Once) [21], region proposition and classification are integrated into one single stage. 

### 2.2. Small CNN models

Given the **same level of accuracy**, it is often beneficial to **develop smaller CNNs** (i.e. CNNs with fewer model parameters), as discussed in [16]. 

- AlexNet model : 240MB of parameters, 80% top-5 accuracy on ImageNet.
- VGG-19 model :575MB of parameters, 87% top-5 accuracy on ImageNet. 
- SqueezeNet [16] model : 4.8MB of parameters, **AlexNet-level** accuracy on ImageNet. 
- GoogLeNetv[25] model : 53MB of parameters, **VGG-19-level** accuracy on ImageNet


### 2.3 Fully convolutional networks

Fully-convolutional networks (FCN) were popularizedby Long et al., who applied them to the **semantic segmentation** domain [20]. 

FCN defines a broad class of CNNs, where the output of the final parameterized layer is a grid rather than a vector.

This is useful in semantic segmentation, where each location in the grid corresponds to the predicted class of a pixel.

FCN models have been applied in other areas as well.

To address the image classification problem, a CNN needs to output a 1-dimensional vector of class probabilities.

One common approach is to have one or more fully connected layers, which by definition output a 1D vector– 1×1×Channels (e.g. [18, 23]). 

However, an alternative approach is to have the final parameterized layer be a convolutional layer that outputs a grid (H×W×Channels), and to then use average-pooling to downsample the grid to 1×1×Channels to a vector of produce class probabilities(e.g. [16, 19]). 

Finally, the R-FCN method that we mentioned earlier in this section is a fully-convolutional network.

## 3. Method Description

### 3.1. Detection Pipeline

Inspired by YOLO [21], we also adopt a **single-stage detection pipeline** : region proposition and classification is performed by one single network simultaneously. 

![](https://i.imgur.com/enbAgkK.png)

1. 입력된 이미지에서 low-resolution, high dimensional feature map 추출

2. Feature map을 ConvDet layer에 입력 & Compute bounding boxes centered around W × H uniformly distributed spatial grids. 
 - Here, `W` and `H` are number of grid centers along horizontal and vertical axes.

Each bounding box is associated with `C + 1` values
- where `C` is the number of classes to distinguish, 
- the extra `1` is for the confidence score



   confidence score
   - how likely does the bounding box actually contain an object
   - A high confidence score = a high probability that an object of interest does exist and
   that the overlap between the predicted bounding box and the ground truth is high. 


Similarly to YOLO [21], we define the confidence score as $$Pr(Object) \times IOU^{pred}_{truth}$$


The other `C` scalars represents the conditional class probability distribution given that the object exists within the bounding box.

More formally, we denote the conditional probabilities as $$Pr(class_c \mid Object), c \in [1,C]$$

We assign the label with the highest conditional probability to this bounding box and we use

![](https://i.imgur.com/wMT0Fjg.png)

as the metric to estimate the confidence of the bounding box prediction.

Finally, we keep the top `N` bounding boxes with the highest confidence and use Non-Maximum Suppression (NMS) to filter redundant bounding boxes to obtain the final detections. 

During inference, the entire detection pipeline consists of only **one forward pass** of one neural network with minimal post-processing.


