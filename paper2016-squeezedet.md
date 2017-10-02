|논문명|SqueezeDet: Unified, Small, Low Power Fully Convolutional Neural Networks for Real-Time Object Detection for Autonomous Driving|
|-|-|
|저자(소속)|Bichen Wu(버클리)|
|학회/년도|CVPR 2017, [논문](https://arxiv.org/abs/1612.01051)|
|키워드|KITTI, |
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

이미지 데이터는 중요한 요소중 하나이다. 

utonomous driving some basic requirements for image object detectors include the following` 
- Accuracy:  the detector ideally should achieve **100% recall** with **high precision** on objects of interest. 
- Speed: The detector should have real-time or faster inference speed to reduce the latency of the vehicle control loop. 
- Small model size: As discussed in [16], smaller model size brings benefits of more efficient distributed training, less communication overhead to export new models to clients through wireless update, less energy consumption and more feasible embedded system deployment.
- Energy efficiency: Desktop and rack systems may have the luxury of burning 250W of power for neural network computation, but embedded processors targeting automotive market must fit within a much smaller power and energy envelope.


### 1.2 Pipeline

The detection pipeline of SqueezeDet is inspired
by [21]: first, we use stacked convolution filters to extract a
high dimensional, low resolution feature map for the input
image. Then, we use ConvDet, a convolutional layer to take
the feature map as input and compute a large amount of object
bounding boxes and predict their categories. Finally, we
filter these bounding boxes to obtain final detections. The
“backbone” convolutional neural net (CNN) architecture of
our network is SqueezeNet [16], which achieves AlexNet
level imageNet accuracy with a model size of < 5MB that
