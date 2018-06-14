def main():
    alcool = 0
    gasolina = 0
    diesel = 0

    while True:
        codigo = int(input())

        if not 1 <= codigo <= 4:
            while True:
                codigo = int(input())

                if 1 <= codigo <= 4:
                    break

        if codigo == 4:
            break

        if codigo == 1:
            alcool += 1

        elif codigo == 2:
            gasolina += 1

        else:
            diesel += 1

    print("MUITO OBRIGADO")
    print("Alcool: %d" % (alcool))
    print("Gasolina: %d" % (gasolina))
    print("Diesel: %d" % (diesel))


if __name__ == "__main__":
    main()
