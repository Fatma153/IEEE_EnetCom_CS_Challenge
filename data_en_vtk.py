# Dans ce code on a comme input une image (.png) et on l'a transformé a un tableau vtk
# On a passé par un tableau numpy
#***********************************************************************************************************

from PIL import Image , ImageEnhance
from numpy import *
import vtk
from pyvista import *
from vtk.util import numpy_support
from scipy.io import *



mat = loadmat('/home/lamis_/Downloads/Cs_challenge/Sph392.mat')
radial = loadmat('/home/lamis_/Downloads/Cs_challenge/prem3L_noocean.mat')


print('radial = ', radial)
global_=np.array(radial['__globals__'])
VTK_data_global = numpy_support.numpy_to_vtk(num_array=global_.ravel(), deep=True)
print('global_ = ', global_)
MI = np.array(radial['MI'])
VTK_data_MI= numpy_support.numpy_to_vtk(num_array=MI.ravel(), deep=True)
print('MI  = ', MI)
#print(MI)
radius =np.array(radial['RD'])
VTK_data_radius = numpy_support.numpy_to_vtk(num_array=radius.ravel(), deep=True)
print('radius = ', radius)
n_layers = np.array(radial['nlayer'])
VTK_data_n_layers = numpy_support.numpy_to_vtk(num_array=n_layers.ravel(), deep=True)
print('n_layers = ', n_layers)
#print(mat)
t=np.array(mat['t'])
VTK_data_t = numpy_support.numpy_to_vtk(num_array=t.ravel(), deep=True)

print('t = ', t)
p= np.array(mat['p'])
VTK_data_p = numpy_support.numpy_to_vtk(num_array=p.ravel(), deep=True)

print('p = ', p)
suf_d =np.array(mat['surf_d'])
VTK_data_suf_d = numpy_support.numpy_to_vtk(num_array=suf_d.ravel(), deep=True)

print('suf_d = ',suf_d.shape)
work_space =np.array (mat['__function_workspace__'])
#print('radial = ', radial)
n_layers_= n_layers[0][0]
VTK_data_n_layers_ = numpy_support.numpy_to_vtk(num_array=n_layers_.ravel(), deep=True)
print('n_layers_= ', n_layers_.shape)


