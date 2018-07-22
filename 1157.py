n = int(input())

print("\n".join([str(i) for i in range(1, n+1) if n % i == 0]))
