distancia = int(input()) # A distância percorrida pelo automóvel, em km
combustivel_gasto = float(input())

consumo_medio = distancia / combustivel_gasto

print("%.3f km/l" % consumo_medio)