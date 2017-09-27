|논문명|Fusing LIDAR and Images for Pedestrian Detection using Convolutional Neural Networks|
|-|-|
|저자(소속)| Joel Schlosser (Georgia Tech)|
|학회/년도| ICRA 2016, [논문](http://ieeexplore.ieee.org/abstract/document/7487370/)|
|키워드|KITTI, up-sampling, HHA |
|참고||
|코드||

# Fusing LIDAR and Images for Pedestrian Detection

1. We incorporate LIDAR by `up-sampling` the point cloud to a `dense depth map` 
2. We extracting three features representing different aspects of the 3D scene
3. We use those features as extra image channels

Specifically, we leverage recent work on HHA representations, adapting the code to work on up-sampled LIDAR rather than Microsoft Kinect depth maps.
 - `HHA representations가 up-sampled LIDAR data에 applicable을 보임` 
 
we show that
- 1) using HHA features and RGB images performs better than RGB-only, even without any fine-tuning using large RGB web data
- 2) fusing RGB and HHA achieves the strongest results if done late, but, under a parameter or computational budget, is best done at the early to middle layers of the hierarchical representation, which tend to represent midlevel features rather than low (e.g. edges) or high (e.g. object class decision) level features, 
- 3) some of the less successful methods have the most parameters, indicating that increased classification accuracy is not simply a function of increased capacity in the neural network.

## I. INTRODUCTION

Fusion Idea : This idea arises from the intuition that different sensor types capture `different aspects of a scene`, and that an `improved solution` would combine the strengths of each sensor type.

차별점 : we leverage the depth information to produce HHA image channels (horizontal disparity, height above ground, and angle) as described in [9]
- this representation is successful even on up-sampled LIDAR data