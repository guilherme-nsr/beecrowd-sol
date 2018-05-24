def to_int(l):
    """Retorna uma lista com todos os seus elementos convertidos para
    o tipo inteiro.
    """
    return [int(i) for i in l]


def duracao(horas_inicio, minutos_inicio, horas_fim, minutos_fim):
    """Retorna uma tupla com as horas e os minutos de duração, respecti
    vamente.
    """
    return total_horas, total_minutos


def main():
    input_data = input().split()
    hora_inicial, minuto_inicial, hora_final, minuto_final = to_int(input_data)

    total = duracao(hora_inicial, minuto_inicial, hora_final, minuto_final)

    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (total))


if __name__ == "__main__":
    main()
