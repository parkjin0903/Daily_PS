#include <iostream>
using namespace std;

int main()
{
	int n;

	cin >> n;

	if (n < 1 || n > 100)
		return 0;
	

	for (int i = 0; i < n; i++)  // 1���� n �ٱ��� �ݺ� 
	{
		for (int j = 0; j < i; j++)  //  i���� ����
		{
			cout << " ";
		}

		for (int k = n - i; k > 0; k--)  // n-i���� �� 
		{
			cout << "*";
		}
		
		cout << endl;
	}

	return 0;
}

