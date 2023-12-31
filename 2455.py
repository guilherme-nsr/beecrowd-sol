p1, c1, p2, c2 = map(int, input().split())

pc1 = p1*c1
pc2 = p2*c2

if pc1 == pc2:
	print(0)

elif pc1 > pc2:
	print(-1)

else:
	print(1)