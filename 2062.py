def main():
    input()

    palavras = input().split()

    for i in range(len(palavras)):
        palavra = palavras[i]

        if len(palavra) == 3:
            if palavra.startswith("OB") or palavra.startswith("UR"):
                palavras[i] = palavra[:-1] + 'I'

    print(' '.join(palavras))


if __name__ == "__main__":
    main()
