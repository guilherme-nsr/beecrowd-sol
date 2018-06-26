def main():
    n = int(input())

    for i in range(n):
        l = int(input())

        hash = 0

        for j in range(l):
            entrada = input()

            a = 0
            e = 0
            p = 0

            for k in range(len(entrada)):
                char = entrada[k]

                a += ord(char) - 65  # Posição no alfabeto
                e += j  # Elemento de entrada
                p += k  # Posição do elemento

            hash += a + e + p

        print(hash)


if __name__ == "__main__":
    main()
