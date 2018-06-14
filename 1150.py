def main():
    x = int(input())
    z = int(input())

    while z <= x:
        z = int(input())

    somatorio = 0
    valores = 0

    for i in range(x, z):
        somatorio += i
        valores += 1
        if somatorio >= z:
            break

    print(valores)


if __name__ == "__main__":
    main()
