def main():
    n = int(input())
    
    qtd_saques_tentados = 0
    qtd_bloqueios_tentados = 0
    qtd_ataques_tentados = 0
    
    qtd_saques_bem_sucedidos = 0
    qtd_bloqueios_bem_sucedidos = 0
    qtd_ataques_bem_sucedidos = 0
    
    for i in range(n):
        input()
        s, b, a = map(int, input().split())
        s1, b1, a1 = map(int, input().split())
        
        #print(f's, b, a = {s}, {b}, {a}')
        #print(f's1, b1, a1 = {s1}, {b1}, {a1}')
        
        qtd_saques_tentados += s
        qtd_bloqueios_tentados += b
        qtd_ataques_tentados += a
        
        qtd_saques_bem_sucedidos += s1
        qtd_bloqueios_bem_sucedidos += b1
        qtd_ataques_bem_sucedidos += a1
        
    percentual_saques_bem_sucedidos = qtd_saques_bem_sucedidos/qtd_saques_tentados * 100
    percentual_saques_bem_sucedidos = round(percentual_saques_bem_sucedidos, 2)
    
    percentual_bloqueios_bem_sucedidos = qtd_bloqueios_bem_sucedidos/qtd_bloqueios_tentados * 100
    percentual_bloqueios_bem_sucedidos = round(percentual_bloqueios_bem_sucedidos, 2)
    
    percentual_ataques_bem_sucedidos = qtd_ataques_bem_sucedidos/qtd_ataques_tentados * 100
    percentual_ataques_bem_sucedidos = round(percentual_ataques_bem_sucedidos, 2)
    
    print('Pontos de Saque: %.2f %%.' % (percentual_saques_bem_sucedidos))
    print('Pontos de Bloqueio: %.2f %%.' % (percentual_bloqueios_bem_sucedidos))
    print('Pontos de Ataque: %.2f %%.' % (percentual_ataques_bem_sucedidos))
        
    
if __name__ == '__main__':
    main()
