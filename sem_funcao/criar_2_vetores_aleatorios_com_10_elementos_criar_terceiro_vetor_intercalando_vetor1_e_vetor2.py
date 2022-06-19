from random import sample

numero_1 = sample(range(100), 10)
numero_2 = sample(range(100), 10)
numero_3 = []

x = 0

while x < 10:
    numero_3.append(numero_1[x])
    numero_3.append(numero_2[x])
    x += 1

print(f'Lista 1: {numero_1}')
print(f'Lista 2: {numero_2}')
print(f'Lista 3: {numero_3}')

# from random import randint
#
# lista_1 = []
# lista_2 = []
# lista_3 = []
#
# for x in range(10):
#     num = randint(1, 100)
#     lista_1.append(num)
#     lista_3.append(num)
#     num = randint(1, 100)
#     lista_2.append(num)
#     lista_3.append(num)
#
# print(lista_1)
# print(lista_2)
# print(lista_3)
