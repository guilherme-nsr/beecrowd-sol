def main():
    d, n = to_int(input().split())

    while d != 0 or n != 0:
        valor_contrato = substituir(str(d), '', str(n))

        if valor_contrato == '':
            valor_contrato = '0'

        valor_contrato = int(valor_contrato)

        print(valor_contrato)

        d, n = to_int(input().split())


def to_int(c):
    return [int(i) for i in c]


def substituir(x, y, string):
    """ Retorna uma string com o caracter 'x' substituído pelo 'y' em
    'string'.
    """
    nova_string = ''

    for i in range(len(string)):
        char = string[i]

        if char == x:
            char = y

        nova_string += char

    return nova_string


if __name__ == "__main__":
    main()
