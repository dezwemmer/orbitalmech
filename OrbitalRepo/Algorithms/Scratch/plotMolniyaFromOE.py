# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Orbital Mechanics & Dynamics Software Collection
# Author:   Steven Anderson
# Created:  JUL 2022
# Brief:    Given classical orbital elements for Molniya orbit. 
#           Determine state vector in ECI from OE.
#           (OE > ECI coordinates) and plot.  Based on 
#           Kluever 3.2
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#####
# Givens (Molniya orbit):
semiMajAxis = 26564     # [km]
ecc = 0.7411            # [n/a]
incl = 63.4             # [deg]
LascNode = 200          # [deg]
argPer = -90            # [deg]
trueAnom = 30           # [deg]
mu = 3.986e5            # gravitational constant [km^3/s^2]
rE = 6378               # Radius of Earth [km]


def calcMag(yourVector):
    mag = math.sqrt(yourVector[0]**2 + yourVector[1]**2 + yourVector[2]**2)
    return mag

def rotMatrixPQW_ECI(inclination,lonAscNode,argPeriapsis):
    cOmega = math.cos(math.radians(lonAscNode))
    comega = math.cos(math.radians(argPeriapsis))
    cIncl = math.cos(math.radians(inclination))
    sOmega = math.sin(math.radians(lonAscNode))
    somega = math.sin(math.radians(argPeriapsis))
    sIncl = math.sin(math.radians(inclination))

    Rtilde = np.array([[(cOmega*comega-sOmega*somega*cIncl), (-cOmega*somega-sOmega*comega*cIncl), (sOmega*sIncl)],
                [(sOmega*comega+cOmega*somega*cIncl), (-sOmega*somega+cOmega*comega*cIncl), (-cOmega*sIncl)],
                [(somega*sIncl), (comega*sIncl), (cIncl)]])
    return Rtilde

#####
# (a) Determine the satellite's state vector at this epoch in ECI
param = semiMajAxis*( 1 - ecc**2 )
angMom = math.sqrt( param*mu )

# calculate the orbital radius at true anomaly (trajectory eqn)
rOrb = param / ( 1 + ecc*math.cos(math.radians(trueAnom)) ) 

# find position vector in perifocal (PQW) frame
rPQW = np.array([rOrb*math.cos(math.radians(trueAnom)), rOrb*math.sin(math.radians(trueAnom)), 0 ])

# calculate velocity vector in perifocal (PQW) frame
vPQW = np.array([ (-mu/angMom)*math.sin(math.radians(trueAnom)), (mu/angMom)*(ecc + math.cos(math.radians(trueAnom))), 0 ])


# calculate the overall rotation matrix from PQW to IJK/ECI frame
Rtilde = np.ndarray.round(rotMatrixPQW_ECI(incl,LascNode,argPer),4,out=None)

# calculate the state vectors rECI & vECI from rotation matrix
rECI = np.matmul(Rtilde,rPQW)
vECI = np.matmul(Rtilde,vPQW)


# draw sphere
r = rE
u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:50j]
x = r*np.cos(u)*np.sin(v)
y = r*np.sin(u)*np.sin(v)
z = r*np.cos(v)

# plot as surface (alpha controls opacity)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z, color="b", alpha=0.6)
#point = np.array(r*[1,1,1])
print (rPQW)
ax.scatter(rPQW[0],rPQW[1],rPQW[2],'black')

plt.show()