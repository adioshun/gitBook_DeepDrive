| 논문명 | Convolutional Neural Network Information Fusion based on Dempster-Shafer
Theory for Urban Scene Understanding |
| --- | --- |
| 저자\(소속\) | Masha (Mikhal) Itkina\(스탠포\) |
| 학회/년도 | cs231n 2017, [리포트](http://cs231n.stanford.edu/reports/2017/pdfs/632.pdf) |
| 키워드 |  |
| 데이터셋(센서)/모델 |  |
| 참고 |  |
| 코드 |  |

> Dempster-Shafer 증거이론은 1967 년 Arthur Dempster 가 주창하여 1976 년 Glenn Shafer 가 발전시킨 것으로 이 이론에서는 확신의 정도가 구간으로 표현되고, P(H) 와 P(￢H) 는 더하여 반드시 1 이 될 필요가 없다

# Fusion Framework Dempster-Shafer Theory

Dempster-Shafer은 센서퓨전 프레임워크로, 도심환경에서 동적으로 가려진 물체를 감지 할수 있다. `Dempster-Shafer theory provides a sensor fusion framework that autonomously accounts for obstacle occlusion in dynamic, urban environments.`

하지만, 움직이는 물체에 대하여서는 파라미터 튜닝 작업이 필요 하다. `However, to discern static and moving obstacles, the Dempster-Shafer approach requires manual tuning of parameters dependent on the situation and sensor types. `

제안 방식은 Dempster-Shafer퓨젼 알고리즘을 통해 구해진 probabilistic occupancy grid를 뉴럴 네트워크 입력으로 하여 offset을 학습하고 개선된 결과가 나오게 한다. `The probabilistic occupancy grid (output of the Dempster-Shafer information fusion algorithm) was provided as input to the neural network. The network then learned an offset from the original DST result to improve semantic labeling performance.`




