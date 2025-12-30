COMPRIMENTO_LINHA = 39

def main():
    print_linha_tracejada()
    print_texto('x = 35', 1)
    print_linha_vazia()
    print_texto('x = 35', 16)
    print_linha_vazia()
    print_texto('x = 35', 32)
    print_linha_tracejada()
    
def print_linha_tracejada():
    print('-'*COMPRIMENTO_LINHA)
    
def print_texto(texto, posicao):
    i = 0
    while i < COMPRIMENTO_LINHA:
        is_primeira_posicao = i == 0
        is_ultima_posicao = i == COMPRIMENTO_LINHA - 1
        
        if is_primeira_posicao:
            print('|', end='')
        elif is_ultima_posicao:
            print('|', end='\n')
        elif i == posicao:
            print(texto, end='')
            i += len(texto)
            continue
        else:
            print(' ', end='')
            
        i += 1
        
def print_linha_vazia():
    for i in range(COMPRIMENTO_LINHA):
        is_primeira_posicao = i == 0
        is_ultima_posicao = i == COMPRIMENTO_LINHA - 1
        
        if is_primeira_posicao:
            print('|', end= '')
        elif is_ultima_posicao:
            print('|', end='\n')
        else:
            print(' ', end='')

if __name__ == '__main__':
    main()
