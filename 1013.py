def main():
    a, b, c = to_int(input())

    maior_ab = (a + b + abs(a-b)) / 2
    maior_abc = (maior_ab + c + abs(maior_ab-c)) / 2

    print("%d eh o maior" % (maior_abc))


def to_int(c):
    return [int(i) for i in c.split()]


if __name__ == "__main__":
    main()
