# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Orbital Mechanics & Dynamics Software Collection
# Author:   Steven Anderson
# Created:  Feb 2022
# Brief:    Example 2.1
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

import math
import constantsKluever as const

# Givens:
satAlt = 2124 #km
velInert = 7.58 #km/s
flightPathAngle = 20 #deg

# (a) determine total specific energy
rad = satAlt + const.rE
totSpEnergy = velInert**2 / 2 - const.mu / rad
print('Total Specific Energy: {:.3f} [km^2/s^2]'.format(totSpEnergy))

# (b) angular momentum
angMom = rad * velInert * math.cos(math.radians(flightPathAngle))
print('Angular Momentum: {:.3f} [km^2/s]'.format(angMom))

# (c) eccentricity and orbit type
semiMajorAxis = - const.mu / (2 * totSpEnergy)
param = angMom**2 / const.mu
ecc = math.sqrt(1 - param / semiMajorAxis)
print('Eccentricity: {:.3f}'.format(ecc))


