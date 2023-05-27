# Python 3.4.3

def main():
  while True:
    try:
      CONTRA_STRIKE = '0'

      qtd_total_gameplays, meu_identificador = input().split()
      qtd_total_gameplays = int(qtd_total_gameplays)

      qtd_meus_gameplays = 0

      for i in range(qtd_total_gameplays):

        identificador, jogo = input().split()
        if identificador == meu_identificador and jogo == CONTRA_STRIKE:
          qtd_meus_gameplays += 1

      print(qtd_meus_gameplays)

    except EOFError:
      break

if __name__ == '__main__':
	main()