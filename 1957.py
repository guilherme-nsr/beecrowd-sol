def main():
    v = int(input())

    hexadecimal = dec2hex(v)

    print(hexadecimal)


def inverter(s):
    invertida = ''

    for i in range(len(s)-1, -1, -1):
        invertida += s[i]

    return invertida


def dec2hex(decimal):
    hexadecimal = ''
    valor = decimal
    quociente_nulo = False

    while not quociente_nulo:
        quociente = valor // 16
        resto = valor % 16
        valor = quociente

        hex = str(resto)
        if resto > 9:
            hex = chr(ord('A') + (resto-10))

        hexadecimal += hex

        quociente_nulo = quociente == 0

    return inverter(hexadecimal)


if __name__ == "__main__":
    main()
