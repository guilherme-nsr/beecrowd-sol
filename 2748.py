# -*- coding: utf-8 -*-

def main():
  print_borda_horizontal()
  print_linha('Roberto', 10)
  print_linha()
  print_linha('5786', 10)
  print_linha()
  print_linha('UNIFEI', 10)
  print_borda_horizontal()

def print_borda_horizontal():
  for i in range(39):
    print('-', end='')
  print()

def print_linha(texto='', start=-1):
  print('|', end='')
  i = 0
  while i < 37:
    if i == start-2:
      print(texto, end='')
      i = i + len(texto) - 1
    else:
      print(' ', end='')
    i = i + 1
  print('|')

if __name__ == '__main__':
  main()
