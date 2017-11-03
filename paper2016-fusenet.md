|논문명 |FuseNet: Incorporating Depth into Semantic Segmentation via Fusion-Based CNN Architecture |
| --- | --- |
| 저자\(소속\) | Caner Hazirbas\(Munich\) |
| 학회/년도 | ACCV 2016, [논문](https://link.springer.com/chapter/10.1007/978-3-319-54181-5_14) |
| 키워드 | Hazirbas2016, RGB+Depth map -> Segmentation, |
| 데이터셋(센서)/모델 |NYU,SUN-RGBD / VGG 16-layer model pre-trained on the ImageNet dataset  |
| 관련연구||
| 참고 | |
| 코드 |[Caffe](https://github.com/tum-vision/fusenet) |



# FuseNEt

- Fully Convolution Network를 이용하여 Encode단계에서 fuse depth features + RGB feature maps하도록 한다. `propose an encoder-decoder type network, where the encoder part is composed of two branches of networks that simultaneously extract features from RGB and depth images and fuse depth features into the RGB feature maps as the network goes deeper`


## 1 Introduction

- FuseNet제안 `we propose an encoder-decoder type network, referred to as FuseNet, `
    - where the **encoder** part is **composed of two branches** of networks that simultaneously extract features from RGB and depth images and fuse depth features into the RGB feature maps as the network goes deeper

- 두가지 퓨젼 방식으로 테스트 수행 `We propose and examine two different ways for fusion of the RGB and depth channels. We also analyze the proposed network architectures, referred to as **dense and sparse fusion** (see Fig. 3), in terms of the level of fusion.`

## 2 Related Work

### 2.1 A fully convolutional network (FCN) architecture

- FCN 제안됨 A fully convolutional network (FCN) architecture has been introduced in [3] that 
    - combines semantic information from a deep, coarse layer with appearance information from a shallow, fine layer to produce accurate and detailed segmentations by applying end-to-end training. 

- FCN단점 해결한 **DeconvNet** 제안됨 Noh et al. [6] have proposed a novel network architecture for semantic segmentation, referred to as **DeconvNet**, 
    - which alleviates the limitations of fully convolutional models (e.g., very limited resolution of labeling). 
    - DeconvNet is composed of **deconvolution** and **unpooling layers** on top of the VGG 16-layer net [11]. 

- To retrieve semantic labeling on the full image size, Zeiler et al. [12] have introduced a network composed of deconvolution and unpooling layers. 

- **SegNet **제안됨 `Concurrently, a very similar network architecture has been presented [13] based on the VGG 16-layer net [11], referred to as SegNet. `

- DeconvNet대비 SegNet의 **다른점 **`In contrast to DeconvNet, `
    - SegNet consists of **smoothed unpooled feature maps** with convolution instead of **deconvolution**. 

- SegNet의 성능 개선방안 제안됨 `Kendall et al. [14] further improved the segmentation accuracy of SegNet by applying dropout [15] during test time [16].`

### 2.2 semantic segmentation algorithms

- 일부 최근 알고리즘 중에 CNN+CRF하는 방식이 있다. `Some recent semantic segmentation algorithms combine the strengths of** CNN **and **conditional random field (CRF)** models. `

- 그동안은 pixel classification 정확도가 나빳다. `It has been shown that the poor pixel classification accuracy, `
    - 왜냐 하면 due to the invariance properties that make CNNs good for high level tasks, 
    - CNN+CRF model로 해결 가능 하다. can be overcome by combining the responses of the CNN at the final layer with a fully connected CRF model [8]. 

- [4]에서 둘을 합쳤다. `CNN and CRF models have also been combined in [4]. More precisely, the method proposed in [4] `
    - applies mean field approximation as the inference for a CRF model with Gaussian pairwise potentials, 
    - where the mean field approximation is modeled as a recurrent neural network, 
    - and the defined network is trained end-to-end refining the weights of the CNN model. 
    
    
- [7]에서도 patch-patch context between image regions학습을 위해 둘을 합쳤다. `Recently, Lin et al. [7] have also combined CNN and CRF models for learning patch-patch context between image regions, and have achieved the current state-of-the-art performance in semantic segmentation.` 
    - One of the main ideas in [7] is to define CNN-based pairwise potential functions to capture semantic correlations between neighboring patches. 
    - Moreover, efficient piecewise training is applied for the CRF model in order to avoid repeated expensive CRF inference during the course of back-propagation.
    
### 2.3 scene labeling

- In [2] a feed-forward neural network has been proposed for **scene labeling**. 
    - The long range (pixel) label dependencies can be taken into account by capturing sufficiently large input context patch, around each pixel to be labeled. 
    - The method [2] relies on a RCNN, i.e. a sequential series of networks sharing the same set of parameters. 
    - Each instance takes as input both an RGB image and the predictions of the previous instance of the network. 
    
RCNN-based approaches are known to be difficult to train, in particular, with large data, since long-term dependencies are vanished while the information is accumulated by the recurrence [5].


### 2.4 LSTM

- Byeon et al. [5] have presented long short term memory (LSTM) recurrent neural networks for natural scene images taking into account the complex spatial dependencies of labels. 
- LSTM networks have been commonly used for **sequence classification**.
- These networks include 
    - recurrently connected layers to learn the dependencies between two frames, 
    - and then transfer the probabilistic inference to the next frame. 
- This allows to easily memorize the context information for long periods of time in sequence data. 

- It has been shown [5] that LSTM networks can be generalized well to any vision-based task and efficiently capture local and global contextual information with a low computational complexity.
    
### 2.5 Fusion 
    
- 최근 퓨전이 segmentation에 영향을 미치고 있다. 
    - State-of-the-art CNNs have the ability to perform **segmentation** on **different kinds of input** sources such as RGB or even RGB-D. 

- 간단한 방법은 4rd 채널로 Depth를 학습 하는것이다. `Therefore a trivial way to incorporate depth information would be to stack it to the RGB channels and train the network on RGB-D data assuming a **four-channel input**. `
    - 이 방법은 충분히 정보를 활용하는 것이 아니다. `However, it would not fully exploit the structure of the scene encoded by the depth channel. `

- This will be also shown experimentally in Sect. 4. 

- 네트워크 층을 깊게 하여 정확도와 강건성을 얻을수 있따. `By making use of deeper and wider network architecture one can expect the increase of the robustness and the accuracy. `

- Hence, one may define a network architecture with more layers. Nevertheless, this approach would require huge dataset in order to learn all the parameter making the training infeasible even in the case when the parameters are initialized with a pre-trained network.   
    
### 2.6  The State of the Arts on RGB-D Data 

#### A. HHA (Depth RCNN)

- 새로운 **representation** 이 제안 되었따. `A new representation of the depth information has been presented by Gupta et al. [1-Saurabh2014]. `

- This representation, referred to as **HHA**, consists of three channels: 
    - disparity, 
    - height of the pixels 
    - angle between of normals and the gravity vector based on the estimated ground floor, respectively. 
    
- By making use of the HHA representation, a superficial improvement was achieved in terms of segmentation accuracy [1]. 

- On the other hand, the information retrieved only from the RGB channels still dominates the HHA representation. 

- 살펴본 봐로는 HHA representation는 깊이 정보를 가지고 있는것 빼고는 추가적 정보를 가지고 있지 않다. `As we shall see in Sect. 4, the HHA representation does not hold more information than the depth itself. `

- 더구나 HHA는 계산 부하가 크다. `Furthermore, computing HHA representation requires high computational cost.`

- 본 논문에서는 적은 계산 부하로 Depth정보를 이용하는 법을 살펴 보겠다. `In this paper we investigate a better way of exploiting depth information with less computational burden.`
  
 #### B. novel LSTM Fusion (LSTM-F)
 
 - [7]은 contextual information을 획득할수 있는 Fuse방법을 제안 하였따. `Li et al. [17] have introduced a novel LSTM Fusion (LSTM-F) model that `
     - captures and fuses **contextual information** from **photometric** and **depth channels** by stacking several convolutional layers and an LSTM layer. 
 
 - The memory layer encodes both short - and long-range spatial dependencies in an image along vertical direction. 
 
 - Moreover, another LSTM-F layer integrates the contexts from different channels and performs bi-directional propagation of the fused vertical contexts. 
 
 - 일반적으로 이런 종류의 아키텍쳐는 복잡하고 학습 시키기가 어렵다. `In general, these kinds of architectures are rather complicated and hence more difficult to train. `
 
 
 ## 3. FuseNet: Unified CNN Framework for Fusing RGB and Depth Channels
 
 ![](https://i.imgur.com/fZMldvd.png)
```
[Fig. 2. The architecture of the proposed FuseNet.] 
- Colors indicate the layer type. 
- The network contains two branches to extract features from RGB and depth images, and the feature maps from depth is constantly fused into the RGB branch, denoted with the red arrows. 
- In our architecture, the fusion layer is implemented as an element-wise summation, demonstrated in the dashed box. (Color figure online)
```

- The network extracts features from the input layer and through filtering provides classification score for each label as an output at each pixel. 

### 3.1 FuseNet Architecture

- 인코더-디코더 방식의 아키텍쳐 설계 `We propose an encoder-decoder type network architecture as shown in Fig. 2. `

- 주요 구성 요소 `The proposed network has two major parts: `
    - (1) the encoder part **extracts features** 
    - (2) the decoder part **upsamples the feature** maps back to **the original input resolution**. 
    
- 인코더-디코더 방식은 DeconvNet [6] and SegNet [13]에서 사용했던 방식으로 segmentation에 좋은 결과를 보임 `This encoder-decoder style has been already introduced in several previous works such as DeconvNet [6] and SegNet [13] and has achieved good segmentation performance.`

- 제안 네트워크는 두개의 encoder branches로 되어 있는 특징이 있따. `Although our proposed network is based on this type of architecture, we further consider to have two encoder branches. `
    - 이 두개의 branch는 RGB & depth images에서 각각 특징을 추출 한다. `These two branches extract features from RGB and depth images. `

- Depth image도 Color이미지 처럼 0~255사이의 값을 가지게 하였다. `We note that the depth image is normalized to have the same value range as color images, i.e. into the interval of [0,255]. `

- 두 입력 정보를 합치기 위해서 **FuseNet**을 제안 한다. `In order to combine information from both input modules,`
    -  depth branch를 feature maps로 Fuse한다. we fuse the feature maps from the **depth branch** into the **feature maps** of the RGB branch. We refer to this architecture as FuseNet (see Fig. 2).



#### A. The encoder part

- 인코더 부분은 VGG를 활용함 `The encoder part of FuseNet resembles the 16-layer VGG net [11], `
    - 단, FCL은 도입 안함 `except of the fully connected layers fc6, fc7 and fc8, `
    - 왜냐 하면 since the fully connected layers reduce the resolution with a factor of 49, which increases the difficulty of the upsampling part. 

- In our network, we always use **batch normalization** (BN) after convolution (Conv) and before rectified linear unit1 (ReLU) to **reduce the internal covariate shift** [18]. 

- CBR Block은 **Conv + BN + ReLU**를 의미한다.  `We refer to the combination of **convolution**, **batch normalization** and **ReLU** as **CBR block**, respectively. `

- BN레이어는 먼저 특징지도를 normalizes하여 zero-mean & unit-variance하게 만든다. 이후 scales & shifts한다. `The BN layer first normalizes the feature maps to have zero-mean and unit-variance, and then scales and shifts them afterwards. `
    - scale/shift파라미터는 학습을 통해 파악한다. `In particular, the scale and shift parameters are learned during training. `

- 결과적으로 Color특징은 Depth 특징에 overwritten 되지 않는다. 하지만 어떻게 둘을 합칠지는 배우게 된다. `As a result, color features are not overwritten by depth features, but the network learns how to combine them in an optimal way.`

#### B. The decoder part

- 디코더 부분은 unpooling을 기억하고 있다가 feature maps을 업샘플링 한다. `The decoder part is a counterpart of the encoder part, where memorized unpooling is applied to upsample the feature maps. `

- 디코더 부분에서도 CBR Block를 사용한다. `In the decoder part, we again use the CBR blocks. `

- 실험삼아 convolution대신 deconvolution를 사ㅇ하였는데 비슷한 성능을 보였다. `We also did experiments with deconvolution instead of convolution, and observed very similar performance. `

- As proposed in [14], we also apply **dropout** in both the encoder and the decoder parts to further boost the performance. 
    - However, we do not use dropout during test time.


#### C. Fusion Block

- 가장 중요한건 **fusion block**이다. `The key ingredient of the FuseNet architecture is the fusion block, `
	- 두개의 Branch를 합친다. `which combines the feature maps of the depth branch and the RGB branch. `
    
- 퓨젼 레이어는 **element-wise summation**로 구현 하였다. `The fusion layer is implemented as **element-wise summation**. `

- CBR block다음에는 항상 fusion layer를 삽입하였다. `In FuseNet, we always insert the fusion layer after the CBR block. `

- By making use of fusion the discontinuities of the features maps computed on the depth image are added into the RGB branch in order to enhance the RGB feature maps. 

- 여러 예에서 봤듯이 Color 도메인과 geometric 도메인은 상호 보완적이다. `As it can be observed in many cases, the features in **the color domain** and in **the geometric domain** complement each other. `


![](https://i.imgur.com/dJXLm2S.png)
```
[Fig. 3. Illustration of different fusion strategies at the second (CBR2) and third (CBR3) convolution blocks of VGG 16-layer net.]
- (a) The fusion layer is only inserted before each pooling layer. 
- (b) The fusion layer is inserted after each CBR block. (Color figure online)
```


- 두 가지 Fusion 전략 제안 Based on this observation, we propose two fusion strategies: 
	- (a) **dense fusion (DF)**, where the fusion layer is added **after each CBR block** of the RGB branch. 
    - (b) **sparse fusion (SF)**, where the fusion layer is only inserted **before each pooling**. 
    
These two strategies are illustrated in Fig. 3.

### 3.2 Fusion of Feature Maps

> In this section, we reason the fusion of the feature maps between the RGB and the depth branches.

## 4. Experimental Evaluation

![](https://i.imgur.com/rQhjCqJ.png)


### 4.1  we compare the FuseNet to network trained with different representation of depth

![](https://i.imgur.com/nEX5KLw.png)
```
[Table 2. Segmentation results of FuseNet in comparison to the networks trained with RGB, depth, HHA and their combinations.] 
- The second part of the table provides the results of variations of FuseNet. 
- We show that FuseNet obtained significant improvements by extracting more informative features from depth.
```

- Depth만 : 42.80(Mean)
- RGB만 : 47.14(Mean)
- FusetNet-SF5 : 48.30(Mean)
- FusetNet-DF5 : 49.86(Mean)

