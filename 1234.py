def main():
    while True:
        try:
            sentenca = input()

            sentenca_dancante = dancante(sentenca)

            print(sentenca_dancante)

        except EOFError:
            break


def dancante(texto):
    resultado = str()

    espacos = 0

    for i in range(len(texto)):
        char = texto[i]

        if char == ' ':
            resultado += ' '
            espacos += 1
            continue

        if (i - espacos) % 2 == 0:
            char = char.upper()

        else:
            char = char.lower()

        resultado += char

    return resultado


if __name__ == "__main__":
    main()
