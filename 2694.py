def is_number(char):
  return ord(char) >= 48 and ord(char) <= 57

def parse_and_sum(s):
  n = ''
  summ = 0

  for i in range(len(s)):
    c = s[i]

    if is_number(c):
      n = n + c

    if not is_number(c) or i == len(s) - 1:
      summ = summ + (int(n) if n != '' else 0)
      n = ''
      continue

  return summ

def main():
  for i in range(int(input())):
    print(parse_and_sum(input()))

if __name__ == '__main__':
  main()