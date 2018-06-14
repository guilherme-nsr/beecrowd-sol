def main():
    senha = int(input())

    while senha != 2002:
        print("Senha Invalida")
        senha = int(input())

    print("Acesso Permitido")


if __name__ == "__main__":
    main()
