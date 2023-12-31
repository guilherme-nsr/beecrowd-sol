#include <stdio.h>

int main() {

	int p1, c1, p2, c2;

	scanf("%d %d %d %d", &p1, &c1, &p2, &c2);

	int pc1, pc2;

	pc1 = p1*c1;
	pc2 = p2*c2;

	if (pc1 == pc2) {
		printf("%d\n", 0);

	} else if (pc1 > pc2) {
		printf("%d\n", -1);

	} else {
		printf("%d\n", 1);
	}

	return 0;
}