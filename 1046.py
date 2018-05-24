def to_int(l):
    """Retorna uma lista com todos os seus elementos convertidos para
    o tipo inteiro.
    """
    return [int(i) for i in l]


def main():
    hora_inicio, hora_fim = to_int(input().split())

    if hora_fim > hora_inicio:
        horas_duracao = hora_fim - hora_inicio
    else:
        horas_duracao = (hora_fim + 24) - hora_inicio

    print("O JOGO DUROU %d HORA(S)" % (horas_duracao))


if __name__ == "__main__":
    main()
