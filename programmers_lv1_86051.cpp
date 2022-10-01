#include <string>
#include <vector>

using namespace std;

int solution(vector<int> numbers) {
    int cum = 0;
    for(int i=0; i<numbers.size(); i++){
        cum += numbers[i];
    }
    int answer = 45-cum;
    return answer;
}
