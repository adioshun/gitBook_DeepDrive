|논문명|Toward Domain Independence for Learning-Based Monocular Depth Estimation|
|-|-|
|저자(소속)| Michele Mancini (), J-MOD^2 저자|
|학회/년도| IEEE 2017, [논문](http://rpg.ifi.uzh.ch/docs/RAL17_Mancini.pdf)|
|키워드| 1 camera, LSTM, KITTI, synthetic datasets |
|참고|[홈페이지](http://www.sira.diei.unipg.it/supplementary/ral2016/extra.html), [Youtube](https://www.youtube.com/watch?v=UfoAkYLb-5I)|
|코드|[caffe??(374M)](http://www.sira.diei.unipg.it/supplementary/ral2016/unipg_models.tar.gz)|

> LSTM이 어떻게 **global scale** 측정 문제를 해결 하였나??

> 기존 연구 : [12] M. Mancini, G. Costante, P. Valigi, and T. A. Ciarfuglia, “Fast robust monocular depth estimation for obstacle detection with fully convolutional networks,” in Intelligent Robots and Systems (IROS), 2016 IEEE/RSJ International Conference on, 2016.

# Towards Domain Independence for Learning-based Monocular Depth Estimation



가상 데이터를 이용하여서도 좋은 성능 보임을 확인 `In this work, we propose a DNN for scene depth estimation that is trained on synthetic datasets, `
- which allow inexpensive generation of ground truth data. 
- We show how this approach is able to generalize well across different scenarios.

단안렌즈의 태생적 제약인 **global scale estimation**을 LSTM을 이용하여 해결 
- In addition, we show how the addition of **Long Short Term Memory (LSTM)** layers in the network 
- helps to alleviate, in sequential image streams, some of the intrinsic limitations of monocular vision,
- such as **global scale estimation**, with low computational overhead.

Stereo 카메라 방식의 단점 
- Lack of robustenss on long-range measuremnet
- pixel matching errors 


## 1.  INTRODUCTION

단안/양안 카메라 모두 깊이 측정에 사용될수 있다. 

### 1.2 양안 카메라 

- 양안카메라 단점 : the detection range and accuracy of stereo cameras are limited by the camera set-up and baseline [3],[4]. 

- 단점 해결 방법 : Exploiting geometric constraints on camera motion and planarity, obstacle detection and navigable ground space estimation can be extended far beyond the normal range ([5], [6]). 

```
[3] P. Pinggera, D. Pfeiffer, U. Franke, and R. Mester, “Know your limits: Accuracy of long range stereoscopic object measurements in practice,” in Computer Vision–ECCV 2014. Springer, 2014, pp. 96–111.
[4] E. R. Davies, Machine vision: theory, algorithms, practicalities. Elsevier,2004.
```

### 1.2 단안 카메라 

최근 머신러닝을 이용한 깊이측정 측정 방법이 양안 카메라 용으로 제안 되었다. ([7], [8], [9], [10], [11]). 

- 머신러닝 방식의 장점: they are able to learn scale without the use of **external metric information**, such as Inertial Measurement Unit (IMU) measurements, and are not subject to any **geometrical constraint**. 

- 머신러닝 방식의 단점 : 학습에 사용된 환경만 적용 가능하다. `On the downside, these systems rely on the quality and variety of the training set and ground truth provided, and often are not able to adapt to unseen environments`


```
[7] D. Eigen, C. Puhrsch, and R. Fergus, “Depth map prediction from a single image using a multi-scale deep network,” in Advances in neural information processing systems, 2014, pp. 2366–2374.
[8] F. Liu, C. Shen, G. Lin, and I. Reid, “Learning depth from single monocular images using deep convolutional neural fields,” IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 38, no. 10, pp. 2024–2039, Oct 2016.
[9] A. Roy and S. Todorovic, “Monocular depth estimation using neural regression forest,” 2016.
[10] A. Saxena, M. Sun, and A. Y. Ng, “Make3d: Learning 3d scene structure from a single still image,” Pattern Analysis and Machine Intelligence, IEEE Transactions on, vol. 31, no. 5, pp. 824–840, 2009.
[11] R. Garg and I. Reid, “Unsupervised cnn for single view depth estimation: Geometry to the rescue,” arXiv preprint arXiv:1603.04992, 2016.
```
### 1.3 Domain independence

domain independence는 중요한 도전 과제 이다. 

이전 연구[12]에서 가상의 synthetic urban dataset를 가지고 KITTI에 적용하여 좋은 성과를 보임을 확인 헀다. `In our previous work [12] we showed that training a CNN with a inexpensive generated, densely-labeled, synthetic urban dataset, achieved promising results on the KITTI dataset benchmark using RGB and optical flow inputs.`

```
[12] M. Mancini, G. Costante, P. Valigi, and T. A. Ciarfuglia, “Fast robust monocular depth estimation for obstacle detection with fully convolutional networks,” in Intelligent Robots and Systems (IROS), 2016 IEEE/RSJ International Conference on, 2016.
```

본 연구에서는 가상데이터를 이용하여 비젼 기반 깊이 측정의 **domain independence**을 가져 오는 방안을 연구 하였다. 

- 성능향상을 위해 invariant에 중요한 요소인 **optical flow**레이어를 제거 하였다. `we reduce the computational complexity of the network by removing the network dependence on optical flow, even if it often acts as a environment-invariant feature. `
- 제거로 인해 발생하는 정보 손신은 LSTM레이러를 이용하여 만외 하였다. `To balance this loss of information, we exploit the input stream sequentiality by using Long Short Term Memory (LSTM) layers, a specific form of Recurrent Neural Networks (RNNs).`

## 2. RELATED WORK

###### Stereo camera 제약

- Traditional vision-based depth estimation is based on **stereo vision** [13]. 

- 양안 카메라 제약 Its main limitations lie on 
    - the lack of robustness on long range measurements and 
    - pixel matching errors. 

- 부가적으로 : weight and power consumption minimization is highly desirable. 

```
[13] D. Scharstein and R. Szeliski, “A taxonomy and evaluation of dense two-frame stereo correspondence algorithms,” International journal of computer vision, vol. 47, no. 1-3, pp. 7–42, 2002.
```

###### Monocular camera /w geometric methods 제약

- Monocular depth estimation based on geometric methods is grounded on the **triangulation of consecutive frames**.

- 일부 좋은 성과를 보이지만[14], [15], [16],고속 이동시 성능이 떨어 진다. `the performance of their reconstruction routines drops during high-speed motion, as dense alignment becomes extremely challenging. `

- 또한, **absolute scal** 구하는게 불가능 하다. `In addition, it is not possible to recover the absolute scale of the object distances.`

```
[14] M. Pizzoli, C. Forster, and D. Scaramuzza, “Remode: Probabilistic, monocular dense reconstruction in real time,” in 2014 IEEE International Conference on Robotics and Automation (ICRA). IEEE, 2014, pp. 2609–2616.
[15] J. Engel, T. Schops, and D. Cremers, “Lsd-slam: Large-scale direct monocular slam,” in European Conference on Computer Vision. Springer, 2014, pp. 834–849.
[16] R. A. Newcombe, S. J. Lovegrove, and A. J. Davison, “Dtam: Dense tracking and mapping in real-time,” in 2011 international conference on computer vision. IEEE, 2011, pp. 2320–2327
```


> 본 연구에서는 compute the **scene depth** and the associated **absolute scale** from a single image (i.e., `without processing multiple frames`) 방법을 제안 한다. 

### 2.1 기존 연구 

###### Markov Random Field -> Make3D project

- 기존 학습 기반 깊이 측정 방법은 특정 학습된 도메인에서만 좋은 성과를 보였다. 

- Saxena et al. [17] first proposed a **Markov Random Field** to predict depth from a monocular, horizontally-aligned image, 
    - which then later evolved into the Make3D project [10]. 

- 문제점 : This method tends to suffer in uncontrolled settings, especially when the horizontal alignment condition does not hold. 

```
[17] A. Saxena, S. H. Chung, and A. Y. Ng, “Learning depth from single monocular images,” in Advances in Neural Information Processing Systems, 2005, pp. 1161–1168
```

###### 깊이 측정에 CNN을 적용한 최초의 논문 

- Eigen et al. ([7], [18],exploit for the first time in their work the emergence of Deep Learning solutions for this kind of problems, training a multi scale CNN to estimate depth. 

```
[7] D. Eigen, C. Puhrsch, and R. Fergus, “Depth map prediction from a single image using a multi-scale deep network,” in Advances in neural information processing systems, 2014, pp. 2366–2374.
[18] D. Eigen and R. Fergus, “Predicting depth, surface normals and semanticlabels with a common multi-scale convolutional architecture,” in Proceedings of the IEEE International Conference on Computer Vision, 2015, pp. 2650–2658.
```


###### CNN + Conditional Random Field

- Liu et al. [8] combine a CNN with a Conditional Random Field to improve smoothness. 

```
[8] F. Liu, C. Shen, G. Lin, and I. Reid, “Learning depth from single monocular images using deep convolutional neural fields,” IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 38, no. 10, pp. 2024–2039, Oct 2016
```

###### Neural Regression Forest

- Roy et al. [9] recently proposed a novel depth estimation method based on Neural Regression Forest. 

```
[9] A. Roy and S. Todorovic, “Monocular depth estimation using neural regression forest,” 2016.
```

> 위 논문들은 not domain independent

###### 제안 방식들의 속도 

- 기존의 monocular depth estimation 임베디드 시스템에 사용하기에는 적절하지 않다. 

- [8] and [9]에서 속도 향상이 있지만 1s both on a GTX780 and a Tesla k80로 실시간에 맞지 않다. 

- Conversely, **Eigen et al**. method is able to estimate a coarser resolution (1/4 of the input image) of the scene depth map with a inference time of about **10ms**. 

-** Our system**’s inference time is less than **30ms** on a comparable hardware (Tesla k40) and less than **0.4s** on an embedded hardware (Jetson TK1), making real-time application feasible. 


###### optical flow 제거 

- 베이스라인으로 이전 연구 결과를 사용하였다. 해당 방식은 입력으로 **current frame**과 **optical flow**을 사용한다. `Our previous work propose a baseline solution to the problem, suggesting a Fully Convolutional Network (FCN) fed with both the current frame and the optical flow between current and previous frame [12-기존연구]. `

- optical flow는 invariant feature로는 좋지만 다른 도메인에서 일반화 하기에는 부족하다. 속도 저하도 유발한다.  `Despite optical flow acts as a good environment-invariant feature, it is not sufficient to achieve generalization across different scenarios. Furthermore, the computation of the optical flow considerably increase the overall inference time. `

- 제안방식은 current frame 사용  : In this work, only the current frame is fed into the network: by using a deeper architecture and the LSTM paradigm together with a wise mix of different synthetic datasets we report a significant performance gain in a simpler and more efficient fashion.

###### data scarcity(부족)

- 본 논문에서 다루지 못한 부분은 the training of networks given data scarcity(부족). 

- Recently, Garg et al. [11] proposed an **unsupervised approach** for monocular depth estimation with CNNs. 

    - propose a data augmentation technique 
    - the augmented dataset has to be generated from already acquired images, 
    - this technique is unable to generate unseen environments.

- 본 논문은 가상 데이터를 사용하였다. 
    - 결과가 좋게 나왔다. 
    - 파인 튜닝도 불 필요하다. 

## 3. NETWORK OVERVIEW

### 3.1  Fully Convolutional Network

![](https://i.imgur.com/XZUZ4h3.png)

We propose as a** baseline method** a fully convolutional architecture, structured in a encoder-decoder fashion, as depicted in Figure 2. 

This a very popular architectural choice for several pixel-wise prediction tasks, as optical flow estimation [19] or semantic segmentation [20]. 

In our proposed network, the encoder section corresponds to the popular VGG network [21], pruned of its fully connected layers.

We initialize the encoder weights with the VGG pretrained model for image classification. Models trained on huge image classification datasets, as [22], proved to act as a great generic-purpose feature extractor [23]: low-level features are extracted by convolutional layers closer to the input layer of the net, while layers closer to the output of the net extract high-level, more task-dependent descriptors.

During training, out of the 16 convolutional layers of the VGG net, the weights of the first 8 layers are kept fixed; remaining layers are fine-tuned. 

The decoder section of the network is composed by 2 deconvolutional layers and a final convolutional layer which outputs the predicted depth at original input resolution. 

These layers are trained from scratch, using random weight initialization.

### 3.2 Adding LSTM layers into the picture

문제점 : Any monocular, single image depth estimation method suffers from the infeasibility of correctly estimating the **global scale **of the scene. 

Learning-based methods try to infer global scale from the learned proportions between depicted
objects in the training dataset. 

기존 방법의 실패 : This paradigm inevitably fails when previously unseen environments are evaluated or when
the camera focal length is modified.

제안 방법의 차별점 : We can try to correct these failures by exploiting the sequential nature of the image stream captured by a vision module mounted on a deployed robot. 

        RNN이란 : Recurrent neural networks (RNN) are typically used in tasks where long term temporal dependencies between inputs matter when it comes to performing estimation: text/speech analysis, action recognition in a video stream, person re-identification [24], [25], [26].

Their output is a function of both the current input fed into the network and the past output, so that memory is carried forward through time as the sequence progresses:

$$
y_t = f(Wx_t + Yy_{t-1})
$$
- W represents the weight matrix (as in common feedforward networks) 
- U is called transition matrix.

        LSTM이란 : Long Short Term Memory networks (LSTM) are a special kind of recurrent neural network introduced by Hochreiter & Schmidhuber in 1997 to overcome some of the RNN main issues, as vanishing gradients during training, which made them very challenging to use in practical applications [27]. 

Memory in LSTMs is maintained as a **gated cell **where information can be read, written or deleted. 

During training, the cell learns autonomously how to treat incoming and stored information. 

We insert two LSTM layers between the encoder and decoder section of the previously introduced
FCN network, in a similar fashion of [24]. 

Our motivation is to refine features extracted by the encoder according to the information stored in the LSTM cells, so that the decoder section can return a more coherent depth estimation. 

![](https://i.imgur.com/Gm3FLzj.png)

The proposed LSTM network is depicted in Image 3. 

Dropout is applied before, after and in the middle of the two LSTM layers to improve regularization during training.