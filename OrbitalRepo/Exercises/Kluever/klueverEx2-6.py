# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Orbital Mechanics & Dynamics Software Collection
# Author:   Steven Anderson
# Created:  MAR 2022
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
# (a) Determine eccentricity of elliptical orbit and coast time
# between burnout and thrust maneuver at perigee.
radPer = const.rE + altPer
radApo = const.rE + altApo
ecc = ( radApo - radPer )/( radPer + radApo )
print('Eccentricity: {:.3f} []'.format(ecc))
