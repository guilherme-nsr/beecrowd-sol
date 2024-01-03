#include <stdio.h>
#include <math.h>

int rafael(int x, int y) {
  return pow(3*x, 2) + pow(y, 2);
}

int beto(int x, int y) {
  return 2*pow(x, 2) + pow(5*y, 2);
}

int carlos(int x, int y) {
  return -100*x + pow(y, 3);
}

void print_vencedor(int x, int y) {
  if (rafael(x, y) > beto(x, y) && rafael(x, y) > carlos(x, y)) {
    printf("Rafael ganhou\n");

  } else if(beto(x, y) > rafael(x, y) && beto(x, y) > carlos(x, y)) {
    printf("Beto ganhou\n");

  } else {
    printf("Carlos ganhou\n");
  }
}

int main() {

  int n;
  scanf("%d", &n);

  int x, y;

  for (int i = 0; i < n; i++) {
    scanf("%d %d", &x, &y);

    print_vencedor(x, y);
  }

  return 0;
}
