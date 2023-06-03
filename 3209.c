#include <stdio.h>

int main() {
  int n, k, qtd_tomadas;

  scanf("%d", &n);

  for (int i = 0; i < n; i++) {
    qtd_tomadas = 0;
    scanf("%d", &k);

    for (int j = 0; j < k; j++) {
      int f;
      scanf("%d", &f);

      if(j == k-1) {
        qtd_tomadas += f;
      } else {
        qtd_tomadas += f-1;
      }
    }

    printf("%d\n", qtd_tomadas);
  }

  return 0;
}