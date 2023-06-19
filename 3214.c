#include <stdio.h>

int main() {
  int e, f, c, v, b;
  scanf("%d %d %d", &e, &f, &c);

  v = e+f;
  b = 0;

  while (v >= c) {
    v = v-c;
    b = b+1;
    v = v+1;
  }

  printf("%d\n", b);

  return 0;
}