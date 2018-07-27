def main():
    n = int(input())

    while n != 0:
        matriz = nova_matriz(n, n)

        valor = 1
        inicio = 0
        fim = len(matriz)

        while inicio < fim:
            preencher_extremidades(inicio, fim, matriz, valor)

            valor += 1
            inicio += 1
            fim -= 1

        show_matriz(matriz)
        print()

        n = int(input())


def nova_matriz(m, n, d=0):
    """ Retorna uma lista bidimensional representando uma matriz de
    'm' linhas, 'n' colunas e com o elemento padrão 'd'.
    """
    return [[d]*n for i in range(m)]


def extremidade(i, j, inicio, fim):
    """ Retorna True se o elemento de uma submatriz quadrada localizado
    na linha 'i' e na coluna 'j' está em uma de suas extremidades.

    'inicio' e 'fim' representam, respectivamente, os primeiros e os
    últimos índices da submatriz (linha e coluna) em relação à matriz
    principal.
    """
    return i == inicio or i == fim-1 or j == inicio or j == fim-1


def preencher_extremidades(inicio, fim, matriz, valor):
    """ Preenche as extremidades de uma submatriz com o valor fornecido.

    'inicio' e 'fim' representam, respectivamente, os primeiros e os
    últimos índices da submatriz (linha e coluna) em relação à matriz
    principal.
    """
    for i in range(inicio, fim):
        linha = matriz[i]

        for j in range(inicio, fim):
            if extremidade(i, j, inicio, fim):
                linha[j] = valor


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
