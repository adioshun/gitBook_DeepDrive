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

딥러닝은 최근 많은 발전을 보였지만 아직 효율성은 부족하다. 효율성 증대를 위한 다양한 연구가 있따. 

- over-fitting 예방 :  
	- Dropout [8] and 
	- other regularization techniques, such as **weight decay** and **path regularization** [9]
- vanishing gradient problem : 
	- Normalized variance-preserving weight initialization, such as [10–12], 
- both the training speed and the recognition performance :
	-  Batch normalization [13] 
- improve the flow of information and accordingly help train a very deep network. : 
	- Skip-layer connections between layers (including the output layer) and 
	- other network structure modifications, such as **deeply-supervised nets** [14] and its variant [7], Highway [15], ResNet [16], inception-v4 [3]

본 논문의 제안 
- **Base networks 그룹**으로 구성된 deeply-fused neural net 제안`we introduce a deep fusion approach and present a deeply-fused neural net formed by combining a group of base networks`

- 핵심은 기초 네트워크의 중간 representations 들을 퓨전 하는 것이다. 이때의 결과물은 다음 기초 네트워크의 입력으로 활용된다. `The main idea is to perform fusion over the intermediate representations of the base networks, where the fused output serves as the input of the remaining part of each base network, rather than only over the final representations or the final classification scores,and such fusions are performed several times at different intermediate layers.`

- There is a block-exchangeable property `(the block is the subnetwork between two successive fusions in a base network)`:
	-  switch blocks from one base network to another one within one fusion, 
	- resulting in two different base networks with possibly different depth from the originals `(e.g., deep network being less deep and shallow network being less shallow)`, but the fused net is not changed. 

- 다르게 보면 **fused net**은 서로 다른 기초 네트워크의 그룹으로 구성 할수 있다. `In other words, a fused net can be formed by different groups of base networks. `
	- 덕분에 Thus,the deeply-fused net is able to learn multi-scale representations from much more base networks, and even same-scale representations can be different and learnt from different base networks.

- 또 다른 장점은 정보의 흐름이 개선(`칼만필터 효과??`) 된다는 것이다. `There is one more benefit from deep fusion: the flow of information is improved.`
	- Consider the case where one base network is very deep but the other base network is not deep, which is the choice we suggest. 

The earlier intermediate layer in the deeper base network might have a shorter path through the other base network to the output, which implies that the supervision can be fast transformed to the earlier intermediate layer. 

On the other hand, the later intermediatelayer might also have a shorter path from the input, which indicatesthat the input can be fast flowed to the later intermediate layer. 

As a result,training the fused net composed from a very deep base network is less difficultthan training the very deep base network itself. 

Furthermore, the deep and shallowbase networks are jointly learnt and can benefit from each other. 

## 2 Related Work

we mainly discuss two closely-related lines: 
- network structure design 
- network optimization with the aid of another already trained network.

- 예측치의 평균값을 쓰는것은 성능 향Averaging over a set of network predictors, `which we call decision fusion`, is able to improve the generalization accuracy and has been widely used, e.g., to boost the ImageNet recognition performance [1, 16, 19, 20]. 

Multi-column deepneural networks [21] presents an empirical study about decision fusion, later extendedto an adaptive version, weighted averaging with the weights depending onthe input [22]. 

The averaging approach learns each network separately, which isequivalent to learn the network jointly that averages the loss functions. 

Our approach,in contrast, performs the feature fusion deeply over several intermediatelayers and simultaneously learns the representations of the (base) networks.The inception module in GoogLeNet [20] can be viewed as a fusion stage: concatenatethe outputs of several subnetworks with different lengths. 

It is differentfrom our approach using the summation for fusion. 

The GoogLeNet architecture,consisting of a sequence of inception modules, is also a kind of deep fusion, i.e.,deep concatenation fusion. 

But it is not as direct as our deep summation fusion.The output of each subnetwork in an inception module is narrower than theinput of the subsequent inception module. 

Hence it is necessary to append manychannels with all 0 entries in the output to match the size with the input of thesubsequent inception module or add more convolution operations to form thefused network. 

Skip-layer connection, such as deeply-supervised nets [14] and itsvariant [7], Highway [15], ResNet [16], as we will show, resembles our approachand can be regarded as special examples of our approach.The teacher-student framework suggests that learning a hard-trained networkcan benefit from an easily-trained network. 

For instance, FitNets [17] usesthe intermediate representation of a wider and shallower (but still deep) teachernet that is relatively easy to be trained, as the target of the intermediate representationof a thinner and deeper student net. 

Net2Net [18] also uses a teachernet to help train a (wider or deeper) student net, through a function-preservingtransform to initialize the parameters of the student net according to the parametersof the teacher net. 

Our approach, in our suggested choice: includingone deep base network and one shallow (but could still be deep) network, alsouses the shallow network to help train the deep base network, meanwhile thedeep base network also helps train the shallow network, i.e., they benefit fromeach other and are trained simultaneously.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTYyNzEyMDY0NF19
-->