

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
- Firstly, each 3-D shape is converted into a panoramic view
- Then, a variant of CNN is specifically designed for learning the deep representations directly from such views. 

기존 CNN과 다른점은 **row-wise맥스 풀링층**을 추가 하여 Different from typical CNN, a row-wise max-pooling layer is inserted between the convolution and fully-connected layers, making the learned representations invariant to the rotation around a principle axis

## 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU4NDA0MjI4N119
-->