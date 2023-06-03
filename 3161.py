n, m = map(int, input().split())

frutas_busca = [input().lower() for i in range(n)]

frutas_sheldon_gosta = [input().lower() for i in range(m)]

for i in range(len(frutas_busca)):
  fruta_busca = frutas_busca[i]

  for j in range(len(frutas_sheldon_gosta)):
    fruta_sheldon = frutas_sheldon_gosta[j]

    if fruta_busca in fruta_sheldon or fruta_busca[::-1] in fruta_sheldon:
      print('Sheldon come a fruta ' + fruta_busca)
      break

    else:
      if j == len(frutas_sheldon_gosta) - 1:
        print('Sheldon detesta a fruta ' + fruta_busca)