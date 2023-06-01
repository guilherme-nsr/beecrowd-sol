#include <stdio.h>

void print_sobrinho_meio(int h, int z, int l) {
  if ((h > z && h < l) || (h < z && h > l)) {
    printf("huguinho\n");
  } else if ((z > h && z < l) || (z < h && z > l)) {
    printf("zezinho\n");
  } else {
    printf("luisinho\n");
  }
}

int main() {
  int h, z, l;
  scanf("%d %d %d", &h, &z, &l);

  print_sobrinho_meio(h, z, l);

  return 0;
}