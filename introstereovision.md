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
- Stereo matching을 위한 2가지 조건
 - Camera Parameters
 - Correspondence
 
Camera Parameters를 구하는 작업을 Calibration 이라 한다.
Multi images에서 각 이미지 간에 Correspondence(대응점) 을 찾아야 Stereo matching을 할 수 있겠지?
Correspondence를 찾기 위해서는 각 이미지들이 rectification이 되어있어야 한다.
(epipoline 등의 개념은 이 때 사용되어진다.)
 
- Rectified image 에서 Correspondence 찾기
 - ICA : Ideal 카메라를 가정하며, 같은 밝기 값에서 대응점을 찾아내는 것이다.(=> Ambiguity가 발생하는데 이는 Mask를 통해 해결 가능하다.)
  - 그러나 ICA는 이상적인 모델로 실제로 실현하기에 어려움이 따른다.
  1) Camera property 가 다르다.
    - a) preprocessing compensation, b) robust measure 를 이용하여 해결
  2) Non Lambertian surface
    - 광원이 물체에 부딪혀 반사될 때, 두가지 종류를 가진다. 첫째로 광원이 입사각으로 바로 반사되는 specular와 둘째로 흡수에 의해 전방향으로 퍼지는 diffuse로 나뉜다. 해결책으로는 a) speclar removal, b) robust measure 를 이용해 해결한다.
 
 - Window 사용시, maximum disparity 범위 내에서 minimum cost를 대응점으로 찾아 disparity를 구한다.
    Window size가 작을수록 noise에 민감하며, window size가 클수록 ambiguity을 줄일 수 있다.
 - occlusion 이란 카메라의 보이지 않는 부분에 대한 문제를 뜻한다.
 
  여기까지가 Local method를 이용한 방법이다. Global method의 경우는 1) 대응점에 대한 여러 조건 -> 2) Cost -> 3) Minimize 과정을 거쳐 구하는 것이다.
 
⊙ Issue
 1) ICA - preprocessing
           - robust measure
 2) local method - window
                       - occlusion
 3) global method - cost
                         - minimazation
 
⊙ Stereo matching processing
 1) preprocessing : specular, WB, noise removal
 2) raw cost : pixel-by-pixel ... (AD, etc.)
 3) aggregation : window 통한 SAD, etc.
 4) optimization
 5) post processing : false match 없애기(unique minimum check, consistency check)
 
⊙ Feature based stereo matching -> 잘 대응 되는 점 몇개만 뽑아 이용, 정확도 및 스피드 향상
  1) what is the feature, 2) how to extract, 3) how to describe
 
⊙ Wide band line - occlusion으로 인해 대응점 찾기가 힘들다.


---
## semi-global matching

- 실시간 동작이 가능한 알고리즘 : SGM(semi-global matching)
        - SGM의 disparity matching cost 함수를 조금씩 수정하여 사용
        - eg. 다임러의 경우 이 알고리즘을 FPGA로 구현해서 상용차량에 적용시켰습니다.
        - [Dense Stereo Processing using Semi-Global Matching](http://www.nvidia.com/content/events/sc11/pdf/ke-zhu.pdf)
        - [Code](https://github.com/dhernandez0/sgm)






---



