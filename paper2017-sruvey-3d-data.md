|논문명|Deep Learning Advances in Computer Vision with 3D Data: A Survey
|-|-|
|저자(소속)||
|학회/년도| ACM Computing Surveys 2017, [논문](https://www.mendeley.com/viewer/?fileId=241a7816-fe42-e7ef-0a90-974189bcebfa&documentId=ca50a030-c06a-377c-812d-900466b273d3)|
|키워드||
|참고|Chpter 4|
|코드||

# Deep Learning Advances in Computer Vision with 3D Data: A Survey

## 1. INTRODUCTION

![](https://i.imgur.com/KI3Ir3N.png)

A generic pipeline for processing a 3D scene
- Scans of real scenes can contain millions of points, therefore at first, some form of preprocessing is commonly applied. 
    - Point reduction (i.e., remove redundant points in order to reduce the computational cost),
    - data structuring (i.e., organize the point cloud using data structures like kd-trees or octrees), 
    - hardware exploitation (e.g., GPU calculations) are a few of the methods proposed so far. --- Following, segmentation of the point cloud is typically performed in order to identify semantically meaningful regions. 
- After acquiring the objects of the scene from segmentation, keypoint detection and descriptors extraction are applied to every identified object or scene segment. 
- The extracted representation is subsequently utilized in order to match the scene segments with known object models 
- finally recognize or classify them into a category or even retrieve similar objects.

## 2. RELATED WORK

- 3D scene segmentation 
- 3D keypoint detection / 3D descriptor extraction 
- 3D shape retrieval / 3D object recognition 

> Deeplearning이전에 사용되던 Descriptors/Detector에 대한 연구 들인듯 (연구 년도도 2010년 전)

### 2.1 3D Scene Segmentation

- semantic segmentation/labeling 
- labeling each point of a scene as part of a foreground object of interest or of a background surface. 
- 3D object classification

3D point cloud segmentation methods into five categories `(Nguyen and Le [2013])`
- region-based
- edge-based
- attributes-based
- model-based
- graph-based methods 

### 2.2 3D keypoint detection / 3D descriptor extraction 

3D keypoint detection은 물체 인식/Retrive을 위해서 필수적인 Step 이다. 

Existing approaches `(Tombari et al. [2013])`
- Fixed-scale keypoint detectors : Identify distinctive keypoints at a constant scale given to the algorithm as an input argument
    - Local Surface Patches (LSPs) [Chen and Bhanu 2007]
    - Intrinsic Shape Signatures (ISSs) [Zhong 2009]
    - the 3D detector proposed in Mian et al. [2010] termed as “KeyPoint Quality” (KPQ) in Tombari et al. [2013]
- Adaptive-scale keypoint detectors : Identify keypoints after creating a scale space defined on the surface or alternatively after computing an embedding of the data on a 2D plane. 
    - MeshDoG [Zaharescu et al. 2009]

### 2.3. 3D Object Retrieval and Recognition

- Content-based image retrieval is a well-studied task in 2D computer vision. 

- 3D shape retrieval is one of the first problems 

Given a 3D object query, the goal is to retrieve semantically similar objects from a given database. 

Two steps are included in a typical retrieval pipeline: 
- (a) descriptors extraction from the 3D objects
- (b) matching of the queries’ descriptors with the stored descriptors of the database objects using an appropriate similarity measure. 

Existing approaches on 3D object retrieval can be divided into [Gao and Dai 2014] 
- (a)3D model-based methods , which are based mostly on low-level descriptors extraction from the 3D models, 
- (b)view-based methods , which utilize multiple 2D views of the 3D objects. 


### 2.4 4D Modeling

3D data + Time 

### 2.5. Current Trends


## 3. BACKGROUND ON DNNS

> DNN에 대한 기초 설명 -> 정리 제외 

## 4. ADVANCES IN DEEP LEARNING WITH 3D DATA


연구분야 (5개)

- 입력으로 사용할 descriptors 추출 : The first category includes methods that extract descriptors from the 3D data and give these as input to the DNN. 
- 데이터 수집 : The approaches belonging to the second category exploit RGB-D data (i.e., separate color and depth channels) captured from popular low-cost cameras like Microsoft’s Kinect. 
- 아키텍쳐 설계 : Deep architectures designed to have direct access to the 3D data form the third category. 
- The fourth category includes methods utilizing one or more 2D projections/views of the 3D object/scene captured from different viewpoints and use them to feed the employed deep model. 
- DL methods designed for data captured from hyperspectral cameras are included in the last category.

### 4.1. DL Architectures Exploiting Descriptors Extracted from 3D Data

- A common practice is to extract **low-level descriptors** and then, provide them as input to a DNN in order to get a more effective high-level representation for recognition, retrieval, or other tasks.

> 여러 가공된 Feature들이 있지만 가장 좋은건 Raw정보를 입력 하는것 아닌가? 

### 4.2. DL Architectures Exploiting RGB-D Data

A study of data fusion methods for RGB-D visual recognition can be found in Sanchez-Riera et al. [2016].

RGB-D data를 이용한 최초의 3D 물체 식별 방법은 `Socher et al. [2012]`에 의해 제안 되었다. 
- The authors proposed a combination of convolutional and recursive neural networks where color and depth channels were processed separately. 
 - At first, two single-layer CNNs were employed in order to extract low-level descriptors from the RGB and depth images. 
 - Then, each CNN’s output was forwarded to a different set of RNNs initialized with random weights. 
 - The RNN descriptors extracted from each modality were finally merged and provided to a joint softmax classifier. 
 - The proposed method demonstrated accurate performance in classifying household objects. 


Couprie et al. [2013] used a multiscale CNN for semantic segmentation of indoor RGB-D scenes.
- The network processed the input depth and RGB images at three different scales 
- the upsampled results were combined and forwarded to a classifier in order to get object class labels. 
- The final labeling of the scene was obtained by merging the classi-fier’s predictions with a superpixels segmentation of the scene performed in parallel


The possibility of using transfer learning(전이학습) between CNNs for object recognition was investigated in Alexandre [2014]. 
- The author proposed the employment of four independent CNNs for processing the four input channels of an RGB-D image. 
- The four CNNs were trained sequentially, passing the weights of a trained CNN as input to the next. 
- Experiments on 3D objects from 10 categories indicated that the proposed training strategy can boost the performance.

```
R. Socher, B. Huval, B. Bhat, C. D. Manning, and A. Y. Ng. 2012. Convolutional-recursive deep learning for 3D object classification. InAdvances in Neural Information Processing Systems 25 . 656–664.
C. Couprie, C. Farabet, L. Najman, and Y. Lecun. 2013. Indoor semantic segmentation using depth informa-tion.CoRR abs/1301.3572 (2013).
```

The task of RGB-D **object recognition** was also addressed by Eitel et al. [2015]. 
- A two-stream CNN architecture for RGB-D object recognition was designed in this work too. 
- Each stream (one for color and the other for depth) contained five convolutional and two FC layers. 
- The two streams were originally trained individually and afterward, they were fused together in a FC layer and a softmax classifier. 
- The two CNNs employed for recognition were pretrained for the task of object classification on the ImageNet dataset hence, preprocessing of the input data (especially depth) was required. 


```
A. Eitel, J. T. Springenberg, L. Spinello, M. Riedmiller, and W. Burgard. 2015. Multimodal deep learning for robust RGB-D object recognition. InIEEE/RSJ International Conference on IROS 
```


### 4.3. DL Architectures Exploiting Directly 3D Data

최근 들어 3D Geo정보를 통채로 이용하는 방법이 개발 되기 시작 하였다. 

#### A. 3D ShapeNets `Wu et al. [2015]`

- 3D shapes were provided as input (a 3D voxel grid where each voxel was a binary variable indicating whether it belonged to the 3D shape or it was empty space), while the DBN model was employed. 
- In order to diminish the huge number of parameters required from feeding a fully connected DBN with a 3D voxel volume of normal resolution, convolution with 3D filters was applied. 
- Most specifically, a Convolutional Deep Belief Network (CDBN) with five layers (three convolutional, one fully connected, and one output layer) was proposed. 
- The model was initially pretrained layerwise and afterward, fine-tuned by backpropagation. 
- Standard contrastive divergence was used for training the first four layers, but the more sophis-ticated Fast Persistent Contrastive Divergence (FPCD) was employed for training the top layer. 
- The proposed framework was tested on the tasks of 3D shape classification and retrieval, next-best view prediction, and view-based 2.5D recognition outperform-ing other state-of-the-art methods.

#### B. ModelNet 

- `ShapeNets` 저자 발표 
- large-scale 3D dataset with CAD models from 662 unique categories.

#### C. VoxNet

![](https://i.imgur.com/TJZTH2r.png)

Maturana and Scherer have also employed volumetric (i.e., spatially 3D) representation of the 3D data to perform 3D object recognition [Maturana and Scherer 2015]. 

- In the proposed VoxNet architecture, a volumetric occupancy grid of size 32×32× 32 voxels was at first generated from a point cloud’s segment that was then given as input to a CNN. 
- The employed network was constructed using two convolutional (with 3D filters), one pooling, and two FC layers, while it was trained using SGD with momentum. 
- An object class label was finally predicted for each seg-ment. 
- Data from three different domains were used for evaluating VoxNet.
    - LIDAR data point clouds
    - RGB-D point clouds
    - CAD models 

#### D. boosted VoxNet
Sedaghat et al. [2016] modified VoxNet’s architecture in such a way that the object’s orientation was taken into account. 

In their final model, the class labels were extracted directly from the orientation activations. 


```
[3D ShapeNets] Z. Wu, S. Song, A. Khosla, F. Yu, L. Zhang, X. Tang, and J. Xiao. 2015. 3D shapenets: A deep representation for volumetric shapes. InIEEE Conference on Computer Vision and Pattern Recognition . 1912–1920.
[VoxNet] D. Maturana and S. Scherer. 2015. VoxNet: A 3D convolutional neural network for real-time object recogni-tion. InIEEE/RSJ International Conference on Intelligent Robots and Systems . 922–928
[boosted VoxNet] N. Sedaghat, M. Zolfaghari, and Th. Brox. 2016. Orientation-boosted voxel nets for 3D object recognition. CoRR abs/1604.03351 (2016).
```


#### E. Convolutional AutoEncoder Extreme Learning Machine (CAE-ELM)

A new 3D descriptor learning method combining the strengths of CNNs, AEs, and ELMs

구성 요소 
- Convolutional feature map generation: 
    - in this part of the network, the 3D input data, that is, voxel and Signed Distance Field (SDF) data, were convolved with randomly generated 3D kernels and convolutional feature maps were computed. 
    - Following, average pooling was applied to the feature maps in order to maintain rotation invariance. 
- AE descriptors extraction: 
    - after pooling, each feature map was provided as input to a separate AE. 
    - All AEs were originally initialized with random weights and their final (output) weights were learned via training. 
- ELM classifier
    - in the last part of the network, all descriptors extracted from the AEs were concatenated into a vector that was used for predicting the current 3D shape’s label.

성능평가 결과 ShapeNets(Wu et al. [2015])보다 좋은 성과를 보임 



##### F. Mesh Convolutional Restricted Boltzmann Machines (MCRBMs)
learning high discriminative 3D features from 3D meshes. , Han et al. [2016] 

- The learned features were designed to preserve the structure between local regions and can be used as local or global features. 
- A novel raw representation of the local region, called Local Function Energy Distribution (LFED), was provided as input to the network. 
- In addition, Multiple MCRBMs were combined forming a deeper model, named Mesh Convolutional
Deep Belief Network (MCDBN). 


#### G. 성능 향상 제안 

Qi et al. [2016] elaborated on two factors
- The first proposed CNN included a 3D extension of the `mlpconv layers` proposed in Lin et al. [2013] 
- The second CNN initially took advantage of long anisotropic kernels to consider long-distance interactions and exploited an adapted NIN network [Lin et al. 2013]

```
C. R. Qi, H. Su, M. Niessner, A. Dai, M. Yan, and L. J. Guibas. 2016. Volumetric and multi-view CNNs for object classification on 3D data.arXiv preprint arXiv:1604.03265v2 (2016).
```



#### H. Voxception-ResNet (VRN)

> 여러 DLL 기술들을 적용하여 성능 향상 

voxel-based (i.e., fully 3D) models for shape modeling and 3D object classification

The authors took advantage of recent advancements in the field of DNNs and designed an architecture that relied on 
- (i) inception-style modules [Szegedy et al. 2016], 
- (ii) batch normalization [Ioffe and Szegedy 2015], 
- (iii) residual connections with preactivation (He et al. [2015a, 2016]) 
- (iv) stochastic network depth [Huang et al. 2016]. 

The proposed model,Voxception-ResNet (VRN), is 45 layers deep. 

It should be noted that significant data augmentation was required for training such a deep model.

```
A. Brock, Th. Lim, J. M. Ritchie, and N. Weston. 2016. Generative and discriminative voxel modeling with convolutional neural networks.CoRR abs/1608.04236 (2016).
```

#### I. Deep Sliding Shapes

A pipeline for 3D object detection and recognition in **RGB-D** scenes was presented in Song and Xiao [2016]. 


- 흥미로운 점은 depth channel을 사용하는 대신 TSDF를 이용하여 full 3D voxel grid 컨버젼 하는 방법을 채택 한것이다. `Interestingly, instead of just working on the depth channel, Song and Xiao exploited the raw 3D information of the scenes by converting each depth image to a full 3D voxel grid using a directional Truncated Signed Distance Function (TSDF). `

- A fully 3D convolutional network, called 3D Region Proposal Network (RPN), was then utilized in order to generate 3D object bounding boxes from the 3D voxel grid at two different scales so that it could handle different object sizes. 

- Objectness scores were also provided for each generated object proposal. 

- Moreover, each detected 3D proposal box and its corresponding 2D color patch (i.e., 2D projection of the 3D proposal) were fed to a 3D ConvNet and a 2D ConvNet, respectively, for jointly learning the object’s category and 3D box regression. 

### 4.4. DL Architectures Exploiting 2D Projections/Views of 3D Objects

3D를 여러개의 2D로 투영하여 활용하는것은 일종의 `트릭`으로 많이 사용되고 있다. 
`Collecting multiple 2D projections rendered from different directions in order to rep-resent a 3D shape/object is a “trick” commonly adopted for 3D shape analysis and understanding.`


#### A. 최초 도입한 논문 (2014)

In the aforementioned work, an AE was used in order to generate a global deep representation of a 3D shape for the application scenario of 3D shape retrieval. 

Pose normalization for differences in translation and scale was initially applied to each 3D model, while a set of 2D projections was subsequently collected for each of them. 

After pretraining the stacked RBMs with the projections, the AE was fine-tuned using back-propagation in order to minimize the reconstruction error. 

Finally, the hidden (code) layer was used for representing the corresponding projection/view of the 3D shape in the retrieval process. 

Since more than one code was generated for each model (one per projection), a variant of the Hausdorff distance was used to compute the distance between the final representations of two different 3D shapes. 


```
Z. Zhu, X. Wang, S. Bai, C. Yao, and X. Bai. 2014. Deep learning representation using autoencoder for 3D shape retrieval.CoRR abs/1409.7164 (2014).
```


#### B. Stacked Local Convo-lutional AutoEncoder (SLCAE) (2015)

An AE was also adopted for 3D object retrieval in Leng et al. [2015a]. 

In this method, an extension of the standard AE inspired from CNNs, called Stacked Local Convo-lutional AutoEncoder (SLCAE)

A Local Convolutional Autoencoder (LCAE) is constructed by substituting the FC layers of a standard AE with locally connected layers using the convolution operation.

In the stacked version of LCAE, many encoders were placed on top of each other and the output of the last one was used as the representation of a 3D object. 

The input provided to the proposed AE was multiple depth images of several views of the 3D object, while each layer of the architecture was trained using the gradient descent method. 



```
B. Leng, S. Guo, X. Zhang, and Z. Xiong. 2015. 3D object retrieval with stacked local convolutional autoen-coder.Signal Processing 112, C (2015), 119–128
```


#### C. 3D Convolutional Neural Network (3DCNN) (2016)

Dealing with multiple 2D views of a 3D object at the same time.
 
Each object’s views were sorted into three reasonable sequences before being fed to the network, so that the views were listed in a fixed order. 

The 3DCNN was comprised of four convolutional layers, three subsampling layers, and two FC layers. 

Convolu-tional layers were initially pretrained in the same way of training an AE. 

Afterward, the whole network was fine-tuned using backpropagation. 

The output of the first FC layer was used as the representation of the input data for the retrieval.


> 성능이 좋기는 하지만, SLCAE보다는 약함, indicates that the latter representation is probably a better choice for this task



```
B. Leng, Y. Liu, K. Yu, X. Zhang, and Z. Xiong. 2016. 3D object understanding with 3D convolutional neural networks.Information Sciences 336, C (Oct. 2016), 188–201
```


#### D. Multi-View CNN (MVCNN) (2015)

![](https://i.imgur.com/31qOwzR.png)

Multiple views of a 3D object were also exploited in the work of Su et al. [2015] in order to build a compact shape descriptor for the tasks of 3D object classification and retrieval.

In order to obtain different views of the models, two setups were tested. 
- The first setup included 12 rendered views of the 3D objects by placing an equal number of virtual cameras around them, while the second involved 80 views. 

네트워크 
- All the available views of an object passed through the first part of the network separately 
- and then, elementwise max pooling was performed across all views in the view pooling layer. 
- Finally, the aggregated result passed through the remaining network. 

For retrieval, the penultimate seventh layer of the network (which is fully connected) was used as shape descriptor. 

The employed network was pretrained using the ImageNet1K dataset and then, fine-tuned using the 3D dataset ModelNet40 [Wu et al. 2015] that was used in the experimental evaluation of the MVCNN architecture.


제안된 Shape descriptors(여러 2D)는 3D ShapeNets of Wu et al. [2015]보다 좋은 성능 보임 

```
H. Su, S. Maji, E. Kalogerakis, and E. Learned-Miller. 2015. Multi-view convolutional neural networks for 3D shape recognition. InProceedings of the International Conference on Computer Vision (ICCV’15) 
```

#### E. Pairwise Multi-View CNN (2016)

A different approach for exploiting the multiple views of a 3D object was followed by Johns et al. [2016] for the application scenario of multiview object recognition under unconstrained camera trajectories. 

In this work, the collection of views was organized in **pairs** that were provided to a CNN together with their relative pose. 

The VGG-M network [Chatfield et al. 2014] was employed in this case consisting of five convolutional and three FC layers. 

입력 : Grayscale images + depth images 

The outputs of the convolutional layers from the two images were concatenated before being provided to the first FC layer. 

> 제안 방식은 voxel-based 3D ShapeNets [Wu et al. 2015],  MVCNN보다 좋은 성능 보임 



```
E. Johns, S. Leutenegger, and A. J. Davison. 2016. Pairwise decomposition of image sequences for active multi-view recognition. InProceedings of the IEEE Conference on CVPR . 3183–3822.
```

#### F. GIFT 

A real-time 3D shape **search engine** based on 2D views of 3D objects was presented in Bai et al. [2016]. 

The proposed system exploited GPU for CNN-based feature extraction and utilized two inverted files, 
- one for accelerating the multiview matching process 
- the other for re-ranking the initial results. 

수초 이내에 retrieval process완료 가능. `The retrieval process for a query shape was reported to be completed within a second. `

```
S. Bai, X. Bai, Z. Zhou, Z. Zhang, and L. Jan Latecki. 2016. GIFT: A real-time and scalable 3D shape search engine. InIEEE Conference on Computer Vision and Pattern Recognition (CVPR) .
```

#### G. 2D view + 2D sketch (2015)

> Sketch 데이터가 필요 하므로 참고 활용 어려움 - 생략 

A different approach where 3D models were retrieved based on 2D sketches and 2D views has recently been presented in Wang et al. [2015]. More specifically, Wang et al. proposed an architecture that takes as input a {2D view + sketch} pair of an object. The model consisted of two Siamese CNNs (i.e., two identical subconvolutional networks), one for dealing with the 2D sketch of the 3D object to be retrieved and the other with the 2D view. The two subnetworks were trained separately using SGD and backpropagation. Each subnetwork contained three convolutional layers, each followed by a max-pooling layer, and one FC plus one output layer on top. Every 3D model was characterized by two randomly generated views as far as their angles differed morethan 45◦ . The proposed network was tested on three datasets and achieved the best performance.


#### H. MVD-ELM

Xie et al. [2015b] presented the Multi-View Deep Extreme Learning Machine (MVD-ELM) and tested it on the tasks of 3D shape classification and segmentation. 

Each 3D shape was represented by a collection of **20 2.5D depth** images/projections captured uniformly using a sphere centered at each object. 

The MVD-ELM model contained convolutional and pooling layers. 

The weights in each convolutional layer were shared across all views. The output weights were optimized based on the extracted feature maps. 

###### [확장버젼] FC-MVD-ELM

A Fully Convolutional extension of the proposed model (FC-MVD-ELM) was also presented for the task of 3D shape segmentation. 

This network contained only two convolutional layers without any pooling layer. 

FC-MVD-ELM was trained using the multiview depth images of the training examples. 

Then, all the predicted labels were projected back into the original 3D mesh. 

Finally, the segmentation result was smoothed using graph cuts optimization.
 
 
```
Z. Xie, K. Xu, W. Shan, L. Liu, Y. Xiong, and H. Huang. 2015b. Projective feature learning for 3D shapes with multi-view depth images.Computer Graphics Forum (Proceedings of Pacific Graphics 2015) 34, 6 (2015).
```


#### I. sphere rendering

> 비교 분석 내용 포함 : comparison of volumetric VS. multiview CNN

For the case of multiview CNNs, Qi et al. proposed `sphere rendering` 

sphere rendering is, multiresolution 3D filtering in order to exploit information from mul-tiple scales, and in combination with training data augmentation

```
C. R. Qi, H. Su, M. Niessner, A. Dai, M. Yan, and L. J. Guibas. 2016. Volumetric and multi-view CNNs for object classification on 3D data.arXiv preprint arXiv:1604.03265v2 (2016).
```

### 4.5. DL Architectures Exploiting HyperSpectral Data

![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/HyperspectralCube.jpg/300px-HyperspectralCube.jpg)
HyperSpectral Data, 인공위성등 -> 생략 

### 4.6. DL Architectures Fusing Different 3D Data Modalities


fusion of different data modalities 한 연구들 
- Doulamis and Doulamis [2012]
- Mart ́ ınez and Yannakakis [2014]
- Xu et al. [2015a]
- Zhang et al. [2016b]



```
N. Doulamis and A. Doulamis. 2012. Fast and adaptive deep fusion learning for detecting visual objects. In Proceedings of ECCV 2012. Workshops and Demonstrations . 345–354
H. P. Mart ́ ınez and G. N. Yannakakis. 2014. Deep multimodal fusion: Combining discrete events and contin-uous signals. InProceedings of the 16th International Conference on Multimodal Interaction . 34–41
Q. Xu, S. Jiang, W. Huang, F. Ye, and S. Xu. 2015a. Feature fusion based image retrieval using deep learning. Journal of Information and Computational Science 12, 6 (2015), 2361–2373.
X. Zhang, H. Zhang, Y. Zhang, Y. Yang, M. Wang, H. Luan, J. Li, and T. S. Chua. 2016b. Deep fusion of multiple semantic cues for complex event recognition.IEEE TIP 25, 3 (2016), 1033–1046
```

#### A. FusionNet

> 3D volumetric + 2D pixel, AlexNet network사용




In the work of Hegde and Zadeh [2016], a fusion of volumetric (i.e., 3D) and pixel (i.e., 2D views) representations was attempted for 3D object classification. More specifically, the authors used AlexNet network [Krizhevsky et al. 2012] for the 2D views of each 3D object, while they proposed two 3D CNNs for the volumetric data. The multiview network performed better on ModelNet40 than the volumetric ones, but the highest performance was achieved by the combination of the three different networks, namedFusionNet 

```
V. Hegde and R. Zadeh. 2016. FusionNet: 3D object classification using multiple data representations. CoRR abs/1607.05695 (2016)
```



#### B. Convolutional hypercube pyramid

In a similar vein, RGB, Depth, and Point Cloud data were combined in Zaki et al. [2016]. 

Depth maps and point cloud embedding was initially performed, while a CNN pretrained on RGB images was employed for feature extraction. A Hypercube Pyramid descriptor was proposed for representing multiscale, spatially relevant information for object and instance classification using ELMs. The extracted descriptor was fused with the activations of the pretrained network’s FC layers creating an even more compact representation. The proposed approach was compared to state-of-the-art methods on two benchmark RGB-D datasets presenting superior performance in terms of recognition accuracy


```
H. F. M. Zaki, F. Shafait, and A. Mian. 2016. Convolutional hypercube pyramid for accurate RGB-D object category and instance recognition. InIEEE ICRA . 1685–1692
```
