# [A Survey of Clustering With Deep Learning: From the Perspective of Network Architecture](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8412085)


```
Clustering is a fundamental problem in many data-driven application domains, and clustering
performance highly depends on the quality of data representation. 

Hence, linear or non-linear feature transformations have been extensively used to learn a better data representation for clustering. 

In recent years, a lot of works focused on using deep neural networks to learn a clustering-friendly representation, resulting in a significant increase of clustering performance. 

In this paper, we give a systematic survey of clustering with deep learning in views of architecture. 

Specifically, 
- we first introduce the preliminary knowledge for better understanding of this field. 
- Then, a taxonomy of clustering with deep learning is proposed and some representative methods are introduced. 
- Finally, we propose some interesting future opportunities of clustering with deep learning and give some conclusion remarks.
```


## I. INTRODUCTION

군집화 목적 : The goal of clustering is to categorize similar data into one cluster based on some similarity measures (e.g., Euclidean distance). 

기존 방식은 고차원 데이터에 대하여 좋지 않은 성능을 보임 `Although a large number of data clustering methods have been proposed [1]–[5], conventional clustering methods usually have poor performance on high-dimensional data, due to the inefficiency of similarity measures used in these methods. Furthermore, these methods generally suffer from high computational complexity on large-scale datasets. `

이러한 이유로 차원 축소나 Raw데이터를 다른 형태로 특징을 변환하는 방식이 많이 사용되었다. `For this reason, dimensionality reduction and feature transformation methods have been extensively studied to map the raw data into a new feature space, where the generated data are easier to be separated by existing classifiers.`

변환기의 예는 다음과 같다. `Generally speaking, existing data transformation methods include `
- **linear transformation** like Principal component analysis (PCA) [6] and 
- **non-linear transformation** such as kernel methods [7] and spectral methods [8].

그럼에도 불구 하고 고차원 데이터는 아직도 연구 대상이다. `Nevertheless, a highly complex latent structure of data is still challenging the effectiveness of existing clustering methods.`

딥러닝의 발전 덕분에 이런 문제는 많이 해결 될수 있다. `Owing to the development of deep learning [9], deep neural networks (DNNs) can be used to transform the data into more clustering-friendly representations due to its inherent property of highly non-linear transformation. `

이전 방식은 특징 변환과 군집화를 별개로 생각 하였다. 그래서 특징 변환을 하고 바로 군집 알고리즘에 적용 시키는 형식이었다. `Basically, previous work mainly focuses on feature transformation or clustering independently. Data are usually mapped into a feature space and then directly fed into a clustering algorithm. `

최근들어 DEC기법이 제안 되면서 딥클러스터링 연구가 시작 되었다. `In recent years, deep embedding clustering (DEC) [11] was proposed and followed by other novel methods [12]–[18], making deep clustering become a popular research field. `

```
[11] J. Xie, R. Girshick, and A. Farhadi, ‘‘Unsupervised deep embedding for clustering analysis,’’ in Proc. Int. Conf. Mach. Learn., 2016, pp. 478–487.
[12] F. Li, H. Qiao, B. Zhang, and X. Xi. (2017). ‘‘Discriminatively boosted image clustering with fully convolutional auto-encoders.’’ [Online]. Available: https://arxiv.org/abs/1703.07980
[13] B. Yang, X. Fu, N. D. Sidiropoulos, and M. Hong. (2016). ‘‘Towards K-means-friendly spaces: Simultaneous deep learning and clustering.’’ [Online]. Available: https://arxiv.org/abs/1610.04794
[14] K. G. Dizaji, A. Herandi, C. Deng, W. Cai, and H. Huang, ‘‘Deep clustering via joint convolutional autoencoder embedding and relative entropy minimization,’’ in Proc. IEEE Int. Conf. Comput. Vis. (ICCV), Oct. 2017, pp. 5747–5756.
[15] Z. Jiang, Y. Zheng, H. Tan, B. Tang, and H. Zhou. (2016). ‘‘Variational deep embedding: An unsupervised and generative approach to clustering.’’[Online]. Available: https://arxiv.org/abs/1611.05148
[16] J. Yang, D. Parikh, and D. Batra, ‘‘Joint unsupervised learning of deep representations and image clusters,’’ in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., Jun. 2016, pp. 5147–5156.
[17] C.-C. Hsu and C.-W. Lin, ‘‘CNN-based joint clustering and representation learning with feature drift compensation for large-scale image data,’’ IEEE Trans. Multimedia, vol. 20, no. 2, pp. 421–429, Feb. 2018.
[18] Z. Wang, S. Chang, J. Zhou, M. Wang, and T. S. Huang, ‘‘Learning a taskspecific deep architecture for clustering,’’ in Proc. SIAM Int. Conf. Data Mining, 2016, pp. 369–377.
```

[19] 논문에서 딥클러스터링 기법을 overview로 다루었다. `Recently, an overview of deep clustering was proposed in [19] to review most remarkable algorithms in this field. Specifically, it presented some key elements of deep clustering and introduce related methods. `

```
[19] E. Aljalbout, V. Golkov, Y. Siddiqui, and D. Cremers. (2018). ‘‘Clustering with deep learning: Taxonomy and new methods.’’ [Online]. Available: https://arxiv.org/abs/1801.07648
```

하지만 본 논문에서는 오토인코더에 초점을 두어 overview하였다. `However, this paper mainly focuses on methods based on autoencoder [20], and it was incapable of generalizing many other important methods, e.g., clustering based on deep generative model. What is worse, some up-to-date progress is also missing. Therefore, it is meaningful to conduct a more systematic survey covering the advanced methods in deep clustering.`

기존 군집 알고리즘은 아래와 같이 분류 된다. `Classical clustering methods are usually categorized as `
- partition-based methods [21], 
- density-based methods [22], 
- hierarchical methods [23] 
- and so on. 

딥클러스터가 representation를 학습 하는것을 목적으로 하기에 Loss 기법으로 나눈건 불적합 하다. 대신, 네트워크 구조로 나누어야 한다. `However, since the essence of deep clustering is to learning a clustering-oriented representation, it is not suitable to classify methods according to the clustering loss, instead, we should focus on the network architecture used for clustering. `

> In this paper, we make a survey of deep clustering from the perspective of network architecture.

### 1.1 autoencoder (AE)

The first category uses the autoencoder (AE) to obtain a feasible feature space. 

An autoencoder network provides a non-linear mapping function through learning an encoder and a decoder, where the encoder is a mapping function to be trained, and the decoder is required to be capable to reconstruct the original data from those features generated by the encoder. 

### 1.2 Clustering DNN

The second category is based on feed-forward networks trained only by specific clustering loss, thus we refer to this type of DNN as Clustering DNN (CDNN). 

The network architecture of this category can be very deep and networks pre-trained on large-scale image datasets can further boost its clustering performance. 

### 1.3 GAN and VAE

The third and fourth categories are based on Generative Adversarial Network (GAN) [24] and Variational Autoencoder (VAE) [25] respectively, which are the most popular deep generative models in recent years.

They can not only perform clustering task, but also can generate new samples from the obtained clusters. 



본 논문에서는 구조에 따라 좀더 살펴 보겠다. To be more detailed, 
- we present a taxonomy of existing deep clustering methods based on the network architecture. 
- We introduce the representative deep clustering methods and 
- compare the advantages and disadvantages of different architectures and methods. 
- Finally, some directions are suggested for future development of this field

논문의 구조는 아래와 같다. `The rest of this paper is organized as follows:`
- Section II reviews some preliminaries of deep clustering. 
- Section III presents a taxonomy of existing deep clustering algorithms and introduces some representative methods. 
- Finally, Section IV provides some notable trends of deep clustering and gives conclusion remarks.


## II. PRELIMINARIES


### 2.1 NEURAL NETWORK ARCHITECTURE FOR DEEP CLUSTERING


used to transform inputs to a new feature representation.

#### A. FEEDFORWARD FULLY-CONNECTED NEURAL NETWORK


개요 : A fully-connected network (FCN) consists of multiple layers of neurons, each neuron is connected to every neuron in the previous layer, and each connection has its own weight. The FCN is also known as multi-layer perceptron (MLP). It is a totally general purpose connection pattern and makes no assumptions about the features in the data. 

보통 지도 학습용으로 사용 됨 `It is usually used in supervised learning when labels are provided. `

클러서터링 학습에 사용시 : However, for clustering, a good initialization of parameters of network is necessary because a naive FC network tends to obtain a trivial solution when all data points are simply mapped to tight clusters, which will lead to a small value of clustering loss, but be far from being desired [13].

#### B. FEEDFORWARD CONVOLUTIONAL NEURAL NETWORK

개요 : Convolutional neural networks (CNNs) [26] were inspired by biological process, in which the connectivity pattern between neurons is inspired by the organization of the animal visual cortex. Likewise, each neuron in a convolutional layer is only connected to a few nearby neurons in the previous layer, and the same set of weights is used for every neuron. 

이미지 데이터에 많이 적용됨 : It is widely applied to image datasets when locality and shift-invariance of feature extraction are required. 

군집화 loss학습시 사용 가능 : It can be trained with a specific clustering loss directly without any requirements on initialization, and a good initialization would significantly boost the clustering performance. 

To the best of our knowledge, no theoretical explanation is given in any existing papers, but extensive work shows its feasibility for clustering.


#### C. DEEP BELIEF NETWORK

개요 : Deep Belief Networks (DBNs) [27] are generative graphical models which learn to extract a deep hierarchical representation of the input data. A DBN is composed of several stacked Restricted Boltzmann machines (RBMs) [28]. 

비지도 학습이 적용된 예 : The greedy layer-wise unsupervised training is applied to DBNs with RBMs as the building blocks for each layer. 

Then, all (or part) of the parameters of DBN are fine-tuned with respect to certain criterion (loss function), e.g., a proxy for the DBN log-likelihood, a supervised training criterion, or a clustering loss.

#### D. AUTOENCODER

개요 
- Autoencoder (AE) is one of the most significant algorithms in unsupervised representation learning. 
- It is a powerful method to train a mapping function, which ensures the minimum reconstruction error between coder layer and data layer. 
- Since the hidden layer usually has smaller dimensionality than the data layer, it can help find the most salient features of data. 

지도/비지도 에서 좋은 성과 보임 : Although autoencoder is mostly applied to find a better initialization for parameters in supervised learning, it is also natural to combine it with unsupervised clustering. 

More details and formulations will be introduced in Section III-A.

#### E. GAN & VAE

개요 : Generative Adversarial Network (GAN) and Variational Autoencoder (VAE) are the most powerful frameworks for deep generative learning. 
- **GAN** aims to achieve an equilibrium between a generator and a discriminator, 
- while **VAE** attempts to maximizing a lower bound of the data loglikelihood.

A series of model extensions have been developed for both GAN and VAE. 

군집화에 많이 적용 되었음 `Moreover, they have also been applied to handle clustering tasks. `

The details of the two models will be elaborated in Section III-C and Section III-D, respectively.



### 2.2 LOSS FUNCTIONS RELATED TO CLUSTERING

#### A. Principal Clustering Loss

This category of clustering loss functions contain the **cluster centroids** and **cluster assignments** of samples. 

즉, 학습이 끝나고 군집 결과를 바로 얻을수 있음 `In other words, after the training of network guided by the clustering loss, the clusters can be obtained directly.`

It includes 
- k-means loss [13], 
- cluster assignment hardening loss [11], 
- agglomerative clustering loss [29], 
- nonparametric maximum margin clustering [30] 
- and so on

#### B. Auxiliary Clustering Loss

군집을 위한 representation학습을 진행, 바로 군집 결과를 알수 없음 `The second category solely plays the role of guiding the network to learn a more feasible representation for clustering, but cannot output clusters straightforwardly. `

It means deep clustering methods with merely auxiliary clustering loss require to run a clustering method after the training of network to obtain the clusters. 

There are many auxiliary clustering losses used in deep clustering, such as
- locality-preserving loss [31], which enforces the network to preserve the local property of data embedding;
- group sparsity loss [31], which exploits block diagonal similarity matrix for representation learning; 
- sparse subspace clustering loss [32], which aims at learning a sparse code of data.


### 2.3 PERFORMANCE EVALUATION METRICS FOR DEEP CLUSTERING

#### A. unsupervised clustering accuracy (ACC)

![](https://i.imgur.com/yfHtjoZ.png)
- where yi is the ground-truth label, 
- ci is the cluster assignment generated by the algorithm, 
- and m is a mapping function which ranges over all possible one-to-one mappings between assignments and labels. 

It is obvious that this metric finds the best matching between cluster assignments from a clustering method and the ground truth. 

The optimal mapping function can be efficiently computed by **Hungarian algorithm** [33].


#### B. Normalized Mutual Information (NMI)

![](https://i.imgur.com/B8iAUhY.png)
- where Y denotes the ground-truth labels, 
- C denotes the clusters labels, 
- I is the mutual information metric 
- and H is entropy.


## III. TAXONOMY OF DEEP CLUSTERING

목적 : Deep clustering is a family of clustering methods that adopt deep neural networks to learn clustering-friendly representations.

The loss function (optimizing objective) of deep clustering methods are typically composed of two parts: 
- network loss Ln  
- clustering loss Lc, 

thus the loss function can be formulated as follows:

![](https://i.imgur.com/jfGqPDc.png)

- where λ ∈ [0, 1] is a hype-parameter to balance Ln and Lc.

The network loss Ln is used to learn feasible features and avoid trivial solutions, and the clustering loss Lc encourages the feature points to form groups or become more discriminative.

The network loss can be 
- the reconstruction loss of an autoencoder (AE), 
- the variational loss of a variational encoder (VAE) 
- or the adversarial loss of a generative adversarial network (GAN). 

the clustering loss can be 
- k-means loss, 
- agglomerative clustering loss, 
- locality-preserving loss 
- and so on. 

AE네트워크 기반에서는 네트워크 LOSS는 필수 적이다. `For deep clustering methods based on AE network, the network loss is essential.`

그러나 일부 네트워크에서는 클러스터링 LOSS만 사용 되기도 한다. `But some other work designs a specific clustering loss to guide the optimization of networks, in which case the network loss can be removed.`
- we refer this type of networks trained only by Lc as clustering DNN (CDNN). 

GAN/VAE기반 네트워크에서는 네트워크 LOSS와 클러스터링 LOSS가 같이 통합되어 사용된다. `For GAN-based or VAE-based deep clustering, the network loss and the clustering loss are usually incorporated together. `

본 논문에서는 네트워크 구조에 따라 4종류로 구분 하였다. `In this section, from the perspective of DNN architecture, we divide deep clustering algorithms into four categories: `
- AE-based, 
- CDNN-based, 
- VAE-based, and
- GAN-based deep clustering. 

 
### 3.1 AE-BASED DEEP CLUSTERING

Autoencoder is a kind of neural network designed for unsupervised data representation. 

It aims at minimizing the reconstruction loss. 

An autoencoder may be viewed as consisting of two parts: 
- an encoder function h = fφ(x) which maps original data x into a latent representation h, 
- and a decoder that produces a reconstruction r = gθ (h). 

The reconstructed representation r is required to be as similar to x as possible.

Note that both encoder and decoder can be constructed by
- fully-connected neural network or 
- convolutional neural network.


#### A. 성능 개선 요소 `The performance of autoencoder can be improved from the following perspectives: `
- Architecture: 
 - The original autoencoder is comprised of multiple layer perceptions. 
 - For the sake of handling data with spatial invariance, e.g., image data, convolutional and pooling layers can be used to construct a convolutional autoencoder (CAE).
- Robustness: 
 - To avoid overfitting and to improve robustness, it is natural to add noise to the input.
 - Denoising autoencoder [35] attempts to reconstruct x from x˜, which is a corrupted version of x through some form of noise. Additionally, noise can also be added to the inputs of each layer [14].
- Restrictions on latent features: 
 - Under-complete autoencoder constrains the dimension of latent coder z lower than that of input x, enforcing the encoder to extract the most salient features from original space.
 - Other restrictions can also be adopted, e.g., sparse autoencoder [36] imposes a sparsity constraint on latent coder to obtain a sparse representation.
- Reconstruction loss: 
 - Commonly the reconstruction loss of an autoencoder consists of only the discrepancy between input and output layer, 
 - but the reconstruction losses of all layers can also be optimized jointly [14].
 

The optimizing objective of AE-based deep clustering is thus formulated as follows:
![](https://i.imgur.com/CMue6Fs.png)


The reconstruction loss enforce the network to learn a feasible representation and avoid trivial solutions. 

#### B. 일반적인 네트워크 구조 `The general architecture of AE-based deep clustering algorithms is illustrated in Figure 1,`
![](https://i.imgur.com/aMPdXhg.png)


#### C. 대표적인 기법 들 `some representative methods are introduced as follows:`

##### 가. Deep Clustering Network (DCN)

DCN = 오토인코더 + k-mean 알고리즘 `DCN [13] is one of the most remarkable methods in this field, which combines autoencoder with the k-means algorithm. `

단계 
- In the first step, it pre-trains an autoencoder.
- Then, it jointly optimizes the reconstruction loss and k-means loss. 
 - Since k-means uses discrete cluster assignments, the method requires an alternative optimization algorithm. 


목적 :  The objective of DCN is simple compared with other methods and the computational complexity is relatively low.

##### 나.  Deep Embedding Network (DEN):

DEN [31] proposes a deep embedding network to extract effective representations for clustering. 


단계 
- It first utilizes a deep autoencoder to learn reduced representation from the raw data. 
- Secondly, in order to preserve the local structure property of the original data, a localitypreserving constraint is applied. 
 - Furthermore, it also incorporates a group sparsity constraint to diagonalize the affinity of representations. 
 - Together with the reconstruction loss, the three losses are jointly optimized to fine-tune the network for a clustering-oriented representation.
 - The locality-preserving and group sparsity constraints serve as the auxiliary clustering loss (see Section II-B), 
- thus, as the last step, k-means is required to cluster the learned representations.

##### 다. Deep Subspace Clustering Networks (DSC-Nets):

DSC-Nets [37] introduces a novel autoencoder architecture to learn an explicit non-linear mapping that is friendly to subspace clustering [38]. 

The key contribution is introducing a novel self-expressive layer, which is a fully connected layer without bias and non-linear activation and inserted to the junction between the encoder and the decoder. 

This layer aims at encoding the self-expressiveness property [39] [40] of data drawn from a union of subspaces. 

Mathematically, its optimizing objective is a subspace clustering loss combined with a reconstruction loss. 

Although it has superior performance on several small-scale datasets, it is really memory-consuming and time-consuming and thus can not be applied to large-scale datasets. 

The reason is that its parameter number is O(n^2) for n samples, and it can only be optimized by gradient descent


##### 라. Deep Multi-Manifold Clustering (DMC):

DMC [41] is deep learning based framework for multi-manifold clustering (MMC). 

It optimizes a joint loss function comprised of two parts: 
- the locality preserving objective and 
- the clustering-oriented objective.

The first part makes the learned representations meaningful and embedded into their intrinsic manifold.
- It includes the autoencoder reconstruction loss and locality preserving loss. 

The second part penalizes representations based on their proximity to each cluster centroids, making the representation cluster-friendly and discriminative. 

Experimental results show that DMC has a better performance than the state-of-the-art multi-manifold clustering methods.

##### 마. Deep Embedded Regularized Clustering (DEPICT):

DEPICT [14] is a sophisticated method consisting of multiple striking tricks. 

It consists of a softmax layer stacked on top of a multi-layer convolutional autoencoder.

It minimizes a relative entropy loss function with a regularization term for clustering. 

The regularization term encourages balanced cluster assignments and avoids allocating clusters to outlier samples. 

Furthermore, the reconstruction loss of autoencoder is also employed to prevent corrupted feature representation.

Note that each layer in both encoder and decoder contributes to the reconstruction loss, rather than only the input and output layer. 

Another highlight of this method is that it employs a noisy encoder to enhance the robustness of the algorithm. 

Experimental results show that DEPICT achieves superior clustering performance while having a high computational efficiency

##### 바. Deep Continuous Clustering (DCC):

DCC [42] is also an AE-based deep clustering algorithm.

It aims at solving two limitations of deep clustering. Since most deep clustering algorithms are based on classical center-based, divergence-based or hierarchical clustering formulations, they have some inherent limitations. 
- For one thing, they require setting the number of clusters in priori. 
- For another, the optimization procedures of these methods involve discrete reconfigurations of the objective, which require updating the clustering parameters and network parameters alternatively. 

DCC is rooted in Robust Continuous Clustering (RCC) [43], a formulation having a clear continuous objective and no prior knowledge of clusters number. 

Similar to many other methods, the representation learning and clustering is optimized jointly.



### 3.2 CDNN-BASED DEEP CLUSTERING

CDNN-based algorithms only use the clustering loss to train the network, where the network can be FCN, CNN or DBN.

The optimizing objective of CDNN-based algorithms can be formulated as follows: $$ L = L_c $$

Without the reconstruction loss, CDNN-based algorithms suffer from the risk of obtaining corrupted feature space, when all data points are simply mapped to tight clusters, resulting in a small value of clustering loss but meaningless.

Consequently, the clustering loss should be designed carefully and network initialization is important for certain
clustering loss. 

network initialization에 따른 분류 `For this reason, we divide CDNN-based deep clustering algorithms into three categories according to the ways of network initialization, i.e., `
- unsupervised pre-trained, 
- supervised pre-trained and 
- randomly initialized (non-pre-trained).

#### A. UNSUPERVISED PRE-TRAINED NETWORK

RBMs and autoencoders have been applied to CDNN-based clustering. 

- These algorithms firstly train a RBM or an autoencoder in an unsupervised manner, 
- then fine-tune the network (only encoder part for the autoencoder) by the clustering loss.

Several representative algorithms are introduced as below.

##### 가. Deep Nonparametric Clustering (DNC)

##### 나. Deep Embedded Clustering (DEC)

##### 다. Discriminatively Boosted Clustering (DBC)


#### B. SUPERVISED PRE-TRAINED NETWORK

Although unsupervised pre-training provides a better initialization of networks, it is still challenging to extract feasible features from complex image data. 

Guérin et al. [44] conduct extensive experiments by testing the performance of combinations of different popular CNN architectures pre-trained on ImageNet [45] and different classical clustering algorithms.

The experimental results show that feature extracted from deep CNN trained on large and diverse labeled datasets, combined with classical clustering algorithms, can outperform the state-of-the-art image clustering methods. 

To this effect, when the clustering objective is complex image data, it is natural to make use of the most popular network architectures like VGG [46], ResNet [47] or Inception [48] models, which are pre-trained on large-scale image datasets like ImageNet, to speed up the convergence of iterations and to boost the clustering quality. 

The most remarkable method of this type is introduced as follows:

##### 가. Clustering Convolutional Neural Network (CCNN)


#### C. NON-PRE-TRAINED NETWORK

Despite the fact that a pre-trained network can significantly boost the clustering performance, under the guidance of
a well-designed clustering loss, the networks can also be trained to extract discriminative features.


##### 가. Information Maximizing Self-Augmented Training (IMSAT)

##### 나. Joint Unsupervised Learning (JULE)

##### 다. Deep Adaptive Image Clustering (DAC)





### 3.4 SUMMARY OF DEEP CLUSTERING ALGORITHMS


In this part, we present an overall scope of deep clustering algorithms. 

Specifically, we compare the four categories of algorithms in terms of loss function, advantages, disadvantages
and computational complexity. 

![](https://i.imgur.com/QB3NNnp.png)

#### A. loss function

In regard to the loss function, apart from CDNN-based algorithms, the other three categories of algorithms jointly
optimize both clustering loss Lc and network loss Ln. 

The difference is that the network loss of AE-based algorithms is explicitly reconstruction loss, while the two losses of VAE-based and GAN-based algorithms are usually incorporated together.

AE-based DC algorithms are most common as autoencoder can be combined with almost all clustering algorithms.

The reconstruction loss of autoencoder ensures the network learns a feasible representation and avoid obtaining trivial solutions. 

However, due to the symmetry architecture, the network depth is limited for computational feasibility.

Besides, the hyper-parameter to balance the two losses requires extra fine-tuning. 

In contrast to AE-based DC algorithms, CDNN-based DC algorithms only optimize the clustering loss. 

Therefore, the depth of network is unlimited and supervisedly pre-trained architectures can be used to extract more discriminative features, thus they are capable to cluster large-scale image datasets. 

However, without the reconstruction loss, they have the risk of learning a corrupted feature representation, thus the clustering loss should be welldesigned.

VAE-based and GAN-based DC algorithms are generative DC techniques, as they are capable to generate samples from the finally obtained clusters. 

VAE-based algorithms have a good theoretical guarantee because they minimizes the variational lower bound on the marginal likelihood of data, but it suffer from high-computational complexity.

GAN-based algorithms impose a multi-class priori on general GAN framework. 

They are more flexible and diverse than VAE-based ones. 

Some of them aim at learning interpretable representations and just take clustering task as a specific case.

The shortcomings of GAN-based algorithms are similar to GANs, e.g, mode collapse and converge slowly.

#### B. computational complexity

The computational complexity of deep clustering varies a lot. 

For AE-based and CDNN-based algorithms, the computational cost is highly related to the clustering loss. 

For example, k-means loss results in a relatively low overhead while the cost of agglomerative clustering is extremely high.

At the same time, the network architectures also influence the computational complexity significantly, as a deep CNN
requires a long time to train. 

For VAE and GAN, due to the difficulty to optimize, they usually have a higher computational complexity than efficient methods in the AE-based and CDNN-based categories, e.g., DEC, DCN, DEPICT and so on.

---


Some notations frequently used in the paper and their meanings are presented in Table 1
![](https://i.imgur.com/QJrkVh1.png)


The components of representative algorithms are illutrated in Table 2
![](https://i.imgur.com/EG3bmn5.png)


their contributions are described briefly in Table 3.
![](https://i.imgur.com/lnEiH6X.png)


















