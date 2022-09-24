// XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
// Orbital Mechanics & Dynamics Software Collection
// Author:   Steven Anderson
// Created:  AUG 2022
// Brief:    Example 2.1
//           Calc: tot specific energy, ang momentum, ecc from
//           alt, velInertial, FPA
// XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

#include <cmath>
#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    // Givens:
    const int satAltitude = 2124;       //km
    const float velInertial = 7.58;     //km/s
    const int flightPathAngle = 20;     //deg

    // Constants:
    const int radEarth = 6378;          //km
    const float mu = 3.986e5;           //mu
    const double Pi = 3.14159265358979323846264;

    // Initialize variables
    int rad;
    float totSpEnergy;
    float angMom;
    float semiMajorAxis;
    float param;
    float ecc;

    cout.precision(3);
    cout << fixed;


    // (a) calculate total specific energy
    rad = satAltitude + radEarth;
    totSpEnergy = pow(velInertial,2) / 2 - mu / rad;

    // (b) calculate angular momentum
    angMom = rad * velInertial * cos(flightPathAngle* Pi / 180);

    // (c) calculate eccentricity
    semiMajorAxis = -mu / (2 * totSpEnergy);
    param = pow(angMom,2) / mu;
    ecc = sqrt(1 - (param / semiMajorAxis));

    // output
    cout << "Total Specific Energy: " << totSpEnergy << " [km^2/s^2]" << endl;
    cout << "Angular Momentum: " << angMom << " [km^2/s]" << endl;
    cout << "Eccentricity: " << ecc << " [n/a]" << endl;
    

    return 0;
}