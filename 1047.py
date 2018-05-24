import datetime


def to_int(l):
    """Retorna uma lista com todos os seus elementos convertidos para
    o tipo inteiro.
    """
    return [int(i) for i in l]


def duracao(horas_inicio, minutos_inicio, horas_fim, minutos_fim):
    """Retorna uma tupla com as horas e os minutos de duração, respecti
    vamente.
    """
    if horas_inicio == horas_fim and minutos_inicio == minutos_fim:
        horas_duracao, minutos_duracao = 24, 0

    else:
        horas_duracao = horas_fim - horas_inicio

        if horas_duracao < 0:
            horas_duracao += 24

        minutos_duracao = minutos_fim - minutos_inicio

        if minutos_duracao < 0:
            minutos_duracao += 60
            horas_duracao -= 1

        if horas_duracao < 0:
            horas_duracao += 24

    return horas_duracao, minutos_duracao


def main():
    input_data = input().split()
    hora_inicial, minuto_inicial, hora_final, minuto_final = to_int(input_data)

    total = duracao(hora_inicial, minuto_inicial, hora_final, minuto_final)

    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (total))


if __name__ == "__main__":
    main()
