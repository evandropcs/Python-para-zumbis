def mostrar_chaves(dicionario):
    for chaves in dicionario.keys():
        print(chaves)

def mostrar_valores(dicionario):
    for valores in dicionario.values():
        print(valores)

def mostrar_items(dicionario):
    for chaves, valores in dicionario.items():
        print(chaves, valores)

lista = {'eu': 12, 'tu': 13, 'ele': 14}


if __name__ == '__main__':
    mostrar_chaves(lista)
    mostrar_valores(lista)
    mostrar_items(lista)


