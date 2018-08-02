def main():
    p = int(input().split()[0])
    canos = list(map(int, input().split()))

    for i in range(len(canos)-1):
        cano_atual = canos[i]
        prox_cano = canos[i+1]

        if abs(cano_atual-prox_cano) > p:
            print("GAME OVER")
            return

    print("YOU WIN")


if __name__ == "__main__":
    main()
