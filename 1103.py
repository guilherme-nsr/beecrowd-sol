def main():
    h1, m1, h2, m2 = list(map(int, input().split()))

    while h1 != 0 or m1 != 0 or h2 != 0 or m2 != 0:
        acorda_dia_seguinte = h2 < h1 or (h2 == h1 and m2 <= m1)

        if acorda_dia_seguinte:
            h2 += 24

        minutos = (h2-h1) * 60 + (m2-m1)

        print(minutos)

        h1, m1, h2, m2 = list(map(int, input().split()))


if __name__ == "__main__":
    main()
