def main():
    t = input()

    resultado = 0
    a = 4
    b = 7

    for i in range(12):
        for j in range(12):
            e = float(input())
            if i > 6 and j > a and j < b:
                resultado += e

        if i > 6:
            a -= 1
            b += 1

    d = 1 if t == 'S' else 30

    resultado /= d

    print("%.1f" % (resultado))


if __name__ == "__main__":
    main()
