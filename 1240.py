def main():
    n = int(input())

    for i in range(n):
        a, b = input().split()

        if encaixa(b, a):
            print("encaixa")

        else:
            print("nao encaixa")


def fatia(s, start=0, end=None, passo=1):
    f = ''

    if end is None:
        end = len(s)

    for i in range(start, end, passo):
        f += s[i]

    return f


def encaixa(b, a):
    if len(b) > len(a):
        return False

    if fatia(a, start=len(a)-len(b)) == b:
        return True

    return False


if __name__ == "__main__":
    main()
