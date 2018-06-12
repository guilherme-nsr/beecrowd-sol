def to_float(l):
    return [float(i) for i in l]


def main():
    n = int(input())

    for i in range(n):
        valores = to_float(input().split())
        n1, n2, n3 = valores

        media = (n1*2 + n2*3 + n3*5) / 10

        print("%.1f" % (media))


if __name__ == "__main__":
    main()
