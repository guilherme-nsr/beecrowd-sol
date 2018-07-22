def main():
    n = int(input())

    for i in range(n):
        print("Y") if input().split()[0] == "Thor" else print("N")


if __name__ == "__main__":
    main()
