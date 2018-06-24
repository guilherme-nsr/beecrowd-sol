def main():
    n = int(input())

    for i in range(n):
        valor_a, valor_b = input().split()

        dif_a_b = len(valor_a)-len(valor_b)

        parte_a = ''

        for j in range(len(valor_a)):
            char = valor_a[j]

            if j >= dif_a_b:
                parte_a += char

        if parte_a == valor_b:
            saida = "encaixa"

        else:
            saida = "nao encaixa"

        print(saida)


if __name__ == "__main__":
    main()
