def main():
    n = int(input())

    maior_valor_da_matriz = 2 ** ((n-1)*2)
    t = len(str(maior_valor_da_matriz))

    a = 1

    while n != 0:
        for i in range(n):
            for j in range(n):
                texto = "{:>%d}" % (t)
                print(texto.format(a), end='')

                if j < n-1:
                    print(' ', end='')

                else:
                    print()

                a *= 2

            a = 2**(i+1)

        print()

        n = int(input())

        maior_valor_da_matriz = 2 ** ((n-1)*2)
        t = len(str(maior_valor_da_matriz))

        a = 1


if __name__ == "__main__":
    main()
