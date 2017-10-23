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

현실세계에서 Detector의 성능 향상을 위해서는 다음이 중요하다. exploit sources of information along three orthogonal axis: 
- 1) the integration of multiple feature cues (contours, texture, etc.); 
- 2) the fusion of multiple image modalities (color, depth, etc.); 
-  3) the use of multiple views (frontal, lateral, etc.) of the object by
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTMxNDQ3NTk1Nl19
-->