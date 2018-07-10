def main():
    menor = int(input())
    maior = int(input())

    if menor > maior:
        menor, maior = maior, menor

    print(sum([i for i in range(menor+1, maior) if i % 2 != 0]))


if __name__ == "__main__":
    main()
