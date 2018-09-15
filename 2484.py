def main():
    eof = False
    while not eof:
        try:
            palavra = input()
            texto = palavra[:]

            for i in range(len(palavra)):
                print(' '*i, end='')

                texto = palavra[:len(palavra)-i]

                print(' '.join(texto))

            print()

        except EOFError:
            eof = True


if __name__ == "__main__":
    main()
