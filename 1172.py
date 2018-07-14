def main():
    vetor = new_array(10)

    for i in range(10):
        vetor[i] = int(input())
        if vetor[i] <= 0:
            vetor[i] = 1

    print("\n".join(["X[%d] = %d" % (i, vetor[i]) for i in range(len(vetor))]))


def new_array(n, default=None):
    """ Retorna uma lista com 'n' posições com o valor 'default'."""
    return [default]*n


if __name__ == "__main__":
    main()
