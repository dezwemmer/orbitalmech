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
import constantsKluever as const

#####
# Givens:
altPer = 500 #km 


#####
# Functions:
def computeVel_TA(trueAnomalyDegrees, parameter):
    r = parameter / ( 1 + math.cos(math.radians(trueAnomalyDegrees)) )
    v = math.sqrt( 2*const.mu/r )
    return r,v 

#####
# (a) Compute sat velocity @ TAs (-60,0,90,150,179)
trueAnomalyList = [-60,0,90,150,179]
radPer = const.rE + altPer
param = 2*radPer
trueAnomaly = -60

outList = []
for TA in trueAnomalyList:
    rad,vel = computeVel_TA(TA,param)
    print("At TA {:.1f}:".format(TA))
    print(" Rad: {:.3f} [km], Vel: {:.3f} [km/s]".format(rad,vel))
    outList.append([TA,rad,vel])
# print vertically
#print(np.vstack(outList))

