def to_float(l):
    """Retorna uma lista com todos os seus elementos convertidos para
    o tipo float.
    """
    return [float(i) for i in l]


def main():
    N1, N2, N3, N4 = to_float(input().split())

    media = ((N1*2) + (N2*3) + (N3*4) + (N4*1)) / 10

    print("Media: %.1f" % (media))

    if media >= 7:
        print("Aluno aprovado.")

    elif media < 5:
        print("Aluno reprovado.")

    else:
        print("Aluno em exame.")
        nota_exame = float(input())
        print("Nota do exame: %.1f" % (nota_exame))

        media_final = (media + nota_exame) / 2

        if media_final >= 5:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")

        print("Media final: %.1f" % (media_final))


if __name__ == "__main__":
    main()
