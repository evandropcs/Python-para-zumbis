numeros = [10, -2, 190, -15, 0, 43, 92]

maior = 0
menor = 99999999999

for num in numeros:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(maior)
print(menor)

