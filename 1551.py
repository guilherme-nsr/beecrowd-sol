def main():
    n = int(input())

    for i in range(n):
        frase = input()

        letras_usadas = contar_letras(frase)

        if letras_usadas == 26:
            classificacao = "completa"

        elif letras_usadas >= 13:
            classificacao = "quase completa"

        else:
            classificacao = "mal elaborada"

        print("frase", classificacao)


def eh_letra(char):
    char = char.lower()

    return char >= 'a' and char <= 'z'


def contar_letras(frase):
    contagem = [False]*26

    for i in range(len(frase)):
        char = frase[i]

        if eh_letra(char):
            contagem[ord(char)-97] = True

    return sum([int(informacao) for informacao in contagem])


if __name__ == "__main__":
    main()
