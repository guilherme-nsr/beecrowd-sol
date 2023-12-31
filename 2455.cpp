#include <iostream>

using namespace std;

int main() {

	int p1, c1, p2, c2;

	cin >> p1 >> c1 >> p2 >> c2;

	int pc1, pc2;

	pc1 = p1*c1;
	pc2 = p2*c2;

	if (pc1 == pc2) {
		cout << 0 << endl;

	} else if (pc1 > pc2) {
		cout << -1 << endl;

	} else {
		cout << 1 << endl;
	}

	return 0;
}