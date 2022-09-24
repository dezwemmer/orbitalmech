# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Orbital Mechanics & Dynamics Software Collection
# Author:   Steven Anderson
# Created:  AUG 2022
# Brief:    Example 3.4
#           (Determine satellite state vector) New Boston AFS
#           launch (NBAFS).
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

from os import O_NOINHERIT
import constantsKluever as const
import math
import numpy as np

#####
## Givens:
latNBAFS = 42.9        # [deg]
losRange = 668.3        # [km] @ t0
losEl = 62.5            # [deg] @ t0
losAz = 135.4           # [deg] @ t0
losRangeRate = 2.39     # [km/s] @ t0
losElRate = -0.65       # [deg/s] @ t0
losAzRate = -0.38       # [deg/s] @ t0
lonNBAFS = 240.7       # [deg (from inertial I axis)] @ t0

#####
## Calculate satellite's state vector at epoch t0 in ECI
# (I) Find Inertial Position Vector

# determine inertial position of NBAFS in ECI
posSiteECI = const.rE*np.array([math.cos(math.radians(latNBAFS))*math.cos(math.radians(lonNBAFS)), \
            math.cos(math.radians(latNBAFS))*math.sin(math.radians(lonNBAFS)), \
            math.sin(math.radians(latNBAFS))])
print("Site Position (ECI): ",posSiteECI)

# calculate satellite position relative to NBAFS (in SEZ)
posSatSEZ = losRange * np.array([-math.cos(math.radians(losEl))*math.cos(math.radians(losAz)), \
            math.cos(math.radians(losEl))*math.sin(math.radians(losAz)), \
            math.sin(math.radians(losEl))])
print("Satellite Pos (SEZ): ",posSatSEZ)

# convert satellite position (relative to station) in SEZ to ECI using D matrix
D = np.array([[math.sin(math.radians(latNBAFS))*math.cos(math.radians(lonNBAFS)), -math.sin(math.radians(lonNBAFS)), math.cos(math.radians(latNBAFS))*math.cos(math.radians(lonNBAFS))],
     [math.sin(math.radians(latNBAFS))*math.sin(math.radians(lonNBAFS)), math.cos(math.radians(lonNBAFS)), math.cos(math.radians(latNBAFS))*math.cos(math.radians(lonNBAFS))],
     [-math.cos(math.radians(latNBAFS)), 0, math.sin(math.radians(latNBAFS))]])
posSatECI_site = np.matmul(D,posSatSEZ)
print("Satellite Pos rel2Site (ECI): ",posSatECI_site)

# (a) satellite position relative to ECI frame combines site & sat positions
posSatECI = posSatECI_site + posSiteECI
print("Satellite Pos rel2Inertial (ECI): ", posSatECI)

# (II) Find Inertial Velocity Vector

# calculate velocity components of Sat velocity relative to station (SEZ)
velSatS = -losRangeRate*math.cos(math.radians(losEl))*math.cos(math.radians(losAz)) + \
            losRange*losElRate*math.sin(math.radians(losEl))*math.cos(math.radians(losAz)) + \
            losRange*losAzRate*math.cos(math.radians(losEl))*math.sin(math.radians(losAz))
velSatE = losRangeRate*math.cos(math.radians(losEl))*math.sin(math.radians(losAz)) - \
            losRange*losElRate*math.sin(math.radians(losEl))*math.sin(math.radians(losAz)) + \
            losRange*losAzRate*math.cos(math.radians(losEl))*math.cos(math.radians(losAz))
velSatZ = losRangeRate*math.sin(math.radians(losEl)) + losRange*losElRate*math.cos(math.radians(losEl))
print(math.cos(math.radians(losAz)))
print(-losRangeRate*math.cos(math.radians(losEl))*math.cos(math.radians(losAz)))

# calculate satellite's velocity relative to station (SEZ)
#velSatSEZ = 


