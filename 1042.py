def to_int(l):
    """Retorna uma lista com todos os seus elementos convertidos para
    o tipo inteiro.
    """
    return [int(i) for i in l]


def print_ordem(numero_a, numero_b, numero_c):
    if numero_a <= numero_b <= numero_c:
        print("%d\n%d\n%d" % (numero_a, numero_b, numero_c))

    elif numero_a <= numero_c <= numero_b:
        print("%d\n%d\n%d" % (numero_a, numero_c, numero_b))

    elif numero_b <= numero_a <= numero_c:
        print("%d\n%d\n%d" % (numero_b, numero_a, numero_c))

    elif numero_b <= numero_c <= numero_a:
        print("%d\n%d\n%d" % (numero_b, numero_c, numero_a))

    elif numero_c <= numero_a <= numero_b:
        print("%d\n%d\n%d" % (numero_c, numero_a, numero_b))

    elif numero_c <= numero_b <= numero_a:
        print("%d\n%d\n%d" % (numero_c, numero_b, numero_a))


def main():
    numero_a, numero_b, numero_c = to_int(input().split())

    print_ordem(numero_a, numero_b, numero_c)

    print("\n%d\n%d\n%d" % (numero_a, numero_b, numero_c))


if __name__ == "__main__":
    main()
