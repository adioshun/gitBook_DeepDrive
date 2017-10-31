|논문명 |FuseNet: Incorporating Depth into Semantic Segmentation via Fusion-Based CNN Architecture |
| --- | --- |
| 저자\(소속\) | Caner Hazirbas\(Munich\) |
| 학회/년도 | ACCV 2016, [논문](https://link.springer.com/chapter/10.1007/978-3-319-54181-5_14) |
| 키워드 | RGB+Depth map -> Segmentation, |
| 데이터셋(센서)/모델 |NYU,SUN-RGBD  |
| 관련연구||
| 참고 | |
| 코드 |[Caffe](https://github.com/tum-vision/fusenet) |



# FuseNEt

- Fully Convolution Network를 이용하여 Encode단계에서 fuse depth features + RGB feature maps하도록 한다. `propose an encoder-decoder type network, where the encoder part is composed of two branches of networks that simultaneously extract features from RGB and depth images and fuse depth features into the RGB feature maps as the network goes deeper`


## 1 Introduction

- FuseNet제안 `we propose an encoder-decoder type network, referred to as FuseNet, `
    - where the **encoder** part is **composed of two branches** of networks that simultaneously extract features from RGB and depth images and fuse depth features into the RGB feature maps as the network goes deeper

- 두가지 퓨젼 방식으로 테스트 수행 `We propose and examine two different ways for fusion of the RGB and depth channels. We also analyze the proposed network architectures, referred to as **dense and sparse fusion** (see Fig. 3), in terms of the level of fusion.`

## 2 Related Work