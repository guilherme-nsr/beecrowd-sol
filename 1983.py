def main():
    n = int(input())

    matricula, nota = input().split()
    nota = float(nota)

    maior_nota = nota
    escolhido = matricula

    for i in range(n-1):
        matricula, nota = input().split()
        nota = float(nota)

        if nota > maior_nota:
            maior_nota = nota
            escolhido = matricula

    print(escolhido) if maior_nota >= 8 else print("Minimum note not reached")


if __name__ == "__main__":
    main()
