def to_float(l):
    """Retorna uma lista com todos os seus elementos convertidos para
    o tipo float.
    """
    return [float(i) for i in l]


def get_quadrante(x, y):
    """Retorna um valor inteiro representando o quadrante. Retorna 0
    para a origem, -1 para o eixo X e -2 para o eixo Y.
    """
    if x == y == 0:
        return 0

    elif x == 0:
        return -2

    elif y == 0:
        return -1

    elif x > 0 and y > 0:
        return 1

    elif x < 0 and y > 0:
        return 2

    elif x < 0 and y < 0:
        return 3

    elif x > 0 and y < 0:
        return 4


def main():
    x, y = to_float(input().split())

    quadrante = get_quadrante(x, y)

    if quadrante == 0:
        print("Origem")

    elif quadrante == -1:
        print("Eixo X")

    elif quadrante == -2:
        print("Eixo Y")

    else:
        print("Q%d" % (quadrante))


if __name__ == "__main__":
    main()
