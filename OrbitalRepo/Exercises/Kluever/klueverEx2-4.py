# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Orbital Mechanics & Dynamics Software Collection
# Author:   Steven Anderson
# Created:  MAR 2022
# Brief:    Example 2.4
#           Apollo CM tracked by Earth-based radar station
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

import math
import constantsKluever as const

#####
# Givens:
semiMajorAxis = 424587 #km
ecc = 0.9849

#####
# (a) flight path angle and radial velocity @ TA 330
trueAnomaly = math.radians(330) #radians
flightPathAngle = math.degrees(math.atan( (ecc*math.sin(trueAnomaly))/(1 + ecc * math.cos(trueAnomaly)) ))
param = semiMajorAxis*(1 - ecc**2)
angMom = math.sqrt( const.mu*param )
velRad = ( const.mu/angMom )*ecc*math.sin( trueAnomaly )
print("~At FPA 330 degrees~")
print('  Flight Path Angle: {:.1f} [degrees]'.format(flightPathAngle))
print('  Radial Velocity: {:.3f} [km/s]'.format(velRad))

#####
# (b) calculate velocity and flight path angle at the entry interface (EI) or 122 km altitude
totSpecEnergy = - const.mu / ( 2*semiMajorAxis)
radEI = const.rE + 122
velEI = math.sqrt( 2*( totSpecEnergy + ( const.mu/radEI ) ) )

# because CM is returning to Earth: FPA < 0 and 180<TA<360, so orbitalPosFlag is -1
# TO-DO: add a clean way to introduce a flag and correct TA/FPA per Tbl 2-2
orbitalPosFlag = -1
trueAnomalyEI = math.acos( (1/ecc)*( param/radEI - 1 ) ) * orbitalPosFlag
flightPathAngleEI = math.degrees(math.atan( (ecc*math.sin(trueAnomalyEI))/(1 + ecc * math.cos(trueAnomalyEI)) ))
print("~At Entry Interface (122km)~")
print('  Velocity: {:.1f} [km/s]'.format(velEI))
print('  Flight Path Angle: {:.3f} [degrees]'.format(flightPathAngleEI))