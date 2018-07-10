def main():
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0

    for i in range(5):
        numero = int(input())

        if numero % 2 == 0:
            pares += 1

        else:
            impares += 1

        if numero > 0:
            positivos += 1

        elif numero < 0:
            negativos += 1

    print(pares, "valor(es) par(es)")
    print(impares, "valor(es) impar(es)")
    print(positivos, "valor(es) positivo(s)")
    print(negativos, "valor(es) negativo(s)")


if __name__ == "__main__":
    main()
