def main():
    x = int(input())

    while x != 0:
        if x % 2 != 0:
            x += 1

        soma = sum(range(x, x+9, 2))

        print(soma)

        x = int(input())


if __name__ == "__main__":
    main()
