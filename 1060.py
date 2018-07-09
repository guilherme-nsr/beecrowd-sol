def main():
    positivos = 0

    for i in range(6):
        numero = float(input())

        if numero > 0:
            positivos += 1

    print(positivos, "valores positivos")


if __name__ == "__main__":
    main()
