import os
import logging

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

import numpy as np
import open3d as o3d
import h5py

__all__=[
    "logger"
    "load_light_gripper",
    "load_suction",
    "load_light_suction",
    "load_gripper",
    "get_grasps",
    "get_suctions"
]

def load_gripper():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    transformGripper = np.identity(4)
    transformGripper[2,3] = 0.045
    #load grippers model
    path_gripper = os.path.join(dir_path, os.pardir, "Models/GraspModel80mm.stl")
    o3d_gripper = o3d.io.read_triangle_mesh(path_gripper)
    o3d_gripper.scale(0.001, (0,0,0))
    o3d_gripper.compute_vertex_normals()
    o3d_gripper = o3d_gripper.transform(transformGripper)
    return o3d_gripper


def load_light_gripper():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    transformGripper = np.identity(4)
    transformGripper[2,3] = 0.045
    #load grippers model
    path_gripper = os.path.join(dir_path, os.pardir, "Models/GraspModelLight80mm.stl")
    o3d_gripper = o3d.io.read_triangle_mesh(path_gripper)
    o3d_gripper.scale(0.001, (0,0,0))
    o3d_gripper.compute_vertex_normals()
    o3d_gripper = o3d_gripper.transform(transformGripper)
    return o3d_gripper


def load_suction():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    #load suction model
    path_vacuum = os.path.join(dir_path, os.pardir, "Models/SuctionModel20mm.stl")
    o3d_vacuum = o3d.io.read_triangle_mesh(path_vacuum)
    o3d_vacuum.scale(0.001, (0,0,0))
    o3d_vacuum.compute_vertex_normals()
    return o3d_vacuum


def load_light_suction():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    #load suction model
    path_vacuum = os.path.join(dir_path, os.pardir, "Models/SuctionModelLight20mm.stl")
    o3d_vacuum = o3d.io.read_triangle_mesh(path_vacuum)
    o3d_vacuum.scale(0.001, (0,0,0))
    o3d_vacuum.compute_vertex_normals()
    return o3d_vacuum


def get_suctions(name_file):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(dir_path, os.pardir, "Dataset-suction-cup", name_file, name_file +".hdf5")

    suctions = None
    center = None

    #read
    with h5py.File(path, "r") as f:
        suctions = np.copy(f['grasp'])
        center = np.copy(f['center'])
    
    return suctions, center


def get_grasps(name_file):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(dir_path, os.pardir, "Dataset-parallel-jaws", name_file, name_file +".hdf5")

    grasps = None
    center = None
    #read
    with h5py.File(path, "r") as f:
        grasps = np.copy(f['grasp'])
        center = np.copy(f['center'])
    
    return grasps, center