# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Orbital Mechanics & Dynamics Software Collection
# Author:   Steven Anderson
# Created:  MAR 2022
# Brief:    Example 2.2
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

import math
import constantsKluever as const

#####
# Givens:
semiMajorAxis = 7758 #km
param = 7634 #km

#####
# (a) determine orbital energy
totSpEnergy = -const.mu / (2 * semiMajorAxis)
print('Total Specific Energy: {:.3f} [km^2/s^2]'.format(totSpEnergy))

#####
# (b) angular momentum
angMom = math.sqrt(param * const.mu)
print('Angular Momentum: {:.3f} [km^2/s]'.format(angMom))

#####
# (c) whether or not the satellite will pass through Earth's appreciable
# atmosphere (altitude < 122km)
ecc = math.sqrt(1 - param / semiMajorAxis)
radPer = semiMajorAxis * (1 - ecc)
altPer = radPer - const.rE
if altPer < 122:
    print ("Satellite will pass through appreciable atmosphere")
    print ("Altitude at periapsis is {} km".format(altPer))
else:
    print ("Satellite will not pass through appreciable atmosphere")
    print ("Altitude at periapsis is {:.1f} km".format(altPer))



