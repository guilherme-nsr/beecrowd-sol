# -*- coding: utf-8 -*-


def main():
  print_borda_horizontal()
  print_linha()
  print_linha()
  print_linha()
  print_linha()
  print_linha()
  print_borda_horizontal()

def print_borda_horizontal():
  for i in range(39):
    print('-', end='')
  print()

def print_linha():
  print('|', end='')
  for i in range(37):
    print(' ', end='')
  print('|')

if __name__ == '__main__':
  main()
