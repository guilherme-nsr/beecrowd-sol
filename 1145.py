def to_int(l):
    return [int(i) for i in l]


def main():
    x, y = to_int(input().split())

    numero = 1

    while numero <= y:
        for i in range(x):
            print(numero, end='')
            numero += 1
            if i != x-1:
                print(' ', end='')
        print()


if __name__ == "__main__":
    main()
