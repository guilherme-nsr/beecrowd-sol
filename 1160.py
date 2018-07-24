def main():
    t = int(input())

    for i in range(t):
        entrada = input().split()

        pa, pb = int(entrada[0]), int(entrada[1])
        g1, g2 = float(entrada[2]), float(entrada[3])

        anos = 0

        while pa <= pb:
            pa += pa*(g1/100)
            pa = int(pa)

            pb += pb*(g2/100)
            pb = int(pb)

            anos += 1

            if anos > 100:
                break

        print(anos, "anos.") if anos <= 100 else print("Mais de 1 seculo.")


if __name__ == "__main__":
    main()
