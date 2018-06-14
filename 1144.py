def main():
    n = int(input())

    for base in range(1, n+1):
        for c in range(2):
            print(base, end = ' ')
            for expoente in range(2, 4):
                print(base**expoente + c, end='')
                if expoente != 3:  # Evitando um Presentation Error
                    print(' ', end='')
            print()


if __name__ == "__main__":
    main()
