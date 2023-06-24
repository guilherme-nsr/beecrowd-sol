n = int(input())

is_branco = True
qtd_branco = 0
qtd_preto = 0

for i in range(n):
  for j in range(n):
    if is_branco:
      qtd_branco += 1
    else:
      qtd_preto += 1

    is_branco = not is_branco

print('%d casas brancas e %d casas pretas' % (qtd_branco, qtd_preto))