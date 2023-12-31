#include <stdio.h>

int main() {

	int c, p, f;

	scanf("%d %d %d", &c, &p, &f);

	c*f <= p ? printf("S\n") : printf("N\n");

	return 0;
}