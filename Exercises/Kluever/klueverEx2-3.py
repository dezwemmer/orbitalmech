# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Orbital Mechanics & Dynamics Software Collection
# Author:   Steven Anderson
# Created:  Mar 2022
# Brief:    Example 2.3
#           Chandra X-ray Observatory example
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

import math
import constantsKluever as const

# Givens:
altPer = 14308 #km
altApo = 134528 #km

# (a) calculate angular momentum of orbit
radPer = altPer + const.rE
radApo = altApo + const.rE
semiMajorAxis = (radPer + radApo) / 2
ecc = (radApo - radPer) / (radPer + radApo)
param = semiMajorAxis * (1 - ecc**2)
print (param)
angMom = math.sqrt(param * const.mu)
print('Angular Momentum: {:.3f} [km^2/s]'.format(angMom))

# (b) calculate total energy of orbit
totSpEnergy = -const.mu / (2 * semiMajorAxis)
print('Total Specific Energy: {:.3f} [km^2/s^2]'.format(totSpEnergy))

# (c) calculate radius/velocity/FPA @ true anomaly 120 degrees

# calculate radius using trajectory eqn
rad = param / (1 + ecc * math.cos(math.radians(120)))
# calculate velocity using energy eqn
vel = math.sqrt((totSpEnergy + (const.mu / rad)) * 2)
trueAnomaly = math.radians(120)
flightPathAngle = math.degrees(math.atan( (ecc*math.sin(trueAnomaly))/(1 + ecc * math.cos(trueAnomaly)) ))
print("~At FPA 120 degrees~")
print('  Radius: {:.3f} [km]'.format(rad))
print('  Velocity: {:.3f} [km/s]'.format(vel))
print('  Flight Path Angle: {:.1f} [degrees]'.format(flightPathAngle))

