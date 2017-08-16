# The Point Cloud Data


## 1. 개요 

> [Ronny Restrepo](http://ronny.rest/tutorials/module/pointclouds_01/point_cloud_data/)

|The Point Cloud Data|이미지 데이터와 비교 |
|-|-|
|![](http://i.imgur.com/Bc13san.png)|![](http://i.imgur.com/smzFU5N.png)|



- 포인트 클라우드 데이터는 보통 `N x 3` Numpy 배열로 표현 된다. 
    - 각 N 줄은 하나의 점과 맵핑이 되며 
    - 3(x,y,z) 정보를 가지고 있다. 

- Lidar 센서에서 수집한 정보의 경우는 `reflectance`라는 정보가 추가되어 `N x 4` Numpy 배열이 된다. 
    - reflectance : 반사 시간 정보로 보면 된다. 


이미지 데이터
- 항상 양수 이다. 
- 기준점은 왼쪽 위부터 이다. 
- 좌표값은 정수(integer)이다. 

포인트 클라우드 데이터 
- 양수/음수 이다. 
- 좌표값은 real numbered이다. 
- The positive x axis represents forward.
- The positive y axis represents left.
- The positive z axis represents up.

## 2. Creating Birdseye View of Point Cloud Data