from random import sample

numeros = sample(range(100), 10)
print(numeros)
def maior_menor(n):

    maior = 0
    menor = 999999999999999999999999999
    for num in n:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    return maior, menor

print(maior_menor(numeros))


