COMPRIMENTO_LINHA = 39
CABECALHO_DECIMAL = 'decimal'
CABECALHO_OCTAL = 'octal'
CABECALHO_HEXADECIMAL = 'Hexadecimal'

def main():
    print_linha_tracejada()
    print_cabecalho()
    print_linha_tracejada()
    print_conteudo()
    print_linha_tracejada()

def print_linha_tracejada():
    print('-'*COMPRIMENTO_LINHA)

def print_cabecalho():
    posicao = 0
    while posicao < COMPRIMENTO_LINHA:
        is_primeira_posicao = posicao == 0
        is_ultima_posicao = posicao == COMPRIMENTO_LINHA - 1
        
        if is_primeira_posicao:
            print('|', end='')
        elif is_ultima_posicao:
            print('|', end='\n')
        elif posicao == 12 or posicao == 22:
            print('|', end='')
        elif posicao == 3:
            print(CABECALHO_DECIMAL, end='')
            posicao += len(CABECALHO_DECIMAL)
            continue
        elif posicao == 15:
            print(CABECALHO_OCTAL, end='')
            posicao += len(CABECALHO_OCTAL)
            continue
        elif posicao == 25:
            print(CABECALHO_HEXADECIMAL, end='')
            posicao += len(CABECALHO_HEXADECIMAL)
            continue
        else:
            print(' ', end='')
        
        posicao += 1
        
def print_conteudo():
    numero = 0
    
    while numero < 16:
        print_celulas(numero)
        numero += 1
        
def print_celulas(numero):
    posicao = 0
    while posicao < COMPRIMENTO_LINHA:
        is_primeira_posicao = posicao == 0
        is_ultima_posicao = posicao == COMPRIMENTO_LINHA - 1
        
        decimal = '%d' % (numero)
        octal = '%o' % (numero)
        hexadecimal = '%X' % (numero)
        
        deve_imprimir_pipe = is_primeira_posicao or is_ultima_posicao or posicao == 12 or posicao == 22
        deve_imprimir_nova_linha = is_ultima_posicao
        
        deve_imprimir_decimal = len(decimal)+posicao == 8
        deve_imprimir_octal = len(octal)+posicao == 18
        deve_imprimir_hexadecimal = len(hexadecimal)+posicao == 31
        
        if deve_imprimir_pipe:
            print('|', end='')
            
        elif deve_imprimir_decimal:
            print(decimal, end='')
            posicao += len(decimal)
            continue
            
        elif deve_imprimir_octal:
            print(octal, end='')
            posicao += len(octal)
            continue
            
        elif deve_imprimir_hexadecimal:
            print(hexadecimal, end='')
            posicao += len(hexadecimal)
            continue
            
        else:
            print(' ', end='')
            
        if deve_imprimir_nova_linha:
            print('\n', end='')
        
        posicao += 1


if __name__ == '__main__':
    main()
