#include <stdio.h>

int main() {

	int c[4], f;

	for (int i = 0; i < 4; i++) {
		scanf("%d", &c[i]);

		if (c[i] == 1) {
			f = i;
		}
	}

	printf("%d\n", f+1);

	return 0;
}