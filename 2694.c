#include <stdio.h>

#define TAMANHO_ENTRADA 14

int intpow(int a, int b) {
  int r = 1;

  for (int i = 0; i < b; i++) r = r * a;

  return r;
}

int parse_and_sum(char *relatorio) {
  int sum, u, n;
  sum = 0;
  u = 0;

  for (int i = TAMANHO_ENTRADA-1; i >= 0; i--) {
    if ( relatorio[i] >= 48 && relatorio[i] <= 57) {
      n = relatorio[i] - 48;
      sum = sum + intpow(10, u) * n;
      u++;
    } else {
      u = 0;
    }
  }

  return sum;
}

int main() {
  int n;
  char relatorio[TAMANHO_ENTRADA];

  scanf("%d", &n);

  for (int i = 0; i < n; i++) {
    scanf("%s", relatorio);
    printf("%d\n", parse_and_sum(relatorio));
  }

  return 0;
}