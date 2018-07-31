def main():
    n = input().strip()

    invertido = inverter(n)

    print(invertido)


def inverter(s):
    invertido = ''

    for i in range(len(s)-1, -1, -1):
        invertido += s[i]

    return invertido


if __name__ == "__main__":
    main()
