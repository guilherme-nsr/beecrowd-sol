def main():
    n = int(input())

    dentro = 0
    fora = 0

    for i in range(n):
        numero = int(input())

        if numero >= 10 and numero <= 20:
            dentro += 1

        else:
            fora += 1

    print(dentro, "in")
    print(fora, "out")


if __name__ == "__main__":
    main()
