def main():
    number_in_str = input().strip()
    sign = number_in_str[0]
    
    number_in_float = float(number_in_str)
    
    if number_in_float >= 0 and sign != '-': # prevents printing the "+" sign if input is "-0"
        print('+', end='')
    
    print(f'{number_in_float:.4E}')
    
    
if __name__ == '__main__':
    main()
