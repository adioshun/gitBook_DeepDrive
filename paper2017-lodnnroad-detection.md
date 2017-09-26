|논문명|Fast LIDAR-based Road Detection Using Fully Convolutional Neural Networks
|-|-|
|저자(소속)|Luca Caltagirone|
|학회/년도| 2017, [논문](https://arxiv.org/abs/1703.03613)|
|키워드|도로 탐지  |
|참고|[Youtube](http://goo.gl/efLoHz)|
|코드|[Dataset](http://www.cvlibs.net/datasets/kitti/eval_road.php)|

# LoDNN

CV기반 / DL 기반 로드 탐지에 대한 사전 연구 참고 필요 

Fully convolutional neural network (FCN): FCN is specifically designed for the task of `pixel-wise semantic segmentation` by combining a large receptive field with high-resolution feature maps

## 1. INTRODUCTION

도로 탐지가 중요한 이유 :  obstacle avoidance, road detection can also facilitate path planning and decision making

Survey 논문[1]에 따르면 대부분 monocular camera images기반이고 일부 DNNs이다. 

```
[1] A. B. Hillel, R. Lerner, D. Levi, and G. Raz, “Recent progress in road and lane detection: a survey,” Machine vision and applications, vol. 25, no. 3, pp. 727–745, 2014.
```

DNN기반 논문들 
- [4] the author trains deep deconvolutional networks using a multi-patch approach
- [5] a fully convolutional neural network (FCN) is trained with automatically annotated images.

Lidar Only 또는 camera + LIDAR기반 Road 탐지 논문들 [6-9]

```
[4] R. Mohan, “Deep deconvolutional networks for scene parsing,” arXiv preprint arXiv:1411.4101, 2014.
[5] L. Ankit, K. Mehmet, S. Luis, and M. Hebert, “Map-supervised road detection,” in IEEE Intelligent Vehicles Symposium Proceedings, 2016.
[6] L. Xiao, B. Dai, D. Liu, T. Hu, and T. Wu, “Crf based road detection with multi-sensor fusion,” in Intelligent Vehicles Symposium (IV), 2015.
[7] X. Hu, F. S. A. Rodriguez, and A. Gepperth, “A multi-modal system for road detection and segmentation,” in 2014 IEEE Intelligent Vehicles Symposium Proceedings. IEEE, 2014, pp. 1365–1370.
[8] R. Fernandes, C. Premebida, P. Peixoto, D. Wolf, and U. Nunes, “Road detection using high resolution lidar,” in 2014 IEEE Vehicle Power and Propulsion Conference (VPPC), Oct 2014, pp. 1–6.
[9] P. Y. Shinzato, D. F. Wolf, and C. Stiller, “Road terrain detection: Avoiding common obstacle detection assumptions using sensor fusion,” in 2014 IEEE Intelligent Vehicles Symposium Proceedings. IEEE, 2014, pp. 687–692.
```

## 2. POINT CLOUD TOP-VIEW ROAD DETECTION
