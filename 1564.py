def main():
    while True:
        try:
            n = input()

            if n == '0':
                print("vai ter copa!")

            else:
                print("vai ter duas!")

        except EOFError:
            break


if __name__ == "__main__":
    main()
