def main():
    while True:
        try:
            m, n = to_int(input().split())

            print(fatorial(m)+fatorial(n))

        except EOFError:
            break


def to_int(c):
    return [int(i) for i in c]


def fatorial(n):
    f = 1

    if n == 0:
        return f

    else:
        for i in range(n-1):
            f *= n

            n -= 1

    return f


if __name__ == "__main__":
    main()
