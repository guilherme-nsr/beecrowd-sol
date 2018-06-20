def main():
    n = int(input())

    for i in range(n):
        texto = input()

        palavras = texto.split()

        if len(palavras) == 0:
            mensagem_oculta = ""

        else:
            mensagem_oculta = str()

            for i in range(len(palavras)):
                palavra = palavras[i]

                primeira_letra = palavra[0]

                mensagem_oculta += primeira_letra

        print(mensagem_oculta)


if __name__ == "__main__":
    main()
