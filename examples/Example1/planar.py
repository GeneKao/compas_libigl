import numpy
import compas

from compas.datastructures import Mesh
from compas.datastructures import mesh_flatness
from compas.plotters import MeshPlotter
from compas.utilities import i_to_rgb

import planarize

mesh1 = Mesh.from_json(compas.get('tubemesh.json'))

vertices, faces = mesh1.to_vertices_and_faces()

V1 = numpy.array(vertices, dtype=numpy.float64)
F1 = numpy.array(faces, dtype=numpy.int32)
V2 = planarize.planarize(V1, F1)

mesh2 = Mesh.from_vertices_and_faces(V2, faces)

dev2 = mesh_flatness(mesh2, maxdev=0.02)

plotter = MeshPlotter(mesh2)
plotter.draw_faces(facecolor={fkey: i_to_rgb(dev2[fkey]) for fkey in mesh2.faces()})
plotter.show()