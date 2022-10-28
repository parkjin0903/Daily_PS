#include <iostream>
#include <vector>
using namespace std;

int main(){
	
	int n;
	cin >> n;
	
	vector<int> vec;
	
	while(n>0){
		int num = 0;
		cin >> num;
		vec.push_back(num);
		n--;
	}  
	
	int v = 0;
	cin >> v;
	
	int cnt = 0;
	for(int i = 0; i < vec.size(); i++){
		if(vec[i] == v){
			cnt ++;
		}
	}
	
	cout << cnt << endl;
}
