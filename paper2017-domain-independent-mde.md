|논문명|Toward Domain Independence for Learning-Based Monocular Depth Estimation|
|-|-|
|저자(소속)| Michele Mancini (), J-MOD^2 저자|
|학회/년도| IEEE 2017, [논문](http://rpg.ifi.uzh.ch/docs/RAL17_Mancini.pdf)|
|키워드| 1 camera, LSTM, KITTI, synthetic datasets |
|참고|[홈페이지](http://www.sira.diei.unipg.it/supplementary/ral2016/extra.html), [Youtube](https://www.youtube.com/watch?v=UfoAkYLb-5I)|
|코드||

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

### 1.2 단안 카메라 

최근 머신러닝을 이용한 깊이측정 측정 방법이 양안 카메라 용으로 제안 되었다. ([7], [8], [9], [10], [11]). 

- 머신러닝 방식의 장점: they are able to learn scale without the use of **external metric information**, such as Inertial Measurement Unit (IMU) measurements, and are not subject to any **geometrical constraint**. 

- 머신러닝 방식의 단점 : 학습에 사용된 환경만 적용 가능하다. `On the downside, these systems rely on the quality and variety of the training set and ground truth provided, and often are not able to adapt to unseen environments`


### 1.3 Domain independence

domain independence는 중요한 도전 과제 이다. 

이전 연구[12]에서 가상의 synthetic urban dataset를 가지고 KITTI에 적용하여 좋은 성과를 보임을 확인 헀다. `In our previous work [12] we showed that training a CNN with a inexpensive generated, densely-labeled, synthetic urban dataset, achieved promising results on the KITTI dataset benchmark using RGB and optical flow inputs.`

```
[12] M. Mancini, G. Costante, P. Valigi, and T. A. Ciarfuglia, “Fast robust monocular depth estimation for obstacle detection with fully convolutional networks,” in Intelligent Robots and Systems (IROS), 2016 IEEE/RSJ International Conference on, 2016.
```

본 연구에서는 가상데이터를 이용하여 비젼 기반 깊이 측정의 **domain independence**을 가져 오는 방안을 연구 하였다. 

- 성능향상을 위해 invariant에 중요한 요소인 **optical flow**레이어를 제거 하였다. `we reduce the computational complexity of the network by removing the network dependence on optical flow, even if it often acts as a environment-invariant feature. `
- 제거로 인해 발생하는 정보 손신은 LSTM레이러를 이용하여 만외 하였다. `To balance this loss of information, we exploit the input stream sequentiality by using Long Short Term Memory (LSTM) layers, a specific form of Recurrent Neural Networks (RNNs).`

