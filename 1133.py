def main():
    x = int(input())
    y = int(input())

    if x > y:
        x, y = y, x

    for i in range(x+1, y):
        numero = i

        if numero % 5 == 2 or numero % 5 == 3:
            print(numero)


if __name__ == "__main__":
    main()
