# Python 3.4.3

def main():
  while True:
    try:
      d = input()
      s = input()

      if s in d:
        print('Resistente')
      else:
        print('Nao resistente')

    except EOFError:
      break

if __name__ == '__main__':
  main()
