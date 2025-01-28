# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Orbital Mechanics & Dynamics Software Collection
# Author:   Steven Anderson
# Created:  MAY 2022
# Brief:    Based on Kluever Problem 2.24
#           Calculate characteristics of Earth orbit 
#           User Input: orbital radius, radial velocity, and
#           transverse velocity.
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

from cmath import pi
import sys
sys.path.append("..\Exercises\kluever")
import constantsKluever as const
import math

# Example points
# r = 8250ur km
# v = 1.2054ur + 7.0263ut km/s


def calcMag(yourVector):
    mag = math.sqrt(yourVector[0]**2 + yourVector[1]**2)
    return mag


# get inputs from the user
def getInput():
    print("--Enter the following information--")
    print("Orbital Radius [km]")
    rOrbr = float(input("Radial Component: "))
    rOrbt = float(input("Transverse Component: "))
    print("Orbital Velocity [km/s]")
    velRad = float(input("Radial Component: "))
    velTrans = float(input("Transverse Component: "))

    # store in vector format
    rOrb = [rOrbr,rOrbt]
    vel = [velRad,velTrans]
    
    print("Orbital Radius: ", rOrb)
    print("Velocity: ", vel)
    print("-----------------------------------")

    return rOrb,vel

def print_results(h,E,a,p,ecc,T,rp,ra,fpa,TA):
    print("----Results----")
    print('Angular Momentum:   {:<.2f} [km^2/s]'.format(h))
    print('Energy:             {:<.2f} [km^2/s^2]'.format(E))
    print('Semimajor Axis:     {:<.2f} [km]'.format(a))
    print('Parameter:          {:<.2f} [km]'.format(p))
    print('Eccentricity:       {:<.2f} []'.format(ecc))
    print('Period:             {:<.2f} [h]'.format(T))
    print('Radias (periapsis): {:<.2f} [km]'.format(rp))
    print('Radias (apoapsis):  {:<.2f} [km]'.format(ra))
    print('Flight Path Angle:  {:<.2f} [deg]'.format(fpa))
    print('True Anomaly:       {:<.2f} [deg]'.format(TA))


# compute outputs (input: vectors)
def compute(velocity,radOrbital):
    rOrbMag = calcMag(radOrbital)
    velMag = calcMag(velocity)
    angMom = radOrbital[0]*velocity[1]

    # calc total specific energy
    totSpecEnergy = (velMag**2 / 2) - const.mu / rOrbMag
    
    # calc semimajor axis
    semiMajAxis = -const.mu / (2 * totSpecEnergy)

    # calc parameter
    param = (angMom**2)/const.mu

    # calc eccentricity
    ecc = math.sqrt(1 - param/semiMajAxis)

    # calc orbital period & convert to hours
    period = (2*(math.pi))/(math.sqrt(const.mu))*(semiMajAxis**(3/2))
    period = period/60/60

    # calc radius of periapsis & apoapsis
    radPer = semiMajAxis*(1-ecc)
    radApo = semiMajAxis*(1+ecc)

    # calc flight path angle
    fpa = math.degrees( math.acos( angMom / rOrbMag / velMag ) )
    #fpa2 = math.degrees( math.atan( velocity[0]/velocity[1] ) )

    # calc true anomaly
    trueAnom = math.degrees( math.asin( (velocity[0]*angMom) / (const.mu * ecc) ) )

    print_results(h=angMom,E=totSpecEnergy,a=semiMajAxis,p=param,ecc=ecc,T=period,rp=radPer,ra=radApo,fpa=fpa,TA=trueAnom)

###MAIN###
def main():
    rOrb,vel = getInput()
    compute(velocity=vel,radOrbital=rOrb)


if __name__ == "__main__":
    main()