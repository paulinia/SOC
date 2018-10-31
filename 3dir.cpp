#include<bits/stdc++.h>

using namespace std;

#define FOR(i,n)	for(int i=0;i<(int)n;i++)

int main(){
    int r = 10;
    int s = 10;
    
    cout << setprecision(10);
    
    vector<vector<int> > to_state(1 << s, vector<int>(1 << s, 0));
    vector<int> num_empty(1 << s);
    
    FOR(row, 1 << s){
        FOR(above, 1 << s){
            int stav = 0;
            int p = 0;
            FOR(i, s){
                p += (row & (1 << i) ? 1 : 0);
                if((row & (1 << i)) && (above & (1 << i))) stav |= (1 << i);
            }
            FOR(i, s - 1){
                if((stav & (1 << i)) && (row & (1 << (i + 1)))) stav |= (1 << (i + 1));
            }
            for(int i = 1; i < s; i ++){
                if((stav & (1 << i)) && (row & (1 << (i - 1)))) stav |= (1 << (i - 1));
            }
            to_state[above][row] = stav;
            num_empty[row] = p;
        }
    }
    
    for(long double p = 0; p <= 1; p += 0.01){
        vector<long double> bef(1 << s), aft(1 << s);
        long double q = 1 - p;
        FOR(i, 1 << s) aft[i] = pow(q, num_empty[i]) * pow(1 - q, s - num_empty[i]);
        for(int i = 1; i < r; i ++){
            swap(aft, bef);
            aft.clear();
            aft.resize(1 << s, 0);
            FOR(row, 1 << s){
                FOR(above, 1 << s){
                    aft[to_state[above][row]] += (pow(q, num_empty[row]) * pow(1 - q, s - num_empty[row])) * bef[above];
                }
            }
        }
        long double P = 1 - aft[0];
        cout << p << "\t" << 1 - P << endl;
    }
}
