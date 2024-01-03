qtd_dias, saldo = map(int, input().split())

menor_saldo = saldo

for i in range(qtd_dias):

  movimentacao = int(input())
  saldo = saldo + movimentacao

  if saldo < menor_saldo:
    menor_saldo = saldo

print(menor_saldo)
