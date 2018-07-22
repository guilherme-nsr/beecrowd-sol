def main():
    n = int(input())

    for i in range(n):
        x = int(input())

        if eh_perfeito(x):
            print(x, "eh perfeito")

        else:
            print(x, "nao eh perfeito")


def eh_perfeito(n):
    soma = 0

    for i in range(n-1, 0, -1):
        if n % i == 0:
            soma += i

    return soma == n


if __name__ == "__main__":
    main()    
