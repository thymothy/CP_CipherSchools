#include <bits/stdc++.h>
using namespace std;
bool meet (int x1, int v1, int x2, int v2){
    if ((x1<x2 && v1<=v2)||(x1>x2 && v1>=v2))
    return false;
    else
    return (abs(x1-x2)%abs(v1-v2) == 0);
}

int main(){

    int x1 =6, x2 = 8, v1 = 4, v2 = 2;
    bool a = meet(x1,v1,x2,v2);
    cout<<a;

    return 0;
}