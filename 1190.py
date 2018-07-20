def main():
    t = input()

    resultado = 0
    a = 10

    for i in range(12):
        for j in range(12):
            e = float(input())

            if i > 0 and i < 11 and j > a:
                resultado += e

        if i > 0 and i < 11:
            if i < 5:
                a -= 1

            elif i < 6:
                pass

            else:
                a += 1

    d = 1 if t == 'S' else 30

    resultado /= d

    print("%.1f" % (resultado))


if __name__ == "__main__":
    main()
