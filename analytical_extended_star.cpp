/*
    This code calculates the probability distribution for the cover time of an extended star
*/


#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;

// Function to find a factorial
int factorial(int N)
{
    if (N == 1){
        return 1;
    }
    else {
        return N * factorial(N-1);
        }
}


// Function to find the combinations
int comb(int N, int L)
{
    if (N >= L){
        int i;
        int numerator = 1;
        for (i = N; i > N-L; i--){
            numerator *= i;
        }

        return numerator / factorial(L);
    }
    else {
        return 0;
    }
}

/* Function to find the probability for one arm of an extended star
 Here l is the length of the arm and n is the number of trials
*/
float single_arm_prob(int l, int n, float phi)
{
    if (n >= l) {
        return comb(n-1, l-1) * pow(phi, l) * pow(1-phi, n-l);
    }
    else{
        return 0;
    }

}

// Function to calculate the probability that the cover time is less than or equal to n
float cumulative(int n, int D, int l[], float phi){
    
    float S = 0;
    int n1, n2, n3;
    for (n1=1; n1 < n; n1++){
        for (n2=1; n2 < n; n2++){
            for (n3=1; n3 < n; n3++){
                S += single_arm_prob(l[0], n1, phi) * single_arm_prob(l[1], n2, phi) * single_arm_prob(l[2], n3, phi);
            }
        
        }
    }

    return S;
}

//Starting the main function

int main(){
    int D = 3;

    // Specify the lengths of the arms of the extended star..
    int l[D] = {2, 3, 2};

    // Specify the probabililty of a success
    float phi = 0.3;

    // Open a file to write the output to
    fstream f;
    f.open("prob_dist.dat", ios::out);
    fstream g;
    g.open("cum_dist.dat", ios::out);

    //Calculate the probability that the cover time is exact n
    for (int n = 1; n < 100; n++){
        cout << n << endl;
        f << n << "," << cumulative(n, D, l, phi)-cumulative(n-1, D, l, phi) << endl;
        g << n << "," << cumulative(n, D, l, phi) << endl;
    }

    f.close();
    g.close();
    return 0;

}

// Writing something!
