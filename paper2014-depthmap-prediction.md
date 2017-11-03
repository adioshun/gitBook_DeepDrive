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

There are likely several reasons why the monocular case has not yet been tackled to the same degreeas the stereo one. 

Provided accurate image correspondences, depth can be recovered deterministicallyin the stereo case [5]. 

Thus, stereo depth estimation can be reduced to developing robust imagepoint correspondences — which can often be found using local appearance features. 

By contrast,estimating depth from a single image requires the use of monocular depth cues such as line anglesand perspective, object sizes, image position, and atmospheric effects. 

Furthermore, a global viewof the scene may be needed to relate these effectively, whereas local disparity is sufficient for stereo.

Moreover, the task is inherently ambiguous, and a technically ill-posed problem: Given an image, aninfinite number of possible world scenes may have produced it. 

Of course, most of these are physicallyimplausible for real-world spaces, and thus the depth may still be predicted with considerableaccuracy. 

At least one major ambiguity remains, though: the global scale. 

Although extreme cases(such as a normal room versus a dollhouse) do not exist in the data, moderate variations in room and furniture sizes are present. 

We address this using a scale-invariant error in addition to morecommon scale-dependent errors. 

This focuses attention on the spatial relations within a scene ratherthan general scale, and is particularly apt for applications such as 3D modeling, where the model isoften rescaled during postprocessing.

In this paper we present a new approach for estimating depth from a single image. 

We directlyregress on the depth using a neural network with two components: one that first estimates the globalstructure of the scene, then a second that refines it using local information. 

The network is trainedusing a loss that explicitly accounts for depth relations between pixel locations, in addition to pointwiseerror. 

Our system achieves state-of-the art estimation rates on NYU Depth and KITTI, as wellas improved qualitative outputs.


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTc4NDAyNTk2Ml19
-->