def how_many_leds(valor):
    leds = {'1': 2,
            '2': 5,
            '3': 5,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 3,
            '8': 7,
            '9': 6,
            '0': 6}

    leds_num = 0

    for algarismo in valor:
        leds_num += leds[algarismo]

    return leds_num


def main():
    n = int(input())

    for i in range(n):
        valor = input()

        quant_leds = how_many_leds(valor)

        print("%d leds" % (quant_leds))


if __name__ == "__main__":
    main()
