|논문명 | On-Board Object Detection: Multicue, Multimodal, and Multiview Random Forest of Local Experts|
| --- | --- |
| 저자\(소속\) | \(\) |
| 학회/년도 | IEEE Transactions on Cybernetics 2016, [논문](http://ieeexplore.ieee.org/document/7533479/) |
| 키워드 |EarlyFusopn |
| 데이터셋(센서)/모델 |KITTI |
| 참고 | |
| 코드 | |

# EarlyFusion 

여러 정보`(multicue, multimodality, and strong MV classifier)`들이 합쳐 졌을때 어떤 영향을 미치는지 살펴 보겠다 `we provide an extensive evaluation that gives insight into how each of these aspects (multicue, multimodality, and strong MV classifier) affect accuracy both individually and when integrated together`

사용 센서 :  fusion of RGB and depth maps(Lidar)

## 1. Introducion 

현실세계에서 Detector의 성능 향상을 위해서는 다음이 중요하다. `In order to obtain a detector that successfully operates under realistic conditions, it becomes critical to exploit sources of information along three orthogonal axis`
- 1) the integration of multiple feature cues (contours, texture, etc.); 
- 2) the fusion of multiple image modalities (color, depth, etc.); 
- 3) the use of multiple views (frontal, lateral, etc.) of the object 
by learning a strong classifier that accommodates for both different 3-D points of view and multiple flexible articulations.

![](https://i.imgur.com/Kqp3Cl6.png)
```
Fig. 1. General scheme: from RGB images and LIDAR data to object detection. 
- RGB images and LIDAR data synchronized for multimodal representation.
- Multimodal representation based on RGB images and dense depth maps (obtained from LIDAR sparse data). 
- Multicue feature extraction over the multimodal representation. 
- MV detection of different objects.
```

제안 방식은 그림1에서 보는 바와 같이 성능 평가 할것이다. The proposed method (general scheme in Fig. 1) will be evaluated in key objects for autonomous and semi-autonomous vehicles such as pedestrians, cyclists, and cars.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3MzUyODg3OV19
-->