#include <stdio.h>

int main() {
  int c, n;

  while (scanf("%d", &c) != EOF) {
    for (int i = 0; i < c; i++) {
      scanf("%d", &n);

      if (n > 8000) {
        printf("Mais de 8000!\n");
      } else {
        printf("Inseto!\n");
      }
    }
  }
  return 0;
}