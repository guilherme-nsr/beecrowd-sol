def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        if n == 0:
            break

        alunos = input().split()
        registros = input().split()

        frequencias = []

        for reg in registros:
            aulas = 0
            faltas = 0

            for r in reg:
                if r != 'M':
                    aulas += 1

                if r == 'A':
                    faltas += 1

            try:
                frequencia = faltas/aulas

            except ZeroDivisionError:
                frequencia = 0

            frequencias.append(frequencia)

        proibidos = []

        for i in range(len(frequencias)):
            if frequencias[i] > 0.25:
                proibidos.append(alunos[i])

        print(' '.join(proibidos))


if __name__ == "__main__":
    main()
