def main():
    n = int(input())
    minimo_classificados = int(input())

    pontuacoes = [int(input()) for i in range(n)]

    pontuacoes.sort(reverse=True)

    classificados = minimo_classificados
    
    pontuacao_ultimo_colocado = pontuacoes[minimo_classificados-1]

    for i in range(classificados, len(pontuacoes)):
        pontuacao = pontuacoes[i]

        if pontuacao != pontuacao_ultimo_colocado:
            break

        else:
            classificados += 1

    print(classificados)


if __name__ == "__main__":
    main()
