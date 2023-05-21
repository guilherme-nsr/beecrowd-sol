# Python 3.4.3

def get_ano(anos_transcorridos, ano):
  diferenca = ano - anos_transcorridos

  if diferenca == 0:
    return '1 A.C.'

  if diferenca > 0:
    return '%d D.C.' % (diferenca)

  return '%d A.C.' % (diferenca*-1 + 1)

def main():
  n = int(input())

  for i in range(n):
    anos_transcorridos = int(input())

    print(get_ano(anos_transcorridos, 2015))

if __name__ == '__main__':
  main()