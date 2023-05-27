# Python 3.4.3

def main():
  while True:
    try:
      for i in range(int(input())):
        if(int(input())) > 8000:
          print('Mais de 8000!')
        else:
          print('Inseto!')
    except EOFError:
      break

if __name__ == '__main__':
	main()