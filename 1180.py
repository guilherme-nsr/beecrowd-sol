def main():
    n = int(input())
    vetor = new_array(n)

    elementos = input().split()

    menor = int(elementos[0])
    posicao = 0

    for i in range(len(vetor)):
        vetor[i] = int(elementos[i])
        if vetor[i] < menor:
            menor = vetor[i]
            posicao = i

    print("Menor valor: %d" % (menor))
    print("Posicao: %d" % (posicao))


def new_array(n, default=None):
    """ Retorna uma lista com 'n' posições com o valor 'default'."""
    return [default]*n


if __name__ == "__main__":
    main()
