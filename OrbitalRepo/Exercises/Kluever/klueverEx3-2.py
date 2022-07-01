# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Orbital Mechanics & Dynamics Software Collection
# Author:   Steven Anderson
# Created:  JUN 2022
# Brief:    Example 3.2
#           Classical orbital elements for Molniya orbit. 
#           Determine state vector in ECI from OE.
#           (OE > ECI coordinates)
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

import constantsKluever as const
import math
import numpy as np


#####
# Givens:
semiMajAxis = 26554     # [km]
ecc = 0.7411            # [n/a]
incl = 63.4             # [deg]
LascNode = 200          # [deg]
argPer = -90            # [deg]
trueAnom = 30           # [deg]


def calcMag(yourVector):
    mag = math.sqrt(yourVector[0]**2 + yourVector[1]**2 + yourVector[2]**2)
    return mag

def print_classicalOE(a,e,i,LAN,AP,TA):
    print("----Classical Orbital Elements----")
    print('Semimajor Axis:      {:<.2f} [km]'.format(a))
    print('Eccentricity:        {:<.2f} []'.format(ecc))
    print('Inclination:         {:<.2f} [deg]'.format(i))
    print('Long Asc Node (LAN): {:<.2f} [deg]'.format(LAN))
    print('Arg of Periapsis:    {:<.2f} [deg]'.format(AP))
    print('True Anomaly:        {:<.2f} [deg]'.format(TA))


#####
# (a) Determine the classical orbital elements at this epoch
# from the state vector (r0,v0)
r0Mag = calcMag(r0)
v0Mag = calcMag(v0)
I = np.array([1, 0, 0])
J = np.array([0, 1, 0])
K = np.array([0, 0, 1])

totSpecEnergy = (v0Mag**2 / 2) - (const.mu / r0Mag)
semiMajAxis = -const.mu /(2*totSpecEnergy)

eccVec = (1/const.mu)*((v0Mag**2 - const.mu/r0Mag)*r0 - (np.dot(r0,v0))*v0)
ecc = calcMag(eccVec)

angMomVec = np.cross(r0,v0)
angMom = calcMag(angMomVec)
incl = math.degrees( math.acos(np.dot(K,angMomVec)/angMom) )

ascNodeVec = np.cross(K,angMomVec)

sinLAN = np.dot(J,ascNodeVec)/calcMag(ascNodeVec)
cosLAN = np.dot(I,ascNodeVec)/calcMag(ascNodeVec)
LAN = math.degrees(math.atan2(sinLAN,cosLAN))

cosArgPer = np.dot(ascNodeVec,eccVec)/(calcMag(ascNodeVec)*ecc)
if eccVec[2] < 0:
    argPer = 360 - math.degrees( math.acos(cosArgPer) )
else:
    argPer = math.degrees( math.acos(cosArgPer) )

cosTA= np.dot(eccVec,r0)/(ecc*r0Mag)
TAcheck = np.dot(r0,v0)
if TAcheck < 0:
    TA = 360 - math.degrees( math.acos(cosTA) )
else:
    TA = math.degrees( math.acos(cosTA) )

print_classicalOE(semiMajAxis,ecc,incl,LAN,argPer,TA)

#####
# (b) is this in a Molniya orbit?
# yes, based on a,e,i,and argPer