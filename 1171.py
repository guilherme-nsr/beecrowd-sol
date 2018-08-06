def main():
    numeros = [None]*int(input())

    for i in range(len(numeros)):
        numeros[i] = int(input())

    numeros.sort()

    frequencia = 1

    for i in range(len(numeros)):
        numero = numeros[i]
        nao_eh_o_ultimo = i < len(numeros)-1

        if nao_eh_o_ultimo:
            prox_numero = numeros[i+1]

            if prox_numero != numero:
                print("%d aparece %d vez(es)" % (numero, frequencia))
                frequencia = 0

            frequencia += 1

        else:
            numero_anterior = numeros[i-1]

            if numero != numero_anterior:
                frequencia = 1

            print("%d aparece %d vez(es)" % (numero, frequencia))


if __name__ == "__main__":
    main()
