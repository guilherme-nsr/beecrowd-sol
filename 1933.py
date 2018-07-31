def main():
    a, b = to_int(input().split())

    tem_par = a == b

    if tem_par:
        c = a

    else:
        c = a if a > b else b

    print(c)


def to_int(c):
    return [int(i) for i in c]


if __name__ == "__main__":
    main()
