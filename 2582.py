def main():
    c = int(input())

    for i in range(c):
        x, y = to_int(input().split())

        musica = obter_musica(x+y)

        print(musica)


def to_int(c):
    return [int(i) for i in c]


def obter_musica(c):
    musicas = ["PROXYCITY", "P.Y.N.G.", "DNSUEY!", "SERVERS", "HOST!",
               "CRIPTONIZE", "OFFLINE DAY", "SALT", "ANSWER!", "RAR?",
               "WIFI ANTENNAS"]

    return musicas[c]


if __name__ == "__main__":
    main()
