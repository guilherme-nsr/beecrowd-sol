def main():
    cpf = input()
    
    xxx, yyy, zzzdd = cpf.split('.')
    zzz, dd = zzzdd.split('-')
    
    print(xxx)
    print(yyy)
    print(zzz)
    print(dd)
    
if __name__ == '__main__':
    main()
