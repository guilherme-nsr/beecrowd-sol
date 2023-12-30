# Python 3.9.4

tabela = {
	"E": 0,
	"D": 35,
	"C": 60,
	"B": 85,
	"A": 100
}

nota = int(input())

conceito = ""

for key in tabela:
	nota_limite = tabela[key]

	if nota <= nota_limite:
		conceito = key
		break

print(conceito)