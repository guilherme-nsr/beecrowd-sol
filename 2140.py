NOTAS = [2, 5, 10, 20, 50, 100]

def main():
    POSSIVEIS_VALORES_TROCO = calc_possiveis_valores_troco(NOTAS)
    
    valor_compra, valor_pago = map(int, input().split())
    
    while valor_compra != 0 or valor_pago != 0:
        valor_troco = valor_pago - valor_compra
        print(verificar_possibilidade(valor_troco, POSSIVEIS_VALORES_TROCO))
        
        valor_compra, valor_pago = map(int, input().split())

def calc_possiveis_valores_troco(notas):
    possiveis_valores_troco = []
    
    for nota1 in notas:
        for nota2 in notas:
            soma = nota1+nota2
            if soma not in possiveis_valores_troco:
                possiveis_valores_troco.append(soma)
            
    return possiveis_valores_troco

def verificar_possibilidade(valor_troco, possiveis_valores_troco):
    return 'possible' if valor_troco in possiveis_valores_troco else 'impossible'


if __name__ == '__main__':
    main()
