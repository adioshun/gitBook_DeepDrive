| 논문명 | Unsupervised Monocular Depth Estimation with Left-Right Consistency |
| --- | --- |
| 저자\(소속\) | Clément Godard \(University College London\) |
| 학회/년도 | CVPR 2017, [논문](https://arxiv.org/abs/1609.03677) |
| 키워드 | unsupervised, Monocular |
| 데이터셋 / 모델 | KITTI |
| 참고 | [Youtube](https://www.youtube.com/watch?v=v8cpDQ22bSg), [CVPR](https://www.youtube.com/watch?v=jI1Qf7zMeIs) |
| 코드 | [TF](https://github.com/mrharicot/monodepth) |

![](https://camo.githubusercontent.com/ab4b1afc14f4ecc16bca342564d2e5c6c41ac241/687474703a2f2f76697375616c2e63732e75636c2e61632e756b2f707562732f6d6f6e6f44657074682f6d6f6e6f64657074685f7465617365722e676966)

* Get depth from a single photograph 
* self-supervision with streo data 

* 학습 기반 방식을 이용하여 하나의 이미지에서 깊이를 예측하는 방법은 좋은 결과를 보이고 있다. `Learning based methods have shown very promising results for the task of depth estimation in single images.`

* 그러나 기존 접근 방식은 많은 양의 학습 데이터가 필요한 단점이 있다. `However,most existing approaches treat depth prediction (as a supervised regression problem and as a result), require vast quantities of corresponding ground truth depth data for training.`

* 본 논문에서는 학습시 깊이 정보를 이용하지 않고 상대적으로 얻기 쉬운 **binocular stereo footage**를 사용하는 방법을 제안 한다.  `In this paper, we innovate beyond existing approaches, replacing the use of explicit depth data during training with easier-to-obtain binocular stereo footage.`

* ground truth depth data가 없어도 된다. `We propose a novel training objective that enables our convolutional neural network to learn to perform single image depth estimation, despite the absence of ground truth depth data.`

* **epipolar geometry constraints**을 이용하여서 **disparity images**를 생산 하였다. `Exploiting epipolar geometry constraints, we generate disparity images by training our network with an image reconstruction loss.`

We show that solving for image reconstruction alone results in poor quality depth images.

To overcome this problem,we propose a novel training loss that enforces consistency between the disparities produced relative to both the left and right images, leading to improved performance and robustness compared to existing approaches.

Our method produces state of the art results for monocular depth estimation on the KITTI driving dataset, even outperforming supervised methods that have been trained with ground truth depth.

## 1. Introduction

* 기존에 연구된 깊이 예측 방법은 motion,shape-from-X, binocular, multi-view stereo이다. `Fruitful approaches have relied on structure from motion,shape-from-X, binocular, and multi-view stereo.`

* 단점, 그러나 대부분의 이런 기술들은 많은 observations 이 존재 해야만 한다. `However, most of these techniques rely on the assumption that multiple observations of the scene of interest are available.`

* supervised learning을 통해 해결 가능 `To overcome this limitation,there has recently been a surge in the number of works that pose the task of monocular depth estimation as a supervised learning problem [32, 10, 36].`

* supervised learning의 동작 원리 : These methods attempt to **directly predict the depth** of each pixel in an image using models that have been **trained** offline on **large collections of ground truth depth data**.

* supervised learning의 제약 : While these methods have enjoyed great success, to date they have been **restricted** to scenes where **large image collections** and their corresponding **pixel depths** are available.

### 1.1 제안 방식

* 본 논문에서는 깊이 예측 문제를 **image reconstruction problem** 로 새롭게 바라보았다. `In this work, we take an alternative approach and treat automatic depth estimation as an image reconstruction problem during training.`

* 제안 모델은 depth data가 필요 하지 않다. 대신에 synthesize depth로 학습 된다. `Our fully convolutional model does not require any depth data, and is instead trained to synthesize depth as an intermediate.`

* It learns to predict the pixel-level correspondence between pairs of rectified stereo images that have a known camera baseline.

### 1.2 유사한 기존 연구

There are some existing methods that also address the same problem, but with several limitations.

For example they are not fully differentiable, making training suboptimal \[16\], or have image formation models that do not scale to large output resolutions \[53\].

We improve upon these methods with a novel training objective and enhanced network architecture that significantly increases the quality of our final results.

* 제안 방식 성능 : 35ms/image `Our method is fast and only takes on the order of 35 milliseconds to predict a dense depth map for a 512×256 image on a modern GPU.`

### 1.3 논문의 기여 부분

Specifically, we propose the following contributions:

* 1\) A network architecture that performs end-to-end **unsupervised monocular depth estimation** with a novel training loss that enforces left-right depth consistency inside the network.
* 2\) An evaluation of several training losses and image formation models highlighting the effectiveness of our approach.
* 3\) In addition to showing state of the art results on a challenging** driving dataset** 

## 2. Related Work

이미지에서 깊이 정보를 얻는 여러 방법들 `There is a large body of work that focuses on depth estimation from images, either using`

* pairs \[46\], 
* several overlapping images captured from different viewpoints \[14\],
* temporal sequences \[44\], or 
* assuming a fixed camera, static scene, and changing lighting \[52, 2\]. 

### 2.1 Learning-Based Stereo \(양안카메라\)

* stereo estimation algorithm의 중요한점은 첫 이미지와 두번째 이미지의 유사 정보를 계산 하는 것이다. `The vast majority of stereo estimation algorithms have a data term which computes the similarity between each pixel in the first image and every other pixel in the second image.`

* Typically the stereo pair is rectified and thus the problem of disparity \(i.e.scaled inverse depth\) estimation can be posed as a 1D search problem for each pixel.

* 최근에는 지도 학습 기반 방식이 좋은 성과를 보이고 있따. `Recently, it has been shown that instead of using hand defined similarity measures, treating the matching as a supervised learning problem and training a function to predict the correspondences produces far superior results[54, 31].`

* It has also been shown that posing this binocular correspondence search as a multi-class classification problem has advantages both in terms of quality of results and speed\[38\].

```
[54] J. Zbontar and Y. LeCun. Stereo matching by training a ˇconvolutional neural network to compare image patches. JMLR, 2016
[31] L. Ladicky, C. H ` ane, and M. Pollefeys. Learning the matching function. arXiv preprint arXiv:1502.00652, 2015.
[38] W. Luo, A. Schwing, and R. Urtasun. Efficient deep learning for stereo matching. In CVPR, 2016

```


###### \[DispNet\]

DispNet\[39\]에서는 FCN을 이용하여 두 이미지에서 correspondence field를 계산 하도록 하였다.

* Instead of just learning the matching function, Mayeret al. \[39\] introduced a fully convolutional \[47\] deep network called DispNet that directly computes the correspondence field between two images.

* At training time, they attempt to directly predict the disparity for each pixel by minimizing a regression training loss.

* DispNet has a similar architecture to their previous end-to-end deep optical flow network \[12\].

```
[39] N. Mayer, E. Ilg, P. Hausser, P. Fischer, D. Cremers, A. Dosovit-skiy, and T. Brox. A large dataset to train convolutional networks for disparity, optical flow, and scene flow estimation. In CVPR,
2016
[12] P. Fischer, A. Dosovitskiy, E. Ilg, P. Hausser, C. Hazırba ¨ s¸,V. Golkov, P. van der Smagt, D. Cremers, and T. Brox. Flownet:Learning optical flow with convolutional networks. In ICCV,2015.
```

###### \[단점\]

* 위 방식들은 많은 양의 데이터와, ground truth, 학습 시간이 필요 하다. `The above methods rely on having large amounts of accurate ground truth disparity data and stereo image pairs at training time.`

* 데이터 얻는건 어려워서 최근에는 가상 데이터를 이용하고 있다. `This type of data can be difficult to obtain for real world scenes, so these approaches typically use synthetic data for training.`

* 비록 가상 데이터가 실제와 비슷하긴 하지만, 데이터 생성을 위한 작업은 필요 하다. `Synthetic data is becoming more realistic, e.g. [15],but still requires the manual creation of new content for every new application scenario.`

### 2.2 Supervised Single Image Depth Estimation \(단안카메라\)

###### \[Saxena et al\]

* Saxena et al. \[45\] proposed a patch-based model known as Make3D that

* 동작 과정   
    1. first over-segments the input image into patches   
    2. estimates the 3D location and orientation of local planes to explain each patch.

* 특징 The predictions of the plane parameters are made using a linear model trained offline on a dataset of laser scans, and the predictions are then combined together using an MRF.

* 단점 : The disadvantage of **this** method, and **other planar based approximations**, e.g. \[22\],

  * is that they can have **difficulty modeling** thin structures and, as predictions are made **locally**, lack the global context required to generate realistic outputs. 

```
[45] A. Saxena, M. Sun, and A. Y. Ng. Make3d: Learning 3d scene structure from a single still image. PAMI, 2009.
```

###### \[Liu et al\]

* Instead of **hand-tuning** the unary and pairwiseterms, Liu et al. \[36\] use a **convolutional neural network** \(CNN\)to learn them. 

```
[36] F. Liu, C. Shen, G. Lin, and I. Reid. Learning depth from single monocular images using deep convolutional neural fields. PAMI, 2015.
```

###### \[Ladicky et al\]

* In another local approach, Ladicky et al. \[32\] incorporate semantics into their model to improve their per pixel depth estimation. 

```
[32] L. Ladicky, J. Shi, and M. Pollefeys. Pulling things out of perspective. In CVPR, 2014
```

###### \[Karsch et al\]

* Karsch et al. \[28\] attempt to produce more consistent image level predictions by copying whole depth images from a training set.

* 단점: A drawback of this approach is that it requires the **entire training set** to be available at test time.

```
[28] K. Karsch, C. Liu, and S. B. Kang. Depth transfer: Depth extraction from video using non-parametric sampling. PAMI, 2014.
```

###### \[Eigen et al.\]

* Eigen et al. \[10, 9\] showed that it was possible to produce dense pixel depth estimates using a two scale deep network trained on images and their corresponding depth values.

* Unlike most other previous work in single image depth estimation,

  * they **do not** rely on hand **crafted features** or an **initial** over segmentation and 
  * instead **learn** a **representation** directly from the raw pixel values. 

* 변종 방식들 `Several works have built upon the success of this approach using techniques such as`

  * CRFs to improve accuracy\[35\], 
  * changing the loss from regression to classification \[5\],
  * using other more robust loss functions \[33\], 
  * and incorporating strong scene priors in the case of the related problem of surface normal estimation \[50\]. 

하지만 이 방식도 학습 데이터 필요한건 마찬가지 `Again, like the previous stereo methods, these approaches rely on having high quality, pixel aligned,ground truth depth at training time.`

제안 방식은 **ground truth depth**데이터 대신에 **binocular color image**를 가지고 학습 `We too perform single depth image estimation, but train with an added binocular color image, instead of requiring ground truth depth.`

```
[9] D. Eigen and R. Fergus. Predicting depth, surface normals and semantic labels with a common multi-scale convolutional architecture. In ICCV, 2015. 2
[10] D. Eigen, C. Puhrsch, and R. Fergus. Depth map prediction from a single image using a multi-scale deep network. In NIPS, 2014.
```

### 2.3 Unsupervised Depth Estimation

* 최근들어 ground truth depth데이터 없이 학습이 가능한 방법 들이 제안 되었다. `Recently, a small number of deep network based methods for novel view synthesis and depth estimation have been proposed,which do not require ground truth depth at training time.`

###### \[Flynn et al\]

* Flynn et al. \[13\] introduced a novel **image synthesis network** called **DeepStereo** that generates new views by selecting pixels from nearby images.

* During training,

  * the relative pose of multiple cameras is used to predict the appearance of a held-out nearby image.
  * Then the most appropriate depths are selected to sample colors from the neighboring images, based on plane sweep volumes. 

* At test time,

  * image synthesis is performed on small overlapping patches. 

* As it requires several nearby posed images at test time DeepStereo is **not suitable for monocular depth** estimation.

```
[13] J. Flynn, I. Neulander, J. Philbin, and N. Snavely. Deepstereo: Learning to predict new views from the world’s imagery. In CVPR, 2016.
```

###### \[Deep3D\]

* The Deep3D network of Xie et al. \[53\] also addresses the problem of novel view synthesis,

  * where their goal is to generate the corresponding right view from an input left image \(i.e. the source image\) in the context of binocular pairs. 

* Again using an image reconstruction loss, their method produces a distribution over all the possible disparities for each pixel.

* The resulting synthesized right image pixel values are a combination of the pixels on the same scan line from the left image, weighted by the probability of each disparity.

* 단점 : 메모리 증가 `The disadvantage of their image formation model is that increasing the number of candidate disparity values greatly increases the memory consumption of the algorithm, making it difficult to scale their approach to bigger output resolutions.`

```
[53] J. Xie, R. Girshick, and A. Farhadi. Deep3d: Fully automatic 2d-to-3d video conversion with deep convolutional neural networks. In ECCV, 2016.
```

###### \[Garg et al.\]

* Closest to our model in spirit is the concurrent work of Garg et al. \[16\].

* Like Deep3D and our method, they **train** a network for monocular depth estimation using an **image reconstruction loss**.

* 문제점 : However, their image formation model is not fully differentiable.

* 해결책\(Garg et al\) : To compensate\(보상\), they perform a Taylor approximation to linearize their loss resulting in an objective that is more challenging to optimize.

* 해결책\(본 논문\) Similar to other recent work, e.g. \[43, 56, 57\], our model overcomes this problem by using bilinear sampling \[27\] to generate images, resulting in a fully \(sub-\)differentiable training loss.

```
[16] R. Garg, V. Kumar BG, and I. Reid. Unsupervised CNN for single view depth estimation: Geometry to the rescue. In ECCV, 2016.
[43] V. Patraucean, A. Handa, and R. Cipolla. Spatio-temporal video autoencoder with differentiable memory. arXiv preprint arXiv:1511.06309, 2015
[56] T. Zhou, P. Krahenb ¨ uhl, M. Aubry, Q. Huang, and A. A. Efros. ¨Learning dense correspondence via 3d-guided cycle consistency.CVPR, 2016. 
[57] T. Zhou, S. Tulsiani, W. Sun, J. Malik, and A. A. Efros. View synthesis by appearance flow. In ECCV, 2016.
```

###### \[제안 논문\]

* We propose a fully convolutional deep neural network loosely inspired by the supervised **DispNet** architecture of Mayer et al. \[39\].

* By posing monocular depth estimation as an image reconstruction problem, we can solve for the disparity field without requiring ground truth depth.

* However,only minimizing a photometric loss can result in good quality image reconstructions but poor quality depth.

* Among other terms, our fully differentiable training loss includes a left-right consistency check to improve the quality of our synthesized depth images.

* This type of consistency check is commonly used as a post-processing step in many stereo methods, e.g.\[54\], but we incorporate it directly into our network.

## 3. Method



