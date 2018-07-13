def main():
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


if __name__ == "__main__":
    main()
