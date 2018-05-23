def to_int(l):
    """Retorna uma lista com todos os seus elementos convertidos para
    o tipo inteiro.
    """
    return [int(i) for i in l]


def are_multiplos(a, b):
    return True if a % b == 0 or b % a == 0 else False


def main():
    A, B = to_int(input().split())

    multiplos = are_multiplos(A, B)

    if multiplos:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")


if __name__ == "__main__":
    main()
