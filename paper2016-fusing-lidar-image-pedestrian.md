| 논문명 | Fusing LIDAR and Images for Pedestrian Detection using Convolutional Neural Networks |
| --- | --- |
| 저자\(소속\) | Joel Schlosser \(Georgia Tech\) |
| 학회/년도 | ICRA 2016, [논문](http://ieeexplore.ieee.org/abstract/document/7487370/) |
| 키워드 | KITTI, RGB + HHA, caffe |
| 참고 |  |
| 코드 |  |

# Fusing LIDAR and Images for Pedestrian Detection

1. 라이다를 Depthmap으로 변경 `We incorporate LIDAR by up-sampling the point cloud to a dense depth map`
2. 3개의 특징들을 추출 `We extracting three features representing different aspects of the 3D scene`
3. 이 특징들을 이미지의 새로운 channel로 적용 `We use those features as extra image channels`

Specifically, we leverage recent work on HHA representations, adapting the code to work on up-sampled LIDAR rather than Microsoft Kinect depth maps.

* `HHA representations가 up-sampled LIDAR data에 applicable을 보임` 

## 1. INTRODUCTION

Fusion Idea : This idea arises from the intuition that different sensor types capture `different aspects of a scene`, and that an `improved solution` would combine the strengths of each sensor type.

차별점 : we leverage the depth information to produce HHA image channels \(horizontal disparity, height above ground, and angle\) as described in \[9\]

* this representation is successful even on up-sampled LIDAR data

we show that

* 1\) using HHA features and RGB images performs better than RGB-only, even without any fine-tuning using large RGB web data
* 2\) fusing RGB and HHA achieves the strongest results if done late, but, under a parameter or computational budget, is best done at the early to middle layers of the hierarchical representation, which tend to represent midlevel features rather than low \(e.g. edges\) or high \(e.g. object class decision\) level features, 
* 3\) some of the less successful methods have the most parameters, indicating that increased classification accuracy is not simply a function of increased capacity in the neural network.

## 2. RELATED WORK

Recent papers exploring the RGB + depth data \(\[9\], \[4\]\)

```
[9] Saurabh Gupta et al. “Learning Rich Features from RGB-D Images for Object Detection and Segmentation”. In: CoRR abs/1407.5736 (2014). 
[4] Andreas Eitel et al. “Multimodal Deep Learning for Robust RGB-D Object Recognition”. In: CoRR abs/1507.06821 (2015).
```

Methods based on more traditional parts-model techniques have also explored incorporating depth information \[13\]

```
[13] Cristiano Premebida et al. “Pedestrian detection combining RGB and dense LIDAR data”. In: Intelligent Robots and Systems (IROS 2014), 2014 IEEE/RSJ International Conference on. IEEE, 2014, pp. 4112–4117.
```

본 논문의 기본 아이디어는 \[9\]에서 가져 왔다. R-CNN + HHA  
`The primary basis for our work comes from [9], which describes R-CNNs that utilize methods for assigning horizontal disparity, height, and angle (HHA) to all image pixels, providing additional channels for use in the network.`

기본 RCNN과 다른점은 본 논문은 we do not add SVM-based training을 하지 않았다.  `Unlike the publicly available R-CNN and the training procedure described in the corresponding paper [8-RCNN], we do not add SVM-based training using features learned by the CNNs.`

* 대신에 단순히 CNN을 써서 필터링 하였다. `Instead, we simply use the CNN to filter out detections by the proposal mechanism, and use the proposal’s scores as well.`

* 장점 & 단점 : This has the disadvantage of adding another parameter \(the threshold for filtering\), but has the advantage of simplifying the pipeline and not requiring an additional SVM training with multiple stages \(due to the second-stage training performed after hard negative mining \[8\]\).

In parallel with the development of this paper, \[4\] has recently incorporated fusion with depth data. However, both their depth representation and fusion methods differ from our work.

```
[4] Andreas Eitel et al. “Multimodal Deep Learning for Robust RGB-D Object Recognition”. In: CoRR abs/1507.06821 (2015).
```

We chose to retain the HHA representation described in \[9\] and focused on an exploration of fusion with this data, and have added their architecture as a comparison to the others.

```
[9] Saurabh Gupta et al. “Learning Rich Features from RGB-D Images for Object Detection and Segmentation”. In: CoRR abs/1407.5736 (2014).
```

As a result, there are many different documented approaches \(see \[1\]\) on pedestrian specific datasets such as the Caltech Pedestrian dataset.

```
[1] R. Benenson et al. “Ten Years of Pedestrian Detection,What Have We Learned?” In: ArXiv e-prints (Nov.2014). arXiv: 1411.4304
```

후보영역 추천을 위해서 DPM을 이용하였다. `The region proposal mechanism we chose to utilize for our R-CNNs is a Deformable Parts Model (DPM) proposal method [5].`

We chose this inspired by recent work that showed strong results when DPM was used on combined image and depth information.

```
[5] P. F. Felzenszwalb et al. “Object Detection with Discriminatively Trained Part Based Models”. In: IEEE Transactions on Pattern Analysis and Machine Intelligence 32.9 (2010), pp. 1627–1645.
```

Finally, we use the ADAGRAD \[3\] method of learning rate adaptation during training.

## 3. APPROACH



