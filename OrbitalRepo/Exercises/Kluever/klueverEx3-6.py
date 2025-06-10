# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Orbital Mechanics & Dynamics Software Collection
# Author:   Steven Anderson
# Created:  JUN 2025
# Brief:    Example 3.6
#           Compute satellite's state vector (p,v) based on
#           three LOS observations of ECI position vectors.
#           Determine if the satellite is in a Molniya orbit.
#           (Using Gibbs)
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

import constantsKluever as const
import commonFunctions as fxn
from math import sqrt, sin, cos, radians, pi
import numpy as np

#####
## Givens:
r1 = [-11052.902, -12938.738, 8505.244]     # [km] position vector 1 (ECI)
r2 = [-10378.257, -15955.205, 14212.351]    # [km] position vector 2 (ECI)
r3 = [-9336.222, -17747.079, 18337.068]     # [km] position vector 3 (ECI)


# (I) Calculate 3 auxiliary vectors D, N, S using the 3 ECI position vector measurements
cross23 = np.cross(r2,r3)
cross31 = np.cross(r3,r1)
cross12 = np.cross(r1,r2)
diff23 = fxn.vec3Mag(r2) - fxn.vec3Mag(r3)
diff31 = fxn.vec3Mag(r3) - fxn.vec3Mag(r1)
diff12 = fxn.vec3Mag(r1) - fxn.vec3Mag(r2)
D = cross23 + cross31 + cross12
N = fxn.vec3Mag(r1) * cross23 + fxn.vec3Mag(r2) * cross31 + fxn.vec3Mag(r3) * cross12
S = np.multiply(diff23,r1) + np.multiply(diff31,r2) + np.multiply(diff12,r3)

np.set_printoptions(suppress=True, formatter={'float_kind':'{:0.3f}'.format})
print("D: ", D)
print("N: ", N)
print("S: ", S)

# (II) Check if 3 vectors are coplanar (requirement for Gibbs)
if fxn.gibbsCoPlanarCheck(r1,r2,r3):
    print("Vectors are coplanar.")
else:
    print("Vector are not coplanar.")

# (III) Use Gibbs method to calculate satellite's inertial geocentric velocity vector
v2 = np.multiply( (1/fxn.vec3Mag(r2)) * sqrt(const.mu / fxn.vec3Mag(N) / fxn.vec3Mag(D)), np.cross(D,r2)) \
    + np.multiply(sqrt(const.mu / fxn.vec3Mag(N) / fxn.vec3Mag(D)), S)

print('Sat Inertial Geocentric Velocity Vector (v2): ',v2, 'km/s')

a,e,i,lan,AP,TA = fxn.calcOrbElmFromStateVec(r2,v2)

## NOTE: Since this is a long and skinny orbit (semi major axis and eccentricity) and the argument
#        of periapsis is 270deg, it's in the Southern hemisphere.