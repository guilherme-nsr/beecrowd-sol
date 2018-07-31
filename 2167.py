def main():
    input()
    medidas = to_int(input().split())

    indice = 0

    for i in range(len(medidas)-1):
        medida_atual = medidas[i]
        prox_medida = medidas[i+1]

        if prox_medida < medida_atual:
            indice = i+1
            break

    print(indice+1) if indice != 0 else print(0)


def to_int(c):
    return [int(i) for i in c]


if __name__ == "__main__":
    main()
