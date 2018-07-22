def main():
    qt = int(input())

    for i in range(qt):
        jogadores = input().split()

        jogador1 = jogadores[0]
        j1 = jogadores[1]

        jogador2 = jogadores[2]
        j2 = jogadores[3]

        numeros = input().split()

        n1 = int(numeros[0])
        n2 = int(numeros[1])

        if (n1+n2) % 2 == 0:
            if j1 == 'PAR':
                print(jogador1)

            else:
                print(jogador2)

        else:
            if j1 == 'IMPAR':
                print(jogador1)

            else:
                print(jogador2)


if __name__ == "__main__":
    main()
