# Python 3.4.3

def par(n):
  return n%2 == 0

def impar(n):
  return n%2 != 0

def main():
  qtd_linhas = int(input())
  qtd_colunas = int(input())

  if (par(qtd_linhas) and par(qtd_colunas)) or impar(qtd_linhas) and impar(qtd_colunas):
    print(1)
  else:
    print(0)

if __name__ == '__main__':
	main()