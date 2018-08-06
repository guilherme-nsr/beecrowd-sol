def main():
    for i in range(int(input())):
        m, n = map(int, input().split())

        dicionario = [(input(), input()) for i in range(m)]
        texto = [input() for i in range(n)]

        traduzir_texto(texto, dicionario)

        print("\n".join(texto))
        print()


def traduzir_frase(frase, dicionario):
    palavras = frase.split()

    for i in range(len(palavras)):
        palavra = palavras[i]

        for j in range(len(dicionario)):
            chave, valor = dicionario[j]

            if palavra == chave:
                palavras[i] = valor

    return ' '.join(palavras)


def traduzir_texto(texto, dicionario):
    for i in range(len(texto)):
        linha = texto[i]

        for j in range(len(dicionario)):
            chave, valor = dicionario[j]

            if chave in linha:
                texto[i] = traduzir_frase(texto[i], dicionario)
                break


if __name__ == "__main__":
    main()
