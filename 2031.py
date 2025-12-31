PEDRA = 'pedra'
PAPEL = 'papel'
ATAQUE = 'ataque'

def main():
    n = int(input())
    
    for i in range(n):
        jogador1 = input()
        jogador2 = input()
        
        print(get_resultado(jogador1, jogador2))
        
def get_resultado(jogador1, jogador2):
    if jogador1 == PAPEL and jogador2 == PAPEL:
        return 'Ambos venceram'
        
    if jogador1 == PEDRA and jogador2 == PEDRA:
        return 'Sem ganhador'
        
    if jogador1 == ATAQUE and jogador2 == ATAQUE:
        return 'Aniquilacao mutua'
        
    if jogador1 == ATAQUE:
        return 'Jogador 1 venceu'
        
    if jogador2 == ATAQUE:
        return 'Jogador 2 venceu'
        
    if jogador1 == PAPEL:
        return 'Jogador 2 venceu'
        
    if jogador2 == PAPEL:
        return 'Jogador 1 venceu'
        
    if jogador1 == PEDRA:
        return 'Jogador 1 venceu'
        
    if jogador2 == PEDRA:
        return 'Jogador 2 venceu'


if __name__ == '__main__':
    main()
