#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    for(int i=0; i<numbers.size()-1; i++){
        for(int j=i+1; j<numbers.size(); j++){
            answer.push_back(numbers[i] + numbers[j]);
        }
        
    }
    sort(answer.begin(), answer.end());
    answer.erase(unique(answer.begin(), answer.end()), answer.end()); // unique는 중복을 뒤로 보내고 주소를 리턴
    
    return answer;
}
