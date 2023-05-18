#include <stdio.h>

int main(void) {

  int n, qtd_total_alunos, notas[1000], soma;
  float qtd_alunos_acima_media = 0;

  scanf("%d", &n);

  for (int i = 1; i <= n; i++) {
    scanf("%d", &qtd_total_alunos);

    for (int j = 0; j < qtd_total_alunos; j++) {
      scanf("%d", &notas[j]);
      soma += notas[j];
    }

    for (int j = 0; j < qtd_total_alunos; j++) {
      if (notas[j] > soma / qtd_total_alunos)
        qtd_alunos_acima_media++;
    }

    printf("%.3f%%\n", 100 * qtd_alunos_acima_media/qtd_total_alunos);

    soma = 0;
    qtd_alunos_acima_media = 0;
  }

  return 0;
}