def main():
    n = int(input())

    while n != 0:
        resultados = list(map(int, input().split()))

        joao = sum([resultado for resultado in resultados])
        maria = len(resultados)-joao

        print("Mary won %d times and John won %d times" % (maria, joao))

        n = int(input())


if __name__ == "__main__":
    main()
