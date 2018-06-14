def to_int(l):
    return [int(i) for i in l]


def main():
    vitorias_gremio = 0
    vitorias_inter = 0
    empates = 0
    partidas = 0

    while True:
        inter, gremio = to_int(input().split())

        partidas += 1

        if inter > gremio:
            vitorias_inter += 1

        elif gremio > inter:
            vitorias_gremio += 1

        else:
            empates += 1

        novo_grenal = int(input("Novo grenal (1-sim 2-nao)\n"))

        if novo_grenal != 1:
            break

    if vitorias_inter > vitorias_gremio:
        resultado = "Inter venceu mais"

    elif vitorias_gremio > vitorias_inter:
        resultado = "Gremio venceu mais"

    else:
        resultado = "Nao houve vencedor"

    print("%d grenais" % (partidas))
    print("Inter:%d" % (vitorias_inter))
    print("Gremio:%d" % (vitorias_gremio))
    print("Empates:%d" % (empates))
    print("%s" % (resultado))


if __name__ == "__main__":
    main()
