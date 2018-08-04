def main():
    q = int(input())

    opnioes = input()

    nao_satisfatorio = 0

    for i in range(0, len(opnioes), 2):
        opniao = opnioes[i]

        nao_satisfatorio += int(opniao == '1')

        if nao_satisfatorio >= q/2:
            resultado = 'N'
            break

        resultado = 'Y'

    print(resultado)


if __name__ == "__main__":
    main()
