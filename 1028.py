def main():
    n = int(input())

    for i in range(n):
        f1, f2 = list(map(int, input().split()))

        tamanho_max = mdc(f1, f2)

        print(tamanho_max)


def mdc(a, b):
    while b != 0:
        resto = a % b
        a = b
        b = resto

    return a


if __name__ == "__main__":
    main()
