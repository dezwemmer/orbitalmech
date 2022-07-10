# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Orbital Mechanics & Dynamics Software Collection
# Author:   Steven Anderson
# Created:  JUL 2022
# Brief:    This script is to plot a satellite's orbit 
#           
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#fig = plt.figure()
#ax = fig.gca(projection='3d')

# draw sphere
u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:50j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)

# plot in wireframe
#ax.plot_wireframe(x, y, z, color="r")

# plot as surface (alpha controls opacity)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z, color="b", alpha=0.6)
point = np.array([1,1,1])
ax.scatter(point[0],point[1],point[2],'black')

plt.show()
