# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Orbital Mechanics & Dynamics Software Collection
# Author:   Steven Anderson
# Created:  APR 2022
# Brief:    Example 2.10
#           New Horizons approached Jupiter on hyperbolic 
#           trajectory & followed hyperbolic flyby trajectory
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

import math
import constantsKluever as const

#####
# Givens:
velInfM = 18.427 #km/s
closeApproach = 32.25 #radJupiter

#####
# (a) Calculate SC velocity at Per
radPer = closeApproach*const.rJupiter
totSpecEnergy = ( velInfM**2 ) / 2
velPer = math.sqrt( 2 * ( totSpecEnergy + const.muJupiter / radPer ) )

print ('Velocity at Periapsis: {:.3f} [km/s]'.format(velPer))

#####
# (b) Calculate turning angle (delta) from hyperB flyby
semiMajorAxis = -const.muJupiter / (2 * totSpecEnergy)
ecc = 1 - radPer / semiMajorAxis
turnAngle = math.degrees(2 * math.asin ( 1 / ecc ))
print('Turning Angle: {:.3f} [deg]'.format(turnAngle))
