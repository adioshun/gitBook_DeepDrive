# PCL Library 

> [홈페이지](http://pointclouds.org)

> [Python bindings to the pointcloud library (pcl) ](https://strawlab.github.io/python-pcl/)

## 1. 설치 

- 설치 요구 사항 : 
    - Python 2.7.6, 3.4.0, 3.5.2
    - pcl 1.7.0
    - Cython <= 0.25.2


1. pcl 설치 
```
sudo add-apt-repository ppa:v-launchpad-jochen-sprickerhof-de/pcl
sudo apt-get update
sudo apt-get install libpcl-all
```

> `add-apt-repository`설치 : `sudo apt-get install software-properties-common`

2. cython설치 
```
pip install Cython
```

3. python-pcl 설치 
```
git clone https://github.com/strawlab/python-pcl.git
cd python-pcl
sudo python setup.py clean
sudo make clean
sudo make all
sudo python setup.py install
```




## 2. 활용 

예제 

```python
import pcl
import numpy as np
p = pcl.PointCloud(np.array([[1, 2, 3], [3, 4, 5]], dtype=np.float32))
seg = p.make_segmenter()
seg.set_model_type(pcl.SACMODEL_PLANE)
seg.set_method_type(pcl.SAC_RANSAC)
indices, model = seg.segment()
```