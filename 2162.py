# Python 3.4.3

def main():
  input()

  medidas = list(map(int, input().split()))

  flag = 0
  padrao = 1

  for i in range(1, len(medidas)):
    anterior = medidas[i-1]
    atual = medidas[i]

    if atual > anterior and (flag == -1 or flag == 0):
      flag = 1 # pico

    elif atual < anterior and (flag == 1 or flag == 0):
      flag = -1 # vale

    elif atual > anterior and flag == 1:
      padrao = 0
      break

    elif atual < anterior and flag == -1:
      padrao = 0
      break

    elif atual == anterior:
      padrao = 0
      break

  print(padrao)

if __name__ == '__main__':
  main()