def main():
    pomekons = []

    for i in range(int(input())):
        pomekons.append(input())

    conjunto(pomekons)

    pomekons_nao_capturados = 151 - len(pomekons)

    print("Falta(m) %d pomekon(s)." % (pomekons_nao_capturados))


def conjunto(lista):
    """ Retorna uma lista com os elementos únicos de 'lista'."""
    aux = []

    for elemento in list(lista):
        elemento_repetido = elemento in aux

        if elemento_repetido:
            lista.remove(elemento)

        aux.append(elemento)


if __name__ == "__main__":
    main()
