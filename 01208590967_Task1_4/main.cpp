#include <iostream>
#include <vector>

using namespace std;

int main()
{
    float errorEst = 0.08;
float trueResults[10];
float mpu6050[10] = {0.0, 11.68, 18.95, 23.56, 25.72, 25.38, 22.65, 18.01, 10.14, -0.26}; //estimated
float bno55[10] = {0.0,9.49, 16.36, 21.2, 23.16, 22.8, 19.5, 14.85, 6.79, -2.69}; //measured
for(int i = 0; i<10; i++){
    float KG = errorEst/(errorEst+0.22); //Error in estimation/(error in estimation + error in measure) estimation= more acurate results
    trueResults[i] = bno55[i]+ KG*( mpu6050[i]-bno55[i]);
    errorEst= (1-KG)* errorEst;
}
for (int j = 0; j<10; j++){
    cout<<trueResults[j]<<" ";
}
    return 0;
}
