def main():
    n = int(input())

    for i in range(n):
        x, y = to_int(input().split())

        if x % 2 == 0:
            x += 1

        soma = x

        ultimo_impar = x + (y-1)*2

        soma += sum([j for j in range(x+2, ultimo_impar+1, 2)])

        print(soma)


def to_int(c):
    return [int(i) for i in c]


if __name__ == "__main__":
    main()
