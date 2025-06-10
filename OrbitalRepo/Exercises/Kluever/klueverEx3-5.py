# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Orbital Mechanics & Dynamics Software Collection
# Author:   Steven Anderson
# Created:  MAY 2025
# Brief:    Example 3.5
#           (Determine satellite state vector) New Boston AFS
#           launch (NBAFS) -- This time using an ellipsoidal
#           Earth.
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

import constantsKluever as const
from commonFunctions import calcRotationMatrix_Sez2Eci
from math import sqrt, sin, cos, radians, pi
import numpy as np

#####
## Givens:
hNBAFS = 0.39           # [km] altitude of ground station above ref ellipsoid
latNBAFS = 42.9         # [deg] latitude of ground station
lonNBAFS = 240.7        # [deg (from inertial I axis)] @ t0

losRange = 668.3        # [km] @ t0
losEl = 62.5            # [deg] @ t0
losAz = 135.4           # [deg] @ t0
losRangeRate = 2.39     # [km/s] @ t0
losElRate = -0.65       # [deg/s] @ t0
losAzRate = -0.38       # [deg/s] @ t0

#####
## Functions
def calcSatPos_relStation_Sez(azimuth,elevation,range):
    # Given an azimuth, elevation, and range, return a satellite position relative to station in SEZ frame
    # Inputs:
    #     azimuth (deg)
    #     elevation (deg)
    #     range (km)     
    s = range * -cos(radians(elevation))*cos(radians(azimuth))
    e = range * cos(radians(elevation))*sin(radians(azimuth))
    z = range * sin(radians(elevation))
    return s,e,z

def calcStationRelVelocity_Sez(azimuth,elevation,range,azRate,elRate,rangeRate):
    # Given an azimuth, elevation, range, and their rates, 
    # return a satellite's station-relative velocity in SEZ frame.
    # Inputs:
    #     azimuth (deg)
    #     elevation (deg)
    #     range (km)     
    #     azimuth rate (deg/s)
    #     elevation rate (deg/s)
    #     range rate (km/s)
     velSatS = -rangeRate * cos(radians(elevation)) * cos(radians(azimuth)) + \
               (range * elRate * sin(radians(elevation)) * cos(radians(azimuth))) * (pi/180) + \
               (range*azRate * cos(radians(elevation)) * sin(radians(azimuth))) * (pi/180)
     velSatE = rangeRate * cos(radians(elevation)) * sin(radians(azimuth)) - \
               (range * elRate * sin(radians(elevation)) * sin(radians(azimuth))) * (pi/180) + \
               (range * azRate * cos(radians(elevation)) * cos(radians(azimuth))) * (pi/180)
     velSatZ = rangeRate * sin(radians(elevation)) + range * elRate * cos(radians(elevation)) * (pi/180) 
     return velSatS,velSatE,velSatZ
#####


## Calculate satellite's state vector at epoch t0 in ECI
# (I) Find Inertial Satellite Position Vector

# determine inertial position of NBAFS in ECI (using ellipsoidal Earth)
N = const.aE / sqrt(1 - const.eE**2 * sin(radians(latNBAFS))**2) # prime vertical radius of curvature
coeffij = N + hNBAFS
coeffk = N * (1 - const.eE**2) + hNBAFS
posSiteECI = np.array([coeffij * cos(radians(latNBAFS)) * cos(radians(lonNBAFS)), \
                       coeffij * cos(radians(latNBAFS)) * sin(radians(lonNBAFS)), \
                       coeffk * sin(radians(latNBAFS))])
print("Site Position (ECI): ",posSiteECI)

# calculate satellite position relative to NBAFS (in SEZ)
posSatSEZ_relStation = calcSatPos_relStation_Sez(losAz,losEl,losRange)

print("Satellite Pos Relative to Site (SEZ): ",posSatSEZ_relStation)

# transform satellite position relative to NBAFS from SEZ to ECI
Tsez2eci = calcRotationMatrix_Sez2Eci(latNBAFS,lonNBAFS)
posSatECI_relStation = np.matmul(Tsez2eci,posSatSEZ_relStation)

print("Satellite Pos Relative to Site (ECI):",posSatECI_relStation)

# satellite position relative to inertial frame (ECI) combines site & sat positions
posSatECI = posSiteECI + posSatECI_relStation
print("Satellite Pos Relative to Inertial (ECI): ", posSatECI)


# (II) Find Inertial Velocity Vector
# calculate velocity components of Sat velocity relative to station (SEZ)

velSatSEZ_relStation = calcStationRelVelocity_Sez(losAz,losEl,losRange,losAzRate,losElRate,losRangeRate)
print("Satellite Vel Relative to Site (SEZ): ", velSatSEZ_relStation)

# transform velocity vector from SEZ to ECI
velSatECI_relStation = np.matmul(Tsez2eci,velSatSEZ_relStation)
print("Satellite Vel Relative to Site (ECI): ", velSatECI_relStation)

# satellite velocity relative to inertial frame (ECI) combines the station-relative velocity and the
# Earth angular velocity
velSatECI = velSatECI_relStation + np.cross([0,0,const.omegaE],posSatECI)



# results
print("////Satellite State Vector////")
print("ECI Pos: ", posSatECI)
print("ECI Velocity: ", velSatECI)
print("//////////////////////////////")

