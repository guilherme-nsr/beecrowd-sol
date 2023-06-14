def get_sequencia_espelho(b, e):
  sequencia = ''.join([str(i) for i in range(b, e+1)])
  espelho = sequencia[::-1]

  return sequencia + espelho

for i in range(int(input())):
  b, e = map(int, input().split())

  print(get_sequencia_espelho(b, e))