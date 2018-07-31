def main():
    input()
    numeros = to_int(input().split())

    multiplos = [0, 0, 0, 0]

    for i in range(len(numeros)):
        numero = numeros[i]

        for j in range(len(multiplos)):
            divisor = j+2

            multiplos[j] += int(numero % divisor == 0)

    print("\n".join(["%d Multiplo(s) de %d" % (quantidade, posicao+2)
          for posicao, quantidade in enumerate(multiplos)]))


def to_int(c):
    return [int(i) for i in c]


if __name__ == "__main__":
    main()
