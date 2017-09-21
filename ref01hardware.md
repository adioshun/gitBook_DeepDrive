

![](http://i.imgur.com/SAZPK7T.png)

## LiDAR

![](https://cdn-images-1.medium.com/max/2000/1*ZXWTdEZ3NYN5qz87gXWeGA.png)

MCU는 Nvidia에서 나온 Jetson TK1을 쓰고 있고, Lidar는 Hokuyo ust-10lx \(약140만원\)

- LiDAR sensors : 물체와의 거리측정용 calculating the time taken by a pulse of light to travel to an object and back to the sensor. 

- LiDAR can provide a 360° 3D view of the obstacles

- radar or camera sensors에 비하여 가격이 비싸다. 

http://ssan664.tistory.com/716



- 1960년부터 개발 시작, 2007 DARPA Autonomous Driving Challenge이후 차량에 적용 

거리 오차 : ±2cm

측정 거리 : ~60m(센서 마다 다름~200m)

> Startup : [sweep](http://scanse.io/), $349.00

제약 : 
- LiDAR requires optical filters to remove sensitivity to ambient light and to prevent spoofing from other LiDARs. 
- the laser technology used has to be “eye-safe”. 

More recently the move has been to replace mechanical scanning LiDAR, that physically rotate the laser and receiver assembly to collect data over an area that spans up to 360° with Solid State LiDAR (SSL) that have no moving parts and are therefore more reliable especially in an automotive environment for long term reliability. 

SSLs currently have lower field-of-view (FOV) coverage but their lower cost provides the possibility of using multiple sensors to cover a larger area.



## Radar (radio direction and ranging)

- determine the velocity, range and angle of objects.탐지 뿐만 아니라, 추적도 가능 

- 2차 세계 대전때부터 개발된 기술,radio waves를 이용하여 거리 탐지 

Radar doesn’t necessarily give you granularity of LIDAR, but Radar and LIDAR are very complimentary, and it’s definitely not either/or.

- 다른 센서에 비하여 계산 부하가 작음 

- 거의 모든 환경에 적용 가능, 기상환경이 좋지 않아도 좋은 효과를 보임 

RADAR sensors 분류(거리)
- Short Range Radar (SRR) 0.2 to 30m range 
- Medium Range Radar (MRR) in the 30-80m range 
- Long Range Radar (LRR) 80m to more than 200m range. : ACC, AEBS용으로 사용 

제약 사항 : a car cutting in front of your vehicle, detecting thin profile vehicles such as motorcycles being staggered in a lane and setting distance based on the wrong vehicle due to the curvature of the road. 

해결 방법 : a radar sensor could be paired with a camera sensor in the vehicle to provide additional context to the detection.



## Camera

제약 사항 : adverse weather conditions and variations in lighting. 

장점 : texture, color and contrast information을 습득할수 있는 유일한 장비, Classification 수행 가능 




![](https://i.imgur.com/ExCCr82.png)





## Camera Only Approach company

- Tesla

- Comma 

- AutoX.

---

- [Choosing the Optimum Mix of Sensors for Driver Assistance and Autonomous Vehicles](https://blog.nxp.com/wp-content/uploads/2017/05/Ors_NXP_2017_Embedded_Vision_Summit_Final.pdf): pdf