def main():
    for i in range(int(input())):
        time1_casa, time2_fora = list(map(int, input().split(" x ")))
        time2_casa, time1_fora = list(map(int, input().split(" x ")))

        time1 = time1_casa + time1_fora
        time2 = time2_casa + time2_fora

        if time1 != time2:
            resultado = "Time 1" if time1 > time2 else "Time 2"

        else:
            if time1_fora != time2_fora:
                resultado = "Time 1" if time1_fora > time2_fora else "Time 2"

            else:
                resultado = "Penaltis"

        print(resultado)


if __name__ == "__main__":
    main()
