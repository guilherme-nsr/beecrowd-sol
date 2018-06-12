def main():
    n = int(input())

    for i in range(10):
        tabuada = i + 1

        print("%d x %d = %d" % (tabuada, n, tabuada*n))


if __name__ == "__main__":
    main()
