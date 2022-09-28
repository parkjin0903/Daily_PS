#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    int num = s.length();
    string answer = "";
    if(num%2==1){
        answer = s[num/2];
    }
    else{
        answer = s[num/2-1];
        answer += s[num/2];
    }
    

    return answer;
}
