#include <stdio.h>

int par(int n) {
  return n % 2 == 0;
}

int impar(int n) {
  return n % 2 != 0;
}

int main() {
  int l, c;
  scanf("%d %d", &l, &c);

  if ((par(l) && par(c)) || (impar(l) && impar(c))) {
    printf("1\n");
  } else {
    printf("0\n");
  }

	return 0;
}