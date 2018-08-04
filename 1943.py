def main():
    colocacoes = [1, 3, 5, 10, 25, 50, 100]

    k = int(input())

    for colocacao in colocacoes:
        if colocacao >= k:
            top = colocacao
            break

    print("Top", top)


if __name__ == "__main__":
    main()
