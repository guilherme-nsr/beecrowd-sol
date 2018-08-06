def main():
    for i in range(int(input())):
        primeiro_digito, letra, segundo_digito = input()

        primeiro_digito = int(primeiro_digito)
        segundo_digito = int(segundo_digito)

        if primeiro_digito == segundo_digito:
            solucao = primeiro_digito * segundo_digito

        else:
            if eh_maiuscula(letra):
                solucao = segundo_digito - primeiro_digito

            else:
                solucao = primeiro_digito + segundo_digito

        print(solucao)


def eh_maiuscula(letra):
    return ord(letra) >= 65 and ord(letra) <= 90


if __name__ == "__main__":
    main()
