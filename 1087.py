def main():
    x1, y1, x2, y2 = to_int(input().split())

    while x1 != 0 or y1 != 0 or x2 != 0 or y2 != 0:
        if x1 == x2 and y1 == y2:
            movimentos = 0

        elif (x1 == x2 or y1 == y2) or (modulo(x1, x2) == modulo(y1, y2)):
            movimentos = 1

        else:
            movimentos = 2

        print(movimentos)

        x1, y1, x2, y2 = to_int(input().split())


def to_int(c):
    return [int(i) for i in c]


def modulo(a, b):
    return b-a if a < b else a-b


if __name__ == "__main__":
    main()
