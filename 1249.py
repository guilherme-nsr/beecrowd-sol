def rot13(mensagem):
    codificada = str()

    for char in mensagem:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            if 'a' <= char <= 'z':
                n = (ord(char) - ord('a') + 13) % 26
                char = chr(n + ord('a'))
                codificada += char

            else:
                n = (ord(char) - ord('A') + 13) % 26
                char = chr(n + ord('A'))
                codificada += char

        else:
            codificada += char

    return codificada


def main():
    while True:
        try:
            print(rot13(input()))

        except:
            break


if __name__ == "__main__":
    main()
