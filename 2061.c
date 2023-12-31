#include <stdio.h>
#include <string.h>
 
int main() {
 
  int n, m;
  char acao[7];

  scanf("%d %d", &n, &m);

  for (int i = 0; i < m; ++i) {
    scanf("%s", acao);
    
    if (strcmp(acao, "fechou") == 0) {
      n -= 1;
      n += 2;
    } else {
      n -= 1;
    }
  }

  printf("%d\n", n);

  return 0;
}