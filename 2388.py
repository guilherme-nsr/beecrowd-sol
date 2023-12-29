n = int(input())

distancia_percorrida = 0

for i in range(n):
	tempo, velocidade_media = map(int, input().split())
	
	distancia_percorrida += tempo*velocidade_media

print(distancia_percorrida)