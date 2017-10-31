|논문명 |A comparative study of data fusion for RGB-D based visual recognition |
| --- | --- |
| 저자\(소속\) | JordiSanchez-Riera\(\) |
| 학회/년도 | 2016, [논문](http://www.sciencedirect.com/science/article/pii/S0167865515004298) |
| 키워드 | RGB-D, Fusion|
| 데이터셋(센서)/모델 | |
| 관련연구||
| 참고 | |
| 코드 | |


# A comparative study of data fusion

- 딥러닝의 발전과 함께 데이터 퓨전 분야에 대한 오래된 질문들에 대한 해답을 찾을수 있을까?

- 오래된 질문 
	- 데이터를 합치는데 좋은 방법은 무었인가? `What is the most effective way to combine data for various modalities? `
	- 데이터 퓨전이 성능에 영향을 미치는가? `Does the fusion method affect the performance with different classifiers?`

- 본 논문 
	- 딥러닝을 이용한 early & late fusion비교 ` we present a comparative study for evaluating early and late fusion schemes with several types of SVM and deep learning classifiers on two challenging RGB-D based visual recognition tasks: hand gesture recognition and generic object recognition. `

## 1. Introduction

- 다음 질문들에 대한 답을 본 논문에서 살펴봄 
- What is the most effective way to integrate heterogeneous information from multimodal sensors? 
- Does the design of the fusion method depend on the corresponding applications? 
- Does the employed classification algorithm have an impact on the fusion method and the resultant accuracy?

- 퓨젼의 큰 분류는 2가지 이다. early fusion & late fusion `In the literature, early fusion and late fusion are the two most popular fusion schemes. `

While early fusion approaches integratedata from different modalities before being passed to a classifier,late fusion approaches integrate, at the last stage, of the responsesobtained after individual features learning the model for each descriptor.Although the employment of fusion schemes is a commontechnique in audio-visual domains [6,22,25], the works using RGBDdata [13,18,21,30] are still developed through a unimodal fashion,lacking of studies on how to effectively integrate color and depthmodalities [2,3,20,30]. 

In addition, although deep learning methodshave recently reported promising results when applied to variousmultimedia applications [11,23,27,31], there is no explicit comparisonbetween the deep architectures and traditional classifiers toexplore which is the most suitable classification paradigm for visualrecognition with RGB-D data. 

Typically, in RGB-D applicationsa depth image is used to segment better the object of interest andthen some features are computed for depth and RGB images to afterwardstrain a classifier [8,9,12]. 

In contrast, we want to focuson different levels of feature fusion and deep learning classifiers,where an object itself is already localized and segmented from the image, and no pre-processing steps or other machine learningtechniques are needed.Therefore, in this work we conduct a comparative evaluationstudy of RGB-D visual recognition tasks by assessing the effectivenessof various settings, which include different fusion schemes(e.g., early fusion vs. 

late fusion) and two state-of-the-art learningmechanisms (e.g., SVM vs. deep learning). 

To the best of ourknowledge, this work is the first to explicitly address the fusionevaluation for RGB-D data with deep learning classifiers.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzg3NDkyNTZdfQ==
-->