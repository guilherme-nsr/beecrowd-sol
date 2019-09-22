def main():
	n, amizade_necessaria = map(int, input().split())

	runas = {}

	for i in range(n):
		entrada = input().split()
		runa, valor = entrada[0], int(entrada[1])

		runas[runa] = valor

	input()

	runas_utilizadas = input().split()
	amizade_emitida = 0

	for runa in runas_utilizadas:
		amizade_emitida += runas[runa]
		
	print(amizade_emitida)
	print("You shall pass!") if amizade_emitida >= amizade_necessaria else print("My precioooous")


if __name__ == "__main__":
	main()
