def main():
    while True:
        try:
            texto = input()

            for char in texto:
                texto = texto.replace('_', '<i>', 1)
                texto = texto.replace('_', '</i>', 1)
                texto = texto.replace('*', '<b>', 1)
                texto = texto.replace('*', '</b>', 1)

            print(texto)

        except:
            break


if __name__ == "__main__":
    main()
