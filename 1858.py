def main():
    input()

    pessoas = to_int(input().split())

    algoz = posicao_menor(pessoas)+1

    print(algoz)


def to_int(c):
    return [int(i) for i in c]


def posicao_menor(c):
    menor = c[0]
    posicao = 0

    for i in range(len(c)):
        if c[i] < menor:
            menor = c[i]
            posicao = i

    return posicao


if __name__ == "__main__":
    main()
