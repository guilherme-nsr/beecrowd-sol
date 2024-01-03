def rafael(x, y):
  return (3*x)**2 + y**2

def beto(x, y):
  return 2*x**2 + (5*y)**2

def carlos(x, y):
  return -100*x + y**3

def print_vencedor(x, y):
  if rafael(x, y) > beto(x, y) and rafael(x, y) > carlos(x, y):
    print("Rafael ganhou")

  elif beto(x, y) > rafael(x, y) and beto(x, y) > carlos(x, y):
    print("Beto ganhou")

  else:
    print("Carlos ganhou")

def main():
  for i in range(int(input())):
    x, y = map(int, input().split())

    print_vencedor(x, y)

if __name__ == "__main__":
  main()
