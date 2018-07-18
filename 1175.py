def main():
    n = [None]*20

    for i in range(20):
        n[i] = int(input())

    n = inverter(n)

    mostrar_vetor(n, "N")


def inverter(c):
    r = [None]*len(c)

    for i in range(len(c)):
        r[i] = c[-1-i]

    return r


def mostrar_vetor(c, m):
    """ 'm' é a string que indentifica o vetor no texto exibido."""
    print("\n".join(["%s[%d] = %d" % (m, i, c[i]) for i in range(len(c))]))


if __name__ == "__main__":
    main()
