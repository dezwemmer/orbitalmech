# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Orbital Mechanics & Dynamics Software Collection
# Author:   Steven Anderson
# Created:  APR 2022
# Brief:    Example 2.8
#           Escape velocities for satellites in circular LEO
#           and in GEO
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

import math
import constantsKluever as const

#####
# Givens:
altSat = 300 #km 

#####
# (a) Escape velocity for sat in circular LEO
radSat = const.rE + altSat
vEscLEO = math.sqrt( 2 * const.mu / radSat )
print('Escape velocity LEO (300km): {:.3f} [km/s]'.format(vEscLEO))


#####
# (b) Escape velocity for sat in GEO
vEscGEO = math.sqrt( 2 * const.mu / const.radGEO )
print('Escape velocity GEO: {:.3f} [km/s]'.format(vEscGEO))