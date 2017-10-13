

|논문명 | Multi-view Convolutional Neural Networks for 3D Shape Recognition |
| --- | --- |
| 저자\(소속\) | Hang Su \(\) |
| 학회/년도 | 2015, [논문](https://arxiv.org/abs/1505.00880) |
| 키워드 | MVCNN2015, |
| 데이터셋/모델 | |
| 참고 | |
| 코드 | |


# MVCNN

Representation of 3D shapes for recognition에 대한 학계의 오래된 질문
-  3D Shape는 native 3D formats인 Voxel grid로 표현 해야 할까? View-based로 표현 해야 할까? ` should 3D shapes be represented with descriptors operating on their native 3D formats, such as voxel grid or polygon mesh, or can they be effectively represented with view-based descriptors?`



## 1. Introduction

Native 3D formats인 Voxel grid를 사용 하는 방법이 ShapeNet을 통해 제안 되었다[37]. 

 View-based도 좋은 성능을 보인다. 실험 결과 여러 view로 학습후 하나의 이미지만 보여 줬어도 인식률이 7%나 증가 하였다. ` In particular, a convolutional neural network (CNN) trained on a fixed set of rendered views of a 3D shape and only provided with a single view at test time increases category recognition accuracy by a remarkable 8% (77% → 85%) over the best models [37-ShpaeNet] trained on 3D representations.`
- 이유 1 : 
- 이유 2 :  Adnavced image descriptor와 풍부한  Datasets 들을 사용할수 있다. 

```
[37] Z. Wu, S. Song, A. Khosla, F. Yu, L. Zhang, X. Tang, and J. Xiao. 3D ShapeNets: A deep representation for volumetric shape modeling. In Proc. CVPR, 2015.
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3Mjk1OTE3NzddfQ==
-->