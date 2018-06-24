def main():
    times = 0

    while True:
        n = int(input())

        if n == 0:
            break

        if times >= 1:
            print()

        entradas = []

        for i in range(n):
            entradas.append(input())

        linhas = []

        for i in range(len(entradas)):
            entrada = entradas[i]

            linhas.append(' '.join(entrada.split()))

        tamanho_maior = len(linhas[0])

        for i in range(len(linhas)):
            linha = linhas[i]

            if len(linha) > tamanho_maior:
                tamanho_maior = len(linha)

        for i in range(len(linhas)):
            linha = linhas[i]
            espacos = tamanho_maior-len(linha)
            print(' '*espacos, linha, sep='')

        times += 1


if __name__ == "__main__":
    main()
