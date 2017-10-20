| 논문명 | FusionNet: 3D Object Classification Using Multiple Data Representations |
| --- | --- |
| 저자\(소속\) | Vishakh Hegde \(Standford\) |
| 학회/년도 | NIPS2016, [논문](http://3ddl.cs.princeton.edu/2016/papers/Hegde_Zadeh.pdf) |
| 키워드 | 3D CAD, |
| 데이터셋\(센서\)/모델 | Princeton ModelNet / AlexNet pre-trained on ImageNet |
| 참고 | [ppt](http://3ddl.cs.princeton.edu/2016/slides/zadeh.pdf) |
| 코드 |  |

> 동명의 논문 : FusionNet: A deep fully residual convolutional neural network for image segmentation in connectomics

FuseNet: Incorporating Depth into Semantic Segmentation via Fusion-Based CNN Architecture

![](https://i.imgur.com/Pog63M8.png)

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



