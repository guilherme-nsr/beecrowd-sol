def main():
    m, n = map(int, input().split())

    while m != 0 or n != 0:
        soma = str(m+n)

        soma = soma.replace('0', '')

        print(soma)

        m, n = map(int, input().split())


if __name__ == "__main__":
    main()
