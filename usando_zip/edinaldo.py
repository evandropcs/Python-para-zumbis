"""
Exercício 01 da seção de Strings da Python Brasil:
https://wiki.python.org.br/ExerciciosComStrings

Imprima o nome na vertical.
Faça um programa que receba o nome do usuário e imprima-o na vertical.

    >>> imprimir("Buser tecos show")
    A frase tem 5 vogais e 2 espaços em branco.
    >>> imprimir('Buser  tecos      shiouow')
    A frase tem 8 vogais e 8 espaços em branco.

"""


def imprimir(nome):
    """Escreva aqui em baixo a sua solução"""

    espaco = 0
    vogais = 0

    for letra in list(nome):
        if letra == " ":
            espaco += 1
        if letra in 'aeiou':
            vogais += 1

    print(f'A frase tem {vogais} vogais e {espaco} espaços em branco.')
