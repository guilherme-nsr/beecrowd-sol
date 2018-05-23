def to_int(l):
    """Retorna uma lista com todos os seus elementos convertidos para
    o tipo inteiro.
    """
    return [int(i) for i in l]


def get_preco(codigo):
    if codigo == 1:
        return 4.0

    elif codigo == 2:
        return 4.5

    elif codigo == 3:
        return 5.0

    elif codigo == 4:
        return 2.0

    elif codigo == 5:
        return 1.5

    else:
        return None


def main():
    codigo, quantidade = to_int(input().split())

    preco = get_preco(codigo)

    total = quantidade*preco

    print("Total: R$ %.2f" % (total))


if __name__ == "__main__":
    main()
