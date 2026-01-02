def main():
    numero_caso = 1
    
    while 1==1:
        try:
            n = int(input())
            sequencia = get_sequencia(n)
                
            print_caso(numero_caso, sequencia)
            print_nova_linha()
            
            numero_caso += 1   
        except EOFError:
            break

def get_sequencia(n):
    sequencia = []
    
    numero = 0
    
    while numero <= n:
        if numero == 0:
            sequencia.append(0)
        else:
            for i in range(numero):
                sequencia.append(numero)
        numero += 1
    
    return sequencia
    
def print_nova_linha():
    print()
    
def print_caso(numero_caso, sequencia):
    qtd_numeros_sequencia = len(sequencia)
    
    if qtd_numeros_sequencia == 1:
        texto = '%d numero' % (qtd_numeros_sequencia)
    else:
        texto = '%d numeros' % (qtd_numeros_sequencia)
    
    print(f'Caso {numero_caso}: {texto}')
    
    sequencia = map(str, sequencia)
    print(' '.join(sequencia))


if __name__ == '__main__':
    main()
