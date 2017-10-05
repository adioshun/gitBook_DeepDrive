http://docs.opencv.org/trunk/dd/d53/tutorial_py_depthmap.html




### Disparity와 3D depth의 관계
Under **fronto-parrallel** assumption, the relation between **disparity** and **3D depth** is: 

$$
d = f \times \frac{T}{Z}
$$, 
- d is the disparity
- f is the focal length
- T is the baseline 
- Z is the 3D depth. 

If you treat the image center as the principal point, the 3D coordinate system is settled. 

Then for a pixel (px,py), its 3D coordinate (X, Y, Z) is: 
$$ X = (px-cx)*Z/f$$
$$ Y = (py-cy)*Z/f$$
$$ Z = f*T/d$$

- `cx`, `cy` are the pixel coordinate of image center.

> https://stackoverflow.com/questions/11406849/using-opencv-to-generate-3d-points-assuming-frontal-parallel-configuration

