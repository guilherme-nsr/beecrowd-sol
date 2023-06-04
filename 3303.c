#include <stdio.h>

int len(char *p) {
  int i = 0;
  for ( ; p[i] != '\0'; i++);
  return i;
}

int main() {
  char p[20];
  scanf("%s", p);

  if (len(p) >= 10)
    printf("palavrao\n");
  else
    printf("palavrinha\n");

  return 0;
}