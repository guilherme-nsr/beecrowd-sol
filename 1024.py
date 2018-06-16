def primeira_passada(texto):
    novo_texto = str()

    for char in texto:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            n = ord(char)
            novo_texto += chr(n+3)

        else:
            novo_texto += char

    return novo_texto


def segunda_passada(texto):
    return texto[::-1]


def terceira_passada(texto):
    metade = len(texto)//2
    primeira_metade = texto[:metade]
    segunda_metade = str()

    for char in texto[metade:]:
        n = ord(char)
        segunda_metade += chr(n-1)

    return primeira_metade+segunda_metade


def main():
    n = int(input())

    for i in range(n):
        texto = input()
        print(terceira_passada(segunda_passada(primeira_passada(texto))))


if __name__ == "__main__":
    main()
