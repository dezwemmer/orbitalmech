# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Orbital Mechanics & Dynamics Software Collection
# Author:   Steven Anderson
# Created:  Feb 2022
# Brief:    Example 2.1
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

from inspect import Parameter
import math
import constantsKluever as const

# Givens:
satAlt = 2124 #km
velInert = 7.58 #km/s
FPA = 20 #deg

# (a) determine total specific energy
r = satAlt + const.rE
totSPEnergy = velInert**2 / 2 - const.mu / r
print('Total Specific Energy: {:.3f} [km^2/s^2]'.format(totSPEnergy))

# (b) angular momentum
h = r * velInert * math.cos(math.radians(FPA))
print('Angular Momentum: {:.3f} [km^2/s]'.format(h))

# (c) eccentricity and orbit type
SMA = - const.mu / (2 * totSPEnergy)
param = h**2 / const.mu
ecc = math.sqrt(1 - param / SMA)
print('Eccentricity: {:.3f}'.format(ecc))


