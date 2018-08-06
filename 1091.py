def main():
    k = int(input())

    while k != 0:
        n_origem, m_origem = list(map(int, input().split()))

        for i in range(k):
            n, m = list(map(int, input().split()))

            if n == n_origem or m == m_origem:
                local = "divisa"

            else:
                if m > m_origem:
                    if n < n_origem:
                        local = "NO"

                    else:
                        local = "NE"

                else:
                    if n < n_origem:
                        local = "SO"

                    else:
                        local = "SE"

            print(local)

        k = int(input())


if __name__ == "__main__":
    main()
