n = int(input('Escolha um numero: '))
x = 1
ultimo = 1
penultimo = 1

while x < n:
	if x == n-1:
		print(f'{ultimo}, {penultimo}', end=' ')
	else:
		print(f'{ultimo}, {penultimo},', end=' ')
		ultimo += penultimo
		penultimo += ultimo
	x += 1