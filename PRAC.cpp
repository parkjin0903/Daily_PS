#include <iostream>

using namespace std;

int main(){
	
	int n;
	cin>>n;
	
	int num[n+1];
	int min = 1000000;
	int max = 0;     // 틀린 이유
	
	for(int i=0; i<n; i++){
		cin >> num[i];
		if(min < num[i]){  // 복잡한 조건문 사용
			min = min;
		} else {
			min = num[i];
		}
		if(max > num[i]){
			max = max;
		} else {
			max = num[i];
		}
	}
	
	cout << min << " " << max << "\n";
	
	return 0;
}
