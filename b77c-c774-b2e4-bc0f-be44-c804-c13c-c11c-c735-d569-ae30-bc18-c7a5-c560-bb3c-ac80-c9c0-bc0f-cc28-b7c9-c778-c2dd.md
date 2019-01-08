# [라이다 및 비전 센서 융합 기반 장애물 검지 및 차량 인식](http://dcoll.ajou.ac.kr:9080/dcollection/public_resource/pdf/000000017793_20190108134401.pdf)

> 아주대, 임동진, 석사학위, 2014 

라이다를 이용한 다양한 전방 장애물 및 비전 센서와의 융합을 통한 차량 인식 알고리즘을 제안
- 라이다 포인트 통합을 위한 ABD 및 IEPF 알고리즘
- 추적을 위한 PDAF 알고리즘

구성 
- 트랙을 생성, 삭제하는 **트랙 관리기**
- 라이다 트랙과 비전 정보와의 상대 위치정보를 이용한 **센서 퓨전 알고리즘**


## 1 전체 동작 과정 

![](https://i.imgur.com/1fVZ5Qr.png)

### 1.1 clustering

 출력 정보의 통합을 위하여 Adoptive Breakpoint Detector (ABD)를 이용한 segmentation 을 수행 후 Iterative End Point Fit (IEPF) 알고리즘을 이용한 추가 분할을 수행한다[8]
    - ABD : 이웃한 점들의 거리 정보를 이용하여 불연속점 여부 파악, 한계값 이용 
    - IEPF : 선형 판단, 가드레일(??)

### 1.2 Feature etraction 

추가적인 정보 생성을 위한 feature extraction 을 수행한다[9].
- x,y, 넓이, 각도  
    
![](https://i.imgur.com/HjLbUpV.png)

### 1.3 추적 

장애물을 지속적으로 추적하기 위해 Probabilistic Data Association filter(PDAF)를 이용하여 segment 들의 위치 정보를 기반으로한 추적 알고리즘을 구성

![](https://i.imgur.com/fWnRpMt.png)


PDAF 는 유효 게이트 내에 들어오는 모든 측정치를 이용하여 검지물을 추적하는 방식이며 이를 위하여 <그림 11>에서와 보는 바와
같이 트랙 추정값과 측정 정보의 연관 여부를 판단하는 Gating, 연관
된 데이터를 통합하는 Residual calculation 파트와 모델의 필터링을
수행하는 Kalman 필터의 Measurment update 와 Time update 로 구성
된다[6]. 

Measurment update 와 Time update 에서 사용한 트랙 모델은 식(7)와 같은 종·횡방향 상대거리 및 상대속도를 상태 변수로 가지고 식(8)와
같은 전이 행렬을 가진 등속도 모델을 사용하여 모델링하였다

![](https://i.imgur.com/579RqcT.png)



### 1.4 트랙 관리기 

Track management 에서는 <그림 12> 와 같은 알고리즘을 이용한 트랙의 생성, 삭제, 유지를 관리하는 역할을 수행

![](https://i.imgur.com/9DKOY1S.png)

## 2. 센서 퓨전 

