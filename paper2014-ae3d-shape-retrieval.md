| 논문명 | Deep Learning Representation using Autoencoder for 3D Shape Retrieval |
| --- | --- |
| 저자(소속) | Zhuotun Zhu () |
| 학회/년도 | 2014, 논문 |
| 키워드 | |
| 데이터셋/모델 | |
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


![](https://i.imgur.com/lfzJYCk.png)
```
[Fig. 1. A specific illustration of our method to reconstruct 2D images]
- 첫   줄 : displays the original depth images in gray-scale of the 3D shape, 
- 둘째 줄 : shows the reconstructed ones corresponding to the images of the first row. 
- black dots : indicates those extracted from other different views.
```

그림 1 처럼 3D shape는 여러 depth images로 투영 된다. 학습된 오토 인코더는 재 구성도 성능도 좋다 `As shown in Fig. 1, a 3D shape is projected into many different depth images; the learnt autoencoder can reconstruct the depth images nicely. `

결국 features를 비교하며 검색(`match`) 하는 것은 일종의 **set-to-set distance**문제로 바뀌게 되어 Hausdorff같은 알고리즘(`set-to-set distance`)을 적용 할수 있게 된다. . `Matching 3D shape based on the autoencoder features can be converted to a set-to-set matching problem, conventional set-to-set distance, like the Hausdorff distance, can be adopted.` 

Our autoencoder based 3D shape representation is a deep learning representation; compared to the representations based on local descriptor, e.g. SIFT, it is a global representation. 

This global deep learning representation and the representation based on local descriptors are complementary to each other.

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5MTQ3MTI4NTFdfQ==
-->