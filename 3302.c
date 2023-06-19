#include <stdio.h>

int main() {
  int n, r;
  scanf("%d", &n);

  for (int i = 0; i < n; i++) {
    scanf("%d", &r);
    printf("resposta %d: %d\n", i+1, r);
  }

  return 0;
}