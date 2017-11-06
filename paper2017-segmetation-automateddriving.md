|논문명 |Deep Semantic Segmentation for Automated Driving: Taxonomy, Roadmap and Challenges |
| --- | --- |
| 저자\(소속\) | Mennatullah Siam \(\) |
| 학회/년도 | arXiv Jul 2017 ~ Aug 2017, [논문](https://arxiv.org/abs/1707.02432v2) |
| 키워드 | |
| 데이터셋(센서)/모델 | |
| 관련연구||
| 참고 | |
| 코드 | |

# Deep Semantic Segmentation for Automated Driving: Taxonomy, Roadmap and Challenges

In this paper, the semantic segmentation problem is explored from the perspective of automated driving. 

- 대부분의 세그멘테이션 알고리즘들은 **generic images**에 집중되어 있으며, **prior structure**를 활용하지 못하고 자율주행 차량을 목표로 하고 있지 않다. `Most of the current semantic segmentation algorithms are designed for generic images and do not incorporate prior structure and end goal for automated driving. `
    - 세그멘테이션 알고리즘 분류 `First,the paper begins with a generic taxonomic survey of semantic segmentation algorithms and then discusses how it fits in the context of automated driving. `
    - 정확도와 강건성 확보를 위한 **challenges **들 `Second, the particular challenges of deploying it into a safety system which needs high level of accuracy and robustness are listed. `
    - 다른 대안들 `Third, different alternatives instead of using an independent semantic segmentation module are explored. `
    - **CamVid** 데이터를 이용한 성늘 평가 `Finally, an empirical evaluation of various semantic segmentation architectures was performed on CamVid dataset interms of accuracy and speed.`


## 1. INTRODUCTION

-  시멘틱 세그멘테이션은 아래 부분에서 연구 되었다. `It has been used in `
    - robotics [1][2][3][4]
    - medical applications [5][6]
    - augmented reality [7]
    - most prominently automated driving [8][9][10][11].
    
- 자율 주행에 대한 **두가지** 패러다임 `Two main paradigms for automated driving emerged: `
    - (1)인식 기반 접근법 `The mediated perception approach `
        - 장면 인식을 통해서 얻어진 정보를 컨트롤 할때 활용 `which parses the whole scene and uses this information for the control decision increasing the complexity and the cost of the system. `
    - (2)The behavior reflex paradigm 
        - 센서정보에 반응하는 컨트롤 결정을 맵핑하는 방식 `that relies more on end-to-end learning to map direct sensory input to driving decision `
        - which is an ill-posed problem due to the many possible ambiguous decisions, such as the work in [13][14]. 

- 하지만 최근에 행동 유동성`(affordance)`지표를 이용하는 방법이 제안 되었다. ` However, in [15] an intermediate approach was suggested that learns affordance indicators for the driving scene. `
    - These indicators can then feedback on a simple controller for the final driving decision.
    
    
- 이전 연구에서는 세그멘테이션이 자율 주행에 필요한가? 아닌가?에 대한 연구가 있었다. `The previous work on automated driving pose the important question of whether the solution for automated driving need semantic segmentation module or not?`

- 세그멘티에션에 대한 이전 서베이 논문은 [16]이다. `A related survey in [16] on semantic segmentation literature is presented. `
    - 하지만 이 논문은 자율 주행의 특정 어플리게이션에 대하여 언급 하진 않았다. `However it is not addressing the specific application of automated driving. `

- 본 논문에서는 자율 주행에서 세그멘테이션의 무었이 중요한지와 대한은 무었인지 살펴 본다. `This paper addresses the question on what is the importance of semantic segmentation in automated driving and reviews alternative approaches. `

## 2. DEEP SEMANTIC SEGMENTATION TAXONOMY

![](https://i.imgur.com/YapwmuA.png)

- The literature work in semantic segmentation is categorized into four subcategories: 
    - (1) Classical Methods : reviews the classical approaches before the emergence of deep learning
    - (2) Fully Convolutional Networks : semantic segmentation using deep learning
    - (3) Structured Models : reviews the work that tries to utilize structure in the problem of semantic segmentation. 
        - Thus following the assumption that neighboring pixel labels should be coherent.
    - (4) Spatio-Temporal Models : exploits the temporal information that is present in videos.

### 2.1 Classical methods

- Few years ago, semantic segmentation was seen as a challenging problem to achieve reasonable accuracy. 

#### A. random forest classifier & conditional random fields

- The main approachesused in semantic segmentation was based on** random forest classifier** or **conditional random fields**. 

- In [17] decision forests were used, where each tree was trained on random subsetof the training data. 

- These methods implicitly cluster thepixels while explicitly classifying the patch category. 

- In [18] arandomized decision forest was also used however instead ofusing appearance based features, motion and structure featureswere used. 

- These features include surface orientation, heightabove camera, and track density where faster moving objectshave sparser tracks than static objects. 

- However, these techniquesrely on hand crafted features and perform pixel-wiseclassification independently without utilizing the structure inthe data.

#### B. conditional random fields(CRF)

- On the other hand **conditional random fields(CRF)** were proven to be a good approach for structured prediction problems.

- In [26][27] segmentation is formulated as CRF problem.

- The energy function used in CRF formulation usually contains unary potential and pairwise potential. 

- The unary potential gives a probability of whether the pixel belongs to a certain class. 

- While pairwise potential which is also referred to as smoothness term ensures label consistency among connected pixels. 

- Boosting is another method that can be used to classify pixels. 

- It is based on combining multiple weak classifiers that are based on some shape filter responses, as in [26][35]. 

- However the progress in classical methods was always bounded by the performance of the hand crafted features used. 

- But that was overcome with deep learning as will be discussed in the following sections.

### 2.2 Fully Convolutional Networks(FCN)

- There were mainly three subcategories of the work that was developed.

#### A. The first [19][20][21] used patch-wise training to yield the final classification. 

##### 가. In[19] 

- 입력 = 이미지, 처리 = Laplacian pyramid `an image is fed into a Laplacian pyramid,`
    - each scale is forwarded through a 3-stage network to extract hierarchical features and patch-wise classification is used. 

- 출력 = The output is post processed with a graph based classical segmentation method. `

##### 나. In [21]

 - 후처리 부하를 출이기 위하여 딥러닝을 이용하여 **pixel-wise classification** 실시 `a deep network was used for the final pixel-wise classification to alleviate any post processing needed. `

- However, it still utilized patch-wise training.


#### B. The second subcategory [28][29][30] was focused on end-to-end-learning of pixel-wise classification. 

- FCN이 개발 되면서 시작 되었다. `It started with the work in [28] that developed fully convolutional networks(FCN).`

- 네트워크는 히트맵을 학습하고, 이후 deconvolution 을 이용하여 업샘플링하여 조밀한 수준의 예측이 가능해진다. `The network learned heat maps that was then upsampled with-in the network using deconvolution to get dense predictions. `

- **patch-wise training**와는 다르게 이 방식은 Full 이미지를 사용하여 조밀한 예측이 가능하다. `Unlike patch-wise training methods this method uses the full image to infer dense predictions. `



In[29] a deeper deconvolution network was developed, in whichstacked deconvolution and unpooling layers are used. 

In Segnet [30] a similar approach was used where an encoder decoder architecture was deployed. 

The decoder network up-sampled the feature maps by keeping the maxpooling indicesfrom the corresponding encoder layer. 

In Figure 1 an exampleof the semantic segmentation output of segnet applied in anautomated driving setting is shown.Finally, the work in [36][19][29][37][38][39] focused onmultiscale semantic segmentation. 

Initially in [19] the scaleissue was addressed by introducing multiple rescaled versionsof the image to the network. 

However with the emergence ofend-to-end learning, the skip-net architecture in [28] was usedto merge heatmaps from different resolutions. 

Since these architecturesrely on downsampling the image, loss of resolutioncan hurt the final prediction. 

The work in [39] proposed a ushapedarchitecture network where feature maps from differentinitial layers are upsampled and concatenated for the nextlayers. 

Another work in [36] introduced dilated convolutions,which expanded the receptive field without losing resolutionbased on the dilation factor. 

Thus it provided a better solutionfor handling multiple scales. 

Finally the recent work in [37]provided a better way for handling scale. 

It uses attentionmodels that provides a mean to focus on the most relevantfeatures with-in the image. 

This attention model is able tolearn a weighting map that weighs feature maps pixel-by-pixelfrom different scales.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5OTI5NTQzMDldfQ==
-->