def main():
    qtd_submissoes = int(input())

    while qtd_submissoes != 0:
        submissoes = [input() for i in range(qtd_submissoes)]

        problemas_corretos = get_problemas_corretos(submissoes)
        qtd_problemas_corretos = len(problemas_corretos)
        tempo = get_tempo(submissoes, problemas_corretos)

        print(qtd_problemas_corretos, tempo)

        qtd_submissoes = int(input())


def get_problemas_corretos(submissoes):
    problemas_corretos = []

    for submissao in submissoes:
        problema, tempo, julgamento = submissao.split()

        if julgamento == "correct":
            problemas_corretos.append(problema)

    return problemas_corretos


def get_tempo(submissoes, problemas_corretos):
    tempo_total = 0

    for submissao in submissoes:
        problema, tempo, julgamento = submissao.split()
        tempo = int(tempo)

        if problema in problemas_corretos:
            if julgamento == "correct":
                tempo_total += tempo

            else:
                tempo_total += 20

    return tempo_total


if __name__ == "__main__":
    main()
