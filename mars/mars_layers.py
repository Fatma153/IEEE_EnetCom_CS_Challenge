# Ce code permet d'afficher mars et ses couches interieur en demi cercle

#***********************************************************************************************************************
from pyvista import *
from pyvista.examples import *
from scipy.io import *

plotter = Plotter()




mars =planets.load_mars(radius=3770)

n_layers_= 3
layers=[0,1850,3733, 3763]
colors=['#E47E7B', '#3B271D', '#9C2E35']
for j in range(n_layers_):

    R1 = round(layers[j])
    R2 =round(layers[j+1])


    for i in range(R1,R2,10):

        sphere_i = Sphere(radius=i, start_theta=0 , end_theta=180, start_phi=0 , end_phi=180 )
        plotter.add_mesh(sphere_i , color=colors[j])

plotter.add_mesh(mars, opacity=0.7)
plotter.add_camera_orientation_widget()
plotter.add_axes()




from pyvista import examples

#image_path = examples.planets.download_stars_sky_background(load=False)




plotter.show()

