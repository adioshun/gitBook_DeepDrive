#### Improving 3D perception for Object Detection, Classification and Localization using Fused Multi-modal Sensors [[링크]](http://cse.msu.edu/~gonza647/improving-3d-perception.pdf)

- 프로젝트 기간 : February 21, 2017

## 2. Motivation/Related Work

- LiDAR의 장단점 : Lidars are good in the sense that it provides excellent range information but is highly sparse with limits to object identification;
- 카메라의 장단점 cameras are good in the sense that it allows better object recognition but are limited to range information [1]. 
- 둘의 퓨전 :  It utilizes the shape and pose information from the lidar in order to assist vision
based techniques for vehicle detection and classification. 

- 기존 연구 : Schwarz et al. [2] uses RGB-D information for efficient object recognition and pose estimation using pre-trained convolutional features that provide a rich, semantically meaningful feature set. 
    - 제약 : But it considers that depth information is already aligned and fused; and datasets used are mainly in indoor settings.

```
[1] F. Zhang, D. Clarke, and A. Knoll, “Vehicle detection based on lidar and camera fusion,”in Intelligent Transportation Systems (ITSC), 2014 IEEE 17th International Conference on. IEEE, 2014, pp. 1620–1625.
[2] M. Schwarz, H. Schulz, and S. Behnke, “Rgb-d object recognition and pose estimation based on pre-trained convolutional neural network features,” in Robotics and Automation (ICRA), 2015 IEEE International Conference on. IEEE, 2015, pp. 1329–1335.
```

## 3.  Project Plan
The goal itself can be split into several parts; 
- multi-modal fusion in the first part
- object recognition and localization on top of that fusion.

퓨전시 문제점 : `How would we fuse lidar and camera when`
- lidar data is already very sparse and 
- its Field of View (FOV) overlaps partially with only FOV of the camera. 

해결법 
- Firstly we need **good calibration parameters** that records both the intrinsics and
extrinsics of the lidar and camera respectively. 
    - Good calibration is necessary for good alignment of lidar points onto the images. 
- Secondly, 이미지와 라이다의 픽셀매칭을 위하여 Depth이미지의 손상된 부분을 복구 하는 알고리즘 필요 `we need to devise a way to inpaint the aligned depth image (super resolution of depth image) in order to have pixel-pixel correspondence between image and lidar. `


### 3.1 

기존 pixel-pixel correspondence 연구들 
- Xue et al. [3] capitalizes on low-rankness of depth image to perform depth inpainting.
    - By using both low-rankness and sparse gradient regularization, it allows gradual depth changes for depth image inpainting. 
- Casterona et al. [4], however suggests to fuse the data and estimate the calibration parameters jointly by exploiting natural alignment of depth and intensity edges.

```
[3] H. Xue, S. Zhang, and D. Cai, “Depth image inpainting: Improving low rank matrix completion with low gradient regularization,” arXiv preprint arXiv:1604.05817, 2016.
[4] J. Castorena, U. S. Kamilov, and P. T. Boufounos, “Autocalibration of lidar and optical cameras via edge alignment,” in Acoustics, Speech and Signal Processing (ICASSP), 2016 IEEE
International Conference on. IEEE, 2016, pp. 2862–2866.
```

### 3.2 detect, classify and localize

- Our second step would be to use the fused information to efficiently recognize (detect, classify and localize) objects. 

- Different learning tasks can be deployed for the process. 

###### [Schwarz et al]

Schwarz et al. [2] 
- uses pre-trained convolutional features on both **color images** and **depth images** from two different networks and 
- uses multi-task learning in order to separate classes and retain pose manifolds. 

###### [Zhang et al]

- On theother hand, Zhang et al. [1] proposes 
    - using features from **stereo camera** for object detection in the hypothesis generation phase, 
    - while using range information from lidar for object classification using hypothesis verification phase. 
        - Range data is mainly used to extract shape parameter (13 fourier coefficients) for object classification. 
- 실험결과 위 방식을 쓰면 SVM만으로도 좋은 결과를 얻을수 있다. `It shows that using this approach, even a single layer SVM can attain the objective of detecting and classifying vehicles efficiently. `



###### [또 다른 방법] 

Another method to look into is how to **learn a joint probabilistic generative model** using both lidar and visual information.

We can learn a hidden/latent variable by using both the range and images; the hidden variables can then be used to infer about the object classes. 

- We can use 
    - variational auto-encoder (VAE) 
    - or generative adversarial networks (GAN) 
- for learning to model the hidden variable before inferring about the object classes.

## 4. Datasets 

There are several publicly available datasets that contains both Lidar and images. We can focus on three datasets. 

### 4.1 The KITTI dataset 
- [5] is built in Germany with mainly three different sensors; 
- two Pointgrey Flea2 video camera (10 Hz, 1392 x 512 pixels), a Velodyne-64E 3D laser scanner (10 Hz, 64 laser beams,range 100 m), and a GPS/IMU localization unit. 
- The calibration parameters and benchmarking of objects are provided along with this dataset. 
- 6 hours of traffic scenarios (number of pedestrians, vehicles, bicyclists etc) are covered in the collection.

```
[5] A. Geiger, P. Lenz, C. Stiller, and R. Urtasun, “Vision meets robotics: The kitti dataset,” International Journal of Robotics Research (IJRR), 2013.
```


### 4.2 The Ford Campus Vision and Lidar dataset 

- [6] is built in the city of Dearborn, Michigan. 
- Data acquisition is performed by means of an IMU unit, a Velodyne 3D laser scanner, and a PointGrey Lady-bug 3 omnidirectional camera system. 
- The dataset includes various small and large loop closure events, ranging from feature rich downtown areas to featureless empty parks.


```
[6] G. Pandey, J. R. McBride, and R. M. Eustice, “Ford campus vision and lidar data set,” International Journal of Robotics Research, vol. 30, no. 13, pp. 1543–1552, 2011.
```

> 둘 모두 같은 센서를 사용하였으므로 같이 사용할수 있음 `We plan to use both the datasets for our purpose since both of them seem to use the same type of sensors for data acquisition.`


