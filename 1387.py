def main():
    l, r = list(map(int, input().split()))

    while l != 0 or r != 0:
        print(l+r)

        l, r = list(map(int, input().split()))


if __name__ == "__main__":
    main()
