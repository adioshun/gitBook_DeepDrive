|논문명|[네이버 지식백과] 사용자 상황인식|
|-|-|
|저자(소속)|한국전자통신연구원(ETRI)|
|학회/년도| 2008. 12, [논문](http://terms.naver.com/entry.nhn?docId=3473050&cid=58468&categoryId=58468)|
|키워드|단일 카메라, 연속된 2장의 사진, SIFT[5] 특징점, 삼각측량|

## 양안 카메라

- 정의 : 두 개의 일반 카메라를 병렬적으로 설치하고, 두 카메라에 투영된 영상 간의 시각에 따른 차이를 분석함으로써 대상까지의 거리를 인지하는 방식이다. 사람이 두 눈을 가지고 거리 정보를 파악하는 것과 같은 방식이다.

- 단점 : 스테레오 카메라를 이용하는 방식은 카메라 간의 거리나 방향 등이 정확하게 고정되어야 하는 등 설치상 번잡스러운 문제도 있지만, 영상의 분석에 상당한 리소스를 소비해야 한다는 점이 문제가 된다.

- 단점 : stereo vision is fundamentally limited by the baseline distance between the two cameras. Specifically, the depth estimates tend to be inaccurate when the distances
considered are large

```
- Ashutosh Saxena, Jamie Schulte and Andrew Y. Ng, "Depth Estimation using Monocular and Stereo Cues", IJCAI-2007
- 리뷰논문 : A Taxonomy and Evaluation of Dense Two-Frame Stereo Correspondence Algorithms, 2002
```
There is a distance limit. It depends on the baseline, the focal length and the pixel pitch.


```

        Baseline * Focal length
Depth = ----------------------
        Pixel disparity * Pixel size

Baseline (b) = 8 cm (80 mm)
Focal length (f) = 6.3 mm
Pixel size (p) = 14 um (0.014 mm)


Depth = (80*6.3)/(1*0.014) = 36,000 mm = 36 m
```

출처 : [stackoverflow](https://stackoverflow.com/questions/19421003/how-field-of-view-changes-depth-estimation-in-stereo-vision), [Stereo Accuracy Chart](https://www.ptgrey.com/KB/10022) (Microsoft Excel format), [Depth Estimation using Monocular and Stereo Cues](https://pdfs.semanticscholar.org/4953/1103099c8d17ea34eb09433688e84de4f35f.pdf)

## 단안 카메라 

![](https://i.imgur.com/h9crnc1.png)

로봇과 사람이 동일한 평면상에 있고, 카메라는 지면과 평행하다고 가정해보자. 여기서 h는 지면에서 카메라까지의 높이이니 미리 알고 있는 값이다. 카메라에서 사람의 발끝을 향하는 각도인 θ2는 위에서 사람이 오른쪽에 있는지 왼쪽에 있는지를 구하는 것과 동일한 방법으로 영상 내에 반영된 위치에서 구해낼 수 있다. 여기서 카메라에서 영상까지의 거리를 D라 하면, tan(θ2)=h/D이고, 이 중 h와 θ2는 모두 이미 알고 있는 값이므로, D=h/tan(θ2)라는 간단한 식으로 구할 수 있다.

Beyond stereo/triangulation cues, there are also numerous monocular cues—such as texture variations and gradients defocus, color/haze, etc.—that contain useful and important
depth information.

Depth estimates from monocular cues is entirely based on prior knowledge about the environment and global structure of the image. 

Depth estimation from monocular cues is a difficult task, which requires that we take into account the global structure of the image.


---




