def main():
    while True:
        try:
            n = int(input())

            for i in range(n):
                input()
                print("I am Toorg!")

        except EOFError:
            break


if __name__ == "__main__":
    main()
