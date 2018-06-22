def main():
    n = int(input())

    for i in range(n):
        string1, string2 = input().split()
        print(combinador(string1, string2))


def combinador(string1, string2):
    tail = ''

    if len(string1) > len(string2):
        excedente = len(string1)-len(string2)
        tail = string1[len(string1)-excedente:]
        string1 = string1[:len(string1)-excedente]

    elif len(string2) > len(string1):
        excedente = len(string2)-len(string1)
        tail = string2[len(string2)-excedente:]
        string2 = string2[:len(string2)-excedente]

    resultado = ''

    for i in range(len(string1)):
        char_s1 = string1[i]
        char_s2 = string2[i]

        resultado += char_s1
        resultado += char_s2

    resultado += tail

    return resultado


if __name__ == "__main__":
    main()
