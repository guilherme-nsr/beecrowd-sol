def to_int(l):
    return [int(i) for i in l]


def main():
    n = int(input())

    soma = 0

    for i in range(n):
        x, y = to_int(input().split())

        if x > y:
            x, y = y, x

        for numero in range(x+1, y):
            if numero % 2 != 0:
                soma += numero

        print(soma)
        soma = 0


if __name__ == "__main__":
    main()
