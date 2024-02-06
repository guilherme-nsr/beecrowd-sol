def is_tautogram(phrase):
  words = phrase.split()
  letter = words[0][0].lower()

  for word in words[1:]:
    first_letter = word[0].lower()
    if first_letter != letter:
      return False

  return True

def main():
  phrase = input()

  while phrase != '*':
    print('Y') if is_tautogram(phrase) else print('N')
    phrase = input()

if __name__ == '__main__':
  main()
