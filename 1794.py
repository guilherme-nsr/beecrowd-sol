def main():
    pecas = int(input())

    lavadora_min, lavadora_max = list(map(int, input().split()))
    secadora_min, secadora_max = list(map(int, input().split()))

    possivel_lavar = pecas >= lavadora_min and pecas <= lavadora_max
    possivel_secar = pecas >= secadora_min and pecas <= secadora_max

    possivel = possivel_lavar and possivel_secar

    print("possivel") if possivel else print("impossivel")


if __name__ == "__main__":
    main()
