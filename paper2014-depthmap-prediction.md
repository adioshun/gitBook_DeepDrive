|논문명 |Depth Map Prediction from a Single Image using a Multi-Scale Deep Network |
| --- | --- |
| 저자\(소속\) | David Eigen\(New York University\) |
| 학회/년도 | NIPS 2014, IROS 2015, [논문](https://arxiv.org/abs/1406.2283) |
| 키워드 | Eigen2014a|
| 데이터셋(센서)/모델 |KITTI, NYU Depth |
| 관련연구| [이후연구(Eigen2015)](http://www.cs.nyu.edu/~deigen/dnl/)|
| 참고 |[홈페이지](https://www.cs.nyu.edu/~deigen/depth/) |
| 코드 |[TF](https://github.com/MasazI/cnn_depth_tensorflow), [유사코드Caffe](https://github.com/ayanc/mdepth) |

# DMP-MSnet

- 깊이 예측은 중요하다. `Predicting depth is an essential component in understanding the 3D geometry of a scene. `

- 양안비젼의 local correspondence은 예측에 충분한 방면 `While for stereo images local correspondence suffices for estimation, `

- 단안 비젼은 global and local information을 모두 통합 하여야 하기에 어렵다. `finding depth relations from a single image is less straightforward, requiring integration of both global and local information from various cues. `
	Moreover, the task is inherently ambiguous, with a large source of uncertainty coming from the overall scale. 

- 본 논문은 2개의 네트워크를 통해 이 문제를 해결 하였다. `In this paper, we present a new method that addresses this task by employing two deep network stacks: `
	- one that makes a **coarse global prediction** based on the entire image
	- another that **refines this prediction locally**. 

- We also apply a **scale-invariant error** to help **measure depth relations** rather than scale. 

- By leveraging the raw datasets as large sources of training data, our method achieves state-of-the-art results on both NYU Depth and KITTI, and matches detailed depth boundaries without the need for superpixelation.

## 1. Introduction

- 양안비젼 기반은 연구가 많지만, 단안비젼 기반은 별로 없다. `While there is much prior work on estimating depth based on stereo images or motion [17], there has been relatively little on estimating depth from a single image. `
```
[17] D. Scharstein and R. Szeliski. A taxonomy and evaluation of dense two-frame stereo correspondence algorithms. IJCV, 47:7–42, 2002.
```

### 1.1 양안 기반 방식이 쉬운 이유 

- Provided accurate image correspondences, depth can be recovered deterministicallyin the stereo case [5]. 

- Thus, stereo depth estimation can be reduced to developing robust imagepoint correspondences — which can often be found using local appearance features. 

### 1.2 단안 기반 방식이 어려운 이유 

- 하나의 이미지에서 깊이를 측정하려면 아래와 같은 depth cues이 필요 하다. `By contrast, estimating depth from a single image requires the use of monocular depth cues such as `
	- line angles and perspective
	- object sizes
	- image position
	- atmospheric effects. 

- 또한, Furthermore, a **global view** of the scene may be **needed** to relate these effectively, 
	- where as local disparity is sufficient for stereo.

- 더구나, Moreover, the task is inherently **ambiguous**, and a technically **ill-posed problem**: Given an image, an infinite number of possible world scenes may have produced it. 

- Of course, most of these are physically implausible for real-world spaces, and thus the depth may still be predicted with considerable accuracy. 

- At least one major ambiguity remains, though: the global scale. 

Although extreme cases(such as a normal room versus a dollhouse) do not exist in the data, moderate variations in room and furniture sizes are present. 

We address this using a scale-invariant error in addition to more common scale-dependent errors. 

This focuses attention on the spatial relations within a scene ratherthan general scale, and is particularly apt for applications such as 3D modeling, where the model is often rescaled during post processing.

### 1. 3 제안 방식 

- We directly regress on the depth using a neural network with two components: 
	- one that first estimates the global structure of the scene, 
	- a second that refines it using local information. 

- The network is trained using a **loss** that explicitly accounts for **depth relations between pixel locations**, in addition to pointwise error. 

## 2. Related Work

## 3. Approach

### 3.1 Model Architecture

- Our network is made of two component stacks, shown in Fig. 1. 
	- A **coarse-scale network** first predicts the depth of the scene at a global level. 
	- This is then refined within local regions by a **fine-scale network**. 

- 두 네트워크에 하나의 이미지가 모두 입력 된다. 첫번째 네트워크 결과는  first-layer image features로써  두번째 네트워크에 입력으로 사용된다. `Both stacks are applied to the original input, but in addition, the coarse network’s output is passed to the fine network as additional first-layer image features. `
	- In this way, the local network can edit the global prediction to incorporate finer-scale details.

#### A. Global Coarse-Scale Network


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0NTE5NzU0NDZdfQ==
-->