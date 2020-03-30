from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
from .planarize import planarize_quads as _planarize_quads


def planarize_quads(vertices, faces, kmax=500, maxdev=0.005):
    V1 = np.array(vertices, dtype=np.float64)
    F1 = np.array(faces, dtype=np.int32)
    V2 = _planarize_quads(V1, F1, kmax, maxdev)
    return V2


# def planarize_mesh_proxy(meshdata, kmax=500, maxdev=0.005):
#     import numpy as np
#     from compas.datastructures import Mesh
#     mesh = Mesh.from_data(meshdata)
#     vertices, faces = mesh.to_vertices_and_faces()
#     V1 = np.array(vertices, dtype=np.float64)
#     F = np.array(faces, dtype=np.int32)
#     V2 = planarize_quads(V1, F, kmax, maxdev)
#     for index, (key, attr) in enumerate(mesh.vertices(True)):
#         attr['x'] = V2[index, 0]
#         attr['y'] = V2[index, 1]
#         attr['z'] = V2[index, 2]
#     return mesh.data


__all__ = [_ for _ in dir() if not _.startswith('_')]
