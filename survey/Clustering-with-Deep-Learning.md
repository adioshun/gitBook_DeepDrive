# [Clustering with Deep Learning: Taxonomy and New Methods](https://arxiv.org/abs/1801.07648): 2018.01 [[깃허브]](https://github.com/elieJalbout/Clustering-with-Deep-learning)

> Elie Aljalbout, Vladimir Golkov, Yawar Siddiqui, Daniel Cremers "Clustering with Deep Learning: Taxonomy and new methods"

## 1 INTRODUCTION

- 클러스터링 알고리즘들은 데이터에 영향을 많이 받는다. `The performance of current clustering methods is however highly dependent on the input data.`

- 다른 데이터셋들은 다른 측정방식과 기술들을 필요로 한다. `Different datasets usually require different similarity measures and separation techniques. `

- 결과적으로 여러 기술들을 필요로 한다. ` As a result,dimensionality reduction and representation learning have been extensively used alongside clustering in order to map the input data into a feature space where separation is easier. `

- 딥러닝을 이용함으로써 non-linear mappings이 가능하다. 즉, 수동적인 특징 추출 및 선별이 필요 없다. `By utilizing deep neural networks (DNNs), it is possible to learn non-linear mappings that allow transforming data into more clustering-friendly representations without manual feature extraction/selection.`

- 과거에는 특징 추출 후 클러스터링 순으로 진행 되었다. `In the past, feature extraction and clustering were applied sequentially Ding and He (2004); Trigeorgis et al. (2014).`

- 최근에는 이들을 동시에 진행 하는 방식으로 바뀌었다. ` However, recent work shows that jointly optimizing for both can yield better results Song et al. (2013); Xie et al. (2016); Yang et al. (2016a;b); Li et al. (2017).`

- 본 연구에서는 **fully convolutional autoencoder**을 이용하여 두 단계의 학습 절차를 진행 하도록 하였다. In this case study, we use a fully convolutional autoencoder to learn clustering-friendly representations
of the data by optimizing it with a two-phased training procedure. 
    - In the first phase, the autoencoder is trained with the standard mean squared error reconstruction loss. 
    - In the second phase, the autoencoder is then fine-tuned with a combined loss function consisting of the autoencoder reconstruction loss and a clustering-specific loss.
    



본 논문의 구성은 아래와 같다. `The rest of this paper is organized as follows:`
- At first, we introduce the taxonomy and its building blocks in Section 2. 
- In Section 3, we then present a comprehensive review of clustering methods and analyze them with respect to the proposed taxonomy. 
- Subsequently, in Section 4, we propose a new method based on insights gained in a systematic way from the taxonomy. 
- The evaluation of the proposed method is presented in Section 5, 
- followed by the conclusions in Section 6.

## 2 TAXONOMY


대부분의 딥러닝 기반 클러스터링은 다음 절차로 진행 된다. `The most successful methods for clustering with deep neural networks all work following the same principle:`
- representation learning using DNNs and 
- using these representations as input for a specific clustering method.

![](https://i.imgur.com/s032Amh.png)


Neural network training procedure, consisting of:
- Main neural network branch and its usage
    * Architecture of main neural network branch, described in Section 2.1
    ∗ Set of deep features used for clustering, described in Section 2.2
- Neural network losses:
    ∗ Non-clustering loss, described in Section 2.3
    ∗ Clustering loss, described in Section 2.4
    ∗ Method to combine the two losses, described in Section 2.5
- Cluster updates, described in Section 2.6

(Optional) Re-run clustering after network training, described in Section 2.7


### 2.1 ARCHITECTURE OF MAIN NEURAL NETWORK BRANCH

**main branch**는 입력정보를 잠재적 representation로 변경하여 클러스터링 입력으로 하용한다. `In most DNNs-based clustering methods, the “main branch” of the neural network is used to transform the inputs into a latent representation that is used for clustering. `

과거에는 아래 네트워크들이 이런 목적으로 사용되었다. `The following neural network architectures have previously been used for this purpose:`
- Multilayer Perceptron (MLP)
    - Feedforward network, consisting of several layers of neurons, such that the output of every hidden layer is the input to next one.
- Convolutional Neural Network (CNN)
    - Inspired by biology, more precisely by the organization of the animal visual cortex. 
    - Useful for applications to regular-grid data such as images, if locality and shift-equivariance/invariance of feature extraction is desired.
- Deep Belief Network (DBN)
    - Generative graphical model, consisting of several layers of latent variables. 
    - It is composed of several shallow networks such as restricted Boltzmann machines, such that the hidden layer of each sub-network serves as the visible layer of the next sub-network.
- Generative Adversarial Network (GAN)
    - A system of two competing neural network models G and D that engage in a zero-sum game. 
    - The generator G learns a distribution of interest to produce samples. 
    - The discriminator D learns to distinguish between real samples and generated ones (Goodfellow et al., 2014).
- Variational Autoencoder (VAE)
    - A Bayesian network with an autoencoder architecture that learns the data distribution (generative model).
    

### 2.2 SET OF DEEP FEATURES USED FOR CLUSTERING


위 방법으로 입력을 변환한 후 특징점들은 한개 or 여러개의 뉴럴네트워크 층을 거쳐 클러스터링에 이용된다. `After transforming the input to a more clustering-friendly representation, the features that are then used for clustering can be taken from one or more layers of the deep neural network:`

- One layer
    - Refers to the case where only one layer of the network is used which is beneficial because of its low dimensionality. 
    - In most cases the output of the last layer is used.
- Several layers
    - Refers to the case where the representation is a combination of the outputs of several layers. 
    - Thus, the representation is richer and allows the embedded space to represent more complex semantic representations, which might enhance the separation process and help in the similarity computation (Saito and Tan, 2017).


### 2.3 NON-CLUSTERING LOSS


군집 알고리즘과는 독립적이며, 학습모델의 제약사항을 강화 시킨다. `The non-clustering loss is independent of the clustering algorithm and usually enforces a desired constraint on the learned model. `

활용 가능한 Loss들은 다음과 같다. `Possible options are as follows:`


#### A. No non-clustering loss

No additional non-clustering loss function is used and the network model is only constrained by the clustering loss. 

For most clustering losses, the absence of a non-clustering loss can have a danger of worse representations/results, or theoretically even collapsing clusters (Yang et al., 2016a), but the latter rarely occurs in practice.

#### B.  Autoencoder reconstruction loss

The autoencoder consists of two parts : an **encoder** and a **decoder**. 
- The encoder maps its input x to a representation z in a latent space Z. 
- During training, the decoder tries to reconstruct x from z, making sure that useful information has not been lost by the encoding phase. 

In the context of clustering methods, once the training is done the decoder part is no longer used, and the encoder is left for mapping its input to the latent space Z. 

By applying this procedure, autoencoders can successfully learn useful representations in the cases where the output’s dimensionality is different from the input’s or when random noise is injected to the input (Vincent et al., 2010). 

Additionally, they can also be used for dimensionality reduction goals (Hinton and Salakhutdinov, 2006).

Generally the reconstruction loss is a distance measure dAE(xi, f(xi)) between the input xi to the autoencoder and the corresponding reconstruction f(xi). 

One particular formulation of it is using the mean squared error of the two variables:

![](https://i.imgur.com/56HccWy.png)
- where xi is the input and 
- f(xi) is the autoencoder reconstruction. 

This loss function guarantees that the learned representation preserves important information from the initial one, which is why reconstruction is possible.

#### C. Self-Augmentation Loss 

Hu et al. (2017) proposes a loss term that pushes together the representation of the original sample and their augmentations:

![](https://i.imgur.com/4lH1v22.png)
- where x is the original sample, 
- T is the augmentation function, 
- f(x) is the representation generated by the model, and 
- s is some measure of similarity (for example cross-entropy if f has a softmax nonlinearity).

#### D. Other tasks

Additional information about training samples that is available in the form of targets, even if not perfectly suitable to dictate clustering, can be used in a (multi-task) non-clustering loss to encourage meaningful feature extraction.

## 2.4 CLUSTERING LOSS

군집 알고리즘과 위존적이다. `The second type of functions is specific to the clustering method and the clustering-friendliness of the learned representations, therefore such functions are called clustering loss functions. `

활용 가능한 Loss들은 다음과 같다. `The following are options for clustering loss functions:`

> 각 Loss에 대한 상세 내용은 논문 추가 참고 

#### A. No clustering loss

Even if a neural network has only non-clustering losses (Section 2.3), the features it extracts can be used for clustering after training (Sections 2.6–2.7). 

The neural network serves in this case for changing the representation of the input, for instance changing its dimensionality. 

Such a transformation could be beneficial for the clustering sometimes, but using a clustering loss usually yields better results (Xie et al., 2016; Yang et al., 2016a).

#### B. k-Means loss

Assures that the new representation is k-means-friendly (Yang et al., 2016a), i.e. data points are evenly distributed around the cluster centers.

#### C. Cluster assignment hardening

Requires using soft assignments of data points to clusters. 

For instance, Student’s t-distribution can be used as the kernel to measure the similarity (van der Maaten and Hinton, 2008) between points and centroids.

#### D. Balanced assignments loss

This loss has been used alongside other losses such as the previous one (Dizaji et al., 2017). 

Its goal is to enforce having balanced cluster assignments.

#### E. Locality-preserving loss

This loss aims to preserve the locality of the clusters by pushing nearby data points together (Huang et al., 2014).

#### F. Group sparsity loss

It is inspired by spectral clustering where block diagonal similarity matrix is exploited for representation learning (Ng et al., 2002). 

Group sparsity is itself an effective feature selection method. 

In Huang et al. (2014), the hidden units were divided into G groups, where G is the assumed number of clusters. 

#### G. Cluster classification loss

Cluster assignments obtained during cluster updates (Section 2.6) can be used as “mock” class labels for a classification loss in an additional network branch, in order to encourage meaningful feature extraction in all network layers (Hsu and
Lin, 2017).

#### H. Agglomerative clustering loss

Agglomerative clustering merges two clusters with maximum affinity (or similarity) in each step until some stopping criterion is fulfilled. 

A neural network loss inspired by agglomerative clustering (Yang et al., 2016b) is computed in several steps. 

- First, the cluster update step (Section 2.6) merges several pairs of clusters by selecting the pairs with the best affinity (some predefined measure of similarity between clusters). 
- Then network training retrospectively even further optimizes the affinity of the already merged clusters (it can do so because the affinity is measured in the latent space to which the network maps). 
- After the next cluster update step, the network training switches to retrospectively optimizing the affinity of the newest set of newly merged cluster pairs. 
- In this way, cluster merging and retrospective latent space adjustments go hand in hand. 
- Optimizing the network parameters with this loss function would result in a clustering space more suitable for (agglomerative) clustering.


### 2.5 METHOD TO COMBINE THE LOSSES

In the case where a clustering and a non-clustering loss function are used, they are combined as follows:

![](https://i.imgur.com/TwU9rif.png)
- where Lc(θ) is the clustering loss, 
- Ln(θ) is the non-clustering loss, 
- and α ∈ [0; 1] is a constant specifying the weighting between both functions. 

It is an additional hyperparameter for the network training. 

It can also be changed during training following some schedule. 

```
In phases with α = 1, no non-clustering loss is imposed, with potential disadvantages (see No nonclustering loss in Section 2.3). 
Similarly, in phases with α = 0, no clustering loss is imposed, with potential disadvantages (see No clustering loss in Section 2.4).
```

다음 방식들을 사용하여 α 값을 assign and schedule할수 있다. ` The following are methods to assign and schedule the values of α:`

#### A. Pre-training, fine-tuning

First, α is set to 0, i.e. the network is trained using the nonclustering loss only. 

Subsequently, α is set to 1, i.e. the non-clustering network branches (e.g. autoencoder’s decoder) are removed and the clustering loss is used to train (fine-tune) the obtained network. 

The constraint forced by the reconstruction loss could be lost after training the network long enough for clustering only. 

In some cases, losing such constraints may lead to worse results (see Table 1).

#### B. Joint training

0 < α < 1, for example α = 0.5, i.e. the network training is affected by both loss functions.


#### C. Variable schedule

α is varied during the training dependent on a chosen schedule. 

For instance, start with a low value for α and gradually increase it in every phase of the training.

### 2.6 CLUSTER UPDATES

클러스터링 방식은 두 가지로 분류 될수 있다. `Clustering methods can be broadly categorized into hierarchical and partitional (centroid-based) approaches (Jain et al., 1999). `
- Hierarchical clustering combines methods which aim to build a hierarchy of clusters and data points. 
- On the other hand, partitional (centroid-based) clustering groups methods which create cluster centers and use metric relations to assign each of the data points into the cluster with the most similar center.


딥러닝 클러스터링은 두 가지로 분류 될 수 있다. `In the context of deep learning for clustering, the two most dominant methods of each of these categories have been used. `
- Agglomerative clustering, which is a **hierarchical clustering method**, has been used with deep learning (Yang et al., 2016b). 
    - The algorithm has been briefly discussed in Section 2.4. 
- In addition, k-means, which falls into the category of **centroid-based clustering**, was extensively used (Xie et al., 2016; Yang et al., 2016a; Li et al., 2017; Hsu and Lin, 2017).


During the network training, cluster assignments and centers (if a centroid-based method is used) are updated. 

Updating cluster assignments can have one of the two following forms:

#### 가. Jointly updated with the network model

Cluster assignments are formulated as probabilities, therefore have continuous values between 0 and 1. 

In this case, they can be included as parameters of the network and optimized via back-propagation.


#### 나. Alternatingly updated with the network model

Clustering assignments are strict and updated in a different step than the one where the network model is updated. 

In this case, several scenarios are possible, dependent on two main factors:
- Number of iterations
    - Number of iterations of the chosen clustering algorithm, that are executed at every cluster update step. 
    - For instance, in Xie et al. (2016), at each cluster update step, the algorithm runs until a fixed percentage of points change assignments between two consecutive iterations.
- Frequency of updates
    - How often are cluster updates started
    - For instance in Yang et al. (2016b), for every P network model update steps, one cluster updates step happens.
    

### 2.7 AFTER NETWORK TRAINING

After the training is finished, even if a clustering result was produced in the process, it can make sense to re-run a clustering algorithm from scratch using the learned features, for one of several reasons:

#### 가. Clustering a similar dataset

- The general and the most trivial case is to reuse the learned features representation mapping on another dataset which is similar to the one that has been used but has different data.

#### 나. Obtaining better results

- Under certain circumstances, it is possible that the results of clustering after the training are better than the ones obtained during the learning procedure.

- For instance, in Yang et al. (2016b), such a behavior is reported. One possible reason for this to happen is that the cluster update step during the training doesn’t go all the way till the end (see Number of iterations in Section 2.6).



## 3 RELATED METHODS

![](https://i.imgur.com/ZqPbP1J.png)

### 3.1 Convolutional neural networks as feature extractors 

Some methods utilize convolutional neural networks as feature extractors to improve clustering of image data. 

- JULE (Yang et al., 2016b) follows a hierarchical clustering approach and uses the agglomerative clustering loss as the sole loss function.
- In CCNN (Hsu and Lin, 2017), initialization of the k-means centroids is performed based on the softmax output layer of a convolutional neural network and the output of internal network layers are used as features. 
- IMSAT (Hu et al., 2017) uses the information maximization loss and a selfaugmentation loss. 
- SCCNN (Lukic et al., 2016) uses a convolutional network that was pretrained on a related, domain-specific task (speaker identification) as a feature extractor.

### 3.2 Autoencoders as feature extractors 

In contrast to the aforementioned methods, some of the most promising methods utilize autoencoders as feature extractors. 

Training is performed in two phases.
- In the first phase, the autoencoder is pretrained using a standard reconstruction loss. 
- The second phase differs between the methods: 

#### 가. DEC (Xie et al., 2016), 

In the second phase of DEC (Xie et al., 2016), the network is fine-tuned using the cluster assignment hardening loss. 

DEC is often used as a baseline for new publications. 

DBC (Li et al., 2017) and DEPICT Dizaji et al. (2017) are similar to DEC except for one aspect each: 
    - DBC utilizes a convolutional autoencoder in order to improve clustering of image datasets and 
    - DEPICT adds a balanced assignments loss to the clustering loss to alleviate the danger of obtaining degenerate solutions
    
#### 나. DCN (Yang et al., 2016a)

In contrast to DEC and similar methods, DCN (Yang et al., 2016a) jointly trains the network with both the autoencoder reconstruction loss and the k-means clustering loss in the second phase. 

In, DEN Huang et al. (2014), the second phase is comprised of joint training with a combination of the reconstruction loss, a locality-preserving loss, and a group sparsity loss. 

In Neural Clustering Saito and Tan (2017), the second training phase does not exist and no additional clustering loss is used.

The good results can possibly be attributed to the fact that multiple network layers are concatenated
and used as the clustering features.



### 3.3 Other deep architectures as feature extractors 

- NMMC (Chen, 2015) and UMMC (Chen et al., 2017) each use a deep belief network for feature extraction. 
- UGTAC (Premachandran and Yuille, 2016) uses the penultimate layer of the discriminator in the DCGAN (Radford et al., 2015) architecture as features for k-means++ clustering. 
- VaDE (Zheng et al., 2016) uses a variational autoencoder in combination with a mixture of Gaussians.


### 3.4 Other methods 

Instead of directly using a neural network to extract features, 

- infinite ensemble clustering (Liu et al., 2016) uses neural networks to generate infinite ensemble partitions and to fuse them into a consensus partition to obtain the final clustering.

## 4.  CASE STUDY: NEW METHOD

![](https://i.imgur.com/aL93gvU.png)

학습데이터가 이미지 이므로 `Since the dataset that is to be clustered consists of images,`
- we chose a convolutional architecture for the architecture building block (Section 2.1) and 
- an autoencoder reconstruction loss as the nonclustering loss building block (Section 2.3).

After pretraining the network with this configuration, 
- we chose to keep the non-clustering autoencoder reconstruction loss and 
- add the cluster hardening loss as the clustering loss building block (Section 2.4). 

We decided to keep the **non-clustering loss** in this phase, 
- because other methods(e.g. DEC and DBC) which omit it, have a theoretical risk of collapsing clusters and 
- have also empirically shown to yield worse clustering quality. 
- This is because valuable feature detectors that were previously learned during pretraining can be destroyed. 
- Keeping the non-clustering loss helps to keep those detectors stable. 

For a similar reason, we decided to avoid a training procedure with alternating losses as for instance used by DBC, DEN, and UMMC. 

The necessity for this alternation originates in the hard assignments as enforced by the k-means loss, which is why we chose soft cluster assignments and cluster hardening loss instead. 

This loss is achieved via introducing a clustering layer, which aims at estimating the cluster assignments based on equation (4).

Once both training phases (pretraining on non-clustering loss and fine-tuning on both losses) are completed, the network’s encoder has learned to map its input to a clustering-friendly space. 

Additionally, the resulting network is capable of estimating the cluster assignments. 

However, based on the previous success of re-running clustering from scratch after training (see Section 2.7), we run
the k-means algorithm on the network’s output representation.



## 5. EXPERIMENTAL RESULTS


## 6. CONCLUSION



















