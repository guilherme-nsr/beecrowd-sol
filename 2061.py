qtd_abas, qtd_acoes = map(int, input().split())

for i in range(qtd_acoes):
	acao = input()

	if acao == "fechou":
		qtd_abas -= 1
		qtd_abas += 2

	else:
		qtd_abas -= 1

print(qtd_abas)