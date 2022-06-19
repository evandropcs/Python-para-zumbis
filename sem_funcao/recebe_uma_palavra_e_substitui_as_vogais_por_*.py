# Versão 1:

palavra = input('Escreva uma palavra: ')
palavra_nova = ''
for x in palavra.lower():
    if x == 'a':
        palavra_nova += '*'
    elif x == 'e':
        palavra_nova += '*'
    elif x == 'i':
        palavra_nova += '*'
    elif x == 'o':
        palavra_nova += '*'
    elif x == 'u':
        palavra_nova += '*'
    else:
        palavra_nova += x

print(palavra_nova)

# Versão 2:

# lista_proibida = ['a', 'e', 'i', 'o', 'u']
#
# palavra = 'araucaria'
# palavra_nova = ''
#
# for x in palavra:
#     if x in lista_proibida:
#         palavra_nova += '*'
#     else:
#         palavra_nova += x
#
# print(palavra_nova)

# Versão 3:

# palavra = 'araucaria'
# palavra_nova = ''
#
# for x in palavra:
#     if x in 'a,e,i,o,u':
#         palavra_nova += '*'
#     else:
#         palavra_nova += x
#
# print(palavra_nova)


