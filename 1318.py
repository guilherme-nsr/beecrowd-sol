def main():
    n, m = list(map(int, input().split()))

    while n != 0 or m != 0:
        bilhetes = input().split()

        falsos = 0
        verificados = []

        for i in range(len(bilhetes)):
            bilhete = bilhetes[i]

            if bilhete not in verificados:
                for j in range(i+1, len(bilhetes)):
                    if bilhetes[j] == bilhete:
                        falsos += 1
                        verificados.append(bilhete)
                        break

        print(falsos)

        n, m = list(map(int, input().split()))


if __name__ == "__main__":
    main()
