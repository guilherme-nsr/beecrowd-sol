def main():
    palavra = input().strip()
    while palavra != '0':
        print(calc_qtd_anagramas(palavra))
        try:
            palavra = input().strip()
        except EOFError:
            break
        
def calc_qtd_anagramas(palavra):
    return fatorial(len(palavra))
    
def fatorial(n):
    somatorio = 1
    
    while n > 1:
        somatorio *= n
        n -= 1
        
    return somatorio
    
if __name__ == '__main__':
    main()
