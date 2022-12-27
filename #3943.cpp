#include <iostream>

using namespace std;

 

int N, maxNum;

 

int maxHailStone(int N)

{

        if (maxNum <= N)

                 maxNum = N;

 

        if (N == 1) //기저사례: 1이 끝

                 return maxNum;

        else

                 return N % 2 ? maxHailStone(3 * N + 1) : maxHailStone(N / 2);

}

 

int main(void)

{

        int test_case;

        cin >> test_case;

 

        for (int i = 0; i < test_case; i++)

        {

                 scanf("%d", &N);

                 maxNum = N;

                 printf("%d\n", maxHailStone(N));

        }

        return 0;

}
