notas = []
x = 1
soma = 0
media = 0

while x <= 4:
    notas.append(float(input(f'Digite a {x}ª notas: ')))
    soma = soma + notas[x-1]
    media = soma / len(notas)
    x += 1
print(notas)
print(soma)
print(media)


