#include <iostream>

using namespace std;

int main() {

	int c[4], f;

	for (int i = 0; i < 4; i++) {
		cin >> c[i];

		if (c[i] == 1) {
			f = i;
		}
	}

	cout << f+1 << endl;

	return 0;
}