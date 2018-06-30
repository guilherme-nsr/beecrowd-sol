def main():
    n = int(input())

    for i in range(n):
        dieta = input()
        manha = input()
        almoco = input()

        trapaceou = False

        for j in range(len(manha)):
            alimento = manha[j]

            if not is_in(alimento, dieta):
                trapaceou = True
                break

            elif count(alimento, manha) > 1:
                trapaceou = True
                break

            dieta = remove(alimento, dieta)

        for j in range(len(almoco)):
            alimento = almoco[j]

            if not is_in(alimento, dieta):
                trapaceou = True
                break

            elif count(alimento, almoco) > 1:
                trapaceou = True
                break

            dieta = remove(alimento, dieta)

        if trapaceou:
            print("CHEATER")

        else:
            dieta = ''.join(sorted(dieta))

            print(dieta)


def is_in(char, string):
    for i in range(len(string)):
        carac = string[i]

        if char == carac:
            return True

    return False


def count(char, string):
    c = 0

    for i in range(len(string)):
        carac = string[i]

        if carac == char:
            c += 1

    return c


def remove(char, string):
    nova_string = ''

    for i in range(len(string)):
        carac = string[i]

        if carac == char:
            carac = ''

        nova_string += carac

    return nova_string


if __name__ == "__main__":
    main()
