#include <iostream>

using namespace std;

void print_ws(int n) {
	// prints n whitespaces
	for (int i = 0; i < n; i++) cout << " ";
}

int main() {

	int tws = 7; // number of trailing whitespaces to print
	int bws = -1; // number of between whitespaces to print
	char c = 65; // 'A' char code
	int l = 0; // number of lines printed

	while (l < 9) {
		if (c == 65) {
			print_ws(tws);
			cout << c << endl;

		} else {
			print_ws(tws);
			cout << c;
			print_ws(bws);
			cout << c << endl;
		}

		if (l < 4) {
			tws -= 1;
			bws += 2;
			c += 1;

		} else {
			tws += 1;
			bws -= 2;
			c -= 1;
		}

		l += 1;
	}

	return 0;
}