#include<bits/stdc++.h>

using namespace std;

#define FOR(i,n)	for(int i=0;i<(int)n;i++)

int main(){
    int r = 3;
    int s = 6;
    
    for(long double p = 0; p < 1; p += 0.01){
        long double P = 0;
        int a = 0;
        
        while(a < (1 << (r * s))){
            int boli = 0;
            queue<int> Q;
            FOR(i, s){
                if(a & (1 << i)){
                    Q.push(i);
                }
            }
            
            long double pp = 1;
            FOR(i, s * r){
                if(a & (1 << i)) pp *= p;
                else pp *= (1 - p);
            }
            
            int E[] = {1, -s, -1, s};
            bool je = 0;
            while(Q.size()){
                int v = Q.front();
                Q.pop();
                if(v >= r * s - s){
                    je = 1;
                    break;
                }
                FOR(i, 4){
                    if(v + E[i] >= 0 && v + E[i] < r * s && (!(boli & (1 << (v + E[i])))) && (a & (1 << (v + E[i])))){
                        Q.push(v + E[i]);
                        boli |= (1 << (v + E[i]));
                    }
                }
            }
            if(je){
                P += pp;
            }
            a ++;
        }
        
        cout << p << "\t" << P << endl;
    }
    
}
