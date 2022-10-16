#include<iostream>
#include<algorithm>
using namespace std;

int main() {
	int test, n, m, winner[100];
	int i, j, k;

	cin >> test;

	for (i = 0; i < test; ++i) {
		cin >> n >> m;
		int* pN = new int[n];
		int* pM = new int[m];

		for (j = 0; j < n; j++) {
			cin >> pN[j];
		}
		for (k = 0; k < m; k++) {
			cin >> pM[k];
		}

		sort(pN, pN + n);
		sort(pM, pM + m);

		for (j = 0, k = 0;j<n && k<m;) {
			if (pN[j] >= pM[k]) {
				++k;
			}

			if (pN[j] < pM[k]) {
				++j;
			}
		}

		if (j == n) {
			winner[i] = 1;
		}
		if (k == m) {
			winner[i] = 0;
		}

	}

	for (i = 0; i < test; ++i) {
		if (winner[i] == 1) {
			cout << "B" << endl;
		}
		if (winner[i] == 0) {
			cout << "S" << endl;
		}
	}


	return 0;
}


