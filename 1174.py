def main():
    a = [None]*100

    for i in range(100):
        a[i] = float(input())

    for i in range(len(a)):
        numero = a[i]
        posicao = i

        if numero <= 10:
            print("A[%d] = %.1f" % (posicao, numero))


if __name__ == "__main__":
    main()
