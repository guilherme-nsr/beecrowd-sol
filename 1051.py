def main():
    salario = float(input())

    if salario <= 2000:
        print("Isento")

        return

    faixa_28 = salario - 4500
    if faixa_28 < 0:
        faixa_28 = 0
    salario -= faixa_28

    faixa_18 = salario - 3000
    if faixa_18 < 0:
        faixa_18 = 0
    salario -= faixa_18

    faixa_8 = salario - 2000
    salario -= faixa_8

    imposto = faixa_28*0.28 + faixa_18*0.18 + faixa_8*0.08

    print("R$ %.2f" % (imposto))


if __name__ == "__main__":
    main()
