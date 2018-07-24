def main():
    while True:
        try:
            input()

            velocidades = to_int(input().split())

            mais_veloz = velocidades[0]

            for i in range(1, len(velocidades)):
                if velocidades[i] > mais_veloz:
                    mais_veloz = velocidades[i]

            nivel = 1

            if mais_veloz >= 10 and mais_veloz < 20:
                nivel = 2

            elif mais_veloz >= 20:
                nivel = 3

            print(nivel)

        except EOFError:
            break


def to_int(c):
    return [int(i) for i in c]


if __name__ == "__main__":
    main()
