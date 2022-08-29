# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Orbital Mechanics & Dynamics Software Collection
# Author:   Steven Anderson
# Created:  AUG 2022
# Brief:    Example 3.3
#           (Ground Tracks) Falcon 9 > ISS from Cape. Determine 
#           launch azimuth IOT put upper stage in orbit with 
#           correct incl and moving toward equator after 
#           insertion.
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

import constantsKluever as const
import math
import numpy as np

#####
# Givens:
latLaunch = 28.5           # [deg]
inclISS = 51.65            # [deg]


#####
# (a) Launched from Cape (given latitude) to ISS (given incl).
# Determine launch azimuth to place upper stage in right incl and
# moving towards the equator after orbital insertion.

# using Napier's rules for right spherical triangle
launchAz = math.asin(math.cos(math.radians(inclISS))/math.cos(math.radians(latLaunch)))
print("Launch Azimuth (for ascending): ",math.degrees(launchAz))
print("Launch Azimuth (for descending toward equator): ",90+math.degrees(launchAz))