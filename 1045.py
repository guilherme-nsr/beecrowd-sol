def to_float(l):
    """Retorna uma lista com todos os seus elementos convertidos para
    o tipo float.
    """
    return [float(i) for i in l]


def descending(numero_a, numero_b, numero_c):
    """Retorna uma tupla com os valores em ordem decrescente"""
    if numero_a >= numero_b >= numero_c:
        return numero_a, numero_b, numero_c

    elif numero_a >= numero_c >= numero_b:
        return numero_a, numero_c, numero_b

    elif numero_b >= numero_a >= numero_c:
        return numero_b, numero_a, numero_c

    elif numero_b >= numero_c >= numero_a:
        return numero_b, numero_c, numero_a

    elif numero_c >= numero_a >= numero_b:
        return numero_c, numero_a, numero_b

    elif numero_c >= numero_b >= numero_a:
        return numero_c, numero_b, numero_a


def is_triangulo(a, b, c):
    return False if a >= b + c else True


def is_retangulo(a, b, c):
    return True if a**2 == b**2 + c**2 else False


def is_obtusangulo(a, b, c):
    return True if a**2 > b**2 + c**2 else False


def is_acutangulo(a, b, c):
    return True if a**2 < b**2 + c**2 else False


def is_equilatero(a, b, c):
    return True if a == b == c else False


def is_isosceles(a, b, c):
    return True if a == b or a == c or b == c else False


def main():
    A, B, C = to_float(input().split())

    A, B, C = descending(A, B, C)

    if is_triangulo(A, B, C):
        if is_retangulo(A, B, C):
            print("TRIANGULO RETANGULO")

        elif is_obtusangulo(A, B, C):
            print("TRIANGULO OBTUSANGULO")

        elif is_acutangulo(A, B, C):
            print("TRIANGULO ACUTANGULO")

        if is_equilatero(A, B, C):
            print("TRIANGULO EQUILATERO")

        elif is_isosceles(A, B, C):
            print("TRIANGULO ISOSCELES")
    else:
        print("NAO FORMA TRIANGULO")


if __name__ == "__main__":
    main()
