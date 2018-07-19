def main():
    n = int(input())

    for i in range(n):
        s = input()

        q = int(input())

        for j in range(q):
            r = input()

            if eh_subsequencia(r, s):
                print("Yes")

            else:
                print("No")


def eh_subsequencia(a, b):
    """ Retorna True se 'a' for uma subsequência de 'b'."""
    i = 0
    found = 0
    start = 0
    while i < len(a):
        j = start
        while j < len(b):
            if b[j] == a[i]:
                found += 1
                if found >= len(a):
                    return True
                start = j+1
                break

            j += 1

        i += 1

    return False


if __name__ == "__main__":
    main()
