def main():
    x, y = to_int(input().split())

    while x != 0 and y != 0:
        if y > 0:
            if x > 0:
                quadrante = "primeiro"

            else:
                quadrante = "segundo"

        else:
            if x > 0:
                quadrante = "quarto"

            else:
                quadrante = "terceiro"

        print(quadrante)

        x, y = to_int(input().split())


def to_int(c):
    return [int(i) for i in c]


if __name__ == "__main__":
    main()
