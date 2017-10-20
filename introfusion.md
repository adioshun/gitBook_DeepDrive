## 1. Kalman Filters

> 출처 : [UDACITY SDCE Nanodegree Term 2: Kalman Filters for Sensor Fusion](https://medium.com/@ckyrkou/udacity-sdce-nanodegree-term-2-kalman-filters-for-sensor-fusion-1dde97ea628b)

- 원래 칼만 필터는 연속된 측정값에서 모르는 변수들을 예측(estimates) 할때 사용 한다. `The traditional Kalman Filter is an algorithm that is used to produce estimates for unknown variables given a series of measurements. `

- Bayesian inference을 이용하여 변수들의 결합확률분포 예측한다. `It uses Bayesian inference to estimate a joint probability distribution over the variables for a considered period. `

- 본질적으로 칼만필터는 변수들을 예측 하기 위해 **mean vector** 와 **co-variance matrix**를 유지 하고 있는다.`Essentially, the Kalman Filter maintains a mean vector and co-variance matrix for the estimated variables` 
    - that represent the belief for each possible state through Gaussian functions.

- 이 알고리즘과 변종들`(Extended and Unscented)`은 다음 두 주기 동안 반복된다. `The algorithm and its variants (Extended and Unscented Kalman Filters) iterate on two main cycles:`
 - Measurement Update : In the measurement update step we use new observations from the sensors to update our belief estimation for the unkown variables. 
 - State Prediction. : Then in the state prediction step we predict using a system model (e.g., motion model) the future value of the unknown variables.

![](https://i.imgur.com/I7ymTir.png)


- 멀티센서일때는 각 센서 마다 고유의 measurement update scheme가 있다. `In the case where multiple sensors are used then each sensor has its own measurement update scheme. `

- 멀티 센서여도 The belief about the state of the unkown variables is updated asynchronously each time the measurement is received regardless of the sources sensor.


### 1.2 Extended Kalman Filters (EKF)

- 기본 칼만필터의 단점(drawback)은 it assumes a linear measurement model and state prediction model. 
 - 라이다(LiDar) 센서 has a linear measurement update model
 - 레이더(Radar) 센서 has a non-linear update model. 

- 확장 칼만필터로 해결 가능 `The Extended Kalman Filter attempts to solve such problems `
 - by linearizing the non-linear state transition functions using Taylor Expansion around the mean location of the original function. 
 - In addition, the linearization requires that the **Jacobian** of the state transition is computed.


### 1.3 Unscented Kalman Filters (UKF, 분산점칼만필터)

- 분산점 칼만필터를 이용하여서 **non-linear**현상을 좀더 정확히 모델링 할수 있다. `With Unscented Kalman Filters we are able to accurately model non-linear phenomena. `

- EKF의 **linearizing** 방법 대신, UKF는 **unscented transformatio**를 사용 한다. `Instead of linearizing a non-linear function, UKF uses the unscented transformation to approximate the belief probability distribution.`

- UKF방법은 linearization 보다 성능도 좋고, **Jacobians**연산도 안하게 된다. `In this way it performs better than linearization and does not require to compute Jacobians.`

#### A. 개요 

- UKF의 핵심은 **다변량 가우스 분포**`(Multivariate Gaussian distribution)`를 찾는 것이다. `The main jist(point) of UKF is to find the multivariate Gaussian distribution that approximated the real belief distribution. `

- predicted states가 정규분포`(normaly distributed)`가 아닐수 있지만 UKF는 그렇다고 가정한다. `The predicted states may not be normaly distributed but the UKF assumes that they are.`

- Specifically, the Gaussian distribution approximated the real distribution as close as possible with respect to its mean and covariance matrix.

#### B.  pipeline

- The pipeline for UKF is to 
 - first generate some **samples sigma points** that define the Gaussian. 
 - Then to predict **new sigma points** based on the system model (e.g., motion model). 
 - Using the new sigma points we then **predict the mean and covariance of the Gaussian**. 

- These three steps constitute the **Prediction Step** for the UKF. 

- The **Measurements Update** follows next, 
 - which includes Predicting the new measurements and updating the state belief.




---
[테슬라] 
Preferred: A doctorate degree in an above discipline with specialization in estimation theory or sensor fusion (some common topics include Kalman filters, Particle filters, Multiple Hypothesis Tracking, other Bayesian approaches more generally, …)

---


센서 퓨전은 여러 개의 센서에서 전송하는 데이터를 지능적으로 결합하여 애플리케이션이나 시스템의 성능을 개선하는 소프트웨어입니다. 즉, 복수의 센서에서 나오는 데이터를 취합하여 개별 센서의 결함을 수정하며 그 결과로 정확한 위치와 방향 정보를 계산할 수 있습니다.