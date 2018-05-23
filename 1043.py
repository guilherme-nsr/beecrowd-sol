def to_float(l):
    """Retorna uma lista com todos os seus elementos convertidos para
    o tipo float.
    """
    return [float(i) for i in l]


def is_triangulo(lado_a, lado_b, lado_c):
    """Retorna 'True' caso as medidas de lado formem um triângulo e
    'False' se não.
    """
    if lado_a >= (lado_b + lado_c):
        return False

    if lado_b >= (lado_a + lado_c):
        return False

    if lado_c >= (lado_a + lado_b):
        return False

    return True


def perimetro_triangulo(a, b, c):
    return a + b + c


def area_trapezio(a, b, c):
    return ((a + b) * c) / 2


def main():
    A, B, C = to_float(input().split())

    if is_triangulo(A, B, C):
        perimetro = perimetro_triangulo(A, B, C)
        print("Perimetro = %.1f" % (perimetro))

    else:
        area = area_trapezio(A, B, C)
        print("Area = %.1f" % (area))


if __name__ == "__main__":
    main()
