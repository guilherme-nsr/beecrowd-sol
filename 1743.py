def main():
    primeiro_conector = eval('0b' + ''.join(input().split()))
    segundo_conector = eval('0b' + ''.join(input().split()))

    print("Y") if primeiro_conector ^ segundo_conector == 31 else print("N")


if __name__ == "__main__":
    main()
