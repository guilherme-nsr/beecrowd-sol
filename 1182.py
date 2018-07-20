def main():
    c = int(input())
    t = input()

    resultado = 0

    for i in range(12):
        for j in range(12):
            e = float(input())
            if j == c:
                resultado += e

    d = 1 if t == 'S' else 12

    resultado /= d

    print("%.1f" % (resultado))


if __name__ == "__main__":
    main()
