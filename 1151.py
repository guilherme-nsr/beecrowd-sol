def main():
    n = int(input())

    print_fibonacci(n)


def print_fibonacci(n):
    """ Exibe os 'n' primeiros termos da sequência de Fibonacci."""
    a, b = 0, 1

    for i in range(n):
        print(a, end='')

        if i < n-1:
            print(' ', end='')

        else:
            print()

        a, b = b, a+b


if __name__ == "__main__":
    main()
