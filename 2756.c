#include <stdio.h>

void print_ws(int n) {
	// prints n whitespaces
	for (int i = 0; i < n; i++) printf(" ");
}

int main() {

	int tws = 7; // number of trailing whitespaces to print
	int bws = -1; // number of between whitespaces to print
	int c = 65; // 'A' char code
	int l = 0; // number of lines printed

	while (l < 9) {
		if (c == 65) {
			print_ws(tws);
			printf("%c\n", c);

		} else {
			print_ws(tws);
			printf("%c", c);
			print_ws(bws);
			printf("%c\n", c);
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