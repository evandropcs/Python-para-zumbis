def fatorial(n):
	k = 1
	x = 1
	while x <= n:
		k = k * x
		x += 1
	return k


print(fatorial(5))

