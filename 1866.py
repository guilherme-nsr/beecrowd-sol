def main():
    c = int(input())

    for i in range(c):
        print(0) if int(input()) % 2 == 0 else print(1)


if __name__ == "__main__":
    main()
