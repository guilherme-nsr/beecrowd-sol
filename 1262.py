def main():
    while True:
        try:
            rastro = input()
            p = int(input())
            ciclos = 0

            for i in range(len(rastro)):
                x = rastro[i]

                if x == 'W':
                    ciclos += 1

            leituras = remove_vazio(rastro.split('W'))

            for i in range(len(leituras)):
                leitura = leituras[i]

                if len(leitura) <= p:
                    ciclos += 1

                else:
                    ciclos += len(leitura)//p

                    if len(leitura) % p != 0:
                        ciclos += 1

            print(ciclos)

        except EOFError:
            break


def remove_vazio(c):
    return [i for i in c if i]


if __name__ == "__main__":
    main()
