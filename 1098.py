def main():
    i = 0
    j = 1

    while i <= 2:
        for c in range(3):
            print("I=%g J=%g" % (i, j+i))

            j += 1

        j = 1
        i += 0.2


if __name__ == "__main__":
    main()
