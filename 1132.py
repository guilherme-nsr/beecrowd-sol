def main():
    x = int(input())
    y = int(input())
    soma = 0

    if x > y:
        x, y = y, x

    for numero in range(x, y+1):
        if numero % 13 != 0:
            soma += numero

    print(soma)


if __name__ == "__main__":
    main()
