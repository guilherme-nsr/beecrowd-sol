def main():
    total_amigos = 0
    total_distancia = 0

    while True:
        try:
            input()

            total_distancia += float(input())

            total_amigos += 1

        except EOFError:
            break

    print("%.1f" % (total_distancia/total_amigos))


if __name__ == "__main__":
    main()
