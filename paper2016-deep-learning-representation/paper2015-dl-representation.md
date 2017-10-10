|논문명|Deep Learning Representation using Autoencoder for 3D Shape Retrieval|
|-|-|
|저자(소속)| ()|
|학회/년도| IROS 2015, [논문](http://www.sciencedirect.com/science/article/pii/S0925231216301047)|
|키워드| |
|참고||
|코드||


# Deep Learning Representation

## 1. Introduction

2D CNN이 잘 동작 하는 이유 : image representation에서 특징을 잘 추출 할수가 있어서 

- One reason of the success of deep learning for visual recognition is that the deep learning methods can automatically learn the features with the superior discriminatory power for image representation, rather than using hand-crafted image descriptors.

3D의 문제점 : 3D shape representation에 딥러닝을 바로 적용하는건 어려움 

- Currently, in the context of 3D shape recognition, shape descriptors are mainly hand-crafted and deep learning representation has not been widely applied. 
- It seems that it is hard to directly apply deep learning methods to 3D shape representation, 
    - since deep learning methods need a large amount of data to bridge the visual gap among training examples from the same object category; 
    - and it is unlikely to learn a good representation using a few data with large visual variation.
    
본 논문의 타켓인 `retrieval task`에 위에서 언급한 **지도기반** 방식은 맞지 않는다. `The above developments of deep learning are in a supervised way and are not suitable for retrieval task.`



### 1.1 autoencoder

비지도 기반 방식들 : From the aspect of unsupervised deep learning, 
- Hinton and Krizhevsky [4] proposed the **autoencoder algorithm** with the application of image retrieval, which is then used for some other specific tasks like face alignment [5]. 

```
[4] Alex Krizhevsky, Geoffrey E. Hinton, Using very deep autoencoders for content-based image retrieval, In ESANN. Citeseer, 2011.
[5] Jie Zhang, Shiguang Shan, Meina Kan, Xilin Chen, Coarse-to-fine auto-encoder networks (cfan) for real-time face alignment, In European Conference on Computer Vision, 2014.
```

동작 과정 
- Training autoencoder does not require any label information. 
- The autoencoder can be regarded as a multi-layer sparse coding network. 
- Each node in the autoencoder network can be regarded as a prototype of object image/shape. 
- From the bottom layer to the top layer, the prototype contains richer semantic information and becomes a better representation. 
- After the autoencoder network is learnt, the coefficients obtained by reconstructing image/shape based on prototypes are used as feature for 3D shape matching and retrieval. 
- Since the autoencoder can learn feature adaptively to training data, it can get excellent performance for image retrieval.

### 1.2 deep learning frameworks

![](https://i.imgur.com/IKVZxtG.png)

Until now, few approaches based on **deep learning frameworks** have been proposed to deal with 3D shape retrieval.

- Following [6], Fang et al. [7] trained a deep neural network using **Eigen-shape descriptor** and **Fisher-shape descriptor** 

- **Heat shape descriptor** developed from Heat Kernel Signature is fed into the network

- Wu et al. [8] constructed a large-scale 3D CAD model dataset to train a convolutional deep belief network. 
    - This network learns the distribution of 3D shapes with different categories and arbitrary poses. 
    - Therefore, adopting deep learning approaches for 3D shape retrieval needs to be further justified.

```
[6] Zhuotun Zhu, Xinggang Wang, Song Bai, Cong Yao, Xiang Bai, Deep learning representation using autoencoder for 3d shape retrieval, In Security, Pattern Analysis, and Cybernetics (SPAC), 2014 International Conference on, IEEE, 2014, pp. 279–284.
[7] Yi Fang, Jin Xie, Guoxian Dai, Meng Wang, Fan Zhu, Tiantian Xu, Edward Wong, 3d deep shape descriptor, In IEEE Conference on Computer Vision and Pattern Recognition, 2015, pp. 2319–2328.
[8] Zhirong Wu, Shuran Song, Aditya Khosla, Fisher Yu, Linguang Zhang, Xiaoou Tang, Jianxiong Xiao, 3d shapenets: A deep representation for volumetric shapes, In IEEE Conference on Computer Vision and Pattern Recognition, 2015.

```    
        
                
### 1.3 view-based approaches. 

Different from recent works in [7] and [8], we adopt view-based approaches.

Motivated by other view-based 3D shape methods [9,10], in which a 3D shape can be projected into many 2D depth images, 
    - we aim to use autoencoder to learn a 3D shape representation based on the depth images obtained by projection.

```
[9] Dingyun Chen, Xiaopei Tian, Yute Shen, Ming Ouhyoung, On visual similarity based 3D model retrieval, Computer Graphics Forum 22 (2003) 223–232.
[10] Zhouhui Lian, A. Godil, Xianfang Sun, Visual similarity based 3d shape retrieval using bag-of-features, In Shape Modeling International Conference (SMI), 2010, June 2010, pp. 25–36.
```


### 1.4 Local & Global Representation 

- Our autoencoder based 3D shape representation  = a deep learning representation = global representation (= View based???)



- SIFT = local descriptor



둘은 상호 보완재이다. This global deep learning representation and the representation based on local descriptors are complementary to each other.

## 2. Related work

view-based approaches의 기본 아이디어 `two 3D models are similar if they look similar with each other from all viewing angles`

> 본 논문에서는 view-based approaches를 채택 하였으므로 이에 대한 내용을 많이 다루겠다. 

- In [13], Cyr and Kimia recognized a 3D shape by comparing a view of the shape with all views of 3D objects using shock graph matching. 

- Osada et al. [14] proposed the **shape distribution descriptor** that measures properties based on area, angle, distance and volume measurements between a random set of points on the object. 

- 두 물체의 유사성은 D2함수로 구할수 있다. The similarity between two objects is defined by suitable shape functions, e.g. the D2 function. 

- SIFT를 이용하여 3D모습을 복원 하였다. Ohbuchi et al. [11] utilized local visual features by using the Scale Invariant Feature Transform (SIFT) [15] to retrieve 3D shapes. 

- A host of local features describing the 3D models is integrated into a histogram using Bag-of-Features [16] to reduce the computation complexity. 

- Vranic [17] presented a composite 3D shape feature vector (DESIRE) which consists of **depth buffer images**,** silhouettes** and **ray-extents** of a polygonal mesh. 

The composite of various feature vectors extracted in a canonical coordinate frame generally performs better than the single method which relies on pairwise alignment of 3D objects. 

- Later on, Papadakis et al. [18] made use of a **hybrid descriptor **(Hybrid) which consists of both depth buffer based 2D features and spherical harmonies based 3D features. 
    - The Hybrid adopts two alignment methods to compensate inner rotation variance and then uses Huffman coding to further compress feature descriptors. 
    - Also, they presented a 3D descriptor (PANORAMA) [19] that captures the panoramic view of a 3D shape by projecting it to a lateral surface of a cylinder parallel to one of its three principal axes. 
    -By aligning its principle axes to capture the global information and combining 2D Discrete Fourier Transform and 2D Discrete Wavelet Transform, the PANORAMA outperforms all the other 3D shape retrieval methods on several standard 3D benchmarks. 

- Meanwhile, Lian et al. [10] used **Bag-of-Features** and **Clock Matching (CM-BoF)** on a set of depth-buffer views obtained from the projections of the normalized object. 
    - The CM-BoF method also takes advantage of the preserved local details as well as is ometry-invariant global structure to reach a competing result. 
    - Prior to that, they also proposed a shape descriptor named Geodesic Sphere based Multi-view Descriptors (GSMD) [20] measuring the extend to which a 3D polygon is rectilinear based on the maximum ratio of the surface area to the sum of three orthogonal projected areas. 

- Recently, Bai et al. [21] adopted contour fragments as the input features for learning a BoW model, which is general and efficient for both 2D and 3D shape matching.

### 2.1 Light Field descriptor (LFD) = view-based 3D shape retrieval methods중 가장 유명한 방법 

1. The extraction of LFD begins with the scale and translation normalization while achieving rotation invariance via an exhaustive searching from a great many of views. 
2. Then the silhouette projections, rendered from uniformly sampled positions on a unit sphere, are represented by 10 Fourier coefficients [22] and 35 Zernike moments coefficients [23]. 
3. Finally, the dissimilarity between two objects is measured by the minimum distance of all group matching pairs. 

The LFD is insensitive to similarity transform, geometry degeneracy and noise, etc, thus shows better performance than other competing approaches.