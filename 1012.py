def main():
    pi = 3.14159

    a, b, c = to_float(input())

    triangulo = (a*c) / 2
    circulo = pi * c**2
    trapezio = (a+b)*c / 2
    quadrado = b*b
    retangulo = a*b

    print("TRIANGULO: %.3f" % (triangulo))
    print("CIRCULO: %.3f" % (circulo))
    print("TRAPEZIO: %.3f" % (trapezio))
    print("QUADRADO: %.3f" % (quadrado))
    print("RETANGULO: %.3f" % (retangulo))


def to_float(c):
    return [float(i) for i in c.split()]


if __name__ == "__main__":
    main()
