def main():
    while True:
        try:
            try:
                n = int(input())

                parafusos = []

                for i in range(n):
                    x, y = to_int(input().split())

                    for j in range(x, y+1):
                        parafusos.append(j)

                num = int(input())
                resultado_pesquisa = pesquisar_parafuso(parafusos, num)
                print(resultado_pesquisa)

            except ValueError:
                pass

        except EOFError:
            break


def to_int(c):
    return [int(i) for i in c]


def pesquisar_parafuso(parafusos, num):
    parafusos.sort()
    posicoes = []

    for i in range(len(parafusos)):
        parafuso = parafusos[i]

        if parafuso == num:
            posicoes.append(i)

    if len(posicoes) > 0:
        primeira = posicoes[0]
        ultima = posicoes[-1]
        mensagem = "%d found from %d to %d" % (num, primeira, ultima)

    else:
        mensagem = "%d not found" % (num)

    return mensagem


if __name__ == "__main__":
    main()
