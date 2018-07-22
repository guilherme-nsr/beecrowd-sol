def main():
    idade = int(input())

    soma_idades = 0
    valores_lidos = 0

    while idade > -1:
        soma_idades += idade
        valores_lidos += 1

        idade = int(input())

    print("%.2f" % (soma_idades/valores_lidos))


if __name__ == "__main__":
    main()
