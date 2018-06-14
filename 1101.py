def to_int(l):
    return [int(i) for i in l]


def main():
    m, n = to_int(input().split())
    soma = 0

    while m > 0 and n > 0:
        if m > n:
            m, n = n, m

        for numero in range(m, n+1):
            soma += numero
            print(numero, end=' ')

        print("Sum=%d" % (soma))
        soma = 0

        m, n = to_int(input().split())


if __name__ == "__main__":
    main()
