def main():
    t = int(input())

    for i in range(t):
        n = int(input())

        fibonacci = new_array(n+1)

        a, b = 0, 1

        for i in range(n+1):
            fibonacci[i] = a
            a, b = b, a+b

        print("Fib(%d) = %d" % (n, fibonacci[-1]))


def new_array(n, default=None):
    """ Retorna uma lista com 'n' posições com o valor 'default'."""
    return [default]*n


if __name__ == "__main__":
    main()
