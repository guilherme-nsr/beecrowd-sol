def main():
    p, r = list(map(int, input().split()))

    if p == 0:
        destino = 'C'

    else:
        if r == 0:
            destino = 'B'

        else:
            destino = 'A'

    print(destino)


if __name__ == "__main__":
    main()
