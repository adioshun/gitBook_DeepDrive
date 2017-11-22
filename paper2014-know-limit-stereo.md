|논문명 |Know Your Limits: Accuracy of Long Range Stereoscopic Object Measurements in Practice |
| --- | --- |
| 저자\(소속\) | Peter Pinggera\(\) |
| 학회/년도 | ECCV 2014, [논문](http://www.cvlibs.net/projects/autonomous_vision_survey/literature/Pinggera2014ECCV.pdf) |
| 키워드 | |
| 데이터셋(센서)/모델 | |
| 관련연구||
| 참고 |[Youtube](https://www.youtube.com/watch?v=yNYX8NkoGfo) |
| 코드 | |



# Know Your Limits

- 양안 비젼 응용 서비스 들은 장애물의 속도와 위치를 알기 위해서 높은 수준의 precision를 요구 한다. `Modern applications of stereo vision, such as advanced driver assistance systems and  autonomous vehicles, require highest precision when determining the location and velocity of potential obstacles. `
    - 그렇기 떄문에 **Subpixel disparity**의 정확도는 중요 하다. `Subpixel disparity accuracy in selected image regions is therefore essential.`

- KITTI 같은 데이터 셋은 `dense matching performance`측정하는데 좋은 데이터셋이지만  `local sub-pixel matching accuracy`을 다루기에는 충분하지 않다. 
    - `Evaluation benchmarks for stereo correspondence algorithms, such as the popular Middlebury and KITTI frameworks, provide important reference values regarding dense matching performance, but do not sufficiently treat local sub-pixel matching accuracy. `


- 본 논문에서는 `In this paper, we explore this important aspect in detail. `

    - 최신 스테레오 매칭 접근법들에 대하여 평가를 진행 하였다. `We present a comprehensive statistical evaluation of selected state-of-the-art stereo matching approaches on an extensive dataset and establish reference values for the precision limits actually achievable in practice. `

    - 좋은 알고리즘 선택을 위한 가이드 라인 제공 `We present guidelines on algorithmic choices derived from theory which turn out to be relevant to achieving this limit in practice.`

## 1. Introduction

- 초창기 `Middlebury` 데이터셋으로 시작으로 활발한 연구가 시작됨 `Part of the practicability and performance of modern stereo vision algorithms can arguably be attributed to the seminal Middlebury benchmark study[27], which first provided a comprehensive framework for evaluation and enabled algorithm analysis and comparison. `


- 10년후 `KITTI` 데이터넷으로 더욱 발전함 `Ten years later, the KITTI project [10] presented a new realistic and more challenging benchmark with stereo imagery of urban traffic scenes, triggering a new wave of improved stereo vision algorithms.`


- 위 데이터들은 **dense stereo correspondence**에 초점을 두고 있으며, dense & accurate GT 데이터를 필요로 한다. `These major benchmark studies focus on dense stereo correspondence and are naturally required to provide both dense and accurate ground truth data. `

- 성능 평가는 Algorithm performance is mainly judged by the percentage of pixels whose disparity estimates fall within a given accuracy threshold. 
    - The threshold is commonly setto several pixels (KITTI), or half pixels at best (Middlebury).

