print()
n = int(input('Digite um número: '))

k = 1

while k * (k + 1) * (k + 2) < n:

    k += 1
if k * (k + 1) * (k + 2) == n:
    print()
    print(f'O número {n} é triangular')
    print(f'{k} x {k+1} x {k +2} = {n}')
else:
    print(f'O número {n} não é triangular')

