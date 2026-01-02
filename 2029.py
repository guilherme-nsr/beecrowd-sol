PI = 3.14

def main():
    while True:
        try:
            volume = float(input())
            diametro = float(input())
            
            area_base = calc_area_base(diametro)
            altura = calc_altura(volume, area_base)
            
            print(f'ALTURA = {altura:.2f}')
            print(f'AREA = {area_base:.2f}')

        except EOFError:
            break

def calc_area_base(diametro):
    raio = diametro/2
    return PI*raio**2

def calc_altura(volume, area_base):
    return volume/area_base
    
    
if __name__ == '__main__':
    main()
