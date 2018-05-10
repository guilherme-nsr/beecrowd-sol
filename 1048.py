salario = float(input())

if 0 <= salario <= 400:
	percentual = 15

elif 400.01 <= salario <= 800:
	percentual = 12

elif 800.01 <= salario <= 1200:
	percentual = 10

elif 1200.01 <= salario <= 2000:
	percentual = 7

elif salario > 2000:
	percentual = 4

reajuste = salario * (percentual / 100)
novo_salario = salario + reajuste
print("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: %d %s" % (novo_salario, reajuste, percentual, '%')) 