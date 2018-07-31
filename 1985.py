def main():
    p = int(input())

    total = 0

    for i in range(p):
        produto, quantidade = input().split()

        total += obter_valor(produto, int(quantidade))

    print("%.2f" % (total))


def obter_valor(produto, quantidade):
    return quantidade * (1.5 + (int(produto)-1001))


if __name__ == "__main__":
    main()
