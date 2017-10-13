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
- 오토인코더를 이용하여 특징 학습 ` use autoencoder for feature learning on the 2D images`

## 1. INTRODUCTION

현재(2014) 3D인식에 쓰이는 SD들은 hand-crafted이고 딥러닝은 잘 쓰이지 않는다. `Currently, in the context of 3D shape recognition, shape descriptors are mainly hand-crafted and deep learning representation has not been widely applied.`

딥러닝은 감독기반 학습으로 **retrieval task** 에는 맞지 않다. 비감독기반 학습을 위해 **Autoencode**가 제안 되었다. `The above developments of deep learning are in a supervised way and are not suitable for retrieval task.  From the aspect of unsupervised deep learning, Hinton and Krizhevsky [4] proposed the autoencoder algorithm with the application of image retrieval, which is then used for some other specific tasks like face alignment [5].`

오토인코더 설명 
-  The autoencoder can be regarded as a multi-layer sparse coding network. 
- Each node in the autoencoder network can be regarded as a prototype of object image/shape. 
- From the bottom layer to the top layer, the prototype contains richer semantic information and becomes a better representation. After the autoencoder network is learnt,
the coefficients obtained by reconstructing image/shape based
on prototypes are used as feature for 3D shape matching and
retrieval. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIxMDcwNTk3MDNdfQ==
-->