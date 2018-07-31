def main():
    n = int(input())

    for i in range(n):
        palavra = input()

        valor_numerico = obter_numero(palavra)

        print(valor_numerico)


def obter_erros(a, b):
    """ Retorna o número de letras erradas na palavra 'b', tomando
    a palavra 'a' como correta.
    """
    erros = 0

    for i in range(len(a)):
        if b[i] != a[i]:
            erros += 1

    return erros


def obter_numero(p):
    if len(p) == 5:
        return 3

    if obter_erros("one", p) <= 1:
        return 1

    return 2


if __name__ == "__main__":
    main()
