def main():
    while True:
        x = int(input())

        if x == 0:
            break

        for numero in range(1, x+1):
            print(numero, end='')
            if numero != x:
                print(' ', end='')
        print()


if __name__ == "__main__":
    main()
