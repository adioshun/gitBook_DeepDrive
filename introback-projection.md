|논문명|[네이버 지식백과] 사용자 상황인식|
|-|-|
|저자(소속)|한국전자통신연구원(ETRI)|
|학회/년도| 2008. 12, [논문](http://terms.naver.com/entry.nhn?docId=3473050&cid=58468&categoryId=58468)|
|키워드|단일 카메라, 연속된 2장의 사진, SIFT[5] 특징점, 삼각측량|

> 최근 스테레오보다는 단안 카메라에 집중하는 분위기(eg. 컨티넨탈)
> 거리 측정값은 정확하진 않지만 레이더가 있으니 융합해서 쓰면 스테레오보다 나은 성능. 스테레오 역시 일정거리를 넘어서면 거리값도 신뢰하기 힘듬


## 단안 카메라 

![](https://i.imgur.com/h9crnc1.png)

로봇과 사람이 동일한 평면상에 있고, 카메라는 지면과 평행하다고 가정해보자. 여기서 h는 지면에서 카메라까지의 높이이니 미리 알고 있는 값이다. 카메라에서 사람의 발끝을 향하는 각도인 θ2는 위에서 사람이 오른쪽에 있는지 왼쪽에 있는지를 구하는 것과 동일한 방법으로 영상 내에 반영된 위치에서 구해낼 수 있다. 여기서 카메라에서 영상까지의 거리를 D라 하면, tan(θ2)=h/D이고, 이 중 h와 θ2는 모두 이미 알고 있는 값이므로, D=h/tan(θ2)라는 간단한 식으로 구할 수 있다.

Beyond stereo/triangulation cues, there are also numerous monocular cues—such as texture variations and gradients defocus, color/haze, etc.—that contain useful and important
depth information.

Depth estimates from monocular cues is entirely based on prior knowledge about the environment and global structure of the image. 

Depth estimation from monocular cues is a difficult task, which requires that we take into account the global structure of the image.


---




