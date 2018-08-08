def main():
    risada = input()

    vogais = [letra for letra in risada if letra.lower() in 'aeiou']

    eh_das_mais_engracadas = vogais[::-1] == vogais

    print("S") if eh_das_mais_engracadas else print("N")


if __name__ == "__main__":
    main()
