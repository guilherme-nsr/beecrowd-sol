def main():
    while True:
        try:
            texto = input()

            aliteracoes = aliteracao(texto)
            print(aliteracoes)

        except EOFError:
            break


def aliteracao(texto):
    palavras = texto.split()

    aliteracoes = 0
    i = 0

    while i < len(palavras)-1:
        palavra = palavras[i]
        letra_anterior = palavra[0]
        letra_seguinte = palavras[i+1][0]
        x = palavras[i-1][0]

        if letra_anterior.lower() == letra_seguinte.lower() != x.lower():
            aliteracoes += 1

        i += 1

    return aliteracoes


if __name__ == "__main__":
    main()
