# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Orbital Mechanics & Dynamics Software Collection
# Author:   Steven Anderson
# Created:  JUN 2025
# Brief:    Common Functions
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

import constantsKluever as const
from math import sqrt, sin, cos, acos, atan2, radians, degrees, pi
import numpy as np


def calcRotationMatrix_Sez2Eci(lat,lon):
    # Given a latitude and longitude, calculate the tranformation matrix from SEZ to ECI (IJK).
    D = np.array([[sin(radians(lat))*cos(radians(lon)), -sin(radians(lon)), cos(radians(lat))*cos(radians(lon))],
                         [sin(radians(lat))*sin(radians(lon)), cos(radians(lon)), cos(radians(lat))*sin(radians(lon))],
                         [-cos(radians(lat)), 0, sin(radians(lat))]])
    return D

def calcOrbElmFromStateVec(r,v):
    v = np.array(v)
    r = np.array(r)
    rMag = vec3Mag(r)
    vMag = vec3Mag(v)
    I = np.array([1, 0, 0])
    J = np.array([0, 1, 0])
    K = np.array([0, 0, 1])
    
    totSpecEnergy = (vMag**2 / 2) - (const.mu / rMag)
    semiMajAxis = -const.mu /(2*totSpecEnergy)

    eccVec = (1/const.mu)*((vMag**2 - const.mu/rMag)*r - (np.dot(r,v))*v)
    ecc = vec3Mag(eccVec)

    angMomVec = np.cross(r,v)
    angMom = vec3Mag(angMomVec)
    incl = degrees( acos(np.dot(K,angMomVec)/angMom) )

    ascNodeVec = np.cross(K,angMomVec)

    sinLAN = np.dot(J,ascNodeVec)/vec3Mag(ascNodeVec)
    cosLAN = np.dot(I,ascNodeVec)/vec3Mag(ascNodeVec)
    LAN = degrees(atan2(sinLAN,cosLAN))

    cosArgPer = np.dot(ascNodeVec,eccVec)/(vec3Mag(ascNodeVec)*ecc)
    if eccVec[2] < 0:
        argPer = 360 - degrees( acos(cosArgPer) )
    else:
        argPer = degrees( acos(cosArgPer) )

    cosTA= np.dot(eccVec,r)/(ecc*rMag)
    TAcheck = np.dot(r,v)
    if TAcheck < 0:
        TA = 360 - degrees( acos(cosTA) )
    else:
        TA = degrees( acos(cosTA) )

    print("----Classical Orbital Elements----")
    print('Semimajor Axis:      {:<.2f} [km]'.format(semiMajAxis))
    print('Eccentricity:        {:<.2f} []'.format(ecc))
    print('Inclination:         {:<.2f} [deg]'.format(incl))
    print('Long Asc Node (LAN): {:<.2f} [deg]'.format(LAN))
    print('Arg of Periapsis:    {:<.2f} [deg]'.format(argPer))
    print('True Anomaly:        {:<.2f} [deg]'.format(TA))

    return semiMajAxis,ecc,incl,LAN,argPer,TA





def gibbsCoPlanarCheck(r1,r2,r3):
    # Given 3 ECI position vectors, check that ep < cos(88deg).  Returns a boolean pass/fail.
    isPlanar = False
    ep = np.dot(r1, np.cross(r2, r3)) / np.multiply(vec3Mag(r1),np.linalg.norm(np.cross(r2,r3)))
    
    if isPlanar < cos(radians(88)):
        isPlanar = True
    return isPlanar

def vec3Mag(v):
    # Magnitude of 3D vector
    return sqrt(v[0]**2 + v[1]**2 + v[2]**2)

