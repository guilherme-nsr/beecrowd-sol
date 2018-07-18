def main():
    par = []
    impar = []

    for i in range(15):
        numero = int(input())

        if numero % 2 == 0:
            par = acrescentar(par, numero)

        else:
            impar = acrescentar(impar, numero)

        if len(par) >= 5:
            mostrar_vetor(par, "par")
            par = []

        if len(impar) >= 5:
            mostrar_vetor(impar, "impar")
            impar = []

    mostrar_vetor(impar, "impar")
    mostrar_vetor(par, "par")


def acrescentar(c, e):
    """ Retorna uma lista composta pelos elementos do conjunto 'c'
    seguidos do elemento 'e'.
    """
    new_c = [None]*(len(c)+1)

    for i in range(len(c)):
        new_c[i] = c[i]

    new_c[-1] = e

    return new_c


def mostrar_vetor(c, m):
    """ 'm' é a string que indentifica o vetor no texto exibido."""
    print("\n".join(["%s[%d] = %d" % (m, i, c[i]) for i in range(len(c))]))


if __name__ == "__main__":
    main()
