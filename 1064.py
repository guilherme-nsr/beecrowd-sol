positivos = 0
soma_positivos = 0

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

if a > 0:
    positivos += 1
    soma_positivos += a

if b > 0:
    positivos += 1
    soma_positivos += b

if c > 0:
    positivos += 1
    soma_positivos += c

if d > 0:
    positivos += 1
    soma_positivos += d

if e > 0:
    positivos += 1
    soma_positivos += e

if f > 0:
    positivos += 1
    soma_positivos += f

media_positivos = soma_positivos / positivos

print("%d valores positivos\n%.1f" % (positivos, media_positivos))
