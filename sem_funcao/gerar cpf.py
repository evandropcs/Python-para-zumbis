from random import randint
CPF = str(randint(100000000, 999999999))
contador = 10

for i in range(0, 2):
    digito = 0
    aux = 0
    for key, valeu in enumerate(range(contador, 1, -1)):
        print(CPF[key], valeu)
        valor = int(CPF[key])
        aux += valor * valeu
    digito = 11 - (aux % 11)

    if digito > 9 : digito = 0

    CPF += str(digito)
    contador += 1
print(CPF)