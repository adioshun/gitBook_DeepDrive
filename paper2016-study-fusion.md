|논문명 |A comparative study of data fusion for RGB-D based visual recognition |
| --- | --- |
| 저자\(소속\) | JordiSanchez-Riera\(\) |
| 학회/년도 | 2016, [논문](http://www.sciencedirect.com/science/article/pii/S0167865515004298) |
| 키워드 | RGB-D, Fusion|
| 데이터셋(센서)/모델 | |
| 관련연구||
| 참고 | |
| 코드 | |

> 별 내용 없음 

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

- 퓨젼의 큰 분류는 2가지 이다. **early fusion & late fusion** `In the literature, early fusion and late fusion are the two most popular fusion schemes. `

- 둘의 차이 
	- While **early fusion** approaches integrate data from different modalities **before being passed to a classifier**, 
	- **late fusion** approaches integrate, at the last stage, of the responses obtained **after individual features learning** the model for each descriptor.

- 본 논문에서는 여러 실험을 진행 한다. `Therefore, in this work we conduct a comparative evaluation study of RGB-D visual recognition tasks by assessing the effectiveness of various settings, `
	- which include **different fusion schemes**(e.g., early fusion vs. late fusion) and 
	- two state-of-the-art **learning mechanisms** (e.g., SVM vs. deep learning). 

## 2. Fusion schemes

## 6. Conclusions

- A comparison between two different fusion methods, **early and late fusion**, using RGB-D data is evaluated in this paper. 

- **early fusion** 방식이 효과가 좋다. `First, early fusion is the most effective approach to combine data from different modalities regardless of which classification method or the application is employed. `

- CNN 분류기가 가장 성능이 좋다. `Second, CNN classification algorithm is superior to the other classification algorithms no matter which application is considered. `

- 튜닝후 나머지 분류기들은 성능이 비슷하다. `Third, classifiers using manually tuned features have similar performance, as in the cases of SVMS, SAE, DBN and RBM. `


<!--stackedit_data:
eyJoaXN0b3J5IjpbMjQ4Nzc1MTFdfQ==
-->