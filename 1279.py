def main():
    first = True

    while True:
        try:
            year = int(input())

            if not first:
                print()

            first = False

            if is_ordinary(year):
                print("This is an ordinary year.")

            else:
                if is_leap(year):
                    print("This is leap year.")

                if is_huluculu(year):
                    print("This is huluculu festival year.")

                if is_bulukulu(year):
                    print("This is bulukulu festival year.")

        except EOFError:
            break


def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def is_huluculu(year):
    return year % 15 == 0


def is_bulukulu(year):
    return is_leap(year) and year % 55 == 0


def is_ordinary(year):
    return not is_leap(year) and not is_huluculu(year) and not is_bulukulu(year)


if __name__ == "__main__":
    main()
