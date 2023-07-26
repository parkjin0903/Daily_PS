#include<iostream>
#include<vector>
#include<string>
#include<cstring>
#include<iomanip>
#include<cmath>
#include<algorithm>
#include<queue>

using namespace std;

int main(){
    int n, divisor = 1;
    cin >> n;
    for (int i = 2; i*i <= n; i++) {
        if (n%i == 0) {
            divisor = n/i;
            break;
        }
    }
    cout << n-divisor << '\n';
}