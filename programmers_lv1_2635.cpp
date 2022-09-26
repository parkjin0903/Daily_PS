#include <iostream>
using namespace std;
int N;
int ff(int a, bool f){
	int k = N;
	int i=0;
	while(k >= 0){
		int temp = k;
		if(f) cout << temp <<' ';
		k = a;
		a = temp - a;
		i++;
	}
	return i;
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	cin >> N;
	
	int target = -1;
	int tnum = 0;
	for(int i=N/2; i<=N;i++){
		int a = ff(i, false);
		if(target < a){
			target = a;
			tnum = i;
		}
	}
	
	cout << target << '\n';
	ff(tnum, true);
	return 0;
}
