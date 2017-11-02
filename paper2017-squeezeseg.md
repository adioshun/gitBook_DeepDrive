|논문명|SqueezeSeg: Convolutional Neural Nets with Recurrent CRF for Real-Time Road-Object Segmentation from 3D LiDAR Point Cloud|
|-|-|
|저자(소속)|Bichen Wu (Berkeley)|
|학회/년도| arXiv 2017, [논문](https://arxiv.org/abs/1710.07368v1)|
|키워드| |
|참고|[Youtube](https://www.youtube.com/watch?v=Xyn5Zd3lm6s)|
|코드||


# SqueezeSeg

- 입력 : 3D LiDAR -> Segmentation `In this paper, we address semantic segmentation of road-objects from 3D LiDAR point clouds. `

- We formulate this problem as a **point wise classification problem**

- propose an end-to-end pipeline called **SqueezeSeg** based on convolutional neural networks(CNN): 

- 입력 : LiDAR Point cloud -> 출력 : point-wise label map -> refined -> Instance-level labels
-  the CNN takes a transformed **LiDAR point cloud** as input and directly outputs a **point-wise label map**,
	-  which is then refined by a **conditional random field (CRF)** implemented as a recurrent layer. 
	- **Instance-level labels** are then obtained by conventional clustering algorithms. 

- GTA-V를 이용하여서 가상 데이터 획득 `To obtain extra training data, we built a LiDAR simulator into Grand Theft Auto V (GTA-V), a popular video game, to synthesize large amounts of realistic training data. `

Our experiments show that SqueezeSeg achieves high accuracy with astonishingly fast and stable runtime (8.7 ±0.5 ms per frame), highly desirable for autonomous driving applications. 

Furthermore, additionally training on synthesizeddata boosts validation accuracy on real-world data. 

Our sourcecode and synthesized data will be open-sourced.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjczMDQ1ODExXX0=
-->