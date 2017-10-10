|논문명|3D Mesh Labeling via Deep Convolutional Neural Networks 
|-|-|
|저자(소속)|KAN GUO (Beihang University )|
|학회/년도| ACM 2015, [논문](https://dl.acm.org/citation.cfm?id=2835487)|
|키워드|Kan2015, 7가지 Feature를 CNN을 통해 가공 |
|참고||
|코드||


기존 방법 : **predefined geometric features**사용 `Many previous methods on 3D mesh labeling achieve impressive performances by using predefined geometric features. `

문제점 : **generalization**능력이 약함 `However, the generalization abilities of such low-level features, which are heuristically designed to process specific meshes, are
often insufficient to handle all types of meshes. `

제안 방식 : learn a robust mesh representation that can adapt to various
3D meshes by using CNNs. 


절차 
- In our approach, CNNs are first trained in a supervised manner by using a** large pool of classical geometric features**.
- In the training process, these low-level features are nonlinearly combined
and hierarchically compressed to generate a compact and effective representation
for each triangle on the mesh. 
- Based on the trained CNNs and the mesh representations, a label vector is initialized for each triangle to indicate its probabilities of belonging to various object parts. 
- Eventually, a graph-based mesh-labeling algorithm is adopted to optimize the labels
of triangles by considering the label consistencies. 

## 1. Introducion 

## 3. MESH LABELING VIA CNNS
CNN을 이용하여 효율적인 mesh representations생성 방법 기술 `we will present how to learn compact and effective mesh representations by using deep CNNs. `

1. First, we extract a large pool of geometric features to form a 2D feature matrix so as to characterize each triangle on the mesh. 
2. Second, we present the architecture of the deep CNNs that are used to learn mesh representations from **massive feature matrices**. 
3. Third, we show the details of training the CNNs. 
4. Finally, we make a **brief description** of the mesh label optimizing process.

### 3.1 Geometric Feature Extraction

In our approach, we aim to learn a compact and effective mesh representation from low-level features. 

#### A. 잘 알려진 7가지 Feature추출 
`Thus, we first extract seven types of geometric features that are widely used in existing studies,including: `
1. curvature (CUR) [Gal and Cohen-Or 2006], 
2. PCAfeature (PCA) [Kalogerakis et al. 2010], 
3. shape diameter function(SDF) [Shapira et al. 2010], 
4. distance from medial surface (DIS) [Liuet al. 2009], 
5. average geodesic distance (AGD) [Hilaga et al. 2001],
6. shape context (SC) [Belongie et al. 2002], 
7. spin image (SI)[Johnson and Hebert 1999]. 


While the features are calculated with face areas and different scales in consideration. 

These features can well describe the characteristics of each triangle on a mesh from multiple perspectives.

#### B. Feature 합치기

Given these features, an intuitive solution is to concatenate them into a high-dimensional feature vector (i.e., 600 components in total).

- 단순한 합치기는 오버피팅 문제 유발 `However, as suggested in `Hu et al. [2012]` and `Wang et al.[2012]`, such simple concatenation will degrade the performance of clustering and may lead to over-fitting due to the high-dimensional descriptor space. `
- 오버피팅 문제 해결법 : CNN에 입력으로 사용 
    - To address this problem and to fully utilize the convolutional property of CNNs, we reorganize these 600 components to form a 30 × 20 feature matrix (as shown in Figure 1). 
    - In this manner, low-level geometric features can be nonlinearly combined and hierarchically compressed through various **convolutional operations** in CNNs. 

In experiments, we will demonstrate that the ordering of features as well as the size of feature matrix only slightly change the accuracy of mesh labeling.