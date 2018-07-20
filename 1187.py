def main():
    t = input()

    resultado = 0
    a = 0
    b = 11

    for i in range(12):
        for j in range(12):
            e = float(input())
            if j > a and j < b:
                resultado += e

        a += 1
        b -= 1

    d = 1 if t == 'S' else 30

    resultado /= d

    print("%.1f" % (resultado))


if __name__ == "__main__":
    main()
