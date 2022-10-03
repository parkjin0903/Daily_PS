#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, int m) {
    int temp;
    int temp1;
    temp1 = n * m;
    while(n!=0){
        temp = m % n;
        m = n;
        n = temp;
        }
    vector<int> answer;
    answer.push_back(m);
    answer.push_back(temp1/m);
    
    return answer;
}
