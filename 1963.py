def main():
    a, b = [float(i) for i in input().split()]

    percentual_aumento = (b-a)/a * 100

    print("%.2f%%" % (percentual_aumento))


if __name__ == "__main__":
    main()
