def main():
    x = int(input())

    if x % 2 == 0:
        x += 1

    for i in range(6):
        print(x)

        x += 2


if __name__ == "__main__":
    main()
