def main():
    t = input()

    resultado = 0

    for i in range(12):
        for j in range(12):
            e = float(input())
            if j > i:
                resultado += e

    d = 1 if t == 'S' else 66

    resultado /= d

    print("%.1f" % (resultado))


if __name__ == "__main__":
    main()
