# Ce code permet d'afficher la comaraison entre mars et moon en matiere de couche interieur et en volume

#***********************************************************************************************************************
from pyvista import *
from pyvista.examples import *
from scipy.io import *

plotter = Plotter()




moon =planets.load_moon(radius=1700)

mars = planets.load_mars(radius=3700)

n_layers_= 3
layers=[0,1850,3733, 3690]
colors=['#E47E7B', '#3B271D', '#9C2E35']
for j in range(n_layers_):




    R1 = round(layers[j])
    R2 =round(layers[j+1]) #3480
    if (R1>1700):
        for i in range(R1,R2,10):
            sphere_i = Sphere(radius=i, start_theta=0 , end_theta=270, start_phi=0 , end_phi=180)
            plotter.add_mesh(sphere_i, color=colors[j], opacity=0.1)

plotter.add_mesh(moon)
plotter.add_mesh(mars , opacity=0.8)
plotter.add_camera_orientation_widget()
plotter.add_axes()









plotter.show()

