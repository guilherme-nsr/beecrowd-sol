def main():
    direcoes = ['N', 'L', 'S', 'O']

    n = int(input())

    while n != 0:
        posicao = 360

        comandos = input()

        for comando in comandos:
            if comando == 'D':
                posicao += 90

            else:
                posicao -= 90

            posicao %= 360

        p = abs(posicao) // 90

        print(direcoes[p])

        n = int(input())


if __name__ == "__main__":
    main()
