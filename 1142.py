def main():
    n = int(input())

    w = 1

    for i in range(n):
        for c in range(3):
            print(w+c, end = ' ')
        print("PUM")

        w += 4


if __name__ == "__main__":
    main()
