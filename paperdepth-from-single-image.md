
|논문명|Single image depth estimation by dilated deep residual convolutional neural network and soft-weight-sum inference|
|-|-|
|저자(소속)|Bo Li (Baidu)|
|학회/년도| Apr 2017, [논문](https://arxiv.org/abs/1705.00534)|
|키워드||
|참고||
|코드||


# Single image depth estimation by dilated DNN

The advantages of our method come from the usage of 
- dilated convolution, 
- Skip connection architecture 
- soft-weight-sum inference

## 1. INTRODUCTION

It is a very challenging problem due to its ill-posedness nature.

### 1.1 기존 연구 

- Li et al. [1] predicted the depth and surface normals from a color image by regression on deep CNN features in a **patch based framework**. 

- Liu et al. [2] proposed a **CRF-CNN combined learning framework**. 

- Wang et al. [3] proposed a CNN architecture for joint semantic labeling and depth prediction.

- Eigenet al. [4] proposed a **multi-scale architecture** that 
    - first predicts a coarse global output 
    - then refines it using finer-scale local networks. 

- Cao et al. [5] demonstrated that formulating depth estimation as a classification task is better than direct regression. 

These works demonstrate that, network architecture design plays a central role in improving the performance.


```
[1] Bo Li, Chunhua Shen, Yuchao Dai, A. van den Hengel, and Mingyi He, “Depth and surface normal estimation from monocular images using regression on deep features and hierarchical crfs,” in CVPR, jun 2015, pp. 1119–1127.
[2] Fayao Liu, Chunhua Shen, Guosheng Lin, and Ian Reid, “Learning depth from single monocular images using deep convolutional neural fields,” TPAMI, vol. 38, no. 10, pp. 2024–2039, 2016.
[3] Peng Wang, Xiaohui Shen, Zhe Lin, Scott Cohen, Brian Price, and Alan L Yuille, “Towards unified depth and semantic prediction from a single image,” in CVPR, 2015, pp. 2800–2809.
[4] David Eigen and Rob Fergus, “Predicting depth, surface normals and semantic labels with a common multi-scale convolutional architecture,” in ICCV, 2015, pp. 2650–2658.
[5] Yuanzhouhan Cao, Zifeng Wu, and Chunhua Shen, “Estimating depth from monocular images as classification using deep fully convolutional residual networks,” [Online]. Avaliable: https://arxiv.org/abs/1605.02305, 2016.
```

## 2. NETWORK ARCHITECTURE

![](https://i.imgur.com/ufGlDWV.png)

- $$\time n$$ means the block repeats n times. 
- We present all the hyper-parameters of convolution and pooling layers. 
- All the convolution layers are followed by batch normal layer except the last one. 
- $$/2$$ means the layer’s stride is 2. 
- $$∗4$$ means the deconv layer’s stride is 4. 
- `Dilation` shows the dilated ratio of the correspondent parts.
= $$L1, · · ·L6$$ are our skip connection layers.


Weights are initialized from a pre-trained 152 layers residual CNN [7]. 
- image classification problem. **depth estimation task**로 전이학습 필요 


```
[7] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun, “Deep residual learning for image recognition,” in CVPR, 2016, pp. 770–778.
```

###### depth estimation 전이학습

- **Firstly**, we remove all the **fully connect layers**. 
    - In this way, we greatly reduce the number of model parameters as more than 80% of the parameters are in the fully connect layers [4, 5]. 

- **Secondly**, we take advantage of the **dilated convolution**, which could expand the receptive field of the neuron without increasing the parameters. 

- **Thirdly**,with dilated convolution, we could keep the spatial resolution of feature maps. 

- **Then**, we concatenate intermediate feature maps with the final feature map directly. 

This skip connection design benefits the multi-scale feature fusion and boundarypreserving.

### 2.1 Dilated Convolution: 

Recently, dilated convolution is successfully utilized in the CNN design by Yu et al. [8]. 

![](https://i.imgur.com/HYhcg7b.png)

We refer to `∗l` as a dilated convolution or an l-dilated convolution.

The conventional discrete convolution `∗` is simply the 1-dilated convolution.

```
[8] Fisher Yu and Vladlen Koltun, “Multi-scale context aggregation by dilated convolutions,” in ICLR, 2016, pp. 1–10.
```


### 2.2 Skip Connection: 

As the CNN is of hierarchical structure, which means high level neurons have larger receptive field and more abstract features, while the low level neurons have smaller receptive field and more boundary information.

We propose to concatenate the high-level feature map and the inter-mediate feature map. 

The skip connection structure benefits both the multi-scale fusion and boundary preserving.

## 3. SOFT-WEIGHT-SUM INFERENCE

제안 방식은 use soft-weight-sum inference instead of the hard-threshold method.


--- 
- David Eigen, Depth Map Prediction from a Single Image using a Multi-Scale Deep Network, NIPS 2014, [논문](https://www.cs.nyu.edu/~deigen/depth/depth_nips14.pdf), [Homepage](https://www.cs.nyu.edu/~deigen/depth/),  NYU Depth v2 ,KITTI 
- Andrew Y. Ng, 3-D Depth Reconstruction from a Single Still Image, IJCV 2007, [논문](http://www.cs.cornell.edu/~asaxena/reconstruction3d/saxena_iccv_3drr07_learning3d.pdf), [Homepage](http://www.cs.cornell.edu/~asaxena/learningdepth/) 
- Nidhi Chahal, Depth estimation from single image using machine learning techniques, ICVGIP 16 [논문](https://dl.acm.org/citation.cfm?id=3010019)
---
