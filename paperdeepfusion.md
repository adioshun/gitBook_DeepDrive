|논문명 |Deeply-Fused Nets |
| --- | --- |
| 저자\(소속\) | Jingdong Wang \(MS\) |
| 학회/년도 | May 2016, [논문](https://arxiv.org/abs/1605.07716) |
| 키워드 |DeeplyFusion2016, MV3D에 영향줌 |
| 데이터셋(센서)/모델 | |
| 참고 | |
| 코드 | |

#  DeeplyFusion

중간 representations 을 합치는 기능 수행, 합쳐진 결과는 네트워크의 나머지 부분의 입력으로 작용 
- **Combine** the **intermediate representations** of base networks, 
	- where the **fused output** serves as the **input** of the remaining part of each base network, 
	- and perform such combinations deeply over **several intermediate representations**

제안 알고리즘의 장점 
1. 멀티 스캐일 표현들을 학습 할수 있음 `it is able to learn multi-scale representations as it enjoys the benefits of more base networks, `
	- which could form the same fused network, other than the initial group of base networks. 
2. 성능 개선, Second, in our suggested fused net formed by **one deep** and one **shallow base networks**
	- the flows of the information from the earlier intermediate layer of the deep base network to the output and from the input to the later intermediate layer of the deep base network are **both improved**. 
3. 성능 개선, Last, the deep and shallow base networks are **jointly learnt** and can **benefit from each other**. 

특징 
- 사용된 두 네트워크(Deep & Shallow) 모두 깊이가 줄어듬 the essential depth of a fused net composed from a deep base network and a shallow base network is **reduced**
- 왜냐 하면.. because the fused net could be composed from a less deep base network, 
- 덕분에 ....and thus training the fused net is less difficult than training the initial deep base network.

## 1 Introduction
<!--stackedit_data:
eyJoaXN0b3J5IjpbNTA0MzQ0MzQ1XX0=
-->