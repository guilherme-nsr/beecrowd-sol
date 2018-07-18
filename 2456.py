def main():
    cartas = to_int(input().split())

    if is_crescente(cartas):
        print('C')

    elif is_decrescente(cartas):
        print('D')

    else:
        print('N')


def to_int(c):
    return [int(i) for i in c]


def is_crescente(c):
    for i in range(len(c)-1):
        elemento = c[i]
        prox_elemento = c[i+1]

        if elemento > prox_elemento:
            return False

    return True


def is_decrescente(c):
    for i in range(len(c)-1):
        elemento = c[i]
        prox_elemento = c[i+1]

        if elemento < prox_elemento:
            return False

    return True


if __name__ == "__main__":
    main()
