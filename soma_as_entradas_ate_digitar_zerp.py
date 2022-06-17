soma = 0
while True:
	n = int(input('Digite os números que deseja somar, digite 0 para encerrar a operação:  '))
	if n == 0:
		break
	else:
		soma += n
print(f'a soma dos numeros digitados foi: {soma}')