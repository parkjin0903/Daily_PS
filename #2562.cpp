#include <iostream>

using namespace std;

int main(){
	
	int n;
	cin>>n;
	
	int num[n+1];
	int min = 1000000;
	int max = 0;     // Ʋ�� ����
	
	for(int i=0; i<n; i++){
		cin >> num[i];
		if(min < num[i]){  // ������ ���ǹ� ���
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
