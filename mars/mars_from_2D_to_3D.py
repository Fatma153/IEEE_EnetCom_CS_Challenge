# Dans ce code on a comme input une image (.jpg) et on l'a transformé a un tableau vtk
# On a passé par un tableau numpy
# Permet d'afficher une planete normalement

#***********************************************************************************************************

from PIL import Image
from numpy import *
import vtk
import pyvista as pv
from vtk.util import numpy_support



# on a une data sous forme d' tableau numpy

# Maintenant On convertit numpy array  to a vtk file

#
import vtk
# Create a render window
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
renWin.SetSize(480,480)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# Generate an sphere polydata
sphere = vtk.vtkSphereSource()
sphere.SetThetaResolution(12)
sphere.SetPhiResolution(12)

# Read the image data from a file
reader = vtk.vtkJPEGReader()
reader.SetFileName('/home/lamis_/Downloads/Cs_challenge/mars/marscyl1l (copy).jpg')

# Create texture object
texture = vtk.vtkTexture()
if vtk.VTK_MAJOR_VERSION <= 5:
    texture.SetInput(reader.GetOutput())
else:
    texture.SetInputConnection(reader.GetOutputPort())

# Map texture coordinates
#sphere =Sphere(radius=6731 , center = (0,0,0), start_theta=0, end_theta= 270, start_phi=0, end_phi=270)
map_to_sphere = vtk.vtkTextureMapToSphere()
if vtk.VTK_MAJOR_VERSION <= 5:
    map_to_sphere.SetInput(sphere.GetOutput())
else:
    map_to_sphere.SetInputConnection(sphere.GetOutputPort())
map_to_sphere.PreventSeamOn()

# Create mapper and set the mapped texture as input
mapper = vtk.vtkPolyDataMapper()
if vtk.VTK_MAJOR_VERSION <= 5:
    mapper.SetInput(map_to_sphere.GetOutput())
else:
    mapper.SetInputConnection(map_to_sphere.GetOutputPort())

# Create actor and set the mapper and the texture
actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.SetTexture(texture)

ren.AddActor(actor)

iren.Initialize()
renWin.Render()
iren.Start()




import math
from pyvista import *


DataSet.active_t_coords = Sphere(radius=6371 )



#texture = examples.planets.download_mars_surface(texture=True)
#'/home/lamis_/Downlds/Cs_challenge/mars/marscyl1l.jpg')
#fonction qui perrmet de lire la texture  : =>  read_texture()
pl =Plotter()
pl.add_mesh(sphere, opacity=0.01)
pl.add_composite(sphere)
pl.show()
