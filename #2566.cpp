#include <iostream>
using namespace std;
int i, a, x, c = 0;
int main() {
	for (i = 0; i < 81; i++){
			cin >> a;
			if (a > c)	c = a, x = i;
		}
	printf("%d %d %d", c, x / 9 + 1, x % 9 + 1);
}
