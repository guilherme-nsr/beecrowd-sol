def to_int(l):
    """Retorna uma lista com todos os seus elementos convertidos para
    o tipo inteiro.
    """
    return [int(i) for i in l]


def main():
    dia_inicio = int(input().split()[1])
    sep = " : "
    horas_inicio, minutos_inicio, segundos_inicio = to_int(input().split(sep))

    dia_fim = int(input().split()[1])
    horas_fim, minutos_fim, segundos_fim = to_int(input().split(sep))

    dias_duracao = dia_fim - dia_inicio
    horas_duracao = horas_fim - horas_inicio

    if horas_duracao < 0:
        horas_duracao += 24
        dias_duracao -= 1

    minutos_duracao = minutos_fim - minutos_inicio

    if minutos_duracao < 0:
        minutos_duracao += 60
        horas_duracao -= 1

    segundos_duracao = segundos_fim - segundos_inicio

    if segundos_duracao < 0:
        segundos_duracao += 60
        minutos_duracao -= 1

    if dias_duracao < 0:
        dias_duracao = 0

    print("%d dia(s)" % (dias_duracao))
    print("%d hora(s)" % (horas_duracao))
    print("%d minuto(s)" % (minutos_duracao))
    print("%d segundo(s)" % (segundos_duracao))


if __name__ == "__main__":
    main()
