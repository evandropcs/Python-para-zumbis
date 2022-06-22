# usando zip para listas com o mesmo numeros de elementos
lista_1 = [1, 2, 3 , 5]
lista_2 = ['eu', 'tu', 'ele']

for nome, numero, in zip(lista_2, lista_1):
    print(nome, numero)

# usando zip para listas com numeros diferentes de elementos, retorna NONE para substituir a chave, ou valor ausente.

from itertools import zip_longest

lista_1 = [1, 2, 3, 5]
lista_2 = ['eu', 'tu', 'ele', 'nós', 'eles']

for nome, numero, in zip_longest(lista_2, lista_1):
    print(nome, numero)