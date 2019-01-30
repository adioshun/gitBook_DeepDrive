# [SECOND](https://github.com/traveller59/second.pytorch)

> 내부적으로 [spconv](https://github.com/traveller59/spconv)사용

SECOND 시스템 요구 사항 : ONLY support python 3.6+, pytorch 1.0.0+. Tested in Ubuntu 16.04/18.04., 

SPConv 시스템 요구 사항 : CUDA 9.0+, cmake >= 3.13.2

```
wget https://github.com/Kitware/CMake/releases/download/v3.13.3/cmake-3.13.3.tar.gz
./bootstrap
 make
 make install
```

sudo apt-get install libboost-all-dev


> python3.6인지 확인 

```sh
cd ~
#pip3 install shapely fire pybind11 tensorboardX protobuf scikit-image numba pillow numba
conda install -c conda-forge shapely fire pybind11 tensorboardX protobuf scikit-image numba pillow numba

#pip3 install torch torchvision
conda install -c anaconda pytorch-gpu 

git clone https://github.com/traveller59/spconv.git --recursive
cd spconv
python3 setup.py bdist_wheel
cd ./dist
pip3 install spconv-1.0-cp36-cp36m-linux_x86_64.whl

# Setup cuda for numba
vi ~/.bashrc
export NUMBAPRO_CUDA_DRIVER=/usr/lib/x86_64-linux-gnu/libcuda.so
export NUMBAPRO_NVVM=/usr/local/cuda/nvvm/lib64/libnvvm.so
export NUMBAPRO_LIBDEVICE=/usr/local/cuda/nvvm/libdevice

export PATH="/usr/local/cuda/bin:$PATH"  
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64"
export CUDA_HOME=/usr/local/cuda

export PYTHONPATH=$PYTHONPATH:/workspace/second.pytorch
source ~/.bashrc

cd /workspace
git clone https://github.com/traveller59/second.pytorch.git
```


docker run --runtime=nvidia -it --privileged --network=host -v /tmp/.X11-unix:/tmp/.X11-unix --volume="$HOME/.Xauthority:/root/.Xauthority:rw" -e DISPLAY -v /media/adioshun/data/datasets:/datasets --volume /workspace:/workspace --name 'second'  adioshun/second /bin/bash



---

"pybind11/detail/common.h:112:20: fatal error: Python.h: No such file or directory"

apt install python3.6-dev