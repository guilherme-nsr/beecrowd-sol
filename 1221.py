def main():
    n = int(input())

    for i in range(n):
        x = int(input())

        if is_prime(x):
            print("Prime")

        else:
            print("Not Prime")


def is_prime(n):
    for i in range(int(n**0.5), 1, -1):
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    main()
