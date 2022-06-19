
def localizar(numero, sorte, azar):
    if sorte in numero and azar not in numero:
        lista.append(numero)


lista = []

for x in range(18644, 33087):
    localizar(str(x), '2', '7')

print(len(lista))

