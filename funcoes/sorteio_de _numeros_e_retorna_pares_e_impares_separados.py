# Versão 1:

from random import sample

numeros = sample(range(100), 10)
print(numeros)

def par_impar(n):
    par = []
    impar = []
    for num in n:
        if num % 2 == 0:
            par.append(num)
        impar.append(num)
    return par, impar


par, impar = par_impar(numeros)
print(par)
print(impar)


# Versão 2:
# from random import sample
#
# numeros = sample(range(100), 10)
# print(numeros)
#
# def par_impar(n):
#     par = []
#     impar = []
#     for num in n:
#         x, resto = divmod(num, 10)
#         if resto in [0, 2, 4, 6, 8, 10]:
#             par.append(num)
#         else:
#             impar.append(num)
#     return par, impar
#
#
# par, impar = par_impar(numeros)
# print(par)
# print(impar)