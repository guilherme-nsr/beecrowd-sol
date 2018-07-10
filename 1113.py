def main():
    x, y = to_int(input().split())

    while x != y:
        if x > y:
            print("Decrescente")

        else:
            print("Crescente")

        x, y = to_int(input().split())


def to_int(c):
    return [int(i) for i in c]


if __name__ == "__main__":
    main()
