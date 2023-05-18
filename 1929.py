def main():
  a, b, c, d = map(int, input().split())

  # abc
  if a < b+c and b < a+c and c < a+b:
    print('S')

  # abd
  elif a < b+d and b < a+d and d < a+b:
    print('S')

  # acd
  elif a < c+d and c < a+d and d < a+c:
    print('S')

  # bcd
  elif b < c+d and c < b+d and d < b+c:
    print('S')

  else:
    print('N')

if __name__ == '__main__':
  main()