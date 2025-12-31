def main():
    n = int(input())
    print('%.1f' % get_fibonacci_binet(n))
    
def get_fibonacci_binet(n):
    RAIZ_QUADRADA_DE_CINCO = 5**0.5
    
    primeiro_termo = ((1 + RAIZ_QUADRADA_DE_CINCO) / 2) ** n
    segundo_termo = ((1 - RAIZ_QUADRADA_DE_CINCO) / 2) ** n
    
    return (primeiro_termo - segundo_termo) / RAIZ_QUADRADA_DE_CINCO
    
if __name__ == '__main__':
    main()
