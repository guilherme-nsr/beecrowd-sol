def main():
    s = input()

    bits_um = count('1', s)

    eh_par = bits_um % 2 == 0

    if eh_par:
        print(s+'0')

    else:
        print(s+'1')


def count(x, c):
    """ Retorna o número de ocorrências de 'x' em 'c'."""
    ocorrencias = 0

    for i in range(len(c)):
        if c[i] == x:
            ocorrencias += 1

    return ocorrencias


if __name__ == "__main__":
    main()
