def get_cidade(ddd):
    if ddd == 61:
        return "Brasilia"

    if ddd == 71:
        return "Salvador"

    if ddd == 11:
        return "Sao Paulo"

    if ddd == 21:
        return "Rio de Janeiro"

    if ddd == 32:
        return "Juiz de Fora"

    if ddd == 19:
        return "Campinas"

    if ddd == 27:
        return "Vitoria"

    if ddd == 31:
        return "Belo Horizonte"


def main():
    ddd = int(input())

    cidade = get_cidade(ddd)

    if cidade is not None:
        print(cidade)
    else:
        print("DDD nao cadastrado")


if __name__ == "__main__":
    main()
