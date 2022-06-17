tempo_de_ligacao = int(input("Qual o tempo das ligações ? "))

if tempo_de_ligacao < 200:
	preco = 0.2

elif tempo_de_ligacao <= 400:
	preco = 0.18

elif tempo_de_ligacao > 400 and tempo_de_ligacao <= 800:
	preco = 0.15

else:
	preco = 0.08

print(f'O preço por minuto foi de {preco} e o  preço da conta foi de {tempo_de_ligacao * preco:.2f} R$')