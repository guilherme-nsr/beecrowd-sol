def main():
    n = int(input())

    for i in range(n):
        total = 0

        m = int(input())
        produtos = [None]*m

        for i in range(m):
            produtos[i] = input()

        p = int(input())
        compras = [None]*p

        for i in range(p):
            compras[i] = input()

        for i in range(len(compras)):
            item = compras[i]
            produto = item.split()[0]
            quantidade = int(item.split()[1])

            for j in range(len(produtos)):
                item_tabela = produtos[j]
                nome_produto = item_tabela.split()[0]
                preco = float(item_tabela.split()[1])

                if produto == nome_produto:
                    total += quantidade*preco

        print("R$ %.2f" % (total))


if __name__ == "__main__":
    main()
