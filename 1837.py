def main():
    a, b = input().split()

    a = int(a)
    b = int(b)

    q, r = divisao(a, b)

    print(q, r)


def modulo(n):
    return -n if n < 0 else n


def divisao(a, b):
    aux = modulo(a)

    for i in range(modulo(b)):
        for j in range(-aux, aux+1):
            r = i
            q = j

            if b*q + r == a:
                return q, r


if __name__ == "__main__":
    main()
