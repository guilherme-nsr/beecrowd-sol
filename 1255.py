def main():
    n = int(input())

    for i in range(n):
        texto = input()

        frequencia = histograma(texto)

        frequencias = list(frequencia.values())
        frequencias = sorted(frequencias, reverse=True)

        maior_freq = frequencias.pop(0)

        mais_frequentes = []

        for carac in frequencia:
            if frequencia[carac] == maior_freq:
                mais_frequentes.append(carac)

        mais_frequentes.sort()

        print(''.join(mais_frequentes))


def histograma(texto):
    frequencia = {}

    for char in texto:
        char = char.lower()

        if 'a' <= char <= 'z':
            frequencia[char] = frequencia.get(char, 0) + 1

    return frequencia


if __name__ == "__main__":
    main()
