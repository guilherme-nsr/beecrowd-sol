def main():
	n = int(input())

	comitiva = {'X': 0, 'H': 0, 'E': 0, 'A': 0, 'M': 0}

	for i in range(n):
		raca_membro = input().split()[1]

		comitiva[raca_membro] += 1

	print("%d Hobbit(s)" % comitiva['X'])
	print("%d Humano(s)" % comitiva['H'])
	print("%d Elfo(s)" % comitiva['E'])
	print("%d Anao(s)" % comitiva['A'])
	print("%d Mago(s)" % comitiva['M'])


if __name__ == "__main__":
	main()