def main():
    while True:
        try:
            print(int(input())-1)

        except EOFError:
            break


if __name__ == "__main__":
    main()
