|논문명 |Know Your Limits: Accuracy of Long Range Stereoscopic Object Measurements in Practice |
| --- | --- |
| 저자\(소속\) | Peter Pinggera\(\) |
| 학회/년도 | ECCV 2014, [논문](http://www.cvlibs.net/projects/autonomous_vision_survey/literature/Pinggera2014ECCV.pdf) |
| 키워드 | |
| 데이터셋(센서)/모델 | |
| 관련연구||
| 참고 |[Youtube](https://www.youtube.com/watch?v=yNYX8NkoGfo) |
| 코드 | |



# 

- 양안 비젼 응용 서비스 들은 장애물의 속도와 위치를 알기 위해서 높은 수준의 precision를 요구 한다. `Modern applications of stereo vision, such as advanced driver assistance systems and  autonomous vehicles, require highest precision when determining the location and velocity of potential obstacles. `
    - 그렇기 떄문에 **Subpixel disparity**의 정확도는 중요 하다. `Subpixel disparity accuracy in selected image regions is therefore essential.`

- KITTI 같은 데이터 셋은 `dense matching performance`측정하는데 좋은 데이터셋이지만  `local sub-pixel matching accuracy`을 다루기에는 충분하지 않다. `Evaluation benchmarks for stereo correspondence algorithms, such as the popular Middlebury and KITTI frameworks, provide important reference values regarding dense matching performance, but do not sufficiently treat local sub-pixel matching accuracy. `

- In this paper, we explore this important aspect in detail. 

- We present a comprehensive statistical evaluation of selected state-of-the-art stereo matching approaches on an extensive dataset and establish reference values for the precision limits
actually achievable in practice. 

- For a carefully calibrated camera setup under real-world imaging conditions, a consistent error limit of 1/10 pixel is determined. 

- We present guidelines on algorithmic choices derived from theory which turn out to be relevant to achieving this limit in practice.

