def main():
    while True:
        try:
            enunciado = input()

            simbolos = enunciado.split()
            len_palavras = 0
            palavras = 0

            for i in range(len(simbolos)):
                simbolo = simbolos[i]

                if eh_palavra(simbolo):
                    palavra = remove_char(simbolo, '.', len(simbolo)-1)
                    palavras += 1

                    len_palavras += len(palavra)

            try:
                len_media = int(len_palavras/palavras)

            except ZeroDivisionError:
                len_media = 0

            if len_media <= 3:
                dificuldade = 250

            elif len_media <= 5:
                dificuldade = 500

            elif len_media >= 6:
                dificuldade = 1000

            print(dificuldade)

        except EOFError:
            break


def eh_palavra(string):
    for i in range(len(string)):
        char = string[i]

        if string == '.':
            return False

        if i != len(string)-1 and char == '.':
            return False

        if (char.lower() < 'a' or char.lower() > 'z') and char != '.':
            return False

    return True


def remove_char(string, char, index):
    if string[index] == char:
        nova_string = ''

        for i in range(len(string)):
            carac = string[i]

            if i == index:
                continue

            nova_string += carac

        return nova_string

    return string


if __name__ == "__main__":
    main()
