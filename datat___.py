#Afficher la repartition de rotation et de true_G a partir de la matrice en points


#****************************************************************************************************************************
from pyvista import *
plotter =Plotter()
true_G =read('/home/lamis_/Downloads/ReproducibilityChallenge/input/M1/RTMDWAK_3L_1M.1_pod_1_trueG.vtk')


print('true_G => ',true_G.points)
plotter.add_mesh(true_G.points, color='r' )
#axis_rotation(true_G.points, 90, axis='x', deg=True, inplace=True)
gravity =read('/home/lamis_/Downloads/ReproducibilityChallenge/input/M1/RTMDWAK_3L_1M.1_pod_1_gravity.vtk')

#plotter.add_mesh(gravity.points, color='r')

print('gravity = ', gravity)

rot = read('/home/lamis_/Downloads/ReproducibilityChallenge/input/M1/RTMDWAK_3L_1M.1_pod_1_Rotation.vtk')
plotter.add_mesh(rot.points, color='blue')
print('rotation =>' , rot)


sphere =Sphere(radius =0.975)
plotter.add_mesh(sphere)


axis_rotation(rot.points, 90, axis='x', deg=True, inplace=True )
plotter.add_axes()
plotter.add_camera_orientation_widget()
#true_G_=read('/home/lamis_/Downloads/ReproducibilityChallenge/input/M1/RTMDWAK_3L_1M.1_pod_1_trueG.vtk')

plotter.show()

