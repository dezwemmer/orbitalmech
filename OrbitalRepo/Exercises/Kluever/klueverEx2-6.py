# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Orbital Mechanics & Dynamics Software Collection
# Author:   Steven Anderson
# Created:  APR 2022
# Brief:    Example 2.6
#           Lunar Atmosphere and Dust Environment Explorer
#           (LADEE) launched into highly elliptic orbit.
#           Entered elliptical orbit & made one orbit. Fired
#           rocket @ perigee to incr orbital energy
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

import math
import constantsKluever as const

#####
# Givens:
altPer = 200 #km 
altApo = 278000 #km

#####
# (a1) Determine eccentricity of elliptical orbit
radPer = const.rE + altPer
radApo = const.rE + altApo
ecc = ( radApo - radPer )/( radPer + radApo )
print('Eccentricity: {:.3f} []'.format(ecc))

#####
# (a2) coast time between burnout and thrust maneuver at perigee.
semiMajorAxis = ( radPer + radApo )/2
Tperiod = ( 2*math.pi )/( math.sqrt(const.mu) )*( semiMajorAxis**(3/2) )
print('Period of 1 Orbit: {:.3f} [days]'.format(Tperiod/60/60/24))