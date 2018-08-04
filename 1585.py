def main():
    while True:
        try:
            for i in range(int(input())):
                x, y = list(map(int, input().split()))

                print(int(x*y / 2), "cm2")

        except EOFError:
            break


if __name__ == "__main__":
    main()
