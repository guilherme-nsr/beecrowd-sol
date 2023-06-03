#include <stdio.h>
#include <string.h>

int main() {
  int n, h, b, a, m, d;
  char g[20];

  scanf("%d", &n);

  b = 0;
  a = 0;
  m = 0;
  d = 0;

  for (int i = 0; i < n; i++) {
    scanf("%*s %s %d", g, &h);
    
    if (strcmp(g, "bonecos") == 0) {
      b = b + h;
    } else if (strcmp(g, "arquitetos") == 0) {
      a = a + h;
    } else if (strcmp(g, "musicos") == 0) {
      m = m + h;
    } else if (strcmp(g, "desenhistas") == 0) {
      d = d + h;
    }
  }

  int p = 0;
  p = p + b / 8;
  p = p + a / 4;
  p = p + m / 6;
  p = p + d / 12;

  printf("%d\n", p);

  return 0;
}