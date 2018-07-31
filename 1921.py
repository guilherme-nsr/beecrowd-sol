def main():
    n = int(input())

    barbantes = diagonais(n)

    print(barbantes)


def diagonais(n):
    """ Retorna o número de diagonais de um polígono de 'n' lados."""
    return int(n * (n-3) / 2)


if __name__ == "__main__":
    main()
