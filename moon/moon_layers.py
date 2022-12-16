# Ce code permet d'afficher en demi sphere les couches iterieurs de moon

#***********************************************************************************************************************
from pyvista import *
from pyvista.examples import *
from scipy.io import *

plotter = Plotter()




moon =planets.load_moon(radius=1700)

n_layers_= 4
layers=[0,400,700,1000, 1600,1700]
colors=['#FFD100', '#FFA300', '#BA0C30', '#AAAAAD']
for j in range(n_layers_):




    R1 = round(layers[j])
    R2 =round(layers[j+1]) #3480


    for i in range(R1,R2,10):

        sphere_i = Sphere(radius=i, start_theta=0 , end_theta=180, start_phi=0 , end_phi=180 )
        plotter.add_mesh(sphere_i, color=colors[j])

plotter.add_mesh(moon, opacity=0.7)
plotter.add_camera_orientation_widget()
plotter.add_axes()



plotter.show()

