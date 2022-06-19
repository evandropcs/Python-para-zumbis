par = []
par_divisivel = []

def e_par(x):
    if x % 2 == 0:
        par.append(x)

def divisivel_por_7(x):
    if x % 7 == 0:
        par_divisivel.append(x)

for x in range(1067, 3628):
    e_par(x)

for y in par:
    divisivel_por_7(y)

print()
print(f'O total de números que são pares e divisiveis por 7 é: {len(par_divisivel)}')
print()
print('Segue a lista dos números pares e divisiveis por sete:')
print(par_divisivel)


