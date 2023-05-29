#include <stdio.h>
#include <string.h>

int main() {
  char m[7];
  int t, qtd_j, qtd_t;
  qtd_j = 0;
  qtd_t = 0;
  
  do {
    scanf("%s", m);
    if(strcmp(m, "ABEND") == 0) {
      break;
    }
    scanf("%d", &t);

    if (strcmp(m, "SALIDA") == 0) {
      qtd_j++;
      qtd_t += t;
    }

    else if(strcmp(m, "VUELTA") == 0) {
      qtd_j--;
      qtd_t -= t;
    }

  } while (strcmp(m, "ABEND") != 0);

  printf("%d\n%d\n", qtd_t, qtd_j);

  return 0;
}