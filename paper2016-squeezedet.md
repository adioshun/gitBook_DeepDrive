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