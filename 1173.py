def main():
    vetor = new_array(10)

    v = int(input())

    for i in range(len(vetor)):
        vetor[i] = v
        v*= 2

    print("\n".join(["N[%d] = %d" % (i, vetor[i]) for i in range(len(vetor))]))


def new_array(n, default=None):
    """ Retorna uma lista com 'n' posições com o valor 'default'."""
    return [default]*n


if __name__ == "__main__":
    main()
