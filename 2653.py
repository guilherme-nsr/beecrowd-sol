joias_unicas = []

while True:
  try:
    joia = input()

    if joia not in joias_unicas:
      joias_unicas.append(joia)

  except EOFError:
    break

print(len(joias_unicas))