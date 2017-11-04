|논문명 |A Fully Convolutional Network for Semantic Labeling of 3D Point Clouds |
| --- | --- |
| 저자\(소속\) | \(\) |
| 학회/년도 | arXiv Oct 2017, [논문](https://arxiv.org/abs/1710.01408) |
| 키워드 | 인위성 View,  |
| 데이터셋(센서)/모델 | [ISPRS 3D Semantic Labeling](http://www2.isprs.org/commissions/comm3/wg4/3d-semantic-labeling.html)|
| 관련연구||
| 참고 | |
| 코드 | |



# A Fully Convolutional Network for Semantic Labeling of 3D Point Clouds

- In this paper we present a 1D-fully convolutional network that consumes **terrain-normalized** points directly with the corresponding spectral data,  
    - if available, to generate point-wise labeling while implicitly learning contextual features in an end-to-end fashion. 
    
- Our method uses only the **3D-coordinates** and three **corresponding spectral features** for each point. 

- **Spectral features** may 
    - either be extracted from 2D-georeferenced images, as shown here for Light Detection and Ranging (LiDAR) point clouds, 
    - or extracted directly for passive-derived point clouds, i.e. from muliple-view imagery.
    
## 1. Introduction

## 2. Related Work

- 포인트 클라우드 라벨링은 두 분류로 나눌수 있다. `Point cloud labeling algorithms can generally be grouped into two main categories. `

- Section 2.1 describes“Direct Methods”, 
    - 변환없이 포인트 클라우드 직접 사용 `which operate immediately on the point clouds themselves, and do not change the 3D nature of the data. `

- Section 2.2 describes “Indirect Methods”,
    - 변환(이미지, Volume) 하여 사용 `which transform the input point cloud, `
    - e.g. into an image or a volume, from which known semantic segmentation methods can then be applied. 

- Section2.3 proposes a novel approach 
    - 제안 방법 with 7 specific contributions for semantic classification of point clouds.
    
### 2.1. Direct Methods

- Direct methods assign semantic labels to each element in the point cloud based, fundamentally, on a simple point-wise discriminative model operating on point features. 
    - Such features, known as “eigen-features”, are derived from the covariance matrix of a local neighborhood and provide information on the local geometry of the sampled surface, 
    - e.g. planarity, sphericity, linearity (Lin et al., 2014a). 

- To improve classification,contextual information can explicitly be incorporatedinto the model. 

- For example, Blomley et al. (2016)used covariance features at multiple scales found using the eigen entropy-based scale selection method (Weinmannet al., 2014) and evaluated four different classifiers using the ISPRS 3D Semantic Labeling Contest.
    - 활용 기술 : Their best-performing model used a **Linear Discriminant Analysis (LDA) **classifier in conjunction with various local geometric features. 
    - 제약 : However, **scalability **of this model was limited, due to the dependence upon various** hand crafted features**, and the need to experiment with various models that don’t incorporate contextual features and require effort to tune.

```
Blomley, R., Jutzi, B., Weinmann, M., September 2016. 3d semantic labeling of als point clouds by exploiting multi-scale, multi-type neighborhoods for feature extraction. In: GEOBIA 2016 : Solutions and Synergies
```

- 퓨전 방식 도입 : Motivated by the frequent availability of **coincident 3D data **and **optical imagery**, Ramiya et al.(2014) proposed the use of **point coordinates** and **spectral data** directly, forming a per-point vector of (X,Y,Z,R,G,B)components. 
    - Labeling was achieved by filtering the scene into ground and non-ground points according to Axelsson (2000), then applying a 3D-region-growing segmentation to both sets to generate object proposals.

```
Ramiya, A., Nidamanuri, R. R., Krishnan, R., 2014. Semantic labelling of urban point cloud data. The International Archives of Photogrammetry, Remote Sensing and Spatial Information Sciences 40 (8), 907.
```


- Like Blomley et al. (2016), several geometric features were also derived, although specific details were not published. 
    - Without incorporating contextual features,each segment/proposal was then classified into a selected set of five classes from the main ISPRS 3D SemanticLabeling Contest.

- 그외 여러 연구들 Several other methods were also reported in the literature such as the work by 
    - (Mallet, 2010) which classified full-waveform LiDAR data using a point-wise multi class support vector machine (SVM), 
    - (Chehataet al., 2009) who used random forests (RF) for feature detection and classification of urban scenes collected by airborne LiDAR. 

- 서베이 논문 : The reader is referred to Grilli et al.(2017) for a review. 

```
Grilli, E., Menna, F., Remondino, F., 2017. a review of point clouds segmentation and classification algorithms. ISPRS-International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences, 339–344.
```

- While simple discriminative modelsare well-established, they are unable to consider interactions between 3D points.

- To allow for spatial dependencies between objectclasses by considering labels of the local neighborhood, Niemeyer et al. (2014) proposed a contextual classification method based on Conditional Random Field(CRF). 

- A linear and a random forest models were compared when used for both the unary and the pairwise potentials.

- By considering complex interactions between  points, promising results were achieved, although this came at the cost of computation speed: 3.4 minutes for testing using an RF model, and 81 minutes using the linear model. 

- The speed excludes the additional time needed to estimate the per-point, 131-dimensional feature vector prior to testing.

This contextual classification model was later extended to use a two-layer, hierarchical, high-order CRF, which incorporates spatial and semantic context(Niemeyer et al., 2016). 

The first layer operates on thepoint level (utilizing higher-order cliques and geometricfeatures (Weinmann et al., 2014)), to generate segments.The second layer operates on the generated segments,and therefore incorporates a larger spatial scale.

Used features include geometry and intensity-based descriptors,in addition to distance and orientation to roadfeatures (Golovinskiy et al., 2009)). 

By iteratively propagatingcontext between layers, incorrect classificationscan be revised at later stages; this resulted in good performanceon the ISPRS 3D Semantic Labeling Contest.

However, this method employed multiple algorithms,each designed separately, which would make itchallenging to simultaneously optimize. 

Also, the useof computationally-intensive inference methods wouldlimits the run-time performance. 

In contrast to relying on multiple individually-trained components, an end-to-end learning mechanism is desired.


### 2.2. Indirect Methods

- Indirect methods는 대부분 딥러닝 기술을 사용한다. `Indirect methods – which mostly rely on **deep learning**– offer the potential to learn local and global features in a streamlined, end-to-end fashion (Yosinskiet al., 2015). `

- CNN의 발전과 데이터셋의 구비, 컴퓨팅 파워의 증가로 디러닝 기반 방식이 가능해 졌다. `Driven by the reintroduction and improvement of Convolutional Neural Networks (CNNs)(LeCun et al., 1989; He et al., 2016), the avail abilityof large-scale datasets (Deng et al., 2009), and the affordability of high-performance compute resources such as graphics processing units (GPUs), deep learning has enjoyed unprecedented popularity in recent years.`

- This success in computer vision domains such as 
    - image labeling (Krizhevsky et al., 2012), 
    - object detection(Girshick et al., 2014), 
    - semantic segmentation (Badrinarayananet al., 2017; Long et al., 2015), 
    - target tracking (Wang and Yeung, 2013; Yousefhussienet al., 2016), 
- has generated an interest in applying these frameworks for 3D classification.

- 그러나 nonuniform & irregular한 포인트 클라우드의 특징으로 2D-CNN에 바로 적용 하기는 어렵다. `However, the nonuniform and irregular nature of 3D pointclouds prevents a straightforward extension of 2D-CNNs, which were designed originally for imagery.`

- 그래서 초기 연구는 3D **CAD데이터**를 중심으로 3D를 2D로 변경 하여 진행 하였다. `Hence, initial deep learning approaches have focused on 3D computer-aided design (CAD) objects, and have relied on transforming the 3D data into more tractable 2D images. `
    - For example, Su et al. (2015-MVCNN) rendered multiple synthetic “views” by placing a virtual camera around the 3D object. 
    - Rendered views were passed though replicas of the trained CNN, aggregated using a view poolinglayer, and then passed to another CNN to learn classification labels. 

```
Su, H., Maji, S., Kalogerakis, E., Learned-Miller, E., 2015. Multiview convolutional neural networks for 3d shape recognition. In: Proceedings of the IEEE international conference on computer vision.pp. 945–953.
```

- 다른 연구들은 멀티뷰 방식을 채택 하였다. `Several other methods use the multiview approach with various modifications to the rendered views. `
    - For example, Bai et al. (2016) generated depth images as the 2D views, while other methods accumulated a unique signature from multiple view features,
    - or projected the 3D information into 36 channels,modifying AlexNet (Krizhevsky et al., 2012) to handl esuch input. 

```
Bai, S., Bai, X., Zhou, Z., Zhang, Z., Jan Latecki, L., 2016. Gift: A real-time and scalable 3d shape search engine. In: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. pp. 5023–5032.
```


- 이러한 연구의 서베이 논문 `For further details, the reader is referred to(Savva et al., 2016).`

```
Savva, M., Yu, F., Su, H., Aono, M., Chen, B., Cohen-Or, D., Deng, W., Su, H., Bai, S., Bai, X., et al., 2016. Shrec16 track: large-scale 3d shape retrieval from shapenet core55. In: Proceedings of the Eurographics Workshop on 3D Object Retrieval

```

- 멀티뷰 방식은 **포인트클라우드**에도 적용 되었다. `Similar multiview approaches have also been appliedto ground-based LiDAR point clouds. `

- For example, Boulch et al. (2017) generated a mesh from the Semantic 3DLarge-scale Point Cloud Classification Benchmark(Hackel et al., 2017); 
    - this allowed for the generation of synthetic 2D views based on both RGB information and a 3-channel depth composite. 
    - A two-stream SegNet (Badrinarayanan et al., 2017) network was then fused with residual correction (Audebert et al., 2016) to label corresponding pixels. 
    - 2D labels were then backprojected to the point cloud to generate 3D semantic classification labels. 
```
Boulch, A., Saux, B. L., Audebert, N., 2017. Unstructured Point Cloud Semantic Labeling Using Deep Segmentation Networks. In: Eurographics Workshop on 3D Object Retrieval. The Eurographics Association
```


- Likewise, Caltagirone et al. (2017)generated multiple overhead views, embedded with elevation and density features, to assist with road detection from LiDAR data. 

```
Caltagirone, L., Scheidegger, S., Svensson, L., Wahde, M., June 2017. Fast lidar-based road detection using fully convolutional neural networks. In: 2017 IEEE Intelligent Vehicles Symposium (IV). pp.
1019–1024.
```

- FCN을 이용한 이진 세크멘테이션 연구 진행 `A Fully-Convolutional Network(FCN) (Long et al., 2015) was used for a single-scale binary semantic segmentation {road, not-road}, based on training from the KITTI dataset (Geiger et al., 2013).`

```
Long, J., Shelhamer, E., Darrell, T., 2015. Fully convolutional networks for semantic segmentation. In: IEEE Conference on Computer Vision and Pattern Recognition, CVPR 2015, Boston, MA, USA, June 7-12, 2015. pp. 3431–3440.
```

- Despite their initial adoption, such multiview transformation approaches applied to point clouds lose information on the third spatial dimension through a projective rendering. 

- Simultaneously, they introduce interpolation artifacts and void locations. 

- Together, this complicates the process by unnecessarily rendering the data in 2D, in addition to forcing the network to ignore artificial regions caused by the voids. 

- While this is less consequential to binary classification, multi-class problems require each point be assigned a separate class;     
    - 이 방식은 복잡성과 컴퓨팅 자원을 요구 한다. `this increases the complexity and may reduce the network’s performance.`

- 멀티뷰 방식의 단점으로 딥러닝으로 볼류메틱 방식이 제안 되었다. `In light of these limitations of multiview transformation methods, other authors have taken a volumetric approach to handle points clouds using deep learning. `

- 차량 탐지 알고리즘 `For example Li (2017) presented a method for vehicle detection in ground-based LiDAR point clouds. `
    - The input point cloud was voxelized, and then a fourth binary channel was appended, representing the binary occupancy,i.e. the presence or the absence of a point within each voxel. 
    - A 3D-FCN was then trained and evaluated to produce two maps representing the objectness and bounding box scores, using the KITTI dataset.

```
Li, B., 2017. 3d fully convolutional network for vehicle detection in point cloud. In: IRO
```

- Similarly, Huang and You (2016) generated occupancy voxel grids based on LiDAR point cloud data, 
    - labeling each voxel according to the annotation of its center point. 
    - A 3D-CNN was then trained to label each voxel into one of seven classes; 
    - individual points were then labeled according to their parent voxel. 
    
```
Huang, J., You, S., 2016. Point cloud labeling using 3d convolutional neural network. In: Pattern Recognition (ICPR), 2016 23rd International Conference on. IEEE, pp. 2670–2675.
```

- **voxelization **기법에 대한 다양한 연구도 진행 되었다. `Other authors have explored variations of voxelization methods including, `
    - binary occupancy grid, 
    - density grid, 
    - hitgrid. 

- VoxNet에서는 위 다양한 방식에 대한 테스트가 진행 되었다. `In VoxNet, Maturana and Scherer (2015) tested each voxelization model individually, to train 3D-CNN swith 32x32x32 grid inputs. `
    - To handle multi-resolution inputs, they trained two separate networks each receiving an occupancy grid with different resolution Parallel development of both multiview and volumetric CNNs has resulted in an empirical performance gap.

```
Maturana, D., Scherer, S., 2015. Voxnet: A 3d convolutional neural network for real-time object recognition. In: Intelligent Robots and Systems (IROS), 2015 IEEE/RSJ International Conference on. IEEE, pp. 922–928.
```

- Qi et al. (2016-VMCNN) suggested that results could collectively be improved by merging these two paradigms. 
    - To address this, a hybrid volumentric CNN was proposed,which used long anisotropic kernels to project the 3D volumeinto a 2D-representation. 
    - Outputs were processed using an image-based CNN based on the Network In Network (NIN) architecture (Lin et al., 2014b).
    - To combine the multiview approach with proposed volumetric methods, the 3D-object was rotated to generate different 3D-orientations. 
    - Each individual orientation was processed individually by the same network to generate 2D-representations, which were then pooled together and passed to the image-based CNN.

```
Qi, C. R., Su, H., Nießner, M., Dai, A., Yan, M., Guibas, L. J., 2016. Volumetric and multi-view cnns for object classification on 3d data. In: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. pp. 5648–5656.
```


- Finally, Liu et al. (2017) took a different approach by combining image-like representations with conditional random field in the context of data fusion. 
    - Instead of directly operating on the LiDAR data, they interpolated the DSM map as a separate channel. 
    - Using the imagery and the LiDAR data, two separate probability maps were generated. 
    - A pre-trained FCN was used to estimate the first probability map using optical imagery.
    - Then, by handcrafting another set of features from both the spectral and the DSM map, a logistic regression was applied to generate a second set of probability maps. 
    - At the end of this two-stream process, the two probability maps were combined using high-order CRF to label every pixel into one of six categories.
    
```
Liu, Y., Piramanayagam, S., Monteiro, S. T., Saber, E., July 2017. Dense semantic labeling of very-high-resolution aerial imagery and lidar with fully-convolutional neural networks and higherorder crfs. In: 2017 IEEE Conference on Computer Vision and Pattern Recognition Workshops (CVPRW). pp. 1561–1570.
```