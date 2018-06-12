def main():
    n = int(input())

    total_cobaias = 0
    total_coelhos = 0
    total_ratos = 0
    total_sapos = 0

    for i in range(n):
        cobaia = input()
        cobaias = int(cobaia.split()[0])
        tipo = cobaia.split()[1]

        if tipo == 'C':
            total_coelhos += cobaias

        elif tipo == 'R':
            total_ratos += cobaias

        elif tipo == 'S':
            total_sapos += cobaias

        total_cobaias += cobaias

    perc_coelhos = total_coelhos/total_cobaias * 100
    perc_ratos = total_ratos/total_cobaias * 100
    perc_sapos = total_sapos/total_cobaias * 100

    print("Total: %d cobaias" % (total_cobaias))
    print("Total de coelhos: %d" % (total_coelhos))
    print("Total de ratos: %d" % (total_ratos))
    print("Total de sapos: %d" % (total_sapos))
    print("Percentual de coelhos: %.2f %s" % (perc_coelhos, '%'))
    print("Percentual de ratos: %.2f %s" % (perc_ratos, '%'))
    print("Percentual de sapos: %.2f %s" % (perc_sapos, '%'))


if __name__ == "__main__":
    main()
