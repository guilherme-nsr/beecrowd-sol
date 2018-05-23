def to_int(l):
    """Retorna uma lista com todos os seus elementos convertidos para
    o tipo inteiro.
    """
    return [int(i) for i in l]


def main():
    A, B, C, D = to_int(input().split())

    if B > C and D > A and C + D > A + B and C > 0 < D and A % 2 == 0:
        print("Valores aceitos")
    else:
        print("Valores nao aceitos")


if __name__ == "__main__":
    main()
