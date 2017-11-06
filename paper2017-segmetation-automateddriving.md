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

###### [29]

- In[29] a deeper **deconvolution network** was developed, in which stacked deconvolution and unpooling layers are used. 

###### [ SegNet]

In Segnet [30] a similar approach was used where an encoder decoder architecture was deployed. 

The decoder network up-sampled the feature maps by keeping the maxpooling indicesfrom the corresponding encoder layer. 

###### [19]

> Finally, the work in [36][19][29][37][38][39] focused onmultiscale semantic segmentation. 

Initially in [19] the scale issue was addressed by introducing multiple rescaled versions of the image to the network. 

However with the emergence ofend-to-end learning, the skip-net architecture in [28] was usedto merge heatmaps from different resolutions. 

Since these architectures rely on downsampling the image, loss of resolution can hurt the final prediction. 

###### [39] U Net

The work in [39] proposed a u-shaped architecture network where feature maps from different initial layers are upsampled and concatenated for the next layers. 

###### [36] dilated convolutions

Another work in [36] introduced dilated convolutions, which **expanded the receptive field** without **losing resolution** based on the dilation factor. 

Thus it provided a better solution for handling multiple scales. 

###### [37- Attention model]

Finally the recent work in [37]provided a better way for handling scale. 

It uses attention models that provides a mean to focus on the most relevant features with-in the image. 

This attention model is able to learn a weighting map that weighs feature maps pixel-by-pixel from different scales.

### 2.3  Structured Models

- 이전 접근법들은 데이터 구조 정보를 활용하지 않았다. `The previous approaches in fully convolutional networks do not utilize the structure in the data. `

- 최근 연구에서는  데이터의 prior structure정보를 사용한다. Thus, recent work was directed towards using the prior structure in the data.
	- 특히 자율주행 에서는  prior structure는 세그멘테이션에 좋은 효과를 준다. `Specifically in automotive scenes prior structure can be exploited for better segmentation. `

#### A. CRF

- The commonly used model  to incorporate structure is conditional random field (CRF)[22][23][24]. 

###### [22]
In [22], CRF is used as a post processing stepafter the segmentation network. 

###### [23]
In [23], CRF is also used as post processing to a dilated convolution network to take contextual information into consideration. 

###### [24]

Finally, in [24]the mean field inference algorithm that is used within CRFformulation was formulated as a recurrent network.

#### B. RNN 

Another way to model structure is by using a recurrent neural network (RNN) to capture the long range dependencies of various regions [31]. 

It introduced a different formulation for solving the structured prediction problem. 

A Recurrent layer is used to sweep the image horizontally and vertically, which ensures the usage of contextual information for a better segmentation.

### 2.4 Spatio-Temporal Models

- 지금까지 살펴본 것들은 이미지 세그멘테이션에 관한 것이다. 최근 연구에서는 시간`(temporal )`정보를 이용한 비디오 세그멘테이션이 연구 되고 있다. ` All the discussed work was focused on still image segmentation.Recently some approaches emerged for video semantic segmentation that utilized temporal information [25][32][33][34]. `

###### [25]

In [25] introduced clockworks which are clock signals that control the learning of different layers with different rates. 

###### [32]
In [32] spatio temporal FCN is introduced by using a layer grid of Long Short term memory models(LSTMs). 



> 그러나 기존의 LSTM은 학습량만 늘어 나고 **spatial coherence**를 잘 활용하지 않는다. ` However conventional LSTMs do not utilize the spatial coherence and would end up with more parameters to learn.`

###### [33] convolutional gated recurrent networks

In a recent work [33] **convolutional gated recurrent networks** was used to learn temporal information to leverage the semantic segmentation of videos. 

The recurrent unit used in this work was convolutional which enables it to learn both spatial and temporal information with less number of parameters. 

Thus, it was easier to train and memory efficient.

###### [34]

The work in [34] **combined** the power of both **convolutional gated architectures** and **spatial transformers** for leveraging video semantic segmentation.


## 3. DEEP SEMANTIC SEGMENTATION IN AUTOMATED DRIVING

### 3.1 Problem Structure.

#### A.  Scene Structure

- 사전 정보를 활용하면 복잡한 문제를 단순화 할수 있다. `Prior information could simplify model complexity greatly. `

- 사전 정보에는 여러 종류가 있다. `There are different types of prior information that can be used. `

1. Spatial priors 
	- such as the fact that lanes lie on a ground plane, or that road segmented is mostly in the bottom half of the images. 

2. Geometric priors on the shapes of objects, 
	- for examples lanes are thick lines that are all converging into a vanishing point. 

3. Color priors 
	- such as the color of traffic lights or white lanes. 

4. Location priors,
	- for example the lane, road or buildings locations based on high definition maps or aerial maps.

#### B. Multi-camera Structure: 

- 최근 자유 주행 차는 4개 이상의 여러 카메라를 가지고 있는 경우가 흔하다. `Typically automotive systems uses a multi-camera network. Current systems have at least four cameras and it is increasing to more than ten cameras for future generation systems. `

![](https://i.imgur.com/eE9Mf1M.png)

- 위 그림은 차량에 설치된 4대의 카메라로 차량 주면을 360도 모두 커버 하고 있다Figure 2 shows sample images ofthe four cameras mounted on the car. It covers the entire 360 field of view surrounding the car. 

- The geometric structure of the four cameras and the motion of the car induces a spatio temporal structure across the four images. 

- For example, when the car is turning left, the region imaged by the front camera will be imaged by the right-mirror camera after a delay. 

- There is also similarity in the near-field road surface in all the four cameras as they belong to the same road surface.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTI0NzMzODQ2NF19
-->