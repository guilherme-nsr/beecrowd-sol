def decode_cesar(codificado, chave):
    chave = -chave

    decodificado = str()

    for char in codificado:
        n = (ord(char) - ord('A') + chave) % 26
        char = chr(n + ord('A'))
        decodificado += char

    return decodificado


def main():
    n = int(input())

    for i in range(n):
        codificado = input()
        chave = int(input())

        decodificado = decode_cesar(codificado, chave)

        print(decodificado)


if __name__ == "__main__":
    main()
