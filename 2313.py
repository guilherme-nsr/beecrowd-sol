def main():
    a, b, c = map(int, input().split())
    
    if not is_triangulo(a, b, c):
        print('Invalido')
        return
        
    print(f'Valido-{get_tipo_triangulo(a, b, c)}')
    
    if a > b and a > c:
        is_triangulo_retangulo_return = is_triangulo_retangulo(a, b, c)
    elif b > a and b > c:
        is_triangulo_retangulo_return = is_triangulo_retangulo(b, a, c)
    else:
        is_triangulo_retangulo_return = is_triangulo_retangulo(c, a, b)
    
    print(f'Retangulo: {is_triangulo_retangulo_return}')
    
def is_triangulo(a, b, c):
    if a+b <= c:
        return False
    if a+c <= b:
        return False
    if b+c <= a:
        return False
        
    return True
    
def get_tipo_triangulo(a, b, c):
    if a == b and b == c:
        return 'Equilatero'
        
    if a != b and a != c and b != c:
        return 'Escaleno'
        
    return 'Isoceles'
    
def is_triangulo_retangulo(hipotenusa, cateto1, cateto2):
    return 'S' if hipotenusa**2 == cateto1**2 + cateto2**2 else 'N'
    
if __name__ == '__main__':
    main()
