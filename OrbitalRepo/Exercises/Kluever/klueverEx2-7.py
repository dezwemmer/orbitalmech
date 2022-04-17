# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Orbital Mechanics & Dynamics Software Collection
# Author:   Steven Anderson
# Created:  APR 2022
# Brief:    Example 2.7
#           Satellite in parabolic trajectory about Earth w
#           given perigee altitude
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import constantsKluever as const

#####
# Givens:
altPer = 500 #km 

#####
# Functions:
def computeRadVelfromTA(trueAnomalyDegrees, parameter):
    r = parameter / ( 1 + math.cos(math.radians(trueAnomalyDegrees)) )
    v = math.sqrt( 2*const.mu/r )
    return r,v 

#####
# (a) Compute sat velocity @ TAs (-60,0,90,150,179)
trueAnomalyList = [-60,0,90,150,179]
radPer = const.rE + altPer
param = 2*radPer

outList = []
for TA in trueAnomalyList:
    rad,vel = computeRadVelfromTA(TA,param)
    print("At TA {:.1f}:".format(TA))
    print(" Rad: {:.3f} [km], Vel: {:.3f} [km/s]".format(rad,vel))
    outList.append([TA,rad,vel])

# print results vertically
#print(np.vstack(outList))

#####
# (b) plot satellite velocity vs TA for -179<=TA<=179
# create more data points
TAList = []
velList = []
for i in range(-179,179,20):
    TAList.append(i)
    r,v = computeRadVelfromTA(i,param)
    velList.append(v)

fig,ax = plt.subplots()
ax.plot(TAList,velList)
ax.set_xlabel('True Anomaly [deg]')
ax.set_ylabel('Velocity on a parabola [km/s]')
plt.show()
