def resolver_disputa(sheldon, raj):
  if sheldon == raj:
    # empate
    return 0

  escolhas_derrotadas_por = {
    'pedra': ['lagarto', 'tesoura'],
    'papel': ['pedra', 'Spock'],
    'tesoura': ['papel', 'lagarto'],
    'lagarto': ['Spock', 'papel'],
    'Spock': ['tesoura', 'pedra']
  }
  
  if raj in escolhas_derrotadas_por[sheldon]:
    # sheldon vence
    return 1

  # raj vence
  return -1

def main():

  qtd_disputas = int(input())

  for i in range(qtd_disputas):
    sheldon, raj = input().split()

    if resolver_disputa(sheldon, raj) == 0:
      reacao_sheldon = 'De novo!'
    elif resolver_disputa(sheldon, raj) == 1:
      reacao_sheldon = 'Bazinga!'
    elif resolver_disputa(sheldon, raj) == -1:
      reacao_sheldon = 'Raj trapaceou!'

    print('Caso #' + str(i+1) + ': ' + reacao_sheldon)

if __name__ == '__main__':
  main()