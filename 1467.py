def main():
    while True:
        try:
            valores = list(map(int, input().split()))

            teve_vencedor = False

            for posicao, valor in enumerate(valores):
                if sum([int(valor == escolha) for escolha in valores]) == 1:
                    teve_vencedor = True
                    resultado = chr(posicao+ord('A'))
                    break

            if not teve_vencedor:
                resultado = '*'

            print(resultado)

        except EOFError:
            break


if __name__ == "__main__":
    main()
