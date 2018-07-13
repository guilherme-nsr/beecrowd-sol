def main():
    n = int(input())

    for i in range(n):
        x, y = to_int(input().split())

        try:
            print("%.1f" % (x/y))

        except ZeroDivisionError:
            print("divisao impossivel")


def to_int(c):
    return [int(i) for i in c]


if __name__ == "__main__":
    main()
