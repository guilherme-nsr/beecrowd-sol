def to_int(l):
    return [int(i) for i in l]


def main():
    valores = to_int(input().split())
    a = valores.pop(0)

    for valor in valores:
        if valor > 0:
            n = valor
            break

    soma = 0

    for numero in range(n):
        soma += a + numero

    print(soma)


if __name__ == "__main__":
    main()
