def traduzir_piscada(piscada):
  somatorio = 0

  for i in range(len(piscada)):
    olho = piscada[i]

    if olho == '-':
      continue

    if i == 0:
      somatorio += 4
    elif i == 1:
      somatorio += 2
    elif i == 2:
      somatorio += 1

  return somatorio

def main():
  qtd_gritos = 0
  somatorio = 0

  while qtd_gritos < 3:
    entrada = input()

    if entrada == 'caw caw':
      print(somatorio)
      qtd_gritos += 1
      somatorio = 0

    else:
      somatorio += traduzir_piscada(entrada)

if __name__ == '__main__':
  main()