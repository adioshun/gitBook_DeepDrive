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
- First, it is able to learn multi-scale representations as it enjoys the benefits of more base networks, which could form the same fused network, other than the initial group of base networks. 
- Second, in our suggested fused net formed by one deep and one shallow base networks, the flows of the information from the earlier intermediate layer of the deep base network to the output and from the input to the later intermediate layer of the deep base network are both improved. Last, the deep and shallow
base networks are jointly learnt and can benefit from each other. More
interestingly, the essential depth of a fused net composed from a deep
base network and a shallow base network is reduced because the fused
net could be composed from a less deep base network, and thus training
the fused net is less difficult than training the initial deep base network.


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ2MDE5NzcyOF19
-->