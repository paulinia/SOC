#include<bits/stdc++.h>

using namespace std;

#define FOR(i,n)	for(int i=0;i<(int)n;i++)

int main(){
    int r = 1000;
    int s = 1000;
    
    for(long double p = 0; p <= 1; p += 0.01){
        long double q = 1 - p;
        vector<long double> bef(s, 1), aft(s, q);
        for(int i = 1; i < r; i ++){
            swap(bef, aft);
            FOR(j, s){
                if(!j) aft[j] = q * bef[j];
                else aft[j] = q * (1 - (1 - bef[j]) * (1 - aft[j - 1]));
            }
        }
        long double P = 1.0;
        FOR(i, s){
            P *= (1.0 - q * bef[i]);
        }
        
        cout << p << "\t" << P << endl;
    }
    
}
