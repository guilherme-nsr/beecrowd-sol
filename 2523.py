def main():
    eof = False

    while not eof:
        try:
            alfabeto = input()
            n = input()
            lampadas = list(map(int, input().split()))

            mensagem = ''.join([alfabeto[lampada-1] for lampada in lampadas])

            print(mensagem)

        except EOFError:
            eof = True


if __name__ == "__main__":
    main()
