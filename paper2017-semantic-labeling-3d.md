|논문명 |A Fully Convolutional Network for Semantic Labeling of 3D Point Clouds |
| --- | --- |
| 저자\(소속\) | \(\) |
| 학회/년도 | arXiv Oct 2017, [논문](https://arxiv.org/abs/1710.01408) |
| 키워드 | |
| 데이터셋(센서)/모델 | ISPRS 3D Semantic Labeling|
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

