def main():
    pares = 0

    for i in range(5):
        numero = int(input())

        if numero % 2 == 0:
            pares += 1

    print(pares, "valores pares")


if __name__ == "__main__":
    main()
