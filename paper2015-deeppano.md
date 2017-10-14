

|논문명 | DeepPano: Deep Panoramic Representation for 3-D Shape Recognition |
| --- | --- |
| 저자\(소속\) | Baoguang Shi \(\) |
| 학회/년도 | 2015, [논문](http://ieeexplore.ieee.org/document/7273863/) |
| 키워드 |  |
| 데이터셋/모델 | ModelNet-10, ModelNet-40 |
| 참고 |  |
| 코드 |[Matlab](https://github.com/bgshih/deeppano) |

# DeepPano

제안 : A robust representation of 3-D shapes learned with deep CNN

절차 
1. 파노라마뷰로 변경 `Firstly, each 3-D shape is converted into a panoramic view`
2. 제안된 CNN을 통해 학습 `Then, a variant of CNN is specifically designed for learning the deep representations directly from such views. `

기존 CNN과 다른점은 **row-wise맥스 풀링층**을 추가 하여 invariant에 대처 하도록 함 `Different from typical CNN, a row-wise max-pooling layer is inserted between the convolution and fully-connected layers, making the learned representations invariant to the rotation around a principle axis`

## 1. INTRODUCTION

- Representation에 위해서 성능이 좌우됨 `The performance of many tasks, including shape classification and shape retrieval, heavily depend on the quality of the representation`

본 논문은 DeepPano을 제안, 
- Directly learned from the panoramic views of 3-D models
- The panoramic view is a **cylinder projection** of a 3-D model around its principle axis.
- Therefore, the panoramic views are in the **form of 2-D images**,

Row-Wise Max-Pooling (RWMP) layer  제안
- To make the learned deep features invariant to the rotation around the principle axis
- between the convolution layers and the fully-connected layers. 
- This layer takes the maximum value of each row in the convolutional feature maps. 
- Consequently, the output feature vector is not affected by the shift of the panoramic view, caused by the rotation of 3-D shape.

### 1.1 관련 연구 

기존 연구 동향 분류 : The previous methods on 3-D shape analysis can be coarsely categorized into **model-based** and **view-based** methods. 

#### A. Model based methods 
- Model based methods calculate a set of features directly from the 3-D shape **mesh** or its rendered **voxels**. 

- 예 : Such methods include the Shape Histogram descriptor [2] and the Spin Images [3]. 

#### B. View based methods 
- View based methods represent 3-D shapes by a set of views [4]–[10].

- The views can be 2-D projections of the shape or the panoramic view. 


- 위 방법과 제안의 차이는 **hand-crafted**가 아니라 **CNN**을 이용한다. `However, different from most of the methods mentioned above that use hand-crafted features, we learn the representation from data with a variant of CNN. `


- 비슷한 기존 연구로 **3-D ShapeNets**가 있다. 이와 다른점은 
	- Different from [14] which performs 3-D convolutionson the **voxels**, we extract the representation of a 3-D shapefrom **2-D images**. 
	- 성능도 좋다. Compared with [14], our method achieves better performances on both classification and retrieval tasks(refer to Section III), and is simpler to implement using any open source framework.

### 1.2 기존 연구  PANORAMA와 rotates문제 해결법

Our method is related to previously introduced PANORAMA[6]. 

```
[6] P. Papadakis, I. Pratikakis, T. Theoharis, and S. J. Perantonis,“PANORAMA: A 3d shape descriptor based on panoramic views for unsupervised 3d object retrieval,” Int. J. Comput. Vis., vol. 89, no.2–3, pp. 177–192, 2010
```

기존 연구도 **panoramic views**를 이용하였다. ` In [6], Panagiotis et al. proposed to represent a 3-D shape by the Discrete Fourier Transform and Discrete Wavelet Transform descriptors calculated from a set of panoramic views. `

Panoramoc view의 큰 문제점 : However,the panoramic view shifts when the 3-D shape rotates along its principle axis. 

기존 연구에서는 **normalization**으로 해결 `In [6], this problem is alleviated by pose normalization.`

### 1.3 본 연구와 rotates문제 해결법

![](https://i.imgur.com/daQ7b8F.png)
```
[Fig. 1. Rotation invariance of DeepPano]
- (a) 3-D shapes of the same model, but rotated to different angles; 
- (b) Convolutional feature map for each 3-D shape; 
- (c) Output vectors of the RWMP layer; 
- (d) Comparisons among within model distances, within class distances and between class distances 
```

As illustrated in Fig. 1, the convolutional feature maps extracted from panoramic views shifts when the 3-D shape rotates.

We pool the the responses of each row so that the resulting representation is not affected by this kind of shift. 

As a result, the representation is invariant to the 3-D shape rotation. 

## 2. METHODOLOGY

Our method consists of two main steps: 
1. Generate the panoramic views (Section II-A); 
2. Learn and extract the rotation-invariant representation from the views (Section II-B).

본 논문의 가정(Assumption)사항 : 물체는 upright로 회전되어 있다. 대부분의 Datasets(3-D Warehouse)이 이렇게 되어 있다. ` Throughout this letter, we assume that 3-D models are upright oriented, so that the rotation is along a
axis that is also upright oriented. This assumption is satisfied in many real-world model repositories, such as the 3-D Warehouse[15].`


### 2.1 Panoramic View Construction

The projection process is illustrated in Fig. 2. 

![](https://i.imgur.com/UUM0hjq.png)
```
[Fig. 2. Panoramic view construction]
- (a) Illustration of the panoramic view construction process.
	- p ,q and d are respectively the grid point, 
	- the corresponding point on the axis and the value assigned to that grid point;
- (b) 3-D shapes and their corresponding panoramic views (with some padding)

```

### 2.2 Representation Learning and Extraction

간단한 방법은 CNN에 파노라믹뷰를 학습 시키는 것이다. `A straightforward method is to train a CNN on the panoramic views of all training data, and extract the representation from it. `

하지만, 3D Shape가 회전하면 View가 변하게 된다. 이 변화를 막기 위하여 작업이 필요 하다. `  However, the view shifts when the 3-D shape rotates. This shift will greatly affect the representation produced by the CNN, although the CNN providessome form of translation invariance. `

또한 파노라마로 펼치게 되면 두개의 경계가 ㅇ나타난다.  Moreover, unfolding the lateral surface creates two boundaries on the left and right sides of the panoramic view. 

The boundaries cause artifacts in the convolutional feature maps, thus affecting the representationextracted.In our approach, a variant of CNN is created to learn andextract the representation, handling the issues mentioned above.As illustrated in Fig. 3, firstly, to avoid boundary artifacts, thepanoramic view is padded on one side. 

The padded area iscloned from the other side of the map. 

Specifically, we adopt apadding size where is the height of the view.To obtain rotation-invariance, the representation has to beshift-invariant to the input panoramic view. 

The first few layersof a typical CNN, namely the convolution layers and the maxpoolinglayers produce feature maps that shift together withthe input view. 

Between these layers and the fully-connectedlayers, we insert a layer called the row-wise max-pooling layer(RWMP), which takes the maximum value of each row in theinput map and concatenate them into the output vector. 

Theoutput of the RWMP layer is not affected by the shift of theinput map, thus its output is invariant to the rotation of the 3-Dshape. 

The network is trained on a dataset consisting of pairs of panoramic views and class labels, using the back propagationalgorithm [16]. 

Finally, the representation can be extractedfrom the RWMP layer, or any fully-connected layer after it.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU1ODAwMzU2OF19
-->