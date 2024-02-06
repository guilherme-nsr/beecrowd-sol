def sum_interval(a, b):
  sum = (a+b) * (b-a+1) / 2
  return int(sum)

def main():
  a, b = map(int, input().split())
  print(sum_interval(a, b))

if __name__ == '__main__':
  main()
