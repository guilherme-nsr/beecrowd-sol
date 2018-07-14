def main():
    x = float(input())
    vetor = new_array(100)

    for i in range(len(vetor)):
        vetor[i] = "%.4f" % (x)
        x /= 2

    print("\n".join(["N[%d] = %s" % (i, vetor[i]) for i in range(len(vetor))]))


def new_array(n, default=None):
    """ Retorna uma lista com 'n' posições com o valor 'default'."""
    return [default]*n


if __name__ == "__main__":
    main()
