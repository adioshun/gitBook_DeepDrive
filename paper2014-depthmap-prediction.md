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
	- 단안 비젼은 global and local information을 모두 통합 하여야 하기에 어렵다. finding depth relations from a single image is less straightforward, requiring integration of both global and local information from various cues. 

Moreover, thetask is inherently ambiguous, with a large source of uncertainty coming from theoverall scale. 

In this paper, we present a new method that addresses this task byemploying two deep network stacks: one that makes a coarse global predictionbased on the entire image, and another that refines this prediction locally. 

We alsoapply a scale-invariant error to help measure depth relations rather than scale. 

Byleveraging the raw datasets as large sources of training data, our method achievesstate-of-the-art results on both NYU Depth and KITTI, and matches detailed depthboundaries without the need for superpixelation.

##


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ4NzY0NTI4OV19
-->