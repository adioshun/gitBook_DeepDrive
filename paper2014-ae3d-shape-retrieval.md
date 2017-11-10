| 논문명 | Deep Learning Representation using Autoencoder for 3D Shape Retrieval |
| --- | --- |
| 저자(소속) | Zhuotun Zhu () |
| 학회/년도 | 2014, [논문](https://arxiv.org/abs/1409.7164) |
| 키워드 |AE3D2014, depth images, autoencoder  |
| 데이터셋/모델 |Princeton Shape Benchmark, Engineering Shape Benchmark / RBM |
| 참고 | |
| 코드 | |

# AE3D Shape Retrieval

- 3D를 2D로 투영 `we project 3D shapes into 2D space` 
- 오토인코더를 이용하여 특징 학습 ` use autoencoder for feature learning on the 2D images` (depth images)
	-  we aim to use autoencoder to learn a 3D shape representation based on the depth images obtained by projection.

## 1. INTRODUCTION

현재(2014) 3D인식에 쓰이는 SD들은 hand-crafted이고 딥러닝은 잘 쓰이지 않는다. `Currently, in the context of 3D shape recognition, shape descriptors are mainly hand-crafted and deep learning representation has not been widely applied.`

딥러닝은 감독기반 학습으로 **retrieval task** 에는 맞지 않다. 비감독기반 학습을 위해 **Autoencode**가 제안 되었다. `The above developments of deep learning are in a supervised way and are not suitable for retrieval task.  From the aspect of unsupervised deep learning, Hinton and Krizhevsky [4] proposed the autoencoder algorithm with the application of image retrieval, which is then used for some other specific tasks like face alignment [5].`

```
오토인코더 설명 
- The autoencoder can be regarded as a multi-layer sparse coding network. 
- Each node in the autoencoder network can be regarded as a prototype of object image/shape. 
- From the bottom layer to the top layer, the prototype contains richer semantic information and becomes a better representation. 
- After the autoencoder network is learnt, the **coefficients obtained** by reconstructing image/shape based on prototypes are used as feature for 3D shape matching and retrieval. 
- Since the autoencoder can learn feature adaptively to training data, it can get excellent performance for image
retrieval.
```

본 논문은 View-based 3D Shpae방법에서 영감을 받아 오토인코더를 이용 **Depth image**에서 부터 **3D shape representation**를 학습 하도록 하였다. `Motivated by the view-based 3D shape methods [6], [7], in which a 3D shape can be projected into many 2D depth images, we aim to use autoencoder to learn a 3D shape representation based on the depth images obtained by projection.`

```
[6] Chen, D., Tian, X., Shen, Y., Ouhyoung, M.: On visual similarity based 3d model retrieval. Computer Graphics Forum 22 (2003) 223–232
[7] Lian, Z., Godil, A., Sun, X.: Visual similarity based 3d shape retrieval
using bag-of-features. In: Shape Modeling International Conference (SMI), 2010. (2010) 25–36
```

![](https://i.imgur.com/lfzJYCk.png)
```
[Fig. 1. A specific illustration of our method to reconstruct 2D images]
- 첫   줄 : displays the original depth images in gray-scale of the 3D shape, 
- 둘째 줄 : shows the reconstructed ones corresponding to the images of the first row. 
- black dots : indicates those extracted from other different views.
```

그림 1 처럼 3D shape는 여러 depth images로 투영 된다. 학습된 오토 인코더는 재 구성도 성능도 좋다 `As shown in Fig. 1, a 3D shape is projected into many different depth images; the learnt autoencoder can reconstruct the depth images nicely. `

결국 features를 비교하며 검색(`match`) 하는 것은 일종의 **set-to-set distance**문제로 바뀌게 되어 Hausdorff같은 알고리즘(`set-to-set distance`)을 적용 할수 있게 된다. . `Matching 3D shape based on the autoencoder features can be converted to a set-to-set matching problem, conventional set-to-set distance, like the Hausdorff distance, can be adopted.` 

오토인코드된 representation은 **global representation**이다. SIFT같은건 **local descriptor**이다. `Our autoencoder based 3D shape representation is a deep learning representation; compared to the representations based on local descriptor, e.g. SIFT, it is a global representation. `

This **global deep learning representation** and the **representation based on local descriptors** are complementary(상호 보완적) to each other.

## 2. RELATED WORK

**각 보는 각도마다 같아 보이는 두 물체는 같은 물체 이다**라는 생각에서 시작한 View-based접근 방식은  식별력이 좋은 것으로 알려 져 왔다. `Based on the main idea that “two 3D models are similar if they look similar with each other from all viewing angles”, there are plenty of view-based approaches that have been regarded as the most discriminative methods on literature [8].`

```
[8] Shilane, P., Min, P., Kazhdan, M., Funkhouser, T.: The princeton shape benchmark. In: Shape Modeling Applications, 2004. Proceedings, IEEE (2004) 167–178
```

###### [Cyr and Kimia] 

In [9], Cyr and Kimia recognized a 3D shape by comparing a view of the shape with all views of 3D objects using shock graph matching. 

```
[9] Cyr, C.M., Kimia, B.B.: 3D object recognition using shape similaritybased aspect graph. In: International Conference on Computer Vision. (2001) 254–261
```

###### [Ohbuchi et al.] 

Ohbuchi et al. [10] utilized local visual features by using the **SIFT**(Scale Invariant Feature Transform [11]) to retrieve 3D shapes. 

A host of local features describing the 3D models is integrated into a histogram using Bag-of-Features [12] to reduce the computation complexity.

```
[10] Ohbuchi, R., Osada, K., Furuya, T., Banno, T.: Salient local visual features for shape-based 3D model retrieval. In: Shape Modeling International. (2008) 93–102
```

###### [Vranic]
Vranic [13] presented a composite 3D shape feature vector(DESIRE) which consists of **depth buffer images**, silhouettes and ray-extents of a polygonal mesh. 

The composite of variousfeature vectors extracted in a canonical coordinate framegenerally performs better than the single method which relieson pairwise alignment of 3D objects. 

```
[13] Vranic, D.V.: DESIRE: a composite 3D-shape descriptor. In: International Conference on Multimedia Computing and Systems/International Conference on Multimedia and Expo. (2005) 962–965
```

###### [Papadakiset]

Later on, Papadakiset al. [14] made use of a **hybrid descriptor** (Hybrid) which consists of both **depth buffer based 2D features** + **sphericalharmonies based 3D features**. 

The Hybrid adopts two alignment methods to compensate inner rotation variance and then uses Huffman coding to further compress feature descriptors.

```
[14] Papadakis, P., Pratikakis, I., Theoharis, T., Passalis, G., Perantonis, S.J., Paraskevi, A.: 3D object retrieval using an efficient and compact hybrid shape descriptor. (2008) 9–16
```

###### [PANORAMA]

Also, they presented a 3D descriptor (PANORAMA) [15] that captures the panoramic view of a 3D shape by projecting it to a lateral surface of a cylinder parallel to one of its three principal axes. 

By aligning its principle axes to capture theg lobal information and combining 2D Discrete Fourier Transformand 2D Discrete Wavelet Transform, the PANORAMA **outperforms all the other 3D shape retrieval methods** on several standard 3D benchmarks. 

```
[15] Papadakis, P., Pratikakis, I., Theoharis, T., Perantonis, S.J.: PANORAMA: A 3D shape descriptor based on panoramic views for unsupervised 3D object retrieval. International Journal of Computer Vision 89 (2010) 177–192
```

###### [Lian et al]

Meanwhile, Lian et al. [7] used Bag of-Features and Clock Matching (CM-BoF) on a set of depth buffer views obtained from the projections of the normalized object. 

The CM-BoF method also takes advantage of the preserved local details as well as isometry-invariant global structure to reach a competing result. 

```
[7] Lian, Z., Godil, A., Sun, X.: Visual similarity based 3d shape retrieval using bag-of-features. In: Shape Modeling International Conference (SMI), 2010. (2010) 25–36
```

###### [Geodesic Sphere based Multi-view Descriptors ]

Prior to that, they also proposed a shape descriptor named Geodesic Sphere based Multi-view Descriptors (GSMD) [16] measuring the extend to which a 3D polygon is rectilinear based on the maximum ratio of the surface area to the sum of three orthogonal projected areas. 

```
[16] Lian, Z., Rosin, P.L., Sun, X.: Rectilinearity of 3D meshes. International Journal of Computer Vision 89 (2010) 130–151
```

###### [Bai et al]

Recently, Bai et al. [17] adopted contour fragments as the input features for learning a BoW model, which is general and efficient for both 2D and 3D shape matching.

```
[17] Bai, X., Rao, C., Wang, X.: Shape Vocabulary: A Robust and Efficient Shape Representation for Shape Matching. IEEE Transactions on Image Processing 29 (2014) 3935–3949
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAxNTc2ODk0NF19
-->


---

```
A. 최초 도입한 논문 (2014)

In the aforementioned work, an AE was used in order to generate a global deep representation of a 3D shape for the application scenario of 3D shape retrieval.
Pose normalization for differences in translation and scale was initially applied to each 3D model, while a set of 2D projections was subsequently collected for each of them.
After pretraining the stacked RBMs with the projections, the AE was fine-tuned using back-propagation in order to minimize the reconstruction error.
Finally, the hidden (code) layer was used for representing the corresponding projection/view of the 3D shape in the retrieval process.
Since more than one code was generated for each model (one per projection), a variant of the Hausdorff distance was used to compute the distance between the final representations of two different 3D shapes.

```


```
[또 다른 AE활용 논문] B. Leng, S. Guo, X. Zhang, and Z. Xiong. 2015. 3D object retrieval with stacked local convolutional autoen-coder.Signal Processing 112, C (2015), 119–128

B. Stacked Local Convo-lutional AutoEncoder (SLCAE) (2015)

An AE was also adopted for 3D object retrieval in Leng et al. [2015a].
In this method, an extension of the standard AE inspired from CNNs, called Stacked Local Convo-lutional AutoEncoder (SLCAE)
A Local Convolutional Autoencoder (LCAE) is constructed by substituting the FC layers of a standard AE with locally connected layers using the convolution operation.
In the stacked version of LCAE, many encoders were placed on top of each other and the output of the last one was used as the representation of a 3D object.
The input provided to the proposed AE was multiple depth images of several views of the 3D object, while each layer of the architecture was trained using the gradient descent method.+


```


```

```