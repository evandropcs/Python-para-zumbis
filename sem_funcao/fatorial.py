n = int(input('numero? '))
k = 1
x = 1
while x <= n:
	print(f'{k} x {x} = {k * x}')
	k = k * x
	x += 1
print(k)