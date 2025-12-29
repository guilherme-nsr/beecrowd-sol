def main():

    p, j1, j2, r, a = map(int, input().split())

    j1_cheated = r == 1
    j2_accused_cheat = a == 1

    if j2_accused_cheat and j1_cheated:
        print('Jogador 2 ganha!')
        return
        
    if j2_accused_cheat and not j1_cheated:
        print('Jogador 1 ganha!')
        return

    if not j2_accused_cheat and j1_cheated:
        print('Jogador 1 ganha!')
        return
        
    sum_result = j1+j2
    sum_result_is_even = sum_result%2 == 0
    sum_result_is_odd = sum_result%2 == 1

    j1_chose_even = p == 1
    j1_chose_odd = p == 0

    if sum_result_is_even and j1_chose_even:
        print('Jogador 1 ganha!')
    elif sum_result_is_odd and j1_chose_odd:
        print('Jogador 1 ganha!')
    else:
        print('Jogador 2 ganha!')

if __name__ == '__main__':
    main()
