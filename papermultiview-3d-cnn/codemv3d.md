![](http://i.imgur.com/Myw0TVr.png)

# boston didi team

* [bostondiditeam](https://github.com/bostondiditeam/MV3D)

  * [nepal](https://github.com/s-nepal/MV3D)

  * [zxf8665905](https://github.com/zxf8665905/didi-udacity-compatition) : 추천

    * [lihua213\#1](https://github.com/lihua213/didi-udacity-compatition)

    * [lihua213\#2](https://github.com/lihua213/MV3D): Old version

* [leeyevi](https://github.com/leeyevi/MV3D_TF)

  * [Super-Tree](https://github.com/Super-Tree/MV3D_TF)

* [jinbeibei\(??\)](https://github.com/jinbeibei/mv3d_ros_interface)

## 0. 환경 준비

* install tensorflow-gpu and CUDA.

* A Nvidia GPU card with computation capability

* ubuntu \(\* Cuda7.5에 맞는 버젼은 14.04임\)
* CUDA   
    \(\*environment\_gpu.yml상 버젼 =7.5\)

  * [http://developer.download.nvidia.com/compute/cuda/7.5/Prod/local\_installers/cuda-repo-ubuntu1404-7-5-local\_7.5-18\_amd64.deb](http://developer.download.nvidia.com/compute/cuda/7.5/Prod/local_installers/cuda-repo-ubuntu1404-7-5-local_7.5-18_amd64.deb)
  * `apt-get install cuda-7.5-15`\)

* cuDNN

  * Download cuDNN v5.1  for CUDA 7.5 : [Runtime lib.](https://developer.nvidia.com/compute/machine-learning/cudnn/secure/v5.1/prod_20161129/7.5/libcudnn5_5.1.10-1+cuda7.5_amd64-deb), [소스설치방법](https://github.com/adioshun/System_Setup/wiki/4_CUDA_CuDNN-Setup#driver--cuda-install-script)

* Python3.5 for MV3D related code

* Tensorflow-GPU\(version&gt;1.0\)  
* Python2.7 for ROS related script

```bash
# https://github.com/adioshun/gitBook_DeepDrive/blob/master/papermultiview-3d-cnn/environment_gpu.yml

# conda env create -f environment_gpu.yml --name mv3d_p3_gpu

conda create -n python35 python=3.5
conda install tensorflow-gpu opencv3 shapely scikit-learn keras Cython matplotlib simplejson numba
pip install easydict
```

### 0.1 GPU용으로 설정 변경

`src/net/lib/setup.py` and `src/lib/make.sh` : "arch=sm\_37" \#Google Cloud GPU Tesla K80

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

## 1.9 수정 필요

### A.

![](http://i.imgur.com/va7Lg8J.png)

* `data/raw/kitti/` 경로 밑에 데이터 위치 
* `tracklet_labels.xml`파일은 `2011_09_26_drive_0001_sync` 하위 폴더에 위치 

### B.

`src/kitti_data/pykitti/tracklet.py L289`에서 다운 받은 파일명으로 변경

```
DEFAULT_DRIVE = '2011_09_26_drive_0001'
```

## 2. ./src/make.sh

### 2.1 실행 방법

```
cd src
source activate didi
sudo chmod 755 ./make.sh
./make.sh
```

conda create -n python27 python=2.7

> 아래 \[2.2\]를 직접 실행 하는것 추천

### 2.2 실행시 진행 내용

    #- `python ./net/lib/setup.py build_ext --inplace` : Fast R-CNN (MS)

    #- 'bash ./net/lib/make.sh` : building psroi_pooling layer

    #- build required .so files
    ln -s ./net/lib/roi_pooling_layer/roi_pooling.so ./net/roipooling_op/roi_pooling.so
    ln -s ./net/lib/nms/gpu_nms.cpython-35m-x86_64-linux-gnu.so ./net/processing/gpu_nms.cpython-35m-x86_64-linux-gnu.so
    ln -s ./net/lib/nms/cpu_nms.cpython-35m-x86_64-linux-gnu.so ./net/processing/cpu_nms.cpython-35m-x86_64-linux-gnu.so
    ln -s ./net/lib/utils/cython_bbox.cpython-35m-x86_64-linux-gnu.so ./net/processing/cython_bbox.cpython-35m-x86_64-linux-gnu.so

###### \[에러\]  nvcc 못 찾을경우

* 절대 경로로 수정 후 실행 

###### \[에러\] `arning: calling a constexpr __host__ function from a __host__ __device__ function is not allowed.`

* `make.sh`파일에 아래 flag `--expt-relaxed-constexpr` 추가 

```
if [ -d "$CUDA_PATH" ]; then
    nvcc -std=c++11 -c -o roi_pooling_op.cu.o roi_pooling_op_gpu.cu.cc \
        -I $TF_INC -D GOOGLE_CUDA=1 -x cu -Xcompiler -fPIC $CXXFLAGS \
        -arch=sm_37 --expt-relaxed-constexpr
```

## 3. Preprocess data \(`./src/data.py`\)

> kitti기준, didi data 이용시 `utils/bag_to_kitti` 실행 필요

* MV3D net 학습시 필요한 입력 데이터 생성 
  * Lidar bird eye view features
  * Lidar front view features
  * RGB image
  * Ground Truth label
  * Ground bounding box coordinate
  * time stamp

```
./data/preprocessing/kitti/
    - gt_boxes3d :npy
    - gt_box_plot : png
    - gt_labels : npy
    - rgb : png
    - top : .npy.npz
    - top_image : png
```

| ![](http://i.imgur.com/bb67R50.png) | ![](http://i.imgur.com/AbdY7YU.png) |
| --- | --- |


### 3.9 수정 필요

#### A. data.py 수정

작업 환경

```bash

```

```python
#data.py

if config.cfg.USE_CLIDAR_TO_TOP:
    SharedLib = ctypes.cdll.LoadLibrary('/workspace/mv3d/src/lidar_data_preprocess/'
                                        'Python_to_C_Interface/ver3/LidarTopPreprocess.so')
#if config.cfg.USE_CLIDAR_TO_TOP:
#    SharedLib = ctypes.cdll.LoadLibrary('/home/stu/MV3D/src/lidar_data_preprocess/'
#                                        'Python_to_C_Interface/ver3/LidarTopPreprocess.so')
```

#### B. NameError: name 'MATRIX\_Mt' is not defined

```
# /MV3D/src/net/processing/boxes3d.py 상단에 추가 
# ./src/config.py L126 참고 
#rgb camera
MATRIX_Mt = ([[ 2.34773698e-04, 1.04494074e-02, 9.99945389e-01, 0.00000000e+00],
[ -9.99944155e-01, 1.05653536e-02, 1.24365378e-04, 0.00000000e+00],
[ -1.05634778e-02, -9.99889574e-01, 1.04513030e-02, 0.00000000e+00],
[ 5.93721868e-02, -7.51087914e-02, -2.72132796e-01, 1.00000000e+00]])

MATRIX_Kt = ([[ 721.5377, 0. , 0. ],
[ 0. , 721.5377, 0. ],
[ 609.5593, 172.854 , 1. ]])
```

### A. ./src/config.py

```
#if __C.DATA_SETS_TYPE=='test':
#    __C.DATA_SETS_DIR = osp.abspath('/home/stu/round12_data_test')

if __C.DATA_SETS_TYPE=='test':
    __C.DATA_SETS_DIR = osp.abspath('/workspace/mv3d')
```

### B. roi\_pooling.so을 심볼릭이 아닌 파일로 대체

> 이후에도 같은 문제가 발생 하므로 \[C\]방법 추천

```
cd ./src/net/roipooling_op
mv roi_pooling.so roi_pooling.so~
cp ../../net/lib/roi_pooling_layer/roi_pooling.so ./
```

### C. roi\_pooling.so 수정 버젼 다운 로드

1. [다운로드 roi\_pooling.so](https://github.com/CharlesShang/TFFRCNN/tree/roi_pooling/lib/roi_pooling_layer)

2. chmod +x roi\_pooling.so

## 4. train.py

###### \[에러\] `"tensorflow.python.framework.errors_impl.NotFoundError: YOUR_FOLDER/roi_pooling.so: undefined symbol: ZN10tensorflow7strings6StrCatB5cxx11ERKNS0_8AlphaNumES3"`

* it is related to compilation of roi\_pooling layer.
* A simple fix will be changing "GLIBCXX\_USE\_CXX11\_ABI=1" to "GLIBCXX\_USE\_CXX11\_ABI=0" in "src/net/lib/make.sh" \(line 17\)

OR Download and replace the .so with following file :[\[Download\]](https://github.com/smallcorgi/Faster-RCNN_TF/blob/6e2a941ac250da668cf93899dbd870cc4d838773/lib/roi_pooling_layer/roi_pooling.so), CUDA 8.0, Python 3.5

###### \[에러\] NameError: name 'data\_splitter' is not defined

> user this version of [train.py](https://raw.githubusercontent.com/lihua213/didi-udacity-compatition/development/src/train.py): for python2

###### \[에러\] "module 'tensorflow.python.ops.nn' has no attribute 'convolution'"

> `conda list | grep tensorflow`후 tensorflow\(cpu & gpu\) 버젼을 1.0 이상으로 변경

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



