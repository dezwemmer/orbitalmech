# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Orbital Mechanics & Dynamics Software Collection
# Author:   Steven Anderson
# Created:  MAR 2022
# Brief:    Example 2.5
#           US comm satellite destined for geostationary
#           equatorial orbit.
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

import math
import constantsKluever as const

#####
# Givens:
altPer_GTO = 200 #km 
altApo_GTO = 35786 #km
# circular/LEO > GTO > GEO

#####
# (a) calculate perigee velocity on GTO & LEO circular velocity
radPer_GTO = const.rE + altPer_GTO
radApo_GTO = const.rE + altApo_GTO
radCirc_LEO = radPer_GTO
semiMajorAxis_GTO = ( radPer_GTO + radApo_GTO ) / 2
totSpecEnergy_GTO = -const.mu / ( 2 * semiMajorAxis_GTO )
velPer_GTO = math.sqrt( 2 * ( totSpecEnergy_GTO + const.mu / radPer_GTO ) )
velCirc_LEO = math.sqrt( const.mu / radCirc_LEO )
print('GTO Perigee Velocity: {:.3f} [km/s]'.format(velPer_GTO))
print('LEO Circular Velocity: {:.3f} [km/s]'.format(velCirc_LEO))

#####
# (b) calculate apogee velocity on GTO & GEO circular velocity
velApo_GTO = math.sqrt( 2 * ( totSpecEnergy_GTO + const.mu / radApo_GTO ) )
radCirc_GEO = radApo_GTO
velCirc_GEO = math.sqrt( const.mu / radCirc_GEO )
print('GTO Apogee Velocity: {:.3f} [km/s]'.format(velApo_GTO))
print('GEO Circular Velocity: {:.3f} [km/s]'.format(velCirc_GEO))

#####
# (c) calculate period of GTO
period_GTO = (( 2 * math.pi ) / ( math.sqrt(const.mu) )) * semiMajorAxis_GTO**(3/2)  #seconds
print('GTO Period: {:.2f} [h]'.format(period_GTO/60/60))
