def main():
    i = 1
    j = 7

    while i <= 9:
        for c in range(3):
            print("I=%d J=%d" % (i, j))

            j -= 1

        j = 7
        i += 2


if __name__ == "__main__":
    main()
