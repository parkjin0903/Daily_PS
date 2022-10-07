#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    int num[1000000];
    for(int i=2;i<=n;i++){ // i = 2 3 4 5 6 7 8 9 10
        if(num[i]==1)
            continue;
        for(int j=i*2;j<=n;j+=i){ // j = 4 6 8 10 / j = 6 9 
            num[j]=1;
        }
    }
    for(int i=2;i<=n;i++){
        if(num[i]==0)
            answer++;
    }
    return answer;
}
