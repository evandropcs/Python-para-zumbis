# Variavel global
numeros = [1, 2, 3, 4, 5]

def contagem():
    # Variavel local
    # global numeros
    numeros = [1, 2, 3]
    print(numeros)


contagem()  # Variavel local
print(numeros)  # Variavel Global

