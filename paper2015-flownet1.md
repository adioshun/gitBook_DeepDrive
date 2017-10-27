|논문명 | FlowNet: Learning Optical Flow with Convolutional Networks |
| --- | --- |
| 저자\(소속\) | Alexey Dosovitskiy \(uni-freiburg.de\) |
| 학회/년도 | ICCV 2015, [논문](https://arxiv.org/abs/1504.06852) |
| 키워드 | Dosovitskiy2015,  |
| 데이터셋(센서)/모델 | KITTI, Sintel, Middlebury datasets, synthetic Flying Chairs dataset.  |
| 관련연구| DispNet, FlowNet 2 |
| 참고 |[홈페이지](https://lmb.informatik.uni-freiburg.de/Publications/2015/DFIB15/), [Youtube](https://www.youtube.com/watch?v=g-peWXaQnQc), [poster](http://aims.robots.ox.ac.uk/wp-content/uploads/2015/10/James-Thewlis.pdf)|
| 코드 |[Code](https://github.com/lmb-freiburg/dispnet-flownet-docker), [Caffe](https://github.com/liruoteng/FlowNet) |


# FlowNet

## 1. Introducion 

## 2. Related Work

### 2.1 Optical Flow

#### A. 기존 연구 

- optical flow estimation에 대한 [19-1981]의 연구 이후 많은 확장 논문들이 나왔다[29-1998, 5-2004, 34-2009]. `Variational approaches have dominated optical flow estimation since the work of Horn and Schunck [19].Many improvements have been introduced[29, 5, 34]. `

- 최근 연구는 **displacements** & **combinatorial matching**를 여러 방법`(variational approach)`으로 합치는 것이다[6-2011, 35-2013]. `The recent focus was on large displacements,and combinatorial matching has been integrated into the variational approach [6, 35]. `

- [35-DeepFlow]연구의 **Deep Matching** & **DeepFlow**아이디어를 본 논문에서 활용 하였다. `The work of [35] termed Deep Matching and DeepFlow is related to our work in that feature information is aggregated from fine to coarse using sparse convolutions and max-pooling. `
    - 하지만, 파라미터 들을 손수 작업 해야 한다. However, it does not perform any learning and all parameters are set manually.

- [30-EpicFlow]연구의 **EpicFlow**아이디어의 성공으로 성능이 좋아 졌따. `The successive work of [30] termed EpicFlow has put even more emphasis on the quality of sparse matching as the matches from [35] are merely interpolated to denseflow fields while respecting image boundaries. `

```
[35] P. Weinzaepfel, J. Revaud, Z. Harchaoui, and C. Schmid. DeepFlow: Large displacement optical flow with deep matching. In ICCV, Sydney, Australia, Dec. 2013
[30] J. Revaud, P. Weinzaepfel, Z. Harchaoui, and C. Schmid. EpicFlow: Edge-Preserving Interpolation of Correspondences for Optical Flow. In CVPR, Boston, United States,
June 2015
```

- 본 논문에서 활용한 아이디어 : We only use a variational approach for optional refinement of the flow field predicted by the convolutional net and do not require any handcrafted methods for aggregation, matching and interpolation.


#### B. 머신러닝 기반 optical flow

Several authors have applied machine learning techniques to optical flow before. 

- Sun et al. [32-2018] study **statistics of optical flow** and learn **regularizers** using **Gaussian scale mixtures**; 

- Rosenbaum et al. [31-2013] model local **statistics** of optical flow with **Gaussian mixture models**. 

- Black etal. [4-1997] compute **principal components** of a training set of flow fields. 

To predict optical flow they then estimate coefficients of a linear combination of these ’basis flows’. 

Other methods train classifiers to select among different inertial estimates [21-2015] or to obtain occlusion probabilities [27-2013].

```
[21] R. Kennedy and C. Taylor. Optical flow with geometric occlusion estimation and fusion of multiple frames. In EMMCVPR. 2015
```

#### C. 뉴럴 네트워크를 이용한 비지도 학습 기반 

- There has been work on **unsupervised learning** of **disparity** or **motion** between frames of videos using neural network models. 

- These methods typically use multiplicative interactions to model relations between a pair of images.

- Disparities and optical flow can then be inferred from the latent variables. 

- Taylor et al. [33-2010] approach the task with factored gated restricted Boltzmann machines. 

- Kondaand Memisevic [23-2013] use a special auto encoder called ‘synchrony autoencoder’. 

While these approaches work well in a controlled setup and learn features useful for activity recognition in videos, they are not competitive with classical methods on realistic videos. 







