|논문명 | Deep Feature Flow for Video Recognition|
| --- | --- |
| 저자\(소속\) | Xizhou Zhu\(MS\) |
| 학회/년도 | arXiv Nov 2016 ~ [Jun 2017](https://arxiv.org/abs/1611.07715), CVPR 2017 |
| 키워드 | |
| 데이터셋(센서)/모델 | |
| 관련연구||
| 참고 |[Youtube](https://www.youtube.com/watch?v=J0rMHE6ehGw) |
| 코드 |[MXnet](https://github.com/msracver/Deep-Feature-Flow) |

# DeepFeatureFlow

- 아직은 이미지 인식 네트워크를 비디오에 적용할수 없다. 너무 느리고 컴퓨팅 부하가 크다. `Yet, it is nontrivial to transfer the state-of-the-art image recognition networks to videos as per-frame evaluation is too slow and unaffordable.`

- 비디오 인식을 위한 **deep feature flow**제안 `We present deep feature flow, a fast and accurate framework for video recognition. `

- 자원 소보가 큰 Conv.는 sparse key frames에서만 사용하고 `It runs the expensive convolutional sub-network only on sparse key frames `
    - 이후 flow field를 통해서 특징지도를 다음 frame에 전달 한다. `and propagates their deep feature maps to other frames via a flow field. `

- 속도 향상을 가져 왔다. `It achieves significant speedup as flow computationis relatively fast. `

- The end-to-end training of the whole architecture significantly boosts the recognition accuracy. 

- Deep feature flow is flexible and general. 

It is validatedon two video datasets on object detection and semanticsegmentation. 

It significantly advances the practice ofvideo recognition tasks.
