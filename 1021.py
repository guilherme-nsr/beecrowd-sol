def main():
    valor = float(input())

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

    moeda_um_real = valor // 1
    resto = valor % 1
    valor = resto

    moeda_cinquenta = valor // 0.5
    resto = valor % 0.5
    valor = resto

    moeda_vinte_e_cinco = valor // 0.25
    resto = valor % 0.25
    valor = round(resto, 2)

    moeda_dez = valor // 0.1
    resto = valor % 0.1
    valor = resto

    moeda_cinco = valor // 0.05
    resto = valor % 0.05
    valor = round(resto, 2)

    moeda_um = valor / 0.01

    print("NOTAS:")
    print("%d nota(s) de R$ 100.00" % (cem))
    print("%d nota(s) de R$ 50.00" % (cinquenta))
    print("%d nota(s) de R$ 20.00" % (vinte))
    print("%d nota(s) de R$ 10.00" % (dez))
    print("%d nota(s) de R$ 5.00" % (cinco))
    print("%d nota(s) de R$ 2.00" % (dois))

    print("MOEDAS:")
    print("%d moeda(s) de R$ 1.00" % (moeda_um_real))
    print("%d moeda(s) de R$ 0.50" % (moeda_cinquenta))
    print("%d moeda(s) de R$ 0.25" % (moeda_vinte_e_cinco))
    print("%d moeda(s) de R$ 0.10" % (moeda_dez))
    print("%d moeda(s) de R$ 0.05" % (moeda_cinco))
    print("%d moeda(s) de R$ 0.01" % (moeda_um))


if __name__ == "__main__":
    main()
