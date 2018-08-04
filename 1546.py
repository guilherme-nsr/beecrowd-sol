def main():
    responsaveis = ["Rolien", "Naej", "Elehcim", "Odranoel"]

    n = int(input())

    for i in range(n):
        k = int(input())

        for j in range(k):
            print(responsaveis[int(input())-1])


if __name__ == "__main__":
    main()
