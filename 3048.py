sequencia = [int(input()) for i in range(int(input()))]

numero_procurado = 2
qtd_numeros_marcados = 1

for numero in sequencia[1:]:
	if numero == numero_procurado:
		qtd_numeros_marcados += 1
		
		if numero_procurado == 2:
			numero_procurado = 1
		else:
			numero_procurado = 2

print(qtd_numeros_marcados)