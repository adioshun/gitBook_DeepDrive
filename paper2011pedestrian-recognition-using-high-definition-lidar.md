|논문명 |Pedestrian Recognition Using High-definition LIDAR|
| --- | --- |
| 저자\(소속\) | Kiyosumi Kidono \(Toyota Central R&D Labs\) |
| 학회/년도 | 2011, [논문](http://www.aisl.cs.tut.ac.jp/~jun/pdffiles/kidono-iv2011.pdf) |
| Citation ID / 키워드 | |
| 데이터셋(센서)/모델 | |
| 관련연구||
| 참고 | |
| 코드 |  |



|년도|1st 저자|논문명|코드|
|-|-|-|-|
|||||



# Pedestrian Recognition Using High-definition LIDAR

Two novel features are introduced to improve the classification performance. 
- One is the slice feature, which represents the profile of a human body by widths at the different height levels. 
- The other is the distribution of the reflection intensities of points measured on the target.
    - because each substance has its own unique reflection characteristics

Our approach applies a **support vector machine (SVM)** to train a classifier from these features.

## I. INTRODUCTION

Lidar & Radar 장단점 
- LIDAR has the excellent advantages of high spatial resolution and high range accuracy compared with millimeter wave (MMW) radar, 
- but also the following disadvantages: it does not work robustly in bad weather, such as rain and fog, and its detection range is shorter than MMW radar.


Lidar 큰 장점 : LIDAR which can obtain dense range data


본 논문의 내용 : A method for recognizing pedestrians from 3D range data acquired by high-definition LIDAR is presented in this paper

기존 연구 : A technique for estimating the ego-motion and tracking moving objects using LIDAR has been developed [1], and it has been confirmed that cars, bicycles and pedestrians can be distinguished based on their size and their velocity.

```
[1] T. Miyasaka, Y. Ohama and Y. Ninomiya, ”Ego-Motion Estimation and Moving Object Tracking using Multi-layer LIDAR,” in Proc. 2009 IEEE Intelligent Vehicles Symposium, pp. 151-156, 2009.
```

동작 원리 `The proposed method divides a `
- measured 3D point cloud into clusters corresponding to the objects in the surroundings. 
- Then the pedestrian candidates are extracted by the size of the clusters [3], [4]. 
- Several features are calculated from the 3D point cloud contained in each candidate, 
- and the classifier distinguishes the pedestrians on the basis of the features.
    - Our approach applies a support vector machine (SVM) to train the classifier. 
    - No tracking is considered in this work.
    
```
[3] S. Sato, M. Hashimoto, M. Takita, K. Takagi, and T. Ogawa, ”Multilayer Lidar-Based Pedestrian Tracking in Urban Environments,” in Proc. IEEE Intelligent Vehicles Symposium, pp. 849-854, 2010.
[4] G. Gate, A. Breheret and F. Nashashibi, ”Centralized Fusion for Fast People Detection in Dense Environment,” in Proc. 2009 IEEE Int. Conf. on Robotics and Automation, pp. 76-81, 2009.
```
    
원거리 물체 탐지 성능향상/차별점 `To improve the performance of pedestrian discrimination at a long distance, two novel features are proposed: the slice feature and the distribution of reflection intensities.`
- The slice feature is composed of the widths at different height levels of the human body. 
    - This feature can represent a rough profile of the human body from the head to the legs. 
- The latter feature is also effective for distinguishing pedestrians from false positives. 
    - The wavelength of the laser beam of LIDAR is in the near-infrared (NIR) region. 
    - In the field of spectroscopy [5], it is widely known that NIR lights have different reflection characteristics depending on the materials of the target. 
    - So the reflection intensity is considered to be effective for object recognition.

```
[5] D. Williams, Methods of Experimental Physics, Academic Press, vol. 13, 1976.
```


논문 구성 `This paper is structured as follows:`
- Section II briefly describes previous related work. 
- Section III shows the specification of LIDAR used in this paper. 
- In Section IV, the details of the proposed method for recognizing pedestrians are presented. 
- Section V contains the experimental results and 
- Section VI concludes the paper

