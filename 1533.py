def main():
    n = int(input())

    while n != 0:
        suspeitos = list(map(int, input().split()))

        print(suspeitos.index(sorted(suspeitos)[-2]) + 1)

        n = int(input())


if __name__ == "__main__":
    main()
