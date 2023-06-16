#include <stdio.h>

void print_folhas(int n) {
  int s, f;
  s = (n-1) / 2;
  f = 1;

  while (f < n) {
    for (int i = 0; i < s; i++) printf(" ");
    for (int i = 0; i < f; i++) printf("*");
    printf("\n");

    s = s-1;
    f = f+2;
  }

  for (int i = 0; i < f; i++) printf("*");
  printf("\n");
}

void print_tronco(int n) {
  int s;
  s = (n-1) / 2;

  for (int i = 0; i < s; i++) printf(" ");
  printf("*\n");

  s = s-1;

  for (int i = 0; i < s; i++) printf(" ");
  printf("***\n");
}

int main() {
  int n;

  while (scanf("%d", &n) != EOF) {
    print_folhas(n);
    print_tronco(n);
    printf("\n");
  }

  return 0;
}