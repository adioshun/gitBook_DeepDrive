|논문명|Depth Estimation from Single Image Using CNN-Residual Network|
|-|-|
|저자(소속)|Xiaobai Ma (Standford)|
|학회/년도| cs231n-Report 2017, [논문](http://cs231n.stanford.edu/reports/2017/pdfs/203.pdf)|
|키워드|1 camera, CNN+FC, Pure CNN, CNN+Residual, NYU Depth|
|참고||
|코드|[유사프로젝트](https://github.com/iro-cp/FCRN-DepthPrediction)|

# Depth Estimation from Single Image Using CNN-Residual Network

## 1. Introduction

## 2. Related work
### 2.1. Classic methods

Most works rely on
- camera motion (Structure-from-Motion method [21])
- variation in illumination (Shape-from-Shading [34])
- variation in focus (Shapre-from-Defocus [31]).

기존 연구 문제점
Classic methods rely on
- strong assumptions about the scene geometry,
- relied on hand-crafted features and
- probabilistic graphical models which exploits horizontal alignment of images or other
geometric information.


#### A. Saxena et al
- Saxena et al. [26] predicted depth from a set of image features using linear regression and a MRF,
- and later extend their work into the Make3D system for 3D model generation [27].
- However, the system relies on horizontal alignment of images, and suffers in less controlled settings.

#### B. Liu et al
- Inspired by this work, Liu et al. [15] combine the task of semantic segmenta-tion with depth estimation, where predicted labels are used as additional constraints to facilitate the optimization task.

#### C. Ladicky et al
- Ladicky et al. [10] instead jointly predict labels and depths in a classification approach. Hoiem et al.

#### D.

[6] do not predict depth explicitly, but instead categorize image regions into geometric structures and then compose a simple 3D model of the scene.


### 2.2. Feature-based mapping methods

A second type of related works perform feature-based matching between a given RGB image and the images of a RGB-D repository in order to find the nearest neighbors, the retrieved depth counterparts are then warped and combined to produce the final depth map.

#### A. Karsch

Karsch et al. [7] perform warping using SIFT Flow [16], followed by a global optimization scheme, whereas Konrad et al.

#### B.

[8] compute a median over the retrieved depth maps followed by cross bilateral filtering for smoothing.

#### C. Liu et al

Instead of warping the candidates, Liu et al. [19], formulate the optimization problem as a Conditional Random Field (CRF) with continuous and discrete variable potentials.

Notably, these approaches rely on the assumption that similarities between regions in the RGB images imply also similar depth cues.


### 2.3. CNN based methods

최근 CNN기반 방법들이 제안 되었다. 이 작업있기 때문에 기존 이 **semantic labeling**와 깊은 연관이 AlexNet, VGG 같은 방법을 기반으로 연구 되었다. `Since the task is closely related to semantic labeling, most works have built upon the most successful architectures of the ImageNet Large Scale Visual Recognition Challenge (ILSVRC) [25], often initializing their networks with AlexNet [9] or the deeper VGG [30]. Eigen et al. `

#### A. 최초의 CNN기반 방법 논문
[3]are the first to use CNN for single image depth estimation.

The authors addressed the task by employing two deep network stacks.

- The first network makes a global coarse depth prediction for the whole image,
- The second refines this prediction locally.

```
[3] D. Eigen, C. Puhrsch, and R. Fergus. Depth map prediction from a single image using a multi-scale deep network. In Advances in neural information processing systems, pages
2366–2374, 2014.
```

#### B. 확장 버젼

This idea is later extended in [2], where three stacks of CNN are used to additionally predict surface normals and labels together with depth.

```
[2] D. Eigen and R. Fergus. Predicting depth, surface normals and semantic labels with a common multi-scale convolutional architecture. In Proceedings of the IEEE International Conference on Computer Vision, pages 2650–2658, 2015.
```

#### C. CNN + regression forests

Roy et al. [24] combined CNN with regression forests [14], using very shallow architectures at each tree node, thus limiting the need for big data.

```
[24] A. Roy and S. Todorovic. Monocular depth estimation using neural regression forest. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pages 5506–5514, 2016.
```

#### D. CNNs and graphical models.

Liu et al. [17] propose to learn the unary and pairwise potentials during CNN training in the form of a conditional random field (CRF) loss and achieved state of-the-art result without using geometric priors.

This idea makes sense because the depth values are continuous [18].

```
[17] F. Liu, C. Shen, and G. Lin. Deep convolutional neural fields for depth estimation from a single image. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pages 5162–5170, 2015.
```

#### E. CNNs and graphical models.

Li et al. [13] and Wang et al. [32] use hierarchical CRFs to refine their patch-wise CNN predictions from superpixel down to pixel level.

```
[13] B. Li, C. Shen, Y. Dai, A. van den Hengel, and M. He. Depth and surface normal estimation from monocular images using regression on deep features and hierarchical crfs. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pages 1119–1127, 2015.
[32] P. Wang, X. Shen, Z. Lin, S. Cohen, B. Price, and A. L. Yuille. Towards unified depth and semantic prediction from a single image. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pages 2800–2809, 2015.
```
### 2.4. Fully convolutional networks

researchers are trying to improve CNN method accuracy further.

Recent work has shown that fully convolutional networks(FCNs)[20] is a desirable choice for dense prediction problems due to its ability of taking arbitrarily sized inputs and returning spatial outputs.



#### A. FCN + CRF

[1] uses FCN and adopts CRF as post-processing.

```
[1] Y. Cao, Z. Wu, and C. Shen. Estimating depth from monocular images as classification using deep fully convolutional residual networks. arXiv preprint arXiv:1605.02305, 2016.
```

#### A. dilated convolutions

Besides classical convolutional layers,[12] uses dilated convolutions as an efficient way to expand the receptive field of the neuron without increasing the parameters for depth estimation;

```
[12] B. Li, Y. Dai, H. Chen, and M. He. Single image depth estimation by dilated deep residual convolutional neural network and soft-weight-sum inference. arXiv preprint
arXiv:1705.00534, 2017.
```

#### B.

[23] uses transpose convolution for up-sampling the feature map and output for images egmentation.

```
[23] O. Ronneberger, P. Fischer, and T. Brox. U-net: Convolutional networks for biomedical image segmentation. In International Conference on Medical Image Computing and Computer-Assisted Intervention, pages 234–241. Springer, 2015.
```

#### C.

Laina et al. [11] proposed a fully connected network, which removes the fully connected layers and replaced with efficient residual up-sampling blocks.

```
[11] I. Laina, C. Rupprecht, V. Belagiannis, F. Tombari, and N. Navab. Deeper depth prediction with fully convolutional residual networks. In 3D Vision (3DV), 2016 Fourth International Conference on, pages 239–248. IEEE, 2016.
```

> 본 논문에서 차용한 방법 We closely follow this work in this project.


## 3. Methods

![](https://i.imgur.com/eNr5N5e.png)

### 3.1. CNN+FC

The first architecture follows the work in [3], where the authors used coarse and fine CNN networks to do depth estimation.

- 입력 : RGB image
- 6 convolution layers(파라미터 : 27,232) + 2 fully connected layers(파라미터 : 73,293,824)
- 출력 : depth map

> 많은 파라미터로 overfit문제있음, dropout layers로도 해결 어려움 

### 3.2. Pure CNN

> 오버피팅 문제를 해결하기 위해 FC를  convolution layers로 변경 : CNN+FC 보다 성능 좋음 

다른 CNN based method for depth estimation들은 일반적으로 
- the original image is usually downsampled to have a small height and width feature
- then upsampled to have the size of the final depth map. 

그래서 바꿈 So we changed the last two layers of this network. 
- The second last layer is followed by a 2 × 2 max-pooling layer, 
- the last layer is replaced with a transposed convolution layer to upsample the input.


### 3.3. CNN+Residual

Our third and most promising architecture follows the work in [11]. 

전이학습 수행 : 
- The essence is that we do transfer learning with extracted image features, 
- the transfer learning involves 
    - not only **training the fully connected layer** as we do in classification tasks, 
    - but also **convolution and up projection** to construct a depth map.

- 입력 : RGB
- pretrained ResNet-50 network + unpooling layer(upsampling,고해상도 위해) + convolution
layer +  a projection connection 





## 6. Conclusion

CNN with fully connected layer like the one used in [3] is powerful but can easily **overfit** on the dataset because of the **large number of parameters** in fully connected
layer. 

```
[3] D. Eigen, C. Puhrsch, and R. Fergus. Depth map prediction from a single image using a multi-scale deep network. In Advances in neural information processing systems, pages
2366–2374, 2014.
```

모티베이션 : This motivates us to use only convolutional layers and stack more layers to increase the receptive field. 
- This architecture yields acceptable result while **reduces** a large number of model **parameters**. 

We also try [18] which is a CNN architecture using transfer learning on the ResNet[5] and are able to get reasonable results on the validation set.

```
[18] F. Liu, C. Shen, G. Lin, and I. Reid. Learning depth from single monocular images using deep convolutional neural fields. IEEE transactions on pattern analysis and machine intelligence, 38(10):2024–2039, 2016.
```


