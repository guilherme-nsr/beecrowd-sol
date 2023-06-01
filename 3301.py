def get_sobrinho_meio(h, z, l):
  if (h > z and h < l) or (h < z and h > l):
    return 'huguinho'

  elif (z > h and z < l) or (z < h and z > l):
    return 'zezinho'

  return 'luisinho'

def main():
  h, z, l = map(int, input().split())

  print(get_sobrinho_meio(h, z, l))

if __name__ == '__main__':
  main()