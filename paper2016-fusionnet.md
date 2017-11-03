| 논문명 | FusionNet: 3D Object Classification Using Multiple Data Representations |
| --- | --- |
| 저자\(소속\) | Vishakh Hegde \(Standford\) |
| 학회/년도 | NIPS2016, [논문](http://3ddl.cs.princeton.edu/2016/papers/Hegde_Zadeh.pdf) |
| 키워드 | Hegde2016, 3D CAD + Image = classification |
| 데이터셋\(센서\)/모델 | ModelNet / AlexNet pre-trained on ImageNet |
| 참고 | [ppt](http://3ddl.cs.princeton.edu/2016/slides/zadeh.pdf) |
| 코드 |  |

- [FusionNet: A deep fully residual convolutional neural network for image segmentation in connectomics](https://arxiv.org/abs/1612.05360): 2016, 메디컬 데이터 

![](https://i.imgur.com/Pog63M8.png)
```
[Figure 4: FusionNet is a fusion of three different networks:]
- V-CNN I, V-CNN II and MV-CNN (which is based on AlexNet and pre-trained on ImageNet). 
- The three networks fuse at the scores layers where a linear combination of scores is taken before finding the class prediction. 
- Voxelized CAD models are used for the first two networks and 2D projections are used for latter network
```

# FusionNet

Two data representations

* Volumetric representation, where the 3D object is discretized spatially as binary voxels \(1 if the voxel is occupied and 0 otherwise. \)
* Pixel representation : where the 3D object is represented as a set of `projected 2D` pixel images

목표 : classifying 3D CAD models

성과 : Volumetric CNN \(V-CNN\) architectures 제안

## 1 Introduction

###### 3D를 위한 DNN 설계는 어렵다.

* For example, most information in RGB images is encoded as pixels and pixel intensity distribution for each color channel

* However, information of 3D models reside on the surface, unlike 2D pixel images.

* Therefore, features useful for 2D image classification might not necessarily be sufficient for 3D model classification

###### Shapenets

Volumetric representation in the form of binary voxels was shown by \[27\], to be useful for classification and retrieval of 3D models. They train their network generatively.

```
[27] Z. Wu, S. Song, A. Khosla, F. Yu, L. Zhang, X. Tang, and J. Xiao. 3d shapenets: A deep representation for volumetric shapes. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pages 1912–1920, 2015.
```

###### Voxnet

\[16\] introduced \`Voxnet, a 3D CNN for 3D point cloud data and voxelized models, which performed significantly better than\[27\].

```
[16] D. Maturana and S. Scherer. Voxnet: A 3d convolutional neural network for real-time object recognition. In Intelligent Robots and Systems (IROS), 2015 IEEE/RSJ International Conference on, pages 922–928. IEEE, 2015.
```

###### Deeppano

In \[21\], the authors suggest a new robust representation of 3D data by way of a `cylindrical panoramic projection` that is learned using a CNN.

The authors tested their panoramic representation on ModelNet datasets and outperformed typical methods when they published their work.

```
[21] B. Shi, S. Bai, Z. Zhou, and X. Bai. Deeppano: Deep panoramic representation for 3-d shape recognition. Signal Processing Letters, IEEE, 22(12):2339–2343,
2015.
```

###### Multi-view CNN

There was a significant jump in classification and retrieval performance by `simply using 2D projections of the 3D model` and using networks pre-trained on ImageNet \[4\] for classification as shown by \[24\].

A part of this significant jump in performance is due to highly efficient and data independent features learned in the pre-training stage \(on ImageNet data\), which generalize well to other 2D images.

```
[24] H. Su, S. Maji, E. Kalogerakis, and E. Learned-Miller. Multi-view convolutional neural networks for 3d shape recognition. In Proceedings of the IEEE International Conference on Computer Vision, pages 945–953, 2015.
```

###### Volumetric and multi-view cnns

However, this difference in classification performance between CNNs that use volumetric input and those that use 2D pixel input was partly bridged in a concurrent paper on Volumetric CNNs \[19\].

```
[19] C. R. Qi, H. Su, M. Nießner, A. Dai, M. Yan, and L. Guibas. Volumetric and multi-view cnns for object classification on 3d data. In Proc. Computer Vision and
Pattern Recognition (CVPR), IEEE, 2016.
```

## 2 Related Work: Shape descriptors

Depending on data representations, there has been work on shape descriptors for voxel and point cloud representations, among many others.

* data representations: used to describe these 3D models

### 2.1 과거

In the past, shapes have been represented as `histograms` or `bag of features models`  
which were constructed using surface normals and surface curvatures \[8\].

Other shape descriptors include the `Light Field Descriptor` \[3\], `Heat Kernel Signatures` \[2\] \[12\] and `SPH` \[11\].

머신러닝알고리즘 + 직접 추출한 특징 결합 : Classification of 3D objects has been proposed using `hand-crafted features` along with a machine learning classifier in \[14\], \[26\] and \[1\].

### 2.2 최근

최근 연구도 3D data를 표현하는 좀더 좋은 방법을 찾는데 초점이 맞추어져 있다.  
`However, more recently, the focus of research has also included finding better    
ways to represent 3D data.`

The creators of the Princeton ModelNet dataset have proposed a `volumetric representation` of the 3D model and a 3D Volumetric CNN to classify them \[27-Shapenet\].

More recently, they\(=2D CNN\) have also been used to perform classification and retrieval of 3D CAD models \[27-Shpaenet\] \[16-Voxnet\] \[21-Deeppano\] \[24\] \[10\] \[19\].

```
[24] H. Su, S. Maji, E. Kalogerakis, and E. Learned-Miller. Multi-view convolutional neural networks for 3d shape recognition. In Proceedings of the IEEE International Conference on Computer Vision, pages 945–953, 2015
[10] E. Johns, S. Leutenegger, and A. J. Davison. Pairwise decomposition of image sequences for active multi-view recognition. CoRR, abs/1605.08359, 2016. URL http://arxiv.org/abs/1605.08359.
[19] C. R. Qi, H. Su, M. Nießner, A. Dai, M. Yan, and L. Guibas. Volumetric and multi-view cnns for object classification on 3d data. In Proc. Computer Vision and Pattern Recognition (CVPR), IEEE, 2016.
```

CNNs not only allow for end-to-end training, it is also an automated `feature learning` method.

In particular, the distributed representation of basic features in different layers  
and different neurons means that there are a huge number of ways to aggregate this information in order to accomplish a task like classification or retrieval.

알려짐 바로는 대량의 데이터로 학습을 하게 되면 원래 속해 있지 않는 분류까지도 구분에 해낼수 있다. \(Transfer Learning\) `It is also known that the features learned by training from a large 2D RGB image dataset like ImageNet generalize well, even to images not belonging to the original set of target classes.`

이는 직접 만든 feature이 다른 영역에서는 사용할수 없는것과 비교 하면 반대 적이다. `This is in contrast to handcrafted features which do not necessarily generalize well to other domains or category of images.`

## 3. Methods

![](https://i.imgur.com/WHNmzHb.png)

Most state of the art 3D object classification algorithms are based on using Convolutional Neural Networks \(CNNs\) to discriminate between target classes \[16-Voxnet\] \[21-Deeppano\] \[24-MVCNN\] \[10\] \[19\].

Generative models on voxels have also been used for this problem \[27-3D shapenets\].

Most approaches used to solve the 3D object classification problem involves two steps namely,

* deciding a data representation to be used for the 3D object 
* training a CNN on that representation of the object. 

###### 최근 연구 트랜드 분류

Most state of the art methods

* Use `voxels` \[27\] \[16\] \[19\] 
* Use a set of `multiple 2D projections` of the polygon mesh from several camera positions \[21\] \[24\] \[10\].

#### 3.1 본 논문 제안

본 논문에서는 위 두개 모두 이용 : voxels + multiple 2D projections

* For voxel data: we use `our own neural networks` on multiple orientations of  
  all objects in the training set to learn features which are partly complementary to those learned for pixel data.

* For pixel data: we use ideas from `Multi View CNN (MV-CNN) proposed by [24]` which use **multiple projected views** of the same 3D model and aggregate them in a way which improves the performance over a single projection.

Finally in FusionNet, we combine multiple networks in the final fully connected layer which outputs class scores in a way which improves the classification accuracy over each of its component networks.

## 4 Dataset and Accuracy Measure

ModelNet 사용

## 5 Volumetric CNN \(V-CNN\)

본 논문에서 2개의 CNN을 소개 할것이다. `We introduce two CNNs for volumetric data which constructively combines information from multiple orientations by max-pooling across 60 orientations.`

This is similar to \[24\] which aggregates multiple 2D projections of a 3D polygonal mesh using a well established CNN architecture on 2D RGB images, like VGG-M \[22\].

```
[24] H. Su, S. Maji, E. Kalogerakis, and E. Learned-Miller. Multi-view convolutional neural networks for 3d shape recognition. In Proceedings of the IEEE International Conference on Computer Vision, pages 945–953, 2015.
[22] K. Simonyan and A. Zisserman. Very deep convolutional networks for large-scale image recognition. CoRR, abs/1409.1556, 2014
```

Both our networks also use long range 3D convolutions which aggregate information across a dimension of the object.

In one of the networks, we concatenate the output from kernels of various sizes, similar to the inception module used in \[25\].

```
[25] C. Szegedy, W. Liu, Y. Jia, P. Sermanet, S. E. Reed, D. Anguelov, D. Erhan, V. Vanhoucke, and A. Rabinovich. Going deeper with convolutions. CoRR, abs/1409.4842, 2014. URL http://arxiv.org/abs/1409.4842.
```

### 5.1 Data Augmentation

- ModelNet 의 데이터 양음 많지 않다. `3D Unlike large scale 2D RGB image datasets like ImageNet, there are relatively fewer number of CAD models in ModelNet benchmark datasets. `

- 결국 Volumetric CNN에 입력 값이 충분 하지 않다. `This translates to having fewer number of voxelized input which can be fed to a Volumetric CNN. This will result in features that are not as efficient as those learned for 2D images. `

- 따라서, 회전등의 방법으로 이미지 Augmentation가 필요 하다. `Therefore, it is necessary to augment training data with multiple rotations of voxelized models. `

- 수행한 여러 방법들 

```
We input multiple azimuth and polar rotations of the model to the VolumetricCNN, apart from another non-standard data augmentation method explained in 5.2.1.

We work under the assumption that all CAD models in the dataset are aligned along the gravity axis.

We produce voxels of size 30 × 30 × 30 from polygon meshes after rendering them in 60 different orientations about the gravity axis, where each rendering is defined by θ, the polar angle and φ, the azimuth angle. 

To obtain these 60 orientations, we uniformly sample 60 polar angles from [0, π] and60 azimuth angles from [0, 2π] and use each pair of polar and azimuth angles for rendering voxels.

We perform random sampling of angles to break any symmetry present along the gravity axis.Otherwise, no new information is added for objects which are symmetric about the gravity axis(for example, symmetric objects like vase and bowl). 
```

- rotational invariance 강한 장점이 된다. 
  - We hope that inputting multiple such random rotations will help the neural network learn rotational invariance, both in the polar angle space and in the azimuth angle space. 
  - This is especially important if the polygon mesh being tested on does not have the same polar angle as most meshes belonging to that class in the training set. 
  - This is also important for classifying models constructed from real world data like RGB-D and LiDAR data,where rotational invariance is necessary for good performance

### 5.2 V-CNN I

![](https://i.imgur.com/Bn0wuCZ.png)

```
[Figure 2: Network architecture of V-CNN I.]
- It has three 2D convolution layers, all with kernels of size 3 × 3 and two fully connected layers. 
- The first convolutional layer assumes the number of channels to be 30. 
- A Softmax Loss function is used while training the network.
```

#### A. 네트워크 구조 

- This Volumetric CNN consists of 
  - three 3D **convolution** layers 
  - two **fully connected** layers, 
    - where the **final fully connected** layer is used as a **classifier** as depicted in figure 2. 

- 합성곱 레이어에서 사용된 커널의 목적은 입력 OBJECT에서 Full Depth간 voxel 연관성을 찾는다. `The kernels used in the convolution layer find voxel correlations along the full depth of the object. `

- When trained on different orientations for all models, the hope is to be able to learn long range spatial correlations in the object along all directions while using sparse locally connecting kernels in order to reduce computational complexity. 

- This is difficult to achieve in 2D images where kernels only adapt to spatially local pixel distributions and depend on the kernel-size used for the convolution.

- The **ReLU layer** [17] following the convolution layer introduces non-linearity in the model necessary for class discrimination. 

- The **pooling layer** following ReLU ensures that neurons learning redundant information from a spatially local set of voxels do not contribute to the size of the model. 

- The **kernels** used in all convolution layers in this network are of size `3 × 3`. 
  - While CNNs for 2D image classifiation like AlexNet use kernels of size 11 × 11, we believe that 3 × 3 kernels are sufficient to capture correlations for voxelized data. 
  - The reason is that a single cross-section has a resolution of 30 × 30 (in comparison to a resolutions of 227 × 227 for images used in AlexNet [13]). 

- **Dropout **[23]is used to reduce any over-fitting. 

- A **fully connected layer** 
  - with 40 neurons is used as the **classifier** for ModelNet40 dataset 
  - with 10 neurons as the **classifier** for ModelNet10 dataset. 


#### B. 60번 회전 정보 사용 

- 학습시 60번 회전된 정보 사용 `We use all **60 orientations** of all objects in the training set to train the network. `

- 테스트시 During test time, these 60 orientations of each object is passed through the network till the first fully connected layer. 

- A **max-pooling layer** `aggregates` the activations from all 60 orientations before sending it to the final fully connected layer, which is our classifier. 

- 가중치는 공유되어서 모델 크기 증가 없이 성능 향상 가능 `In other words, we use weight sharing across all 60 orientations, helping us achieve better classification performance without any increase in the model size.`

#### C. Data Augmentation

- ModelNet의 데이터들은 polygon mesh형태로 저장 되어 있다. `The 3D CAD models in both ModelNet40 and ModelNet10 datasets are in the form of polygon mesh,`
  - containing **coordinates of all the vertices** in the mesh and the **ID of each node** forming a polygon. 

- invariance에 대한 학습을 위해서 vertices을 randomly displaced하게 하는 Augmentation을 하였다. `In order to help the Volumetric CNN learn invariance to small deformations, we augment the dataset with meshes whose vertices have been randomly displaced from its original position. `
  - We choose this random displacement from a centered **Gaussian distribution **with a standard deviation of 5. 
  - This standard deviation was chosen after manually inspecting several CAD model files. 

- We use this noisy dataset along with the original dataset to train V-CNN I.


### 5.3 V-CNN II

![](https://i.imgur.com/AQl16vD.png)
```
[Figure 3: Network architecture of V-CNN II.]
It has 2 inception modules. 
- The first inception module is a concatenation of three convolution outputs (of kernel sizes 1×1, 3×3, 5×5). 
  . The convolutional layers in the first inception module assumes the number of channels to be 30. '
- The second inception module is a concatenation of two convolution outputs (of kernel sizes 1 × 1 and 3 × 3). 
- Softmax loss function is used while training the network.
```

#### A. 네트워크 구조 

- GoogLeNet과 같이 본 논문도 인셉션 모둘 사용 `Inspired by the inception module in GoogLeNet [25], we use an inception module for volumetric data to concatenate outputs from filters of size 1×1, 3×3 and 5×5 as depicted in figure 3. `

> inception module in GoogLeNet : concatenates outputs from kernels of different size to capture features across **multiple scales(다양한 크기에 대한 대응)**

- 1×1 kernel은 NIN 아이디어에서 가져 온것이다. `The usage of 1×1 kernel is based on the Network in Network (NIN) [15] idea which abstracts information in the receptive field and encodes a higher representational power without much additional computational cost. `

- These voxels would otherwise have been processed directly by a convolution kernel. 

- 인셉셥 모듈은 계산 복잡도를 줄이기 위해 1 × 1 filter를 이용하지만, `While the inception module uses 1 × 1 filter before applying 3 × 3 or 5 × 5 filters in order to reduce computational complexity,` 
  - 본 논문에서는 하지 않았다. `we do no such thing since the model by itself is very small compared to many state of the art 2D image classification models. `

- 두 군곳에 인셉션 모듈 적용 : We use two such inception modules in our network, followed by a **convolution layer** and **two fully connected layers**. 

- We use **dropout** to reduce any **over-fitting**. 

- As in V-CNN I, a fully connected layer 
  - with 40 neurons is used as the classifier for ModelNet40 dataset 
  - with 10 neurons as the classifier for ModelNet10 dataset. 


- 가중치 공유함 `Similar to V-CNN I, we use weight sharing across all 60 orientations. `

- We aggregate activations from all 60 orientations of the voxelized model from the first fully connected layer using a max-pool.

#### B. Classification 

- 60개의 회전된 정보들은 두 네트워크에서 따로 학습된다. `All 60 randomly generated orientations are used to separately train both networks end to end using Caffe [9]. `

- Each of these orientations are treated as different objects while training.

- The loss function used is Softmax loss, which is a generalization of logistic loss for more than two classes. 

- The weights are updated using Stochastic Gradient Descent with momentum and weight decay. 

- During test time, the 60 views are passed through the network to obtain features from the first fully connected layer after which, a max-pooling layer pools these features across all 60 views before sending it to the final fully connected layer which performs the classification. 

###### [학습시]

- ModelNet40은 처음 부터 학습 `For ModelNet40, we train both V-CNN I and V-CNN II from **scratch**. i.e. using random weight initialization. `

- ModelNet10은 ModelNet40의 가중치 사용 `For ModelNet10 dataset we **finetune** the weights obtained after training the networks on **ModelNet40**. `

- 위 방식은 MV-CNN의 방식을 따라 한것임 `This method is similar to MV-CNN proposed in [24] which uses weights from VGG-M network pre-trained on ImageNet. `

- 위 방식은 성능상으로도 좋음 `This gives a superior performance than using random weight initialization,demonstrating the power of transferring features learned on a big dataset. `

- This also makes a case for building bigger 3D model repositories, perhaps on the scale of ImageNet.


## 6 Multi-View CNN

#### A. 네트워크 구조 

- Multi-View CNN (MV-CNN), introduced in [24] aggregates **2D projections** of the polygon mesh using a standard **VGG-M** network. 

```
[24] H. Su, S. Maji, E. Kalogerakis, and E. Learned-Miller. Multi-view convolutional neural networks for 3d shape recognition. In Proceedings of the IEEE International Conference on Computer Vision, pages 945–953, 2015.
```

- 위 방법은 ModelNet 리더 보드에서 좋은 결과를 보였다. ` This achieved state of the art classification accuracy as seen on the Princeton ModelNet leader-board. `

- MV-CNN과는 달리 Alexnet을 사용하고 20개의 View만 사용 
  - We use** AlexNet** instead of VGG-M and obtain accuracies far better than our Volumetric CNNs explained in section 5 using **only 20 views**, 
  - unlike in [24] where for each of the 20 views, the camera is rotated 0, 90, 180 and 270 degrees along the axis passing through the camera into the centroid of the object, giving 80 views per object. 

- 최근 연구인 [10-pMV-CNN]은 NBV를 예측 한다. `Recent work on Active Multi-View Recognition [10] predicts the Next Best View (NBV) `
  - which is most likely to give the highest extra information about the object, needing a smaller number of image sequences during test-time to predict the model class. 

```
[10] E. Johns, S. Leutenegger, and A. J. Davison. Pairwise decomposition of image sequences for active multi-view recognition. CoRR, abs/1605.08359, 2016. URL
http://arxiv.org/abs/1605.08359.
```

- 가중치 공유 한다. Similar to our V-CNN, we use weight sharing across all 20 viewsto keep the model size intact, while achieving a superior performance.



#### B. Classification 

- We render **multiple 2D projections** of a polygon mesh using cameras **placed on the 20 corners** of an icosahedron(20면체) and use all 20 views for training and testing. 

- 원래 데이터셋에 색정보가 없기 때문에 투영후 얻은 이미지는 Grey-scale이다. `The projections obtained are **grey-scale images** since the original polygon mesh dataset does not have any color information init. `

- We use an **AlexNet** model pre-trained on **ImageNet** before fine-tuning it for 2D projections. 

- Since the 2D projections we obtain are gray-scale, we **replicate pixel values** so that we obtain a **3-channel image** which can be used in AlexNet. 

- We use the **Softmax Loss function** for training, which is a generalization of logistic loss for multiple target classes. 

- While training the network, we used a base** learning rate** of 0.001 and a **momentum value** of 0.9. 

- One of the reasons for superior performance of Multi-View CNN compared to Volumetric CNN is that we use **transfer learning** to warm start the weights learned from ImageNet. 

- We know that weights learned in the initial layers of a neural network on one dataset generalize well to a different dataset [28]. 

- This is not true for Volumetric CNNs due to the absence of very large datasets for 3D models. 

- Since earlier layers in a CNN learn very basic features (for example, the first layer learns features similar to Gabor filter) [28] which are not specific to the dataset, we only fine-tune later fully connected layers, starting from fc6 onward in AlexNet while keeping the remaining layers frozen. 

- While **finetuning**, we consider all 20 views to bedistinct images and train AlexNet end to end. 

- While** testing**, we pass all the 20 views of a 3D object through to the second fully connected layer, fc7 . 

- At this point a **max-pool layer** finds the maxima for each neuron across all 20 views. 

- This aggregate of the 20 views are sent to fc8 for classification,similar to what was done in [24]

## 7 Experiments

![](https://i.imgur.com/9V8wW8z.png)

- V-CNN 1 + V-CNN 2 = 91.95%(ModelNet10), 83.78(MedelNet40)
- MV -CNN = 92.69(ModelNet10), 86.92$(MedelNet40)
- Fusion = 92.11%(ModelNet10), 90.80%(MedelNet40)

---

- voxels + multiple 2D projections

- 3D volumetric + 2D pixel, AlexNet network사용

- In the work of Hegde and Zadeh [2016], a fusion of volumetric (i.e., 3D) and pixel (i.e., 2D views) representations was attempted for 3D object classification.
  - More specifically, the authors used AlexNet network [Krizhevsky et al. 2012] for the 2D views of each 3D object, while they proposed two 3D CNNs for the volumetric data.

- The multiview network performed better on ModelNet40 than the volumetric ones, but the highest performance was achieved by the combination of the three different networks, named FusionNet
