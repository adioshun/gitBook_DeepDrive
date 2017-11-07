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

- 위 그림은 차량에 설치된 4대의 카메라로 차량 주면을 360도 모두 커버 하고 있다. `Figure 2 shows sample images ofthe four cameras mounted on the car. It covers the entire 360 field of view surrounding the car. `

- The geometric structure of the four cameras and the motion of the car induces a spatio temporal structure across the four images. 
	- 예를 들어 차가 좌회전을 하면 전면의 카메라의 이미지는 잠시후 오른쪽 카메라의 이미지가 된다. `For example, when the car is turning left, the region imaged by the front camera will be imaged by the right-mirror camera after a delay. `

- 4대의 카메라의 도로 상태도 같은 것이다. `There is also similarity in the near-field road surface in all the four cameras as they belong to the same road surface.`

### 3.2 Dense High Definition(HD) maps

- HD maps은 물체 탐지 정확도 향상에 중요한 요소 이다. `High accuracy of Object detection is very difficult to achieve and HD maps is an important cue to improve it. `

- 두 종류의 HD maps이 있다. `There are two types of HD maps: `
	- (1) Dense Semantic Point Cloud Maps 
	- (2) Landmark based Maps. 

#### A. Dense Semantic Point Cloud Maps 

- The former is the dense version where the entire scene is **modeled by 3D point cloud** with semantics. 

> **Google** and **TomTom** adopt this strategy. 

- 이 방식은 비싸고 계산 부하가 크다. `As this is high end, it is expensive to cover the entire world and needs large memory requirements. `

- If there is good alignment, 
	- 모든 고정된 장비 들은 map에 표시 되고 `all the static objects (road, lanes, curb, traffic signs) are obtained from the map already `
	- 동적인 물체 들만 배경 제거 기법으로 얻어 낼수 있다. `and dynamic objects are obtained through background subtraction. `

-  TomTom RoadDNA[40] provides an interface to align various sensors like Lidar, Cameras, and others. 

![](blob:https://imgur.com/b1e58cec-4fc0-40b9-888a-e92fbce89e14)
```
Fig. 3: Example of High Definition (HD) map from TomTom RoadDNA 
```

- Figure 3 illustrates this where the pre-mapped semantic point cloud on the right is aligned with an image at run time with other dynamic objects. 

- They have mapped majority of European cities and their system provides an average localization error within 10 cm assuming a coarse location from GPS. 

#### B. Landmark based Maps. 

- Landmark based maps are based on **semantic objects** instead of generic **3D point clouds**. 

- 따라서, 카메라 데이터를 가지고 연구 되었다. `Thus it works primarily for camera data. `

> **Mobileye** and **HERE** follow this strategy. 

- 이 방식은 3D 포인트클라우드의 간단화된 버젼으로 물체를 2D map에 맵핑한다. `This can be viewed as a simple form of the 3D pointcloud where a subset of objects is mapped using a 2D map.`

- 이 방법은 In this method, object detection is leveraged to provide a HD map and the accuracy is improved by aggregating over several observations from different cars.

- In case of a good localization, 
	- HD maps can be treated as a dominant cue 
	-  and semantic segmentation algorithm greatly simplifies to be a refinement algorithm of priors obtained by HD maps. 

- In Figure 3, the semantic point cloud alignment provides an accurate semantic segmentation for static objects.

- Note that it does not cover distant objects like sky. 

- This would need a good confidence measure for localization accuracy,typically some kind of re-projection error is used. 

- HD maps can also be used for validation or post-processing the semantic segmentation to eliminate false positives. 

- For this, both land **markmaps** and **semantic point cloud maps** could be used.

### 3.3 Localization

- **Localization** or **depth estimation** is very critical for automated driving. 

- Having image semantics without localization is not very useful.

#### A. Depth using Structure from Motion(SFM)

- The straightforward approach to augment localization is to have a parallel independent path for computing dense depth using a standard method like structure from motion (SFM) and then augmenting the depth to localize the objects. 

- 깊이 지도는 spatial geometry 를 이해하기 위해서 계산 된다. `Dense depth is computed to understand the spatial geometry of the scene.`

- 정확한 깊이 정보는 semantic segmentation하는데 도움을 준다. `Accurate Depth should help in semantic segmentation and could be passed on as an extra channel. `

그러나 SFM방법은 노이즈가 많고, 학습의 영향을 많이 받는다. `However, SFM estimates are quite noisy and also the algorithm variations over time could affect the training of the network. `

- [18]에서는 포인트 클라우드의 노이즈를 이용하는 방법이 제안 되었다. `But in [18] some cues from the noisy point-cloud was inferred to act as features for segmentation. The cues proposed were: `
	- height above the camera, 
	- distance to the camera path, 
	- projected surface orientation, 
	- feature track density, 
	- and residual reconstruction error. 

- The work in[4] proposed a way of **jointly estimating** 
	- the **semantic segmentation** 
	- and **structure from motion** 
- in a conditional random field formulation.

#### B. LIDAR sensors

- 라이다는 깊이 정보를 제공 하지만, Dese는 이미지 만큼 좋지 않다. `LIDAR sensors provide very accurate depth estimation. However, they are not dense in the image lattice. `

- 이점 때문에 학습시 문제가 된다. `This leads to problems in learning a dense convolutional neural networks features. `

- 하지만 fuse를 통해서 세그멘테이션시 깊이 정보를 제공 할수 있다. `But it can provide a way to fuse semantic segmentation with depth information in a probabilistic framework. `

###### [41]

- In [41] the method fused 
	- a **map** built using **elastic fusion** [42] 
	- and **semantic segmentation** from convolutional neural networks termed as semantic fusion. 

- The class probabilities were maintained for each pixel in the map and updated in an incrementally Bayesian method. 

- 이 논문에서 사용된건 RGB-D카메라이지만 LiDAR도 적용 할수 있다. `The images used in this work were from RGB-D cameras, but it provided potential use of depth from LIDAR sensors. `

- Generally, this is agood research problem to be pursued as LIDAR is becoming a standard sensor for next generation automated driving systems.

```
[41] J. McCormac, A. Handa, A. Davison, and S. Leutenegger, “Semanticfusion: Dense 3d semantic mapping with convolutional neural networks,” arXiv preprint arXiv:1609.05130, 2016.
```


#### C.  Joint In-the-Network Localization

- 최근 CNN을 이용한 연구 중에서structure & camera motion을 예측하는게 있다. `There exists promising algorithms on using convolutional neural networks to estimate structure and camera motion. `

###### [43] Demon

- A recent work in [43]proposed **depth** and **motion** network for learning monocular stereo. 

-  estimating **depth** and **semantics**를 Jointly하게 학습 하는 연구로는 처음이다. `As far as the authors are aware, there is no work on jointly estimating depth and semantics with in a network. `

- This can synergize and potentially aid in the estimation of each other. 

- It can also be trained simultaneously in an end-to-end fashion. 

- This problem can be of potential future direction for further research.
 
```
[43] B. Ummenhofer, H. Zhou, J. Uhrig, N. Mayer, E. Ilg, A. Dosovitskiy, and T. Brox, “Demon: Depth and motion network for learning monocular stereo,” arXiv preprint arXiv:1612.02401, 2016.
```

## 4. CHALLENGES

### 4.1 Computational Bound in Embedded Systems

- 고성능 장비에서도 On a high end automotive platform like Nvidia Tegra X1,
	- **Enet** [44] achieves around **4 fps** 
	- the proposed algorithm in**[45]** achieves around **3 fps** at a slightly higher accuracy. 

- 위 결과는 화소도 낮은(720P )거라 최근 고해상(2 Megapixel)도 적용시 3배는 더 시간이 든다. `This benchmark is for a 720P resolution and the current generation cameras are around 2 Megapixel which will reduce the runtime by another factor of 3X. `

- 상용화 하기에는 속도가 좋지 않다. `This is clearly not acceptable for a commercial solution to handle high speed objects for highway driving. `

- 해상도를 낮추면 10fps까지 가능하지만, 이것도 빠른게 아니며, 사고 위험도 생긴다. `Reducing the resolution to VGA (640x480) bringsit close to 10 fps which is still not reasonable and reducing resolution degrades accuracy and misses small objects which might be critical. `

- 서라운딩 뷰의 경우 가메라가 최소 4대 이므로 시간이 4대 더 든다. `Additionally, for full surround view sensing at least 4 cameras need to be employed which adds in another factor of 4X. `

- 하드웨어 최적화가 진행 중이다. `However the industry is moving towards custom hardware accelerators for CNNs which will enable the possibility of doing multi-camera semantic segmentation at a higher frame rate, Nvidia Xavier for instance supports 30 teraops.`

- 네트워크 경량화도 연구 되고 있따. `There is also active research on efficient network design which will improve the performance.`

### 4.2 Need of large annotated datasets

- 딥러닝의 성공에는 이미지넷 데이터넷이 있다. 세그멘테이션은 이미지넷보다 더 많은 데이터를 요구 한다. `The real potential of deep learning was unveiled becauseof the large dataset Imagenet[46]. The functional complexity of semantic segmentation is much higher and it requires a significantly larger dataset relative to Imagenet. `

- 세그멘테이션용 데이터의 테깅하는데는 한장에 한시간이나 걸리며 소요 시간이 크다. `Annotation for semantic segmentation is time consuming, typically it can take around an hour for annotating a single image. `
	- LIDAR등의 정보를 사용하면 속도 향상을 가져 올수 있따. `It can be speeded up by the availability of other cues like LIDAR or exploiting temporal propagation and bootstrapping classifier.`

- 유명한 semantic segmentation를 위한 차량용 데이터 셋은 `The popular semantic segmentation automotive datasets are `
	- CamVid [18] 
	- cityscapes [11]. 

- 전체를 합치면 5000개 정도 되지만 상대적으로 적은 수이다. `The latter has a size of 5000 annotation frames which is relatively small. `

- 위 데이터로 학습한 모델은 다른 도시 환경이나 새로운 환경(터널)등에는 잘 동작 하지 않는다. `The algorithms trained on this dataset do not generalize well to data tested on other cities and with unseen objects like tunnels.`

- 이를 해결 하기 위해 가상 데이터도 사용 할수 있다. `To compensate for that, synthetic datasets like `
	- Synthia [9]
	- Virtual KITTI [47]
-  were created. 

- There is some literature which demonstrates that a combination produces reasonable results in small datasets. 
	- But they are still limited for a commercial deployment of an automated driving system.

- 최근의 데이터셋 `Hence there is a recent effort to build larger semantic segmentation datasets like `
	- Mapillary Vistas dataset [48] : Mapillary dataset comprises of 25,000images with 100 classes. 
	- Toronto City [49]. 

-위 데이터들은 기후 변화나 카메라에 따른 다양한 variability들을 제공한다. `It also offers large variability in terms of weather condition, camera type and geographic coverage.`

- 토론토 도시 데이터는 `Toronto City is a massive semantic segmentation, mapping and 3D reconstruction dataset covering `
	- 712 km 2 of land, 
	- 8439km of road 
	- around 400,000 buildings. 

- 주석 작업은 자동화되어 진행 된다. `The annotation is completely automated by leveraging Aerial Drone data, HDmaps, city maps and LIDARs. `

- 이후 사람이 확인 및 수정을 한다. `It is then manually verified and refined.`

### 4.3 Learning Challenges

#### A. Class imbalance

- 오브젝트간 불균형 : There is severe class imbalance due to the fact that important objects like **pedestrians** are under represented unlike **sky** and **building**. 

- 문제점 : This could also create a bias to **ignore small objects**. 

- 해결 방법 #1 : This could be handled by a **weighting scheme** in the error function. 

- 해결 방법 #2 : Another potential solution is to use **mask predictions** on detected bounding boxes of these small objects as in [50][51].


#### B. Unobserved Objects

- soft-max 분류기의 특징으로 인해 이전에 보지 못한 물체는 처리 하지 못한다. `Because the soft-max classifier is normalized to probability one, it doesn’t handle previous unseen objects. `

- 분류기는 학습된 Class 분류 중에서만 Match를 진행 한다. `The classifier matches it to one of the previously trained classes. `

- 모든 물체를 학습 시키는건 불가능 하다. `It is not possible to cover all possible objects in training phase '
	- (eg: a rare animal like Kangaroo or a rare vehicles like construction truck). 

- 해결법 : 불확실성 기반 학습 `This could be handled by measuring uncertainty of the output classification, `
	- similar to **Bayesian Segnet** [52].

#### C. Complexity of Output

- 세그멘테이션의 결과값은 여러개의 윤곽선들이다. `The output representation of semantic segmentation is a set of complex contours and can be very complex in very high textured scenes. `

- **mapping** 나 **maneuvering**등의 후처리 작업이 필요 하며 이를 통해 단순화 할수 있다. `The post processing modules like mapping or maneuvering require a much simpler representation of objects. `

This leads to a question of learning to classify this simpler representation directly instead of semantic segmentation.


#### D. Recovering individual objects: Pixel-wise Semantic segmentationproduces regions of same object and hence does notprovide individual objects in a segment. 

This might be neededfor tracking applications which tend to track objects likepedestrians individually. 

One solution is to use post processingclassifier to further sub-divide the regions but this could be directly classified instead. 

However, a recent instance levelsegmentation paradigm can segment different instances of thesame class as in [50] without the need for post processing.5) Goal Orientation: Semantic segmentation is a genericproblem and at the moment there is no goal orientation towardsthe end goal of automated driving. 

For example, there maynot be a need for accurate contour of objects or in detectingirrelevant objects like sky for end driving goal. 

This could beachieved by customizing the loss function (eg: weighting ofimportant objects) but a modular end to end system will bescalable to automatically perform it.6) Variable object complexity: A typical automotive scenehas large complexity variability with simple structures likeroad or sky and complex structures like pedestrians. 

Pedestrianshave higher complexity due to large appearance variationsand articulations. 

Thus instead of using a small complexitynetwork across the image, a variable complexity network likea cascaded CNN [53] will be more efficient.7) Corner Case Mining: As the object detection parts aretightly coupled, it is difficult to do hard negative mining and toanalyze corner cases. 

Even when the corner cases are knownconceptually, it can be hard to record video sequences forthe same. 

Synthetic sequences could be used to design suchscenarios.
<!--stackedit_data:
eyJoaXN0b3J5IjpbNTg3MDUyMzc3XX0=
-->