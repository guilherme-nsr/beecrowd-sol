#include <iostream>

using namespace std;

int main() {

	int x, m;

	cin >> x >> m;
	
	do {

		cout << x*m << endl;
		cin >> x >> m;

	} while (x != 0 || m != 0);

	return 0;
}