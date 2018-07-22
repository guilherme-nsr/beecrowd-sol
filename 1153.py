def main():
    n = int(input())

    print(fatorial(n))


def fatorial(n):
    """ Retorna o fatorial de 'n'."""
    f = 1

    if n == 0:
        return f

    for i in range(n-1):
        f *= n

        n -= 1

    return f


if __name__ == "__main__":
    main()
