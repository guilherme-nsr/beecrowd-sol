def main():
    n = int(input())

    while n != 0:
        matriz = nova_matriz(n, n)

        preencher_primeira_coluna(matriz)
        preencher_linhas(matriz)

        show_matriz(matriz)
        print()

        n = int(input())


def nova_matriz(m, n, d=0):
    """ Retorna uma lista bidimensional representando uma matriz de
    'm' linhas, 'n' colunas e com o elemento padrão 'd'.
    """
    return [[d]*n for i in range(m)]


def preencher_primeira_coluna(matriz):
    """ Preenche a primeira coluna da matriz com valores inteiros
    crescentes a partir de 1.
    """
    x = 1

    for i in range(len(matriz)):
        linha = matriz[i]

        linha[0] = x

        x += 1


def preencher_linhas(matriz):
    """ Preenche a matriz com os elementos restantes das linhas."""
    for i in range(len(matriz)):
        linha = matriz[i]
        ja_foi_um = False

        for j in range(1, len(matriz)):
            elemento = linha[j-1]

            if elemento == 1:
                ja_foi_um = True

            if not ja_foi_um:
                elemento -= 1

            else:
                elemento += 1

            linha[j] = elemento


def show_matriz(matriz):
    for i in range(len(matriz)):
        linha = matriz[i]
        primeiro_elemento = linha[0]

        print("{:>3}".format(primeiro_elemento), end='')

        for j in range(1, len(linha)):
            elemento = linha[j]

            print("{:>4}".format(elemento), end='')

        print()


if __name__ == "__main__":
    main()
