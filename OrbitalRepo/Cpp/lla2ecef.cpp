// Simple script to convert LLA to ECEF

#include <cmath>
#include <iostream>
// using namespace std;

class geodeticCoords {
    public:
        double latitude;
        double longitude;
        double altitude;    // HAE

        // Constructor
        geodeticCoords() {
            latitude = 0.0;
            longitude = 0.0;
            altitude = 0.0;
        }
        
        geodeticCoords(double inLatitude, double inLongitude, double inAltitude) {
            latitude = inLatitude;
            longitude = inLongitude;
            altitude = inAltitude;
        }
};

void getCoords(geodeticCoords& coords) {
    // Reference to the object is passed to the function so the value exists outside this function.
    coords.latitude = radians(32.21060); //rad
    coords.longitude = radians(-110.99169); //rad
    coords.altitude = 884.2248; //m
    // TODO: convert to radians & check all units
}

int main() {
    geodeticCoords AmountainGeod;
    //geodeticCoords AmountainGeod(32.21060, -110.99169, 2901);

    getCoords(AmountainGeod);

    std::cout << "~~Geodetic coordinates~~" << std::endl;
    std::cout << "Latitude" << std::endl;
    std::cout << AmountainGeod.latitude << std::endl;
    std::cout << "Longitude" << std::endl;
    std::cout << AmountainGeod.longitude << std::endl;
    std::cout << "Altitude" << std::endl;
    std::cout << AmountainGeod.altitude << std::endl;

    std::cout << "~~ECEF coordinates~~" << std::endl;
    
    // ECEF Formulation
    double radEqu = 6378137.0; //m
    double radPolar = 6356752.314245; //m
    double e2 = 1 - pow(radPolar,2) / pow(radEqu,2);
    double N = radEqu / sqrt(1 - e2 * pow(sin(AmountainGeod.latitude),2));
    std::cout << "N " << N << std::endl;
    double x = (N + AmountainGeod.altitude) * cos(AmountainGeod.latitude) * cos(AmountainGeod.longitude);
    std::cout << "X coord: " << x << std::endl;
    return 0;
}

