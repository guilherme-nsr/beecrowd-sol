#include <stdio.h>

int main() {
	int qtd_estrelas, qtd_estrelas_visitadas, qtd_carneiros_roubados, estrela_atual, jornada_interrompida, voltou;
  long long qtd_total_carneiros;

  scanf("%d", &qtd_estrelas);

  int carneiros[qtd_estrelas];
  
  qtd_total_carneiros = 0;

  for(int i = 0; i < qtd_estrelas; i++) {
    scanf("%d", &carneiros[i]);
    qtd_total_carneiros += carneiros[i];
  }

  qtd_estrelas_visitadas = 1;
  qtd_carneiros_roubados = 0;
  estrela_atual = 0;
  jornada_interrompida = 0;

  while(jornada_interrompida == 0) {
    if(carneiros[estrela_atual] % 2 == 0) {
      if(carneiros[estrela_atual] > 0) {
        qtd_carneiros_roubados += 1;
        carneiros[estrela_atual] -= 1;
      }

      estrela_atual -= 1;
      voltou = 1;
    } else {
      if(carneiros[estrela_atual] > 0) {
        qtd_carneiros_roubados += 1;
        carneiros[estrela_atual] -= 1;
      }

      estrela_atual += 1;
      voltou = 0;
    }

    if(estrela_atual >= qtd_estrelas || estrela_atual < 0) {
      jornada_interrompida = 1;
    } else {
      if(voltou == 0) {
        qtd_estrelas_visitadas += 1;
      }
    }
  }

  long long qtd_carneiros_nao_roubados = qtd_total_carneiros - qtd_carneiros_roubados;
  printf("%d %lld\n", qtd_estrelas_visitadas, qtd_carneiros_nao_roubados);

	return 0;
}