# PCL Library 

> [Python bindings to the pointcloud library (pcl) ](https://github.com/strawlab/python-pcl)

## 1. 설치 

```
sudo add-apt-repository ppa:v-launchpad-jochen-sprickerhof-de/pcl
sudo apt-get update
sudo apt-get install libpcl-all
```

> `add-apt-repository`설치 : `sudo apt-get install software-properties-common`

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