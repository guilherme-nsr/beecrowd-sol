def main():
    n = int(input())

    for base in range(1, n+1):
        for expoente in range(1, 4):
            print(base**expoente, end='')
            if expoente != 3:  # Evitando um Presentation Error
                print(' ', end='')
        print()


if __name__ == "__main__":
    main()
