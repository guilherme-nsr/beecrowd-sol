import math

def main():
    entrada = input()

    while entrada != '0':
        a, b, c = to_int(entrada.split())

        print(int(math.sqrt(a*b * (100/c))))

        entrada = input()


def to_int(c):
    return [int(i) for i in c]


if __name__ == "__main__":
    main()
