numeros = [1, 3, 5, 8, 54, 776, 998, 887, 101, 2]

par = [x for x in numeros if x % 2 == 0]
impar = [x for x in numeros if x % 2 == 1]

print(sorted(par))
print(sorted(impar))


