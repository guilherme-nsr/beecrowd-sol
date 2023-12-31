tws = 7 # trailing whitespaces
bws = -1 # between whitespaces
c = 65 # 'A' char code
l = 0 # number of lines printed

while l < 9:
	if c == 65:
		print(' '*tws + chr(c))
	else:
		print(' '*tws + chr(c) + ' '*bws + chr(c))

	if l < 4:
		tws -= 1
		bws += 2
		c += 1
	
	else:
		tws += 1
		bws -= 2
		c -= 1

	l += 1
