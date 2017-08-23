
> https://github.com/CharlesShang/TFFRCNN

git clone --recursive https://github.com/adioshun/MV3D_TF.git


conda create -n python2_gpu python=2.7


conda install -y numpy Cython tensorflow-gpu matplotlib scikit-learn PIL
pip install easydict opencv_python pyyaml



conda install -c anaconda cudatoolkit=7.5



## Downloads KITTI object datasets.

- [Object Detection Evaluation 2012](http://www.cvlibs.net/datasets/kitti/eval_object.php)

```
 % Specify KITTI data path so that the structure is like

 % {kitti_dir}/object/training/image_2
 %                            /image_3
 %                            /calib
 %                            /lidar_bv
 %							 /velodyne
       

 % {kitti_dir}/object/testing/image_2
 %                           /image_3
 %                           /calib
 %                           /lidar_bv
 %							/velodyne




wget http://kitti.is.tue.mpg.de/kitti/data_object_image_2.zip




wget http://kitti.is.tue.mpg.de/kitti/data_object_image_3.zip


wget http://kitti.is.tue.mpg.de/kitti/data_object_velodyne.zip



wget http://kitti.is.tue.mpg.de/kitti/data_object_calib.zip


wget http://kitti.is.tue.mpg.de/kitti/data_object_label_2.zip

```
`/lidar_bv` 폴더 생성

```


## Build the Cython modules

 cd $MV3D/lib
 make
 
 
## Make Lidar Bird View data
```
# edit the kitti_path in tools/read_lidar.py
# then start make data
python tools/read_lidar.py
```




`./train_net.py --device gpu --device_id 0 --weights /workspace/MV3D_TF/data/pretrain_model/VGG_imagenet.npy --imdb kitti_train --iters 50001 --cfg /workspace/MV3D_TF/experiments/cfgs/faster_rcnn_end2end.yml --network MV3D_train`