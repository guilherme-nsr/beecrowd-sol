def main():   
    disponivel = list(map(int, input().split()))
    requisitado = list(map(int, input().split()))
    
    qtd_indisponivel = 0
    
    for i in range(len(disponivel)):
        qtd_disponivel = disponivel[i]
        qtd_requisitado = requisitado[i]
        
        if qtd_requisitado > qtd_disponivel:
            qtd_indisponivel += qtd_requisitado - qtd_disponivel
            
    print(qtd_indisponivel)
        
    
if __name__ == '__main__':
    main()
