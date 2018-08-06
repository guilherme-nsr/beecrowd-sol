def main():
    a, d = list(map(int, input().split()))

    while a != 0 or d != 0:
        atacantes = list(map(int, input().split()))
        defensores = list(map(int, input().split()))

        penultimo_defensor = sorted(defensores, reverse=True)[-2]

        alguem_impedido = False

        for atacante in atacantes:
            if atacante < penultimo_defensor:
                alguem_impedido = True
                break

        print('Y') if alguem_impedido else print('N')

        a, d = list(map(int, input().split()))


if __name__ == "__main__":
    main()
