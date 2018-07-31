def main():
    n = int(input())

    for i in range(n):
        h, m, o = input().split()

        if int(h) < 10:
            h = "0%s" % (h)

        if int(m) < 10:
            m = "0%s" % (m)

        log = "%s:%s - " % (h, m)

        porta_abriu = bool(int(o))

        if porta_abriu:
            log += "A porta abriu!"

        else:
            log += "A porta fechou!"

        print(log)


if __name__ == "__main__":
    main()
