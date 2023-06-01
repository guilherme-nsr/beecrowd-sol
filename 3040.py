def escolher_arvore(h, d, g):
  if h < 200 or h > 300:
    return False

  if d < 50:
    return False

  if g < 150:
    return False

  return True

def main():
  for i in range(int(input())):
    h, d, g = map(int, input().split())
    if escolher_arvore(h, d, g):
      print('Sim')
    else:
      print('Nao')

if __name__ == '__main__':
  main()