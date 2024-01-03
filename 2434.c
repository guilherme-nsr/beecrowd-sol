#include <stdio.h>

int main() {
  
  int n, saldo;

  scanf("%d %d", &n, &saldo);

  int mov, menor;
  menor = saldo;

  for (int i = 0; i < n; i++) {
    scanf("%d", &mov);

    saldo = saldo + mov;

    if (saldo < menor) {
      menor = saldo;
    }
  }

  printf("%d\n", menor);

  return 0;
}
