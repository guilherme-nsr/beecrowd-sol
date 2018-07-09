def main():
    unidades1, preco1 = convert_entrada(input())
    unidades2, preco2 = convert_entrada(input())

    total = preco1*unidades1 + preco2*unidades2

    print("VALOR A PAGAR: R$ %.2f" % (total))


def convert_entrada(entrada):
    return [int(entrada.split()[1]), float(entrada.split()[2])]


if __name__ == "__main__":
    main()
