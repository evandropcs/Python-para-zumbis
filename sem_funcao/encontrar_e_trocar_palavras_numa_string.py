animal = 'Um tigre, dois tigres, três tigres'
print(animal.find('tigre'))  # Retorna o indicie onde a palavra tigre começa
print(animal.find('tigre', 4))  # Retorna o indicie após o quarto, onde a palavra tigre começa
print(animal.replace('tigre', 'gato'))   # Substitui as palavras tigre por gato