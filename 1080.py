def main():
    maior = int(input())
    posicao_maior = 1

    for i in range(99):
        valor = int(input())

        if valor > maior:
            maior = valor
            posicao_maior = i + 2

    print(maior)
    print(posicao_maior)


if __name__ == "__main__":
    main()
