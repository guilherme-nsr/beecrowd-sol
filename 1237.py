def main():
    while True:
        try:
            string1 = input()
            string2 = input()

            maior = maior_substring(string1, string2)

            print(maior)

        except EOFError:
            break


def maior_substring(string1, string2):
    menor = string1
    maior = string2

    if string2 < string1:
        maior = string1
        menor = string2

    length = len(menor)

    maior_sub = 0

    for i in range(length):
        for j in range(i, length):
            if maior_sub == len(menor):
                return maior_sub

            substring = menor[i:j + 1]

            if substring in maior:
                if len(substring) > maior_sub:
                    maior_sub = len(substring)

    return maior_sub


if __name__ == "__main__":
    main()
