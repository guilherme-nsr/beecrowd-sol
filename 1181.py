def main():
    m = nova_matriz(12, 12)

    l = int(input())
    t = input()

    resultado = 0

    for i in range(len(m)):
        linha = m[i]

        for j in range(len(linha)):
            linha[j] = float(input())
            if i == l:
                resultado += linha[j]

    d = 1 if t == 'S' else 12

    resultado /= d

    print("%.1f" % (resultado))


def nova_matriz(l, c, d=0):
    """ Retorna uma lista representando uma matriz de 'l' linhas,
    'c' colunas com o elemento padrão 'd'.
    """
    matriz = [None]*l

    for i in range(l):
        matriz[i] = [d]*c

    return matriz


if __name__ == "__main__":
    main()
