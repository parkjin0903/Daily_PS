#include <iostream>
using namespace std;

int main()
{
	int nScore[5] = { 0, };
	int nTotal = 0;
	int nAvg = 0;

	for (int i = 0; i < 5; i++)
	{
		cin >> nScore[i];

		if (nScore[i] < 40)
			nScore[i] = 40;

		nTotal += nScore[i];
	}

	nAvg = nTotal / 5;

	cout << nAvg;

	return 0;	
}
