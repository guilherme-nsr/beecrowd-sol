def main():
    s, t, f = to_int(input().split())

    if s == 0:
        s = 24

    print((s+t+f) % 24)


def to_int(c):
    return [int(i) for i in c]


if __name__ == "__main__":
    main()
