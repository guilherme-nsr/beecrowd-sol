def main():
    binario = input()
    numero_inteiro = binario_to_int(binario)
    
    m = int(input())
    
    divisores = []
    
    for i in range(m):
        d = int(input())
        
        if numero_inteiro % d == 0:
            divisores.append(d)
            
    if len(divisores) == 0:
        print('Nenhum')
        return
        
    divisores.sort()
    
    for i in range(len(divisores)):
        d = divisores[i]
        is_ultimo_elemento = i == len(divisores) - 1
        
        if is_ultimo_elemento:
            print(d, end='\n')
        else:
            print(d, end=' ')
        
def binario_to_int(binario):
    """i = len(binario) - 1
    p = 0
    somatorio = 0
    
    while i >= 0:
        somatorio += int(binario[i]) * 2**p
        i = i-1
        p = p+1
        
    return somatorio"""
    
    return int(binario, 2)
    
if __name__ == '__main__':
    main()
