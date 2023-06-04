#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

void strlwr(char *p) {
  for ( ; *p; ++p) *p = tolower(*p);
}

char *strrev(char *str) {
  if (!str || ! *str)
    return str;

  int i = strlen(str) - 1, j = 0;

  char ch;
  while (i > j) {
    ch = str[i];
    str[i] = str[j];
    str[j] = ch;
    i--;
    j++;
  }

  return str;
}

int main() {
  int n, m;
  scanf("%d %d", &n, &m);

  char fruta[100];
  char *frutas_busca[n], *frutas_lista[m];

  for (int i = 0; i < n; i++) {
    scanf("%s", fruta);
    strlwr(fruta);

    frutas_busca[i] = malloc(strlen(fruta) + 1);
    strcpy(frutas_busca[i], fruta);
  }

  for (int i = 0; i < m; i++) {
    scanf("%s", fruta);
    strlwr(fruta);

    frutas_lista[i] = malloc(strlen(fruta) + 1);
    strcpy(frutas_lista[i], fruta);
  }

  char fruta_rev[100];

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (strstr(frutas_lista[j], frutas_busca[i]) != NULL) {
        printf("Sheldon come a fruta %s\n", frutas_busca[i]);
        break;
      }

      strcpy(fruta_rev, frutas_busca[i]);
      strrev(fruta_rev);

      if (strstr(frutas_lista[j], fruta_rev) != NULL) {
        printf("Sheldon come a fruta %s\n", frutas_busca[i]);
        break;
      }

      if (j == m -1) {
        printf("Sheldon detesta a fruta %s\n", frutas_busca[i]);
      }
    }
  }

  return 0;
}