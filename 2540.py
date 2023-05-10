import math

while True:
  try:
    qtd_votos = int(input())
    votos = input().split()

    votos_impeachment = list(filter(lambda voto: voto == '1', votos))
    qtd_votos_impeachment = len(votos_impeachment)
    qtd_necessaria_impeachment = math.ceil(qtd_votos*2/3)
    
    if qtd_votos_impeachment >= qtd_necessaria_impeachment:
      print("impeachment")
    else:
      print("acusacao arquivada")
  except EOFError:
    break
