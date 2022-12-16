#Afficher la repartition de rotation et de true_G a partir de la matrice en points


#****************************************************************************************************************************
from pyvista import *
plotter =Plotter()
true_G =read('https://github.com/Fatma153/IEEE_EnetCom_CS_Challenge/releases/download/Planetary_Models/RTMDWAK_3L_1M.1_pod_1_trueG.vtk')


print('true_G => ',true_G.points)
plotter.add_mesh(true_G.points, color='r' )
#axis_rotation(true_G.points, 90, axis='x', deg=True, inplace=True)
gravity =read('https://github.com/Fatma153/IEEE_EnetCom_CS_Challenge/releases/download/Planetary_Models/RTMDWAK_3L_1M.1_pod_1_gravity.vtk')

#plotter.add_mesh(gravity.points, color='r')

print('gravity = ', gravity)

rot = read('https://github.com/Fatma153/IEEE_EnetCom_CS_Challenge/releases/download/Planetary_Models/RTMDWAK_3L_1M.1_pod_1_Rotation.vtk')
plotter.add_mesh(rot.points, color='blue')
print('rotation =>' , rot)


sphere =Sphere(radius =0.975)
plotter.add_mesh(sphere)


axis_rotation(rot.points, 90, axis='x', deg=True, inplace=True )
plotter.add_axes()
plotter.add_camera_orientation_widget()


plotter.show()

