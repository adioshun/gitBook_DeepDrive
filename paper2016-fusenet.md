|논문명 |FuseNet: Incorporating Depth into Semantic Segmentation via Fusion-Based CNN Architecture |
| --- | --- |
| 저자\(소속\) | Caner Hazirbas\(Munich\) |
| 학회/년도 | ACCV 2016, [논문](https://link.springer.com/chapter/10.1007/978-3-319-54181-5_14) |
| 키워드 | RGB+Depth map -> Segmentation, |
| 데이터셋(센서)/모델 |NYU,SUN-RGBD  |
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

- 새로운 representation 이 제안 되었따. `A new representation of the depth information has been presented by Gupta et al. [1-Saurabh2014]. `

- This representation, referred to as HHA, consists of three channels: 
    - disparity, 
    - height of the pixels 
    - angle between of normals and the gravity vector based on the estimated ground floor, respectively. 
    
    By making use of the HHA representation, a superficial improvement was achieved in terms of segmentation accuracy [1]. On the other hand, the information retrieved only from the RGB channels still dominates the HHA representation. As we shall see in Sect. 4, the HHA representation does not hold more information than the depth itself. Furthermore, computing HHA representation requires high computational cost. In this paper we investigate a better way of exploiting depth information with less computational burden.
    