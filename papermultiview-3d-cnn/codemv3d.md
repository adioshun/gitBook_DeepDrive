![](http://i.imgur.com/Myw0TVr.png)

## 0. 환경 준비

* install tensorflow-gpu and CUDA. 

A Nvidia GPU card with computation capability &gt; 3  
CUDA  
Python3.5 for MV3D related code  
Tensorflow-GPU\(version&gt;1.0\)  
Python2.7 for ROS related script

```bash
conda create -n "mv3d3" python=3.5
source activate mv3d3
conda install tensorflow-gpu 
conda install Cython matplotlib

```

### 0.1 GPU용으로 설정 변경

`src/net/lib/setup.py` and `src/lib/make.sh` : "arch=sm\_30"

```
# Which CUDA capabilities do we want to pre-build for?
# https://developer.nvidia.com/cuda-gpus
#   Compute/shader model   Cards
#   6.1              P4, P40, Titan X so CUDA_MODEL = 61
#   6.0                    P100 so CUDA_MODEL = 60
#   5.2                    M40
#   3.7                    K80
#   3.5                    K40, K20
#   3.0                    K10, Grid K520 (AWS G2)
#   Other Nvidia shader models should work, but they will require extra startup
#   time as the code is pre-optimized for them.
CUDA_MODELS=30 35 37 52 60 61
```

test

```python
import tensorflow as tf
sess = tf.Session()
print(tf.__version__) # version more than v1.
```

## 1. 데이터 다운로드

![](http://i.imgur.com/TqGRi0G.png)

[The KITTI Vision Benchmark Suite Raw Data](http://www.cvlibs.net/datasets/kitti/raw_data.php)

## 2. ./src/make.sh

### 2.1 실행 방법

```
cd src
source activate didi
sudo chmod 755 ./make.sh
./make.sh
```

> 아래 [2.2]를 직접 실행 하는것 추천 

### 2.2 실행시 진행 내용

    #- `python ./net/lib/setup.py build_ext --inplace` : Fast R-CNN (MS)

    #- 'bash ./net/lib/make.sh` : building psroi_pooling layer

    #- build required .so files
    ln -s ./net/lib/roi_pooling_layer/roi_pooling.so ./net/roipooling_op/roi_pooling.so
    ln -s ./net/lib/nms/gpu_nms.cpython-35m-x86_64-linux-gnu.so ./net/processing/gpu_nms.cpython-35m-x86_64-linux-gnu.so
    ln -s ./net/lib/nms/cpu_nms.cpython-35m-x86_64-linux-gnu.so ./net/processing/cpu_nms.cpython-35m-x86_64-linux-gnu.so
    ln -s ./net/lib/utils/cython_bbox.cpython-35m-x86_64-linux-gnu.so ./net/processing/cython_bbox.cpython-35m-x86_64-linux-gnu.so

에러 : `"tensorflow.python.framework.errors_impl.NotFoundError: YOUR_FOLDER/roi_pooling.so: undefined symbol: ZN10tensorflow7strings6StrCatB5cxx11ERKNS0_8AlphaNumES3"`

* it is related to compilation of roi\_pooling layer.
* A simple fix will be changing "GLIBCXX\_USE\_CXX11\_ABI=1" to "GLIBCXX\_USE\_CXX11\_ABI=0" in "src/net/lib/make.sh" \(line 17\)

## 3. Preprocess data \(`./src/data.py`\)

* we get the required inputs for MV3D net. It is saved in kitti. 
  * didi data 이용시 `utils/bag_to_kitti` 실행 필요 
* for process raw data to input network input format
* Ouput : 
  * Lidar bird eye view features
  * Lidar front view features
  * RGB image 
  * Ground Truth label
  * Ground bounding box coordinate
  * time stamp

| ![](http://i.imgur.com/bb67R50.png) | ![](http://i.imgur.com/AbdY7YU.png) |
| --- | --- |


## 4. trainer.py

---

File Structure

```
├── data   <-- all data is stored here. (Introduced in detail below)
│   ├── predicted  <-- after prediction, results will be saved here.
│   ├── preprocessed   <-- MV3D net will take inputs from here(after data.py) 
│   └── raw <-- raw data
├── environment_cpu.yml  <-- install cpu version.
├── README.md
├── saved_model                 <--- model and weights saved here. 
├── src        <-- MV3D net related source code 
│   ├── config.py
│   ├── data.py
│   ├── didi_data
│   ├── kitti_data
│   ├── lidar_data_preprocess
│   ├── make.sh
│   ├── model.py
│   ├── mv3d_net.py
│   ├── net
│   ├── play_demo.ipynb
│   ├── __pycache__
│   ├── tracking.py   <--- prediction after training. 
│   ├── tracklets
│   └── train.py    <--- training the whole network. 
│── utils    <-- all related tools put here, like ros bag data into kitti format
│    └── bag_to_kitti  <--- Take lidar value from ROS bag and save it as bin files.
└── external_models    <-- use as a submodule, basically code from other repos.
    └── didi-competition  <--- Code from Udacity's challenge repo with slightly modification, sync with Udacity's new
     updates regularly.
```

Related data are organized in this way. \(Under /data directory\)

```
├── predicted <-- after prediction, results will be saved here.
│   ├── didi <-- when didi dataset is used, the results will be put here
│   └── kitti <-- When kitti dataset used for prediction, put the results here
│       ├── iou_per_obj.csv   <-- What will be evaluated for this competition, IoU score
│       ├── pr_per_iou.csv   <--precision and recall rate per iou, currently not be evaluated by didi's rule
│       └── tracklet_labels_pred.xml  <-- Tracklet generated from prediction pipeline. 
├── preprocessed  <-- Data will be fed into MV3D net (After processed by data.py)
│   ├── didi <-- When didi dataset is processed, save it here
│   └── kitti <-- When Kitti dataset is processed, save it here
│       ├── gt_boxes3d
│           └── 2011_09_26
│               └── 0005
|                   |___ 00000.npy
├       |── gt_labels
│           └── 2011_09_26
│               └── 0005 
|                   |___ 00000.npy
|       ├── rgb
│           └── 2011_09_26
│               └── 0005 
|                   |___ 00000.png
|       ├── top
│           └── 2011_09_26
│               └── 0005 
|                   |___ 00000.npy
|       └── top_image
|           └── 2011_09_26
|               └── 0005 
|                   |___ 00000.png
└── raw  <-- this strictly follow KITTI raw data file format, while seperated into didi and kitti dataset. 
    ├── didi <-- will be something similar to kitti raw data format below. 
    └── kitti
        └── 2011_09_26
            ├── 2011_09_26_drive_0005_sync
            │   ├── image_02
            │   │   ├── data
            │   │   │   └── 0000000000.png
            │   │   └── timestamps.txt
            │   ├── tracklet_labels.xml
            │   └── velodyne_points
            │       ├── data
            │       │   └── 0000000000.bin
            │       ├── timestamps_end.txt
            │       ├── timestamps_start.txt
            │       └── timestamps.txt
            ├── calib_cam_to_cam.txt
            ├── calib_imu_to_velo.txt
            └── calib_velo_to_cam.txt
```



