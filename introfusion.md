## Kalman Filters

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


### Extended Kalman Filters (EKF)

While the traditional Kalman Filter has many applications its main drawback is that it assumes a linear measurement model and state prediction model. 

This may be a fair assumption under specific conditions but in general real-word systems are non-linear. 

For example. the lidar sensor has a linear measurement update model, whereas, the radar sensor has a non-linear update model. 

The Extended Kalman Filter attempts to solve such problems by linearizing the non-linear state transition functions using Taylor Expansion around the mean location of the original function. 

In addition, the linearization requires that the Jacobian of the state transition is computed.






---
[테슬라] 
Preferred: A doctorate degree in an above discipline with specialization in estimation theory or sensor fusion (some common topics include Kalman filters, Particle filters, Multiple Hypothesis Tracking, other Bayesian approaches more generally, …)

---


센서 퓨전은 여러 개의 센서에서 전송하는 데이터를 지능적으로 결합하여 애플리케이션이나 시스템의 성능을 개선하는 소프트웨어입니다. 즉, 복수의 센서에서 나오는 데이터를 취합하여 개별 센서의 결함을 수정하며 그 결과로 정확한 위치와 방향 정보를 계산할 수 있습니다.