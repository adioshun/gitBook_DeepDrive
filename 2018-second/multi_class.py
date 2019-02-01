#!/usr/bin/env python
# coding: utf-8

# In[1]:


from second.pytorch.inference import TorchInferenceContext
import second.core.box_np_ops as box_np_ops


# In[2]:


import numpy as np
import pickle
import math
import sys
from glob import glob
from pathlib import Path
import pykitti
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[3]:


point_size = 1.0
axes_str = ['X', 'Y', 'Z']
axes_limits = [
    [-20, 80], # X axis range
    [-20, 20], # Y axis range
    [-3, 10]   # Z axis range
]
num_features = 4


# In[4]:


def kitti_anno_to_corners(info, annos=None):
    rect = info['calib/R0_rect']
    P2 = info['calib/P2']
    Tr_velo_to_cam = info['calib/Tr_velo_to_cam']
    if annos is None:
        annos = info['annos']
    dims = annos['dimensions']
    loc = annos['location']
    rots = annos['rotation_y']
    scores = None
    if 'score' in annos:
        scores = annos['score']
    boxes_camera = np.concatenate([loc, dims, rots[..., np.newaxis]], axis=1)
    boxes_lidar = box_np_ops.box_camera_to_lidar(boxes_camera, rect, Tr_velo_to_cam)
    boxes_corners = box_np_ops.center_to_corner_box3d(
        boxes_lidar[:, :3],
        boxes_lidar[:, 3:6],
        boxes_lidar[:, 6],
        origin=[0.5, 0.5, 0],
        axis=2)
    
    return boxes_corners, scores, boxes_lidar


# In[5]:


def draw_box(pyplot_axis, vertices, axes=[0, 1, 2], color='black'):
    """
    Draws a bounding 3D box in a pyplot axis.
    
    Parameters
    ----------
    pyplot_axis : Pyplot axis to draw in.
    vertices    : Array 8 box vertices containing x, y, z coordinates.
    axes        : Axes to use. Defaults to `[0, 1, 2]`, e.g. x, y and z axes.
    color       : Drawing color. Defaults to `black`.
    """
    vertices = vertices[axes, :]
    connections = [
        [0, 1], [1, 2], [2, 3], [3, 0],  # Lower plane parallel to Z=0 plane
        [4, 5], [5, 6], [6, 7], [7, 4],  # Upper plane parallel to Z=0 plane
        [0, 4], [1, 5], [2, 6], [3, 7]  # Connections between upper and lower planes
    ]
    for connection in connections:
        pyplot_axis.plot(*vertices[:, connection], c=color, lw=0.5)


# In[6]:


def draw_point_cloud(ax, title, points, boxes_corners, axes=[0, 1, 2], xlim3d=None, ylim3d=None, zlim3d=None):
    """
    Convenient method for drawing various point cloud projections as a part of frame statistics.
    """
    ax.scatter(*np.transpose(points[:, axes]), s=point_size, c=points[:, 3], cmap='gray')
    ax.set_title(title)
    ax.set_xlabel('{} axis'.format(axes_str[axes[0]]))
    ax.set_ylabel('{} axis'.format(axes_str[axes[1]]))
    if len(axes) > 2:
        ax.set_xlim3d(*axes_limits[axes[0]])
        ax.set_ylim3d(*axes_limits[axes[1]])
        ax.set_zlim3d(*axes_limits[axes[2]])
        ax.set_zlabel('{} axis'.format(axes_str[axes[2]]))
    else:
        ax.set_xlim(*axes_limits[axes[0]])
        ax.set_ylim(*axes_limits[axes[1]])
    # User specified limits
    if xlim3d!=None:
        ax.set_xlim3d(xlim3d)
    if ylim3d!=None:
        ax.set_ylim3d(ylim3d)
    if zlim3d!=None:
        ax.set_zlim3d(zlim3d)

    for boxes_corner in boxes_corners:
        t_rects = np.transpose(boxes_corner)
        draw_box(ax, t_rects, axes=axes, color=(1,0,0))


# In[7]:


def draw_point_cloud_color(ax, title, points, colors, axes=[0, 1, 2], xlim3d=None, ylim3d=None, zlim3d=None):
    """
    Convenient method for drawing various point cloud projections as a part of frame statistics.
    """
    ax.scatter(*np.transpose(points[:, axes]), s=point_size, c=colors, cmap='gray')
    ax.set_title(title)
    ax.set_xlabel('{} axis'.format(axes_str[axes[0]]))
    ax.set_ylabel('{} axis'.format(axes_str[axes[1]]))
    if len(axes) > 2:
        ax.set_xlim3d(*axes_limits[axes[0]])
        ax.set_ylim3d(*axes_limits[axes[1]])
        ax.set_zlim3d(*axes_limits[axes[2]])
        ax.set_zlabel('{} axis'.format(axes_str[axes[2]]))
    else:
        ax.set_xlim(*axes_limits[axes[0]])
        ax.set_ylim(*axes_limits[axes[1]])
    # User specified limits
    if xlim3d!=None:
        ax.set_xlim3d(xlim3d)
    if ylim3d!=None:
        ax.set_ylim3d(ylim3d)
    if zlim3d!=None:
        ax.set_zlim3d(zlim3d)


# In[8]:


def network_inference_by_path(kitti_info, v_path, sampling):
    print(v_path)
    points = np.fromfile(v_path, dtype=np.float32, count=-1).reshape([-1, num_features])
    points = points[1::sampling] # sampling

    inputs = inference_ctx.get_inference_input_dict(kitti_info, points)
    with inference_ctx.ctx():
        det_annos = inference_ctx.inference(inputs)

    boxes_corners, scores, boxes_lidar = kitti_anno_to_corners(kitti_info, det_annos[0])
    class_names = det_annos[0]['name']

    # f2 = plt.figure(figsize=(15, 8))
    # ax2 = f2.add_subplot(111, projection='3d')                    
    # draw_point_cloud(ax2, 'Velodyne scan', points, boxes_corners, xlim3d=(-10,30))
    # plt.show()
    
    return points, boxes_corners, class_names


# In[9]:


def bounding_box(points, min_x=-np.inf, max_x=np.inf, min_y=-np.inf,
                        max_y=np.inf, min_z=-np.inf, max_z=np.inf):
    """ Compute a bounding_box filter on the given points

    Parameters
    ----------                        
    points: (n,3) array
        The array containing all the points's coordinates. Expected format:
            array([
                [x1,y1,z1],
                ...,
                [xn,yn,zn]])

    min_i, max_i: float
        The bounding box limits for each coordinate. If some limits are missing,
        the default values are -infinite for the min_i and infinite for the max_i.

    Returns
    -------
    bb_filter : boolean array
        The boolean mask indicating wherever a point should be keeped or not.
        The size of the boolean mask will be the same as the number of given points.

    """

    bound_x = np.logical_and(points[:, 0] > min_x, points[:, 0] < max_x)
    bound_y = np.logical_and(points[:, 1] > min_y, points[:, 1] < max_y)
    bound_z = np.logical_and(points[:, 2] > min_z, points[:, 2] < max_z)

    bb_filter = np.logical_and(bound_x, bound_y, bound_z)

    return bb_filter


# In[10]:


info_path = '/datasets/kitti_infos_train.pkl'
config_path = Path('/workspace/second.pytorch/second/configs/all.fhd.config')
ckpt_path = Path('/workspace/second.pytorch/second/pretrained_models_v1.5/multiclass_model/voxelnet-74240.tckpt')
# voxelnet-296960.tckpt # 사람\n",
# voxelnet-74240.tckpt # multi"


# - voxelnet-296960.tckpt # 사람
# - voxelnet-74240.tckpt # multi
# 
# 

# In[11]:


car_lidar_file_paths = sorted(glob('/datasets/testing/velodyne/*.bin'))
ped_lidar_file_paths = sorted(glob('/datasets/testing/velodyne/*.bin'))
res_lidar_file_paths = sorted(glob('/datasets/testing/velodyne/*.bin'))
lidar_file_paths = car_lidar_file_paths


# In[12]:


import os
os.environ["CUDA_VISIBLE_DEVICES"]="1"
publish_topic_name = '/inference_results'
lidar_frame_step = 1
point_sampling_step = 1


# In[13]:


# Network model load
with open(info_path, 'rb') as f:
    kitti_infos = pickle.load(f)
inference_ctx = TorchInferenceContext()
inference_ctx.build(config_path)
inference_ctx.restore(ckpt_path)


# In[14]:


idx=0
points, boxes_corners, class_names = network_inference_by_path(kitti_infos[0], lidar_file_paths[idx], point_sampling_step)
idx = idx+lidar_frame_step


# In[15]:


labels = np.zeros(points.shape[0])
for boxes_corner, class_name in zip(boxes_corners, class_names):
    x_max = np.max(boxes_corner[:,0])
    x_min = np.min(boxes_corner[:,0])
    y_max = np.max(boxes_corner[:,1])
    y_min = np.min(boxes_corner[:,1])
    z_max = np.max(boxes_corner[:,2])
    z_min = np.min(boxes_corner[:,2])

    if class_name == 'Pedestrian':
        labels = labels + 1*bounding_box(points, x_min, x_max, y_min, y_max, z_min, z_max)
    elif class_name == 'Cyclist':
        labels = labels + 2*bounding_box(points, x_min, x_max, y_min, y_max, z_min, z_max)
    elif class_name == 'Car':
        labels = labels + 3*bounding_box(points, x_min, x_max, y_min, y_max, z_min, z_max)
    elif class_name == 'Van':
        labels = labels + 4*bounding_box(points, x_min, x_max, y_min, y_max, z_min, z_max)


for i, label in enumerate(labels):
    points[i,3] = label*100


# In[ ]:


print(points)


# In[ ]:



