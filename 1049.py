def get_animal(vertebra, tipo_animal, alimentacao):
    if vertebra == "vertebrado":
        if tipo_animal == "ave":
            if alimentacao == "carnivoro":
                return "aguia"

            if alimentacao == "onivoro":
                return "pomba"

        if tipo_animal == "mamifero":
            if alimentacao == "onivoro":
                return "homem"

            if alimentacao == "herbivoro":
                return "vaca"

    if vertebra == "invertebrado":
        if tipo_animal == "inseto":
            if alimentacao == "hematofago":
                return "pulga"

            if alimentacao == "herbivoro":
                return "lagarta"

        if tipo_animal == "anelideo":
            if alimentacao == "hematofago":
                return "sanguessuga"

            if alimentacao == "onivoro":
                return "minhoca"


def main():
    vertebra = input()
    tipo_animal = input()
    alimentacao = input()

    animal = get_animal(vertebra, tipo_animal, alimentacao)

    print(animal)


if __name__ == "__main__":
    main()
