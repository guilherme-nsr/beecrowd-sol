def main():
    s = 0
    numerador = 1
    denominador = 1

    while numerador < 40:
        s += numerador/denominador

        numerador += 2
        denominador *= 2

    print("%.2f" % (s))


if __name__ == "__main__":
    main()
