def main():
    
    palavra = input().strip()
    
    while palavra != '0':
        resultado = calc_qtd_anagramas(palavra)
        print(resultado % 100000007)
        
        try:
            palavra = input().strip()
        except EOFError:
            break
        
def calc_qtd_anagramas(palavra):
    ocorrencias = get_ocorrencias(palavra)
    
    fatorial_letras_totais = fatorial(len(palavra))
    fatorial_repeticoes = calc_fatorial_repeticoes(ocorrencias)
    
    return fatorial_letras_totais // fatorial_repeticoes
    
def fatorial(n):
    somatorio = 1
    
    while n > 1:
        somatorio *= n
        n -= 1
        
    return somatorio
    
def get_ocorrencias(palavra):
    ocorrencias = {}
    
    for letra in palavra:
        if letra not in ocorrencias.keys():
            ocorrencias[letra] = 1
        else:
            ocorrencias[letra] += 1
            
    return ocorrencias
    
def calc_fatorial_repeticoes(ocorrencias):
    resultado = 1
    
    for ocorrencia in ocorrencias.values():
        resultado *= fatorial(ocorrencia)
        
    return resultado

    
if __name__ == '__main__':
    main()
