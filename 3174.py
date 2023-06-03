horas_bonecos = 0
horas_arquitetos = 0
horas_musicos = 0
horas_desenhistas = 0

for i in range(int(input())):
  elfo, grupo, horas = input().split()
  horas = int(horas)

  if grupo == "bonecos":
    horas_bonecos += horas
  elif grupo == "arquitetos":
    horas_arquitetos += horas
  elif grupo == "musicos":
    horas_musicos += horas
  elif grupo == "desenhistas":
    horas_desenhistas += horas

qtd_presentes = 0
qtd_presentes += horas_bonecos // 8
qtd_presentes += horas_arquitetos // 4
qtd_presentes += horas_musicos // 6
qtd_presentes += horas_desenhistas // 12

print(qtd_presentes)