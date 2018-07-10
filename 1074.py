def main():
    n = int(input())

    for i in range(n):
        numero = int(input())

        saida = ''

        if numero == 0:
            saida = "NULL"

        else:
            if numero % 2 == 0:
                saida = "EVEN "

            else:
                saida = "ODD "

            if numero > 0:
                saida += "POSITIVE"

            else:
                saida += "NEGATIVE"

        print(saida)


if __name__ == "__main__":
    main()
