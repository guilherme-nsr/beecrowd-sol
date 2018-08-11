def main():
    eof = False

    while not eof:
        try:
            senha = input()

            qtd_uppercase = sum([int(char.isupper()) for char in senha])
            qtd_lowercase = sum([int(char.islower()) for char in senha])
            qtd_numeros = sum([int(char.isdecimal()) for char in senha])

            primeiro_requisito = qtd_uppercase >= 1 and qtd_lowercase >= 1 \
                and qtd_numeros >= 1

            segundo_requisito = senha.isalnum()
            terceiro_requisito = len(senha) >= 6 and len(senha) <= 32

            senha_valida = primeiro_requisito and segundo_requisito and \
                terceiro_requisito

            if senha_valida:
                print("Senha valida.")

            else:
                print("Senha invalida.")

        except EOFError:
            eof = True


if __name__ == "__main__":
    main()
