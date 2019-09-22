def main():
	n = int(input())

	votos = [int(input()) for i in range(n)]

	print("S") if votos[0] == max(votos) else print("N")


if __name__ == "__main__":
	main()