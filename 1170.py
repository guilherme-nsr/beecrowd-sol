def main():
    for i in range(int(input())):
        comida = float(input())

        dias = 0

        while comida > 1:
            comida -= 0.5*comida

            dias += 1

        print(dias, "dias")


if __name__ == "__main__":
    main()
