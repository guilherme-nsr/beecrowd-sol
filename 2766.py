QTD_LINHAS_ENTRADA = 10
LINHAS_PARA_IMPRIMIR = [2, 6, 8]

def main():
    for i in range(QTD_LINHAS_ENTRADA):
        nome = input()
        if i in LINHAS_PARA_IMPRIMIR:
            print(nome)
    
    
if __name__ == '__main__':
    main()
