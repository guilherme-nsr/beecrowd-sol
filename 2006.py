def main():
    t = int(input())
    chas = map(int, input().split())

    print(sum([int(cha == t) for cha in chas]))


if __name__ == "__main__":
    main()
