def main():
    total_gasto = 0
    consumo_total = 0
    dias = 0

    for i in range(int(input())):
        total_gasto += float(input())
        frutas = input().split()

        consumo = len(frutas)
        consumo_total += consumo
        dias += 1

        print("day %d: %d kg" % (dias, consumo))

    print("%.2f kg by day" % (consumo_total/dias))
    print("R$ %.2f by day" % (total_gasto/dias))


if __name__ == "__main__":
    main()
