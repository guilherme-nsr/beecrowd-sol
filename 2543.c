#include <stdio.h>

#define CONTRA_STRIKE 0

int main() {
  int qtd_total_gameplays, meu_id, id, jogo, qtd_meus_gameplays;

  while (scanf("%d %d", &qtd_total_gameplays, &meu_id) != EOF) {
    qtd_meus_gameplays = 0;

    for (int i = 0; i < qtd_total_gameplays; i++) {
      scanf("%d %d", &id, &jogo);

      if (id == meu_id && jogo == CONTRA_STRIKE) {
        qtd_meus_gameplays++;
      }
    }

    printf("%d\n", qtd_meus_gameplays);
  }

	return 0;
}