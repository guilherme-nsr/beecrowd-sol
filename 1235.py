def main():
    n = int(input())

    for i in range(n):
        texto = input()

        metade_tamanho = int(len(texto)/2)

        primeira_metade = texto[:metade_tamanho]
        segunda_metade = texto[metade_tamanho:]

        frase_decifrada = primeira_metade[::-1] + segunda_metade[::-1]

        print(frase_decifrada)


if __name__ == "__main__":
    main()
