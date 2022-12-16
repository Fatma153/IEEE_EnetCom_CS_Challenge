from pyvista import *
plotter_1 = Plotter()
#__Model 1 __

plotter = Plotter()
actor = Actor()
datamapper = DataSetMapper()
plane = Plane(center=(0,0,0),direction=(0,0,1))
pod_1 = read('https://github.com/Fatma153/IEEE_EnetCom_CS_Challenge/releases/download/Planetary_Models/RTMDWAK_3L_1M.1_pod_1_model.vtk')

plotter.add_mesh(pod_1 )
datamapper.SetInputData(pod_1)
actor.mapper= datamapper
plotter.add_actor(actor)

true_G =read('https://github.com/Fatma153/IEEE_EnetCom_CS_Challenge/releases/download/Planetary_Models/RTMDWAK_3L_1M.1_pod_1_trueG.vtk')

plotter.add_mesh(true_G )
datamapper.SetInputData(true_G)
actor.mapper= datamapper
plotter.add_actor(actor)

gravity =read('https://github.com/Fatma153/IEEE_EnetCom_CS_Challenge/releases/download/Planetary_Models/RTMDWAK_3L_1M.1_pod_1_gravity.vtk')

plotter.add_mesh(gravity)
datamapper.SetInputData(gravity)
actor.mapper= datamapper
plotter.add_actor(actor)

rot = read('https://github.com/Fatma153/IEEE_EnetCom_CS_Challenge/releases/download/Planetary_Models/RTMDWAK_3L_1M.1_pod_1_Rotation.vtk')

plotter.add_mesh(rot)
datamapper.SetInputData(rot)
actor.mapper= datamapper
plotter.add_actor(actor)
line = plotter.add_axes()
plotter.add_camera_orientation_widget()


plotter.show()


































