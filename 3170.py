qtd_bolinhas = int(input())
qtd_galhos = int(input())

qtd_bolinhas_necessarias = qtd_galhos // 2
diferenca = qtd_bolinhas_necessarias - qtd_bolinhas

print("Amelia tem todas bolinhas!") if diferenca <= 0 else print("Faltam %d bolinha(s)" % (diferenca))