## 양안 카메라

- 정의 : 두 개의 일반 카메라를 병렬적으로 설치하고, 두 카메라에 투영된 영상 간의 시각에 따른 차이를 분석함으로써 대상까지의 거리를 인지하는 방식이다. 사람이 두 눈을 가지고 거리 정보를 파악하는 것과 같은 방식이다.

- 단점 : 스테레오 카메라를 이용하는 방식은 카메라 간의 거리나 방향 등이 정확하게 고정되어야 하는 등 설치상 번잡스러운 문제도 있지만, 영상의 분석에 상당한 리소스를 소비해야 한다는 점이 문제가 된다.

- 측정 거리 : 카메라의 해상도, 화각, 초점거리, baseline에 따라 거리정보의 신뢰도
 - 40m+ : KITTI데이터셋 이미지
 - 80m+ : 카메라 해상도를 높히고 초점거리가 긴 렌즈를 사용(단점, 화각이 좁아짐)

- 스테레오 매칭 논문이 대부분 [kitti 데이터](http://www.cvlibs.net/datasets/kitti/eval_stereo.php)써서 벤치마크 결과와 비교

- stereo matching에 요구되는 컴퓨팅 자원이 높은 편, 가격 문제로 요즘 자율주행이나 ADAS에서 스테레오카메라의 입지는 점점 좁아져가고 있습니다.ㅠㅠ 




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

---
## semi-global matching

- 실시간 동작이 가능한 알고리즘 : SGM(semi-global matching)
        - SGM의 disparity matching cost 함수를 조금씩 수정하여 사용
        - eg. 다임러의 경우 이 알고리즘을 FPGA로 구현해서 상용차량에 적용시켰습니다.
        - [Dense Stereo Processing using Semi-Global Matching](http://www.nvidia.com/content/events/sc11/pdf/ke-zhu.pdf)
        - [Code](https://github.com/dhernandez0/sgm)






---



