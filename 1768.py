def print_tronco(n):
  s = (n-1) // 2
  print(' '*s + '*')

  s = s-1
  print(' '*s + '***')

def print_folhas(n):
  s = (n-1) // 2
  f = 1


  while f < n:
    print(' '*s + '*'*f)
    s = s-1
    f = f+2

  print('*'*f)


while True:
  try:
    n = int(input())

    print_folhas(n)
    print_tronco(n)
    print()
  except EOFError:
    break