# cette parcelle de code convient a tracer la couche exterieure de code

# url :https://github.com/ddelatte/CraterSegCNN/find/master
from pyvista import *

import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import numpy as np
from vtk import *
from vtk.util.numpy_support import vtk_to_numpy
from vtkmodules.vtkIOXML import vtkXMLUnstructuredGridReader

plotter_1 = Plotter()
#__Model 1 __
plotter = Plotter()


pod_1 = read('https://github.com/Fatma153/IEEE_EnetCom_CS_Challenge/releases/download/Planetary_Models/RTMDWAK_3L_1M.1_pod_1_model.vtk')
# ===> Vp de M1
plotter.add_mesh(pod_1 )

plotter.add_axes()
plotter.add_camera_orientation_widget()
plotter.show()






# afficher les sections de fromage (density && speed_wave) =>  matplotlib3D


#rendre les fichiers de numpy en .vtk  et puis les afficher => en pyvista



















