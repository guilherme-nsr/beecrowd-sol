def main():
    tweet = input()

    if len(tweet) <= 140:
        print("TWEET")

    else:
        print("MUTE")


if __name__ == "__main__":
    main()
