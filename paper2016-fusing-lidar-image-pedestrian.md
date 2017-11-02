| 논문명 | Fusing LIDAR and Images for Pedestrian Detection using Convolutional Neural Networks |
| --- | --- |
| 저자\(소속\) | Joel Schlosser \(Georgia Tech\) |
| 학회/년도 | ICRA 2016, [논문](http://ieeexplore.ieee.org/abstract/document/7487370/) |
| 키워드 | Joel2016,  KITTI, RGB + HHA, caffe |
| 참고 |  |
| 코드 |  |

# Fusing LIDAR and Images for Pedestrian Detection

1. 라이다를 Depthmap으로 변경 `We incorporate LIDAR by up-sampling the point cloud to a dense depth map`
2. 3개의 특징들을 추출 `We extracting three features representing different aspects of the 3D scene`
3. 이 특징들을 이미지의 새로운 channel로 적용 `We use those features as extra image channels`

Specifically, we leverage recent work on HHA representations, adapting the code to work on up-sampled LIDAR rather than Microsoft Kinect depth maps.

* `HHA representations가 up-sampled LIDAR data에 applicable을 보임` 

## 1. INTRODUCTION

- 정의 Fusion Idea : This idea arises from the intuition that different sensor types capture `different aspects of a scene`, and that an `improved solution` would combine the strengths of each sensor type.

- 차별점 : Depth정보를 HHA로 바꾸어서 적용.  we leverage the depth information to produce HHA image channels \(horizontal disparity, height above ground, and angle\) as described in \[9\]

	- this representation is successful even on up-sampled LIDAR data

- we show that

  * HHA+RGB가 파인튜닝된 RGB보다 성능이 좋다. `using HHA features and RGB images performs better than RGB-only, even without any fine-tuning using large RGB web data`
  * fusing RGB and HHA achieves the strongest results if done late, but, under a parameter or computational budget, is best done at the early to middle layers of the hierarchical representation, which tend to represent midlevel features rather than low \(e.g. edges\) or high \(e.g. object class decision\) level features, 
  * some of the less successful methods have the most parameters, indicating that increased classification accuracy is not simply a function of increased capacity in the neural network.

## 2. RELATED WORK

- Recent papers exploring the RGB + depth data \(\[9\], \[4\]\)

```
[9] Saurabh Gupta et al. “Learning Rich Features from RGB-D Images for Object Detection and Segmentation”. In: CoRR abs/1407.5736 (2014). 
[4] Andreas Eitel et al. “Multimodal Deep Learning for Robust RGB-D Object Recognition”. In: CoRR abs/1507.06821 (2015).
```

- Methods based on more traditional parts-model techniques have also explored incorporating depth information \[13\]

```
[13] Cristiano Premebida et al. “Pedestrian detection combining RGB and dense LIDAR data”. In: Intelligent Robots and Systems (IROS 2014), 2014 IEEE/RSJ International Conference on. IEEE, 2014, pp. 4112–4117.
```

- 본 논문의 기본 아이디어는 \[9\]에서 가져 왔다. R-CNN + HHA  `The primary basis for our work comes from [9], which describes R-CNNs that utilize methods for assigning horizontal disparity, height, and angle (HHA) to all image pixels, providing additional channels for use in the network.`

- 기본 RCNN과 다른점은 본 논문은 we do not add SVM-based training을 하지 않았다.  `Unlike the publicly available R-CNN and the training procedure described in the corresponding paper [8-RCNN], we do not add SVM-based training using features learned by the CNNs.`

- 대신에 단순히 CNN을 써서 필터링 하였다. `Instead, we simply use the CNN to filter out detections by the proposal mechanism, and use the proposal’s scores as well.`

- 장점 & 단점 : This has the disadvantage of adding another parameter \(the threshold for filtering\), but has the advantage of simplifying the pipeline and not requiring an additional SVM training with multiple stages \(due to the second-stage training performed after hard negative mining \[8\]\).

- In parallel with the development of this paper, \[4\] has recently incorporated fusion with depth data. 
	- However, both their depth representation and fusion methods differ from our work.

```
[4] Andreas Eitel et al. “Multimodal Deep Learning for Robust RGB-D Object Recognition”. In: CoRR abs/1507.06821 (2015).
```

- 본 논문은 HHA를 최대한 활용 하였다. `We chose to retain the HHA representation described in \[9\] and focused on an exploration of fusion with this data, and have added their architecture as a comparison to the others.`

```
[9] Saurabh Gupta et al. “Learning Rich Features from RGB-D Images for Object Detection and Segmentation”. In: CoRR abs/1407.5736 (2014).
```

- As a result, there are many different documented approaches \(see \[1\]\) on pedestrian specific datasets such as the Caltech Pedestrian dataset.

```
[1] R. Benenson et al. “Ten Years of Pedestrian Detection,What Have We Learned?” In: ArXiv e-prints (Nov.2014). arXiv: 1411.4304
```

- 후보영역 추천을 위해서 DPM을 이용하였다. `The region proposal mechanism we chose to utilize for our R-CNNs is a Deformable Parts Model (DPM) proposal method [5].`

- 최근 연구에서 DPM은 이미지와 Depth정보를 합치는데 뛰어난 성능을 보인는 것으로 나타났다. `We chose this inspired by recent work that showed strong results when DPM was used on combined image and depth information.`

```
[5] P. F. Felzenszwalb et al. “Object Detection with Discriminatively Trained Part Based Models”. In: IEEE Transactions on Pattern Analysis and Machine Intelligence 32.9 (2010), pp. 1627–1645.
```

- Finally, we use the ADAGRAD \[3\] method of learning rate adaptation during training.

## 3. APPROACH

### 3.1 Overview

- RGB와 HHA에 대하여 둘다 CNN을 학습 시켜 후보영역을 분류하게 하였다. `We train a CNN with both RGB and HHA channels to classify region proposals. `

- 후보영역은 네트워와는 별도로 추출 된다. CNN을 통해 Classification되고, rescored된다.  `Proposals are extracted independently from the network model, classified by the CNN, and finally rescored. `

- Rescoring 마지막 소프트맥스 레이어에서 사용하기 위해 필요 하다. `Rescoring is necessary because, as noted in[12], the final softmax layer of the CNN tends to produc every peaked scores which can interfere with the generation of precision-recall curves. `

- 본 논문은 SVM Score를 사용하였다. `We use the SVM scores from the proposal mechanism as the final classification score of the patch. `

- The CNN can then be seen as a kind of filtering mechanism for the region proposals.

### 3.2 Base Network Design

- **R-CNN**과 **DPM**을 활용 하였다. `The R-CNN approach from [8] is followed here, with the Deformable Parts Model (DPM; [5]) used as the mechanism for proposing regions. `

- 보행자 비율이 2-1이기 때문에 368x160 pixels를 입력으로 하였다. `Because a height-to-width ratio of approximately 2-1 is common for pedestrian regions, we chose fixed dimensions of 368x160 pixels (height x width)for the network input to minimize the amount of distortion prospective pedestrian patches undergo before classification.`


- Also, these dimensions are evenly down-sampled by the CNN, resulting in feature maps with integer dimensions at every level of the CNN. 

- The base CNN design is shown inTable I.

![](https://i.imgur.com/R6mrO5Y.png)

### 3.3 Extracting Depth Features (HHA) from LIDAR

- **HHA**를 추출 하기 위해 [9]의 알고리즘을 사용하였다. 다른점은 보통 **Stereo camera**에서 추출 하지만 우리는 **UP-sample된 LiDAR**에서 추출 했다는 것이다. `To obtain the HHA data channels, we utilize the algorithms described in [9] except we extract this from up-sampled LIDAR rather than stereo. `

```
[9] Saurabh Gupta et al. “Learning Rich Features from RGB-D Images for Object Detection and Segmentation”.
In: CoRR abs/1407.5736 (2014). 
```

- 업샘플링된 LiDAR와 DPM based image를 이용하는 방법은 [13]에서 제안 되었으며 결과가 좋다. `LIDAR-based up-sampling has been proposed for the DPM-based image and depth fusion classifier [13] (to which we compare our work), and has been shown to be effective. `
	- In that work, however, only depth maps have been used as opposed to the full HHA representation. 

```
[13] Cristiano Premebida et al. “Pedestrian detection combining RGB and dense LIDAR data”. In: Intelligent
Robots and Systems (IROS 2014), 2014 IEEE/RSJ International Conference on. IEEE, 2014
```

- 중요한것은 업샘플링된 LiDAR나 HHA는 모두 stereo보다 노이즈가 많다. `Note that both the up-sampled LIDAR and HHA representation have significantly more noise as well as much smaller image coverage than stereo. `

- 하지만, 속도는 stereo보다 빠르다. `However, these implementations can be faster since stereo computation is not required and they make use of a simpler sensor that does not need calibration. `

![](https://i.imgur.com/yKeSUm1.png)

Example HHA results can be seen in Figure 2. 

- 그림자에 가려진 보행자가 이미지 보다 HHA에서 더 잘 보이는 점을 주목 하자. `Note that the shadowed person in the original image shows up more clearly in the HHA channel data. `
	- 이런 장점 때문에 HHA를 사용한다. `This is a good example of the intuition behind how incorporating the HHA channels will improve the performance of the network.`

### 3.4  Proposal Mechanism

- As mentioned by Girshick [7], **sparser proposals** lead to **higher mAP**. 

- As such, we selected a proposal method specifically tuned to pedestrians as opposed to a general objectdetector. 

- We use the **proposals** and **SVM scores** produced by Premebida [13] but use only the RGB-based proposals forthe KITTI dataset as the input to our CNN filtering pipeline.

- We do not use their full depth-based proposals to make afair comparison to their work.

### 3.5 Fusion Architectures

- 중요한 질문은 Fuse를 어느 시점에 해야 하는가 이다. `Given this pipeline, we explore the key question: at which point in the network should the RGB and HHA data be fused for optimal results? `
	- Should it be done at the input level, 
    - afterlow-level features (edges), 
    - after mid-level features (motifs and low-level shapes), 
    - or after high-level features (objectclass decisions)? 
    
- 이 질문에 대답 하기 위하여 여러 경우에 대하여 실험 하였다. ` To answer this question, we experimented with the following fusion architectures (displayed in Figure3): `

![](https://i.imgur.com/DopPPdX.png)

- Network A: One fully six-channel (RGBHHA) network

- Network B: Two three-channel sub-networks (RGB and HHA); fused after the norm2 layer and before the conv3 layer

- Network C: Two three-channel sub-networks (RGB and HHA); fused after the relu3 layer and before the conv4 layer

- Network D: Two three-channel sub-networks (RGB and HHA); fused after the pool5 layer and before the fc6 layer

- Network E: Four sub-networks (RGB, H, H, and A); fused after the relu3 layer and before the conv4 layer

- Network F: Four sub-networks (RGB, H, H, and A); fused after the pool5 layer and before the fc6 layer 

- We refer to the network from [4] as Network G throughout

```
[4] Andreas Eitel et al. “Multimodal Deep Learning for Robust RGB-D Object Recognition”. In: CoRR abs/1507.06821 (2015). 
```


- 각 네트워크는 그림1의 Basic 네트워크를 기본으로 한다. `Each network derives from the architecture described in Table I, which is itself the network from [11-Caffe]. `

- For each sub-network, parts of the base architecture are copied and eventually fused. 

- We experimented with a spread of fusion at various levels. 

- Note that we also experimented with using a single sub-network for **HHA vs. splitting the HHA channels** into their own individual sub-networks; 
	- unlike the RGB channels, the individual channels in the HHA representationdiffer in the type of information they represent, 
    - and so it was hypothesized that learning channel-specific filters would increase performance.
    
 > learning channel-specific filters would increase performance

- 중요한 고려 요소는 각 네트워크의 파라미터 수이다. `An important consideration for each network is the numberof parameters (weights) in the network. `
	- 파라미터 수는 수행 속도에 영향을 준다. `This affects both training time as well as classification speed during deployment.`
    - 네트워크별 파라미터 수는 다음 표에 정리 되어 있다. `A comparison of the parameter counts for the different network architectures can be found in Table II.`


## 4. Experimental Design




## 5. Results

![](https://i.imgur.com/OeYqGM3.png)
```
[Fig. 5. Percent improvement in mAP in the three difficulty categories, for all conditions.]
- Note that the RGB network without pre-training performed worse than the original input proposal mechanism,
- and that there is a distinct pattern where early and late layers perform well, middle layers come next,
while intermediate ones between them do not perform as well.
```

- 파인튜닝 하는것보다 퓨젼하는게 성능이 더 좋다. `From Figure 5, it is apparent that the more successful fusion methods are able to perform quite well and improve over the proposal mechanism even without any fine-tuning.`

- NetworkD가 성능이 가장 좋고 앞단 퓨젼인 Network A, B가 그 다음이다. `Network D, in particular, is able to perform quite well across the board, although the early fusion networks (A & B) are close seconds. `

- 흥미로운 점은 Interestingly, the gain in performance between using a column per channel (e.g. 3 columns for HHA,Network C vs. E or D vs. F) does not consistently improve or decrease performance despite adding more parameters to the network. 

- [4]에서 가져온  파인튜닝이 없는 Network G가 성능이 안 좋다. ` Network G, which mirrors that in [4], performs quite poorly without any fine-tuning. `
	- 파라미터가 적어서 그런것 같다(??) `This is not surprising,given the small amount of training available. 
	- 하지만, Network D도 많은 수의 파라미터가 있는데도 성능이 좋게 나왔다. `However, note that Network D has a large number of parameters as well(though still less than G) and can do quite well without finetuning.`


- Conv레이어 이후에 퓨젼 하는게 쉽다. (fully-connected layers를 학습할 필요가 없으므로)
	- It might be that fusing after the convolution layers,`without having to train the fully-connected layers to combine the modalities`, might be easier. 

- 다르게 보면 In other words, combining the filter outputs on each modality and learning a classifier on top of those two sets of feature maps is easier than learning hidden representations for each modality alone andthen fusing the resulting hidden representations.




- While the above results provide some interesting findings, we continued our experiments by performing two additional modifications. 

- 뒷단 퓨전이 성능은 좋지만, 파라미터가 늘어나서 연산 부하가 크다. ` First, while the late fusion methods perform well they incur significant cost due to their large number of parameters. `

- The early fusion networks cannot trivially be fine-tuned (since there is a different number of channels),but the middle layers can be fine-tuned up to the fusion portion. 

- Hence, we fine-tuned Network E to see if we could get better performance while retaining the smaller number ofparameters. 

- Second, since Network G had good performancewhen fine-tuned in work that occurred in parallel with thiswork, we performed this dual-column fine-tuning where boththe RGB and depth columns were initialized with the RGB basedtraining.


## 6. Discussion and Conclusions


