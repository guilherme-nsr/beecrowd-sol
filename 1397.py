def main():
    n = int(input())

    while n != 0:
        pontos_a, pontos_b = 0, 0

        for i in range(n):
            a, b = list(map(int, input().split()))

            pontos_a += int(a > b)
            pontos_b += int(b > a)

        print(pontos_a, pontos_b)

        n = int(input())


if __name__ == "__main__":
    main()
