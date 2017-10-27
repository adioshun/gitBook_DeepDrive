|논문명 | FlowNet: Learning Optical Flow with Convolutional Networks |
| --- | --- |
| 저자\(소속\) | Alexey Dosovitskiy \(uni-freiburg.de\) |
| 학회/년도 | ICCV 2015, [논문](https://arxiv.org/abs/1504.06852) |
| 키워드 | Dosovitskiy2015,  |
| 데이터셋(센서)/모델 |  |
| 관련연구| DispNet, FlowNet 2 |
| 참고 |[홈페이지](https://lmb.informatik.uni-freiburg.de/Publications/2015/DFIB15/), [Youtube](https://www.youtube.com/watch?v=g-peWXaQnQc), [poster](http://aims.robots.ox.ac.uk/wp-content/uploads/2015/10/James-Thewlis.pdf)|
| 코드 |[Code](https://github.com/lmb-freiburg/dispnet-flownet-docker), [Caffe](https://github.com/liruoteng/FlowNet) |


# FlowNet

## 1. Introducion 

## 2. Related Work

### 2.1 Optical Flow

Variational approaches have dominatedoptical flow estimation since the work of Horn andSchunck [19]. 

Many improvements have been introduced[29, 5, 34]. 

The recent focus was on large displacements,and combinatorial matching has been integrated into thevariational approach [6, 35]. 

The work of [35] termed DeepMatchingand DeepFlow is related to our work in that featureinformation is aggregated from fine to coarse usingsparse convolutions and max-pooling. 

However, it doesnot perform any learning and all parameters are set manually.The successive work of [30] termed EpicFlow hasput even more emphasis on the quality of sparse matchingas the matches from [35] are merely interpolated to denseflow fields while respecting image boundaries. 

We only usea variational approach for optional refinement of the flowfield predicted by the convolutional net and do not requireany handcrafted methods for aggregation, matching and interpolation.Several authors have applied machine learning techniquesto optical flow before. 

Sun et al. 

[32] study statisticsof optical flow and learn regularizers using Gaussianscale mixtures; Rosenbaum et al. 

[31] model local statisticsof optical flow with Gaussian mixture models. 

Black etal. 

[4] compute principal components of a training set offlow fields. 

To predict optical flow they then estimate coef-ficients of a linear combination of these ’basis flows’. 

Othermethods train classifiers to select among different inertialestimates [21] or to obtain occlusion probabilities [27].There has been work on unsupervised learning of disparityor motion between frames of videos using neuralnetwork models. 

These methods typically use multiplicativeinteractions to model relations between a pair of images.Disparities and optical flow can then be inferred fromthe latent variables. 

Taylor et al. 

[33] approach the taskwith factored gated restricted Boltzmann machines. 

Kondaand Memisevic [23] use a special autoencoder called ‘synchronyautoencoder’. 

While these approaches work well in a controlled setup and learn features useful for activityrecognition in videos, they are not competitive with classicalmethods on realistic videos. 







