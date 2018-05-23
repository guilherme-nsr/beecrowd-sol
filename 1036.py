import math


def to_float(l):
    """Retorna uma lista com todos os seus elementos convertidos para
    o tipo float.
    """
    return [float(i) for i in l]


def bhaskara(a, b, c):
    """Retorna uma tupla contendo as raízes reais da equação, ou 'None'
    caso elas não existam.
    """
    delta = b**2 - 4*a*c

    if a == 0 or delta < 0:
        return None

    else:
        raiz_delta = math.sqrt(delta)

        x1 = (-b + raiz_delta) / (2*a)
        x2 = (-b - raiz_delta) / (2*a)

        return x1, x2


def main():
    A, B, C = to_float(input().split())

    if bhaskara(A, B, C) is None:
        print("Impossivel calcular")
    else:
        x1, x2 = bhaskara(A, B, C)

        print("R1 = %.5f" % (x1))
        print("R2 = %.5f" % (x2))


if __name__ == "__main__":
    main()
