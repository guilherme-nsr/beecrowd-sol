def main():
    n = int(input())

    romano = dec2roman(n)

    print(romano)


def dec2roman(decimal):
    decimals = (900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    romans = ('CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    roman = ''

    for i in range(len(decimals)):
        c = decimal // decimals[i]
        roman += romans[i]*c
        decimal -= decimals[i]*c

    return roman


if __name__ == "__main__":
    main()
