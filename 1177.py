def main():
    t = int(input())
    vetor = new_array(1000)
    c = list(range(0, t))
    j = 0

    for i in range(len(vetor)):
        vetor[i] = c[j]
        j += 1
        if j > len(c)-1:
            j = 0

    print("\n".join(["N[%d] = %d" % (i, vetor[i]) for i in range(len(vetor))]))


def new_array(n, default=None):
    """ Retorna uma lista com 'n' posições com o valor 'default'."""
    return [default]*n


if __name__ == "__main__":
    main()
