def main():
    times = 0

    while True:
        n = int(input())
        if n == 0:
            break

        if times >= 1:
            print()

        palavras = []

        palavra = input()
        palavras.append(palavra)
        maior = len(palavra)

        for i in range(n-1):
            palavra = input()
            palavras.append(palavra)

            if len(palavra) > maior:
                maior = len(palavra)

        for palavra in palavras:
            espacos = maior - len(palavra)
            print("%s%s" % (espacos*' ', palavra))

        times += 1


if __name__ == "__main__":
    main()
