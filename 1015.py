def main():
    x1, y1 = to_float(input())
    x2, y2 = to_float(input())

    distancia = ((x2-x1)**2 + (y2-y1)**2)**0.5

    print("%.4f" % (distancia))


def to_float(c):
    return [float(i) for i in c.split()]


if __name__ == "__main__":
    main()
