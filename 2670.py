def main():
    a1 = int(input())
    a2 = int(input())
    a3 = int(input())

    menor = a2*2 + a3*4
    tempo2 = a1*2 + a3*2
    tempo3 = a1*4 + a2*2

    if (tempo2) < menor:
        menor = tempo2

    if (tempo3) < menor:
        menor = tempo3

    print(menor)


if __name__ == "__main__":
    main()
