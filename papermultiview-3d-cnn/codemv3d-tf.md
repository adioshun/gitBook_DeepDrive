
> https://github.com/CharlesShang/TFFRCNN


## 0. setup the python environment. 

```bash
#Google cloud GPU Tesla K80
#Ubuntu 16.4
conda create -n python2_gpu python=2.7
conda install -y numpy Cython tensorflow-gpu matplotlib scikit-learn PIL
pip install easydict opencv_python pyyaml
conda install -c anaconda cudatoolkit=7.5
```
OR

```

```

## 1. git clone 
```
git clone --recursive https://github.com/leeyevi/MV3D_TF.git
```

## 2. Downloads KITTI object datasets.

> [Object Detection Evaluation 2012](http://www.cvlibs.net/datasets/kitti/eval_object.php)

```
# cd /workspace/MV3D/data/KITTI/object
wget http://kitti.is.tue.mpg.de/kitti/data_object_image_2.zip
wget http://kitti.is.tue.mpg.de/kitti/data_object_image_3.zip
wget http://kitti.is.tue.mpg.de/kitti/data_object_velodyne.zip
wget http://kitti.is.tue.mpg.de/kitti/data_object_calib.zip
wget http://kitti.is.tue.mpg.de/kitti/data_object_label_2.zip
```

`/workspace/MV3D/data/KITTI/object/{testing/training}/lidar_bv` 폴더 생성


## 3. Make Lidar Bird View data

- change the root_dir in `read_lidar.py` file





![](http://i.imgur.com/sJi1PFV.png)
## Build the Cython modules

 cd $MV3D/lib
 make
 
 

```
# edit the kitti_path in tools/read_lidar.py
# then start make data
python tools/read_lidar.py
```




`./train_net.py --device gpu --device_id 0 --weights /workspace/MV3D_TF/data/pretrain_model/VGG_imagenet.npy --imdb kitti_train --iters 50001 --cfg /workspace/MV3D_TF/experiments/cfgs/faster_rcnn_end2end.yml --network MV3D_train`


###### [에러] undefined symbol: ZN10tensorflow7strings6StrCatB5cxx11ERKNS0_8AlphaNumES3"
```
#/workspace/MV3D_TF/lib/make.sh

        #g++ -std=c++11 -shared -o roi_pooling.so roi_pooling_op.cc \
        g++ -std=c++11 -shared -D_GLIBCXX_USE_CXX11_ABI=0 -o roi_pooling.so roi_pooling_op.cc \
                roi_pooling_op.cu.o -I $TF_INC  -D GOOGLE_CUDA=1 -fPIC $CXXFLAGS \
                -lcudart -L $CUDA_PATH/lib64

```