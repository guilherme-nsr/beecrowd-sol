def main():
    calcular = True
    while calcular:
        notas_validas = 0
        soma_notas = 0
        media_calculada = False

        while not media_calculada:
            nota = float(input())

            if nota >= 0 and nota <= 10:
                soma_notas += nota
                notas_validas += 1

            else:
                print("nota invalida")

            if notas_validas >= 2:
                media = soma_notas/2
                media_calculada = True

        print("media = %.2f" % (media))

        opcao_valida = False
        while not opcao_valida:
            opcao = int(input("novo calculo (1-sim 2-nao)"))
            print()

            if opcao == 1:
                opcao_valida = True

            elif opcao == 2:
                calcular = False
                opcao_valida = True


if __name__ == "__main__":
    main()
