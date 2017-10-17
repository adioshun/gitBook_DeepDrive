| 논문명 | Pairwise Decomposition of Image Sequences for Active Multi-View Recognition |
| --- | --- |
| 저자\(소속\) | Edward Johns (Imperial College London, UK) |
| 학회/년도 | May 2016, [논문](https://arxiv.org/abs/1605.08359) |
| 키워드 |  |
| 데이터셋(센서)/모델 |  |
| 참고 |[CVPR2016](https://www.youtube.com/watch?v=7Bw0HGlidtg)  |
| 코드 |  |


# Pairwise MVCNN

We propose to bring Convolutional Neural Networks to generic multi-view recognition, by 
- decomposing an image sequence into a set of image pairs, 
- classifying each pair independently, and 
- then learning an object classifier by weighting the contribution of each pair

제안 방식의 장점 : This allows for recognition over arbitrary(임의) camera trajectories(궤도), without requiring explicit training over the potentially infinite number of camera paths and lengths. 

Building these pairwise relationships then naturally extends to the **next-best-view problem** in an active recognition framework. 
- To achieve this, we train a second Convolutional Neural Network to map directly from an observed image to next viewpoint.

Finally, we incorporate this into a trajectory optimisation task, whereby the best recognition confidence is sought for
a given trajectory length.

## 1. Introduction

![](https://i.imgur.com/hsqKgpl.png)
```
[Figure 1]
- We propose a method for multi-view object recognition, by decomposing an image sequence into a set of image pairs. 
- Training on these pairs then allows for recognition and trajectory planning, without the need to train directly over the infinite possible number of camera paths that may exist.
```

그림 1을 예로 볼때 카메라를 어느 위치에 두는게 가장 좋은 결과를 가져 올까? `Consider the scenario in Figure 1. What trajectory should the camera move around the object in order to achieve the highest recognition confidence in a given time?`
- 실생활에서는 multi-view image sequence에서 물체를 인식하는게 single-image에서 인식하는것보다 더 realistic setting이다. `For practical tasks, recognition from a multi-view image sequence is a more realistic setting than the single-image recognition tasks typically addressed in computer vision, and controlling a camera actively for efficient recognition has great significance in real-world applications, where time or power constraints become realities. `

학계에서는 3D 메쉬를 인조 회색 이미지`(synthetic greyscale images)`로 렌더링 하여 분류 하는게 좋은 성능을 보이는 것으로 알려져 있다. `It was subsequently shown that rendering these meshes as synthetic greyscale images, and classifying objects in a view-based manner with a CNN architecture acting over a fixed trajectory, achieved state of-the-art results for multi-view recognition [35].`

하지만 이 방식을 입력 이미지의 **fixed-length**가 필요 하기 때문에 일반적으로 사용하기는 어렵다. `However, extending this to generalised recognition over trajectories of arbitrary paths and lengths is not readily adopted by traditional CNN architectures, due to the need for fixed-length input data.`

>  **fixed-lengtht** ???

```
[35-MVCNN2015] H. Su, S. Maji, E. Kalogerakis, and E. G. Learned-Miller. Multi-view Convolutional Neural Networks for 3D Shape Recognition. In Proceedings of the International Conference on Computer Vision (ICCV), 2015.
```

### 1.1 CNNs for Generalised Multi-View Recognition

One solution to multi-view recognition with CNNs would be to simply concatenate all observed images into a single input to a network. 

However, this would require intractable training due to the large size of each input, but more importantly, due to the need to train over every possible path of all possible lengths, which is of potentially infinite scale. 

We propose to address this by relaxing the joint model over images and decomposing an image sequence into a set of pairs, one for every pair of images across the sequence.Pairwise representations of full distributions have been popular in computer vision for learning distributions of local features [19] and parts [10], and we migrate this idea from the image space domain to the temporal domain.Given this decomposition, a CNN is then trained on a fixed length input consisting of the image pair, together with the relative pose between the associated viewpoints. 

To achieve classification of the full sequence, an ensemble framework is adopted, with weighting to increase the contribution of those image pairs which cover a more informative set of poses


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQ4Njg0NDMyNF19
-->