def main():
    eof = False

    while not eof:
        try:
            n, r = list(map(int, input().split()))

            voltaram = list(map(int, input().split()))

            nao_voltaram = [str(mergulhador) for mergulhador in range(1, n+1)
                            if mergulhador not in voltaram]

            if len(nao_voltaram) > 0:
                print(' '.join(nao_voltaram), end=' \n')

            else:
                print('*')

        except EOFError:
            eof = True


if __name__ == "__main__":
    main()
