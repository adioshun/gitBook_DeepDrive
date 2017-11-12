| 논문명 | Efficient Deep Learning for Stereo Matching |
| --- | --- |
| 저자\(소속\) | Wenjie Luo \(\toronto Uni.\) |
| 학회/년도 | CVPPR2016, [논문](http://ieeexplore.ieee.org/document/7780983/) |
| 키워드 | Luo2016, |
| 데이터셋\(센서\)/모델 | KITTI |
| 관련연구 | Stereo Matching by Training a Convolutional Neural Network to Compare Image Patches [2015](https://arxiv.org/abs/1510.05970), [code](https://github.com/jzbontar/mc-cnn) |
| 참고 | [홈페이지](http://www.cs.toronto.edu/deepLowLevelVision/), [CVPR2016](https://www.youtube.com/watch?v=EEqCf_eno5c), [KITTI\_LB](http://www.cvlibs.net/datasets/kitti/eval_scene_flow_detail.php?benchmark=stereo&result=b54624a9eed52b4c8e6c76b411179dce4bd7d4d8) |
| 코드 | [Code](https://bitbucket.org/saakuraa/cvpr16_stereo_public/src) |

# DL4SM

* 기존 분단위 소요 시간을 초단위로 줄임 
* We train our network by treating the problem as **multi-class classification**, where the classes are all possible **disparities**

## 1. Introducion

* stereo 기반 깊이 증정의 챌린지들   
    -Dealing with cclusions,

  * large saturated areas and 
  * repetitive patterns

* 기존 접근 방법들 `Many approaches have been developed that try to aggregate information from local matches.`

  * Cost aggregation, 
    * for example, averages disparity estimates in a local neighborhood.
    * Similarly, semi-global block matching and Markov random field based methods combine pixelwise predictions and local smoothness into an energy function. 

* 기존 방법의 cost functions 문제점 `However all these approaches employ cost functions that are`

  * hand crafted, 
  * where only a linear combination of features is learned from data.

## 1.1 최근 CNN기반 방법들

* 최근 CNN을 이용하여 `learn how to match for the task of stereo estimation`\[30, 28\]. 

```
[30] J. Zbontar and Y. LeCun. Stereo matching by training a convolutional neural network to compare image patches. arXiv preprint arXiv:1510.05970, 2015. 
[28] S. Zagoruyko and N. Komodakis. Learning to compare image patches via convolutional neural networks. In CVPR,2015
```

* 최근 CNN기반 연구는 이진 분류 문제 푸는 방식을 이용하여 네트워크 파라미터를 학습하게 한다. `Current approaches learn the parameters of the matching network by treating the problem as binary classification;`

  * 외쪽 이미지 Patch에서 오른쪽 이미지 patch 예측 `Given a patch in the left image, the task is to predict if a patch in the right image is the correct match.`

* \[29-Zbontar2015\]가 좋은 성능을 보이지만 예측시 **분단위** 시간 필요 `While [29] showed great performance in challenging benchmarks such as KITTI [11], it is computationally very expensive,requiring a minute of computation in the GPU.`

  * 이유는 siamese architecture를 사용해서 이다. `This is due to the fact that they exploited a siamese architecture followed by concatenation and further processing via a few more layers to compute the final score`

```
[29-Zbontar2015] J. Zbontar and Y. LeCun. Computing the stereo matching cost with a convolutional neural network. In CVPR, 2015
```

## 1.2 제안하는 CNN기반 방법

* 제안 방식은 **초단위** 예측 가능 `In contrast, in this paper we propose a matching network which is able to produce very accurate results in less than a second of GPU computation.`

* 초단위 예측을 위해 Towards this goal,

  * we exploit a **product layer** which simply computes the **inner product** between the two representations of a siamese architecture.

* We train our network by treating the problem as **multi-class classification**, where the classes are all possible disparities.

  * This allows us to get **calibrated scores**, which result in much better matching performance when compared to \[29\]. 

![](https://i.imgur.com/wMokNMJ.png)

```
Figure 1: To learn informative image patch representations we employ a siamese network which extracts marginal distributions over all possible disparities for each pixel.
```

* KITTI이용 성능 평가  We demonstrate the effectiveness of our approach on the challenging KITTI benchmark and show competitive results when exploiting smoothing techniques.

* 코드 다운로드 : Our code and datacan be fond online at:[http://www.cs.toronto.edu/deepLowLevelVision](http://www.cs.toronto.edu/deepLowLevelVision).

## 2. Related Work

### 2.1 tune the hyper-parameters

* 초반기 학습 기반 방식들은 initially computed matching cost 보정에 초점을 맞추었다. `Early learning based approaches focused on correcting an initially computed matching cost [16, 17].`

```
[16] D. Kong and H. Tao. A method for learning matching errors for stereo computation. In BMVC, 2004. 
[17] D. Kong and H. Tao. Stereo matching via learning multiple experts behaviors. In BMVC, 2006
```

* 이후 파라미터 보정을 위한 학습도 진행 되었되다. `Learning has been also utilized to tune the hyper-parameters of the energy-minimization task.`
  * Among the first to train these hyper-parameters were \[31, 21, 19\], which investigated different forms of probabilistic graphical models.

### 2.2 Slanted plane models

* Slanted plane models model groups of pixels with slanted 3D planes.

* **강건함**이 주 목적이어서 **자율주행차**에 많이 사용된 `They are very competitive in autonomous driving scenarios, where robustness is key.`

* They have a long history, dating back to \[2\] and were shown to be very successful on the Middleburry benchmark \[22, 15,3, 24\] as well as on KITTI \[25, 26, 27\].

```
[2] S. Birchfield and C. Tomasi. Multiway cut for stereo and motion with slanted surfaces. In CVPR, 1999. 
[25] K. Yamaguchi, T. Hazan, D. McAllester, and R. Urtasun. Continuous markov random fields for robust stereo estimation. In ECCV, 2012. 
[26] K. Yamaguchi, D. McAllester, and R. Urtasun. Robust monocular epipolar flow estimation. In CVPR, 2013. 2, 
[27] K. Yamaguchi, D. McAllester, and R. Urtasun. Efficient joint segmentation, occlusion labeling, stereo and flow estimation. In ECCV. 2014.
```

### 2.3 Holistic models

* Holistic models which solve jointly many tasks have also been explored.

* 장점 : many tasks in **low-level** and **high level-vision** are related, and thus one can benefit from solving them together.

* For example\[5-2010, 6-2011, 4-2012, 18-2014, 13-2015\] jointly solved for stereo and semantic segmentation.

* Guney and Geiger \[12\] investigated the utility of high-level vision tasks such as object recognition and semantic segmentation for stereo matching.

```
[12] F. Guney and A. Geiger. Displets: Resolving stereo ambiguities using object knowledge. In CVPR, 2015.
```

### 2.4 Estimating the confidence

* 각 match의 **신뢰도**를 측정하는것은 중요한 요소이다. `Estimating the confidence of each match is key when employing stereo estimates as a part of a pipeline.`

* 학습 기반 신뢰도 측정 방법 `Learning methods were successfully applied to this task, e.g.,`

  * by combining several confidence measures via a random forest classifier \[14\], 
  * by incorporating random forest predictions into a Markov random field \[23\].

```
[14] R. Haeusler, R. Nair, and D. Kondermann. Ensemble learning for confidence measures in stereo vision. In CVPR, 2013
[23] A. Spyropoulos, N. Komodakis, and P. Mordohai. Learning to detect ground control points for improving the accuracy of stereo matching. In CVPR, 2014.
```

### 2.5 Zbontar2015

* CNN은 high-level에 좋은 성능을 보였으며 최근에는 low-level에도 좋은 성능 보임 `Convolutional neural networks(CNN) have been shown to perform very well on`
  * **high-level vision** tasks such as `image classification`, `object detection` and `semantic segmentation`
  * **low-level vision** tasks such as `optical flow prediction` \[10\]. 

```
[10] P. Fischer, A. Dosovitskiy, E. Ilg, P. Hausser, C. Hazirbas ¨ and V. Golkov. FlowNet: Learning Optical Flow with Convolutional Networks. In ICCV, 2015.
```

* 기존 연구 : In the context of **stereo estimation**, \[29-Zbontar2015\] utilize CNN to **compute the matching cost** between two image patches.

  * they used a `siamese network` which takes the **same sized left and right image** patches with a few fully-connected layers on top to predict the matching cost. 
  * They trained the model to minimize a binary cross-entropy loss. 

* 유사 연구 `In similar spirit to [29],`

  * \[28\] investigated different CNN based architectures for comparing image patches. 
  * They found concatenating left and right image patches as different channels works best, at the cost of being very slow.

```
[29-Zbontar2015] J. Zbontar and Y. LeCun. Computing the stereo matching cost with a convolutional neural network. In CVPR, 2015
[28] S. Zagoruyko and N. Komodakis. Learning to compare image patches via convolutional neural networks. In CVPR, 2015.
```

### 2.6 제안 방식과의 다른점

Our work is most similar to \[29, 28\] with two main differences.

###### \[First\]

* we propose to learn a probability distribution over all disparity values using a smooth target distribution.

* As a consequence we are able to capture correlations between the different disparities implicitly.

* This contrasts a \[29\] which performs independent binary predictions on image patches.

###### \[Second\]

* on top of the convolution layers we use a simple dot-product layer to join the two branches of the network.

* This allows us to do a orders of magnitude **faster** computation.

> 저자의 다른 연구 \[30, 7\]도 dot-product layer를 사용 `We note that in concurrent work unpublished at the time of submission of our paper [30, 7] also introduced a dot-product layer.`

```
[30] J. Zbontar and Y. LeCun. Stereo matching by training a convolutional neural network to compare image patches. arXiv preprint arXiv:1510.05970, 2015
[7] Z. Chen, X. Sun, L. Wang, Y. Yu, and C. Huang. A deep visual correspondence embedding model for stereo matching costs. In ICCV, 2015
```



