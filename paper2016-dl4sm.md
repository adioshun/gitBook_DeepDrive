|논문명 | Efficient Deep Learning for Stereo Matching |
| --- | --- |
| 저자\(소속\) | Wenjie Luo \(\toronto Uni.) |
| 학회/년도 | CVPPR2016, [논문](http://ieeexplore.ieee.org/document/7780983/) |
| 키워드 | |
| 데이터셋(센서)/모델 | KITTI |
| 관련연구|Stereo Matching by Training a Convolutional Neural Network to Compare Image Patches [2015](https://arxiv.org/abs/1510.05970), [code](https://github.com/jzbontar/mc-cnn)|
| 참고 |[홈페이지](http://www.cs.toronto.edu/deepLowLevelVision/), [CVPR2016](https://www.youtube.com/watch?v=EEqCf_eno5c), [KITTI_LB](http://www.cvlibs.net/datasets/kitti/eval_scene_flow_detail.php?benchmark=stereo&result=b54624a9eed52b4c8e6c76b411179dce4bd7d4d8) |
| 코드 |[Code](https://bitbucket.org/saakuraa/cvpr16_stereo_public/src) |



# DL4SM

- 기존 분단위 소요 시간을 초단위로 줄임 
- We train our network by treating the problem as **multi-class classification**, where the classes are all possible **disparities**

## 1. Introducion

- stereo 기반 깊이 증정의 챌린지들 
    -Dealing with cclusions, 
    - large saturated areas and 
    - repetitive patterns

- 기존 접근 방법들 `Many approaches have been developed that try to aggregate information from local matches.` 
    - Cost aggregation, 
        - for example, averages disparity estimates in a local neighborhood.
        - Similarly, semi-global block matching and Markov random field based methods combine pixelwise predictions and local smoothness into an energy function. 
        
- 기존 방법의 cost functions 문제점 `However all these approaches employ cost functions that are` 
    - hand crafted, 
    - where only a linear combination of features is learned from data.
  

## 1.1 최근 CNN기반 방법들 
        
- 최근 CNN을 이용하여 `learn how to match for the task of stereo estimation`[30, 28]. 

```
[30] J. Zbontar and Y. LeCun. Stereo matching by training a convolutional neural network to compare image patches. arXiv preprint arXiv:1510.05970, 2015. 
[28] S. Zagoruyko and N. Komodakis. Learning to compare image patches via convolutional neural networks. In CVPR,2015
```

- 최근 CNN기반 연구는 이진 분류 문제 푸는 방식을 이용하여 네트워크 파라미터를 학습하게 한다. `Current approaches learn the parameters of the matching network by treating the problem as binary classification; `
    - 외쪽 이미지 Patch에서 오른쪽 이미지 patch 예측 `Given a patch in the left image, the task is to predict if a patch in the right image is the correct match.`

- [29-Zbontar2015]가 좋은 성능을 보이지만 예측시 **분단위** 시간 필요 `While [29] showed great performance in challenging benchmarks such as KITTI [11], it is computationally very expensive,requiring a minute of computation in the GPU. `
    - 이유는 siamese architecture를 사용해서 이다. `This is due to the fact that they exploited a siamese architecture followed by concatenation and further processing via a few more layers to compute the final score`
    
```
[29-Zbontar2015] J. Zbontar and Y. LeCun. Computing the stereo matching cost with a convolutional neural network. In CVPR, 2015
```
    
## 1.2 제안하는 CNN기반 방법 

- 제안 방식은 **초단위** 예측 가능 `In contrast, in this paper we propose a matching network which is able to produce very accurate results in less than a second of GPU computation. `

- 초단위 예측을 위해 Towards this goal, 
    - we exploit a **product layer** which simply computes the **inner product** between the two representations of a siamese architecture.

- We train our network by treating the problem as **multi-class classification**, where the classes are all possible disparities.
    - This allows us to get **calibrated scores**, which result in much better matching performance when compared to [29]. 


![](https://i.imgur.com/wMokNMJ.png)
```
Figure 1: To learn informative image patch representations we employ a siamese network which extracts marginal distributions over all possible disparities for each pixel.
```

- KITTI이용 성능 평가  We demonstrate the effectiveness of our approach on the challenging KITTI benchmark and show competitive results when exploiting smoothing techniques. 

- 코드 다운로드 : Our code and datacan be fond online at:http://www.cs.toronto.edu/deepLowLevelVision.

## 2. Related Work

Over the past decades many stereo algorithms have beendeveloped. 

Since a discussion of all existing approacheswould exceed the scope of this paper, we restrict ourselvesmostly to a subset of recent methods that exploit learningand can mostly be formulated as energy minimization.Early learning based approaches focused on correctingan initially computed matching cost [16, 17]. 

Learninghas been also utilized to tune the hyper-parameters of theenergy-minimization task. 

Among the first to train thesehyper-parameters were [31, 21, 19], which investigated differentforms of probabilistic graphical models.Slanted plane models model groups of pixels withslanted 3D planes. 

They are very competitive in autonomousdriving scenarios, where robustness is key. 

Theyhave a long history, dating back to [2] and were shown tobe very successful on the Middleburry benchmark [22, 15,3, 24] as well as on KITTI [25, 26, 27].Holistic models which solve jointly many tasks havealso been explored. 

The advantage being that many tasksin low-level and high level-vision are related, and thusone can benefit from solving them together. 

For example[5, 6, 4, 18, 13] jointly solved for stereo and semantic segmentation.Guney and Geiger [12] investigated the utilityof high-level vision tasks such as object recognition and semanticsegmentation for stereo matching.Estimating the confidence of each match is key whenemploying stereo estimates as a part of a pipeline. 

Learningmethods were successfully applied to this task, e.g., bycombining several confidence measures via a random forestclassifier [14], or by incorporating random forest predictionsinto a Markov random field [23].Convolutional neural networks(CNN) have been shownto perform very well on high-level vision tasks such as imageclassification, object detection and semantic segmentation.More recently, CNNs have been applied to low-levelvision tasks such as optical flow prediction [10]. 

In the contextof stereo estimation, [29] utilize CNN to compute thematching cost between two image patches. 

In particular,they used a siamese network which takes the same sizedleft and right image patches with a few fully-connected layerson top to predict the matching cost. 

They trained themodel to minimize a binary cross-entropy loss. 

In similarspirit to [29], [28] investigated different CNN based architecturesfor comparing image patches. 

They found concatenating left and right image patches as different channelsworks best, at the cost of being very slow.Our work is most similar to [29, 28] with two main differences.First, we propose to learn a probability distributionover all disparity values using a smooth target distribution.As a consequence we are able to capture correlationsbetween the different disparities implicitly. 

This contrastsa [29] which performs independent binary predictions onimage patches. 

Second, on top of the convolution layerswe use a simple dot-product layer to join the two branchesof the network. 

This allows us to do a orders of magnitudefaster computation. 

We note that in concurrent workunpublished at the time of submission of our paper [30, 7]also introduced a dot-product layer.