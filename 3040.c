#include <stdio.h>

int escolher_arvore(int h, int d, int g) {
  if (h < 200 || h > 300 || d < 50 || g < 150) {
    return 0;
  }

  return 1;
}

int main() {
  int n, h, d, g;
  scanf("%d", &n);

  for (int i = 0; i < n; i++) {
    scanf("%d %d %d", &h, &d, &g);

    if(escolher_arvore(h, d, g)) {
      printf("Sim\n");
    } else {
      printf("Nao\n");
    }
  }

  return 0;
}