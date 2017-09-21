|논문명|Deep Learning Advances in Computer Vision with 3D Data: A Survey
|-|-|
|저자(소속)||
|학회/년도| ACM Computing Surveys 2017, [논문](https://www.mendeley.com/viewer/?fileId=241a7816-fe42-e7ef-0a90-974189bcebfa&documentId=ca50a030-c06a-377c-812d-900466b273d3)|
|키워드||
|참고|Chpter 4|
|코드||

# Deep Learning Advances in Computer Vision with 3D Data: A Survey

## 1. INTRODUCTION

![](https://i.imgur.com/KI3Ir3N.png)

A generic pipeline for processing a 3D scene
- Scans of real scenes can contain millions of points, therefore at first, some form of preprocessing is commonly applied. 
    - Point reduction (i.e., remove redundant points in order to reduce the computational cost),
    - data structuring (i.e., organize the point cloud using data structures like kd-trees or octrees), 
    - hardware exploitation (e.g., GPU calculations) are a few of the methods proposed so far. --- Following, segmentation of the point cloud is typically performed in order to identify semantically meaningful regions. 
- After acquiring the objects of the scene from segmentation, keypoint detection and descriptors extraction are applied to every identified object or scene segment. 
- The extracted representation is subsequently utilized in order to match the scene segments with known object models 
- finally recognize or classify them into a category or even retrieve similar objects.

## 2. RELATED WORK

- 3D scene segmentation 
- 3D keypoint detection / 3D descriptor extraction 
- 3D shape retrieval / 3D object recognition 

> Deeplearning이전에 사용되던 Descriptors/Detector에 대한 연구 들인듯 (연구 년도도 2010년 전)

### 2.1 3D Scene Segmentation

- semantic segmentation/labeling 
- labeling each point of a scene as part of a foreground object of interest or of a background surface. 
- 3D object classification

3D point cloud segmentation methods into five categories `(Nguyen and Le [2013])`
- region-based
- edge-based
- attributes-based
- model-based
- graph-based methods 

### 2.2 3D keypoint detection / 3D descriptor extraction 

3D keypoint detection은 물체 인식/Retrive을 위해서 필수적인 Step 이다. 

Existing approaches `(Tombari et al. [2013])`
- Fixed-scale keypoint detectors : Identify distinctive keypoints at a constant scale given to the algorithm as an input argument
    - Local Surface Patches (LSPs) [Chen and Bhanu 2007]
    - Intrinsic Shape Signatures (ISSs) [Zhong 2009]
    - the 3D detector proposed in Mian et al. [2010] termed as “KeyPoint Quality” (KPQ) in Tombari et al. [2013]
- Adaptive-scale keypoint detectors : Identify keypoints after creating a scale space defined on the surface or alternatively after computing an embedding of the data on a 2D plane. 
    - MeshDoG [Zaharescu et al. 2009]

### 2.3. 3D Object Retrieval and Recognition

- Content-based image retrieval is a well-studied task in 2D computer vision. 

- 3D shape retrieval is one of the first problems 

Given a 3D object query, the goal is to retrieve semantically similar objects from a given database. 

Two steps are included in a typical retrieval pipeline: 
- (a) descriptors extraction from the 3D objects
- (b) matching of the queries’ descriptors with the stored descriptors of the database objects using an appropriate similarity measure. 

Existing approaches on 3D object retrieval can be divided into [Gao and Dai 2014] 
- (a)3D model-based methods , which are based mostly on low-level descriptors extraction from the 3D models, 
- (b)view-based methods , which utilize multiple 2D views of the 3D objects. 


### 2.4 4D Modeling

3D data + Time 

### 2.5. Current Trends


## 3. BACKGROUND ON DNNS

> DNN에 대한 기초 설명 -> 정리 제외 

## 4. ADVANCES IN DEEP LEARNING WITH 3D DATA










