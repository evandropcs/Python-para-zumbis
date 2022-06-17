soma = 0
x = 0
while x < 10:
    n = int(input(f'Digite o {x+1}º número: '))
    soma += n
    x += 1
print(f'A soma dos 10 inteiros é {soma}')
print(f'A média dos 10 inteiros é {soma/x:.0f}')s