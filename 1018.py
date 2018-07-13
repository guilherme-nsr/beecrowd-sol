def main():
    valor = int(input())

    valor_saida = valor

    cem = valor // 100
    resto = valor % 100
    valor = resto

    cinquenta = valor // 50
    resto = valor % 50
    valor = resto

    vinte = valor // 20
    resto = valor % 20
    valor = resto

    dez = valor // 10
    resto = valor % 10
    valor = resto

    cinco = valor // 5
    resto = valor % 5
    valor = resto

    dois = valor // 2
    resto = valor % 2
    valor = resto

    um = valor

    print(valor_saida)
    print("%d nota(s) de R$ 100,00" % (cem))
    print("%d nota(s) de R$ 50,00" % (cinquenta))
    print("%d nota(s) de R$ 20,00" % (vinte))
    print("%d nota(s) de R$ 10,00" % (dez))
    print("%d nota(s) de R$ 5,00" % (cinco))
    print("%d nota(s) de R$ 2,00" % (dois))
    print("%d nota(s) de R$ 1,00" % (um))


if __name__ == "__main__":
    main()
