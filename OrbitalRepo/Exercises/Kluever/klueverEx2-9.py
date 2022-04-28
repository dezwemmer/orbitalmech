# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Orbital Mechanics & Dynamics Software Collection
# Author:   Steven Anderson
# Created:  APR 2022
# Brief:    Example 2.9
#           MER-A spacecraft at burnout 
#           and in GEO
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

import math
import constantsKluever as const

#####
# Givens:
altSC = 225 #km
vSC = 11.4 #km/s
flightPathAngle = 5 #deg 

#####
# (a) Departure hyperbolic excess speed vInfP
radBurnout = const.rE + altSC
velBurnout = vSC
totSpecEnergy = ( velBurnout**2 / 2 ) - ( const.mu / radBurnout )
vInfP = math.sqrt( 2 * totSpecEnergy )
print('Departure hyperbolic excess speed: {:.3f} [km/s]'.format(vInfP))

#####
# (b) True anomaly of departure asymptote (thetaInfP)
angMom = radBurnout * velBurnout * math.cos(math.radians(flightPathAngle))
param = angMom**2 / const.mu
semiMajAxis = -const.mu / ( 2*totSpecEnergy )
ecc = math.sqrt( 1 - param / semiMajAxis )
thetaInfP = math.acos(-1 / ecc)
print('True Anomaly of Departure Asymptote: {:.2f} [deg]'.format(math.degrees(thetaInfP)))