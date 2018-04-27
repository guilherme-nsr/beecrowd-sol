nome = input()
salario = float(input())
vendas = float(input()) # O total de vendas efetuadas pelo vendedor no mês (em dinheiro)

TOTAL = salario + (vendas * 0.15) # O valor que o vendedor receberá no fim do mês

print("TOTAL = R$ %.2f" % TOTAL)