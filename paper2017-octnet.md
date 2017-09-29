|논문명|OctNet: Learning Deep 3D Representations at High Resolutions |
|-|-|
|저자(소속)| Gernot Riegler (Graz University)|
|학회/년도| CVPR 2017, [논문](https://arxiv.org/abs/1611.05009)|
|키워드| |
|참고||
|코드|[Torch](https://github.com/griegler/octnet)|



# OctNet


To alleviate this problem, Riegler et al. (2017) propose OctNets,a 3D convolutional network, that allows for training deep architectures at significantly higher resolutions. 

They build onthe observation that 3D data (e.g., point clouds, meshes) is oftensparse in nature. 

The proposed OctNet exploits this sparsity property by hierarchically partitioning the 3D space into aset of octrees and applying pooling in a data-adaptive fashion.

This leads to a reduction in computational and memory requirements as the convolutional network operations are defined on the structure of these trees and thus can dynamically allocate resources depending on the structure of the input.



