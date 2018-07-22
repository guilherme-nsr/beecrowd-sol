def main():
    n = int(input())

    for i in range(n):
        x = int(input())

        if eh_primo(x):
            print(x, "eh primo")

        else:
            print(x, "nao eh primo")


def eh_primo(n):
    for i in range(n-1, 1, -1):
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    main()
