def main():
    eof = False

    while not eof:
        try:
            print("\n".join(sorted([input() for i in range(int(input()))])))

        except EOFError:
            eof = True


if __name__ == "__main__":
    main()
