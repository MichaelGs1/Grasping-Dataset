import os
import sys
import copy

import open3d as o3d
import numpy as np

from utils import load_suction, load_light_suction, get_suctions, logger

def main(file_name, number, light=False):
    suctions, center = get_suctions(file_name)

    # load mesh
    mesh = o3d.io.read_triangle_mesh(os.path.join(os.pardir, "EGAD", file_name + ".obj"))
    mesh.scale(0.001, (0,0,0))
    mesh.compute_vertex_normals()
    mesh = mesh.transform(center)

    # load gripper
    o3d_vacuum = load_light_suction() if light else load_suction()
    logger.info("Total grasps : {0}".format(suctions.shape[0]))

    # display
    list_geo = []
    np.random.shuffle(suctions)
    for i in range(suctions.shape[0]):
        suction = suctions[i][0:4,0:4]

        model = copy.copy(o3d_vacuum)
        model.paint_uniform_color([0,1,0])
        model.transform(suction)
        list_geo.append(model)

        # add to display until number 
        if (len(list_geo) >= int(number)):
            break

    origin = o3d.geometry.TriangleMesh.create_coordinate_frame(0.1)
    list_geo.append(mesh)
    list_geo.append(origin)
    o3d.visualization.draw_geometries(list_geo)


if __name__ == "__main__":
    if (len(sys.argv) != 3 and len(sys.argv) != 4):
        logger.error("Usage : python3 show_suctions.py file_name number_display light")
        exit()
    else:
        file_name = sys.argv[1]
        number = sys.argv[2]
        if (len(sys.argv) == 4 and sys.argv[3] == "light"):
            main(file_name, number, light=True)
        else:
            main(file_name, number)