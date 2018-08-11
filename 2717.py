def main():
    amanha = int(input()) < sum(map(int, input().split()))

    if amanha:
        print("Deixa para amanha!")

    else:
        print("Farei hoje!")


if __name__ == "__main__":
    main()
