def main():
    for i in range(int(input())):
        num_pessoas = int(input())

        idioma_nativo = input()

        tem_nao_nativo = False

        for j in range(num_pessoas-1):
            if input() != idioma_nativo:
                tem_nao_nativo = True

        if tem_nao_nativo:
            print("ingles")

        else:
            print(idioma_nativo)


if __name__ == "__main__":
    main()
