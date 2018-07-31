def main():
    while True:
        try:
            hora, minuto = to_int(input().split(':'))

            total_minutos = hora*60 + minuto

            hora_maxima = total_minutos + 60  # Em minutos

            atraso_max = hora_maxima - 480
            if atraso_max < 0:
                atraso_max = 0

            print("Atraso maximo:", atraso_max)

        except EOFError:
            break


def to_int(c):
    return [int(i) for i in c]


if __name__ == "__main__":
    main()
