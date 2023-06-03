qtd_tomadas = 0

for i in range(int(input())):
  entrada = list(map(int, input().split()))
  qtd_filtros = entrada[0]
  filtros = entrada[1:]
  
  for j in range(qtd_filtros):
    if j == qtd_filtros-1:
      qtd_tomadas += filtros[j]
    else:
      qtd_tomadas += filtros[j]-1

  print(qtd_tomadas)
  qtd_tomadas = 0