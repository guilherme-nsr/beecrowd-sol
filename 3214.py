e, f, c = map(int, input().split())

v = e+f
b = 0

while v >= c:
  v = v-c
  b = b+1
  v = v+1

print(b)