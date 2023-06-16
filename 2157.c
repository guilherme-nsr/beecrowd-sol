#include <stdio.h>

void print_intrev(int n) {
  int r = 0;

  while (n != 0) {
    r = n % 10;
    n = n / 10;

    printf("%d", r);
  }
}

int main() {
  int c, b , e, auxb, q;
  scanf("%d", &c);

  for (int i = 0; i < c; i++) {
    scanf("%d %d", &b, &e);
    auxb = b;
    
    for ( ; b <= e; b++) printf("%d", b);
    for ( ; e >= auxb; e--) print_intrev(e);

    printf("\n");
  }

  return 0;
}