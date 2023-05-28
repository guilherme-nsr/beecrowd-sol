# Python 3.4.3

def main():
  qtd_jipes_voltar = 0
  qtd_turistas_voltar = 0

  entrada = input().split()
  movimento = entrada[0]
  if len(entrada) == 2:
    qtd_turistas = int(entrada[1])

  while movimento != 'ABEND':
    if movimento == 'SALIDA':
      qtd_jipes_voltar += 1
      qtd_turistas_voltar += qtd_turistas

    elif movimento == 'VUELTA':
      qtd_jipes_voltar -= 1
      qtd_turistas_voltar -= qtd_turistas

    entrada = input().split()
    movimento = entrada[0]
    if len(entrada) == 2:
      qtd_turistas = int(entrada[1])

  print(qtd_turistas_voltar)
  print(qtd_jipes_voltar)

if __name__ == '__main__':
  main()