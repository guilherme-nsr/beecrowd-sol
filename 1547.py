def main():
  n = int(input())

  for i in range(n):
    qt, s = map(int, input().split())
    guesses = list(map(int, input().split()))

    best_guess_index = 0
    best_guess_diff = abs(s - guesses[0])

    for i in range(1, qt):
      guess = guesses[i]
      guess_diff = abs(s - guess)

      if guess_diff < best_guess_diff:
        best_guess_diff = guess_diff
        best_guess_index = i

    print(best_guess_index + 1)


if __name__ == '__main__':
  main()
