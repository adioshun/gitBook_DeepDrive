
# List 

[Awesome Autonomous Vehicles](https://github.com/takeitallsource/awesome-autonomous-vehicles)

[Bookmark of 3D CNN Rearch](https://github.com/NotAndOr/bookmarks/blob/master/20170203.md)

# Project

[Project: Development of AEB System for Pedestrian Protection (4th year)](https://github.com/nlkim0817/ProjAEB_4thYear)

# 참고 논문

- [3D Convolutional Neural Networks — A Reading List](http://davidstutz.de/3d-convolutional-neural-networks-a-reading-list/)



---
[3D Vehicle Detection](https://experiencor.github.io/sdc_3d.html)

1. Detect 2D BBoxes of other vehicles visible on CAMERA frame. This can be achieved by YOLOv2 or SqueezeDet. It turns out that SqueezeDet works better for this job and is selected.

2. Determine the dimension and the orientation of detected vehicles. As demonstrated in [https://arxiv.org/abs/1612.00496], dimension and orientation of other vehicles can be regressed from the image patch of corresponding 2D BBoxes.

3. Determine the location in 3D of detected vehicles. This can be achived by localizing the point cloud region whose projection stays within the detected 2D BBoxes.